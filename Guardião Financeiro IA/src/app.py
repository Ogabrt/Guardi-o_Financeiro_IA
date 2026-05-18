from pathlib import Path
import json
import pandas as pd
import streamlit as st

BASE_DIR = Path(__file__).resolve().parent.parent
DATA_DIR = BASE_DIR / "data"

@st.cache_data
def carregar_dados():
    transacoes = pd.read_csv(DATA_DIR / "transacoes.csv")
    historico = pd.read_csv(DATA_DIR / "historico_atendimento.csv")
    with open(DATA_DIR / "perfil_investidor.json", "r", encoding="utf-8") as f:
        perfil = json.load(f)
    with open(DATA_DIR / "produtos_financeiros.json", "r", encoding="utf-8") as f:
        produtos = json.load(f)
    return transacoes, historico, perfil, produtos

def calcular_resumo(transacoes):
    entradas = transacoes[transacoes["tipo"] == "entrada"]["valor"].sum()
    saidas = transacoes[transacoes["tipo"] == "saida"]["valor"].sum()
    saldo = entradas - saidas
    gastos_categoria = (
        transacoes[transacoes["tipo"] == "saida"]
        .groupby("categoria")["valor"]
        .sum()
        .sort_values(ascending=False)
    )
    return entradas, saidas, saldo, gastos_categoria

def recomendar_produtos(perfil, produtos):
    recomendados = []
    perfil_risco = perfil["perfil_investidor"].lower()
    aceita_risco = perfil["aceita_risco"]
    objetivo = perfil["objetivo_principal"].lower()

    for produto in produtos:
        risco = produto["risco"].lower()

        if not aceita_risco and risco == "alto":
            continue

        if "reserva" in objetivo and risco == "baixo":
            recomendados.append(produto)
        elif perfil_risco == "moderado" and risco in ["baixo", "medio"]:
            recomendados.append(produto)
        elif perfil_risco == "arrojado":
            recomendados.append(produto)

    return recomendados[:3]

def responder_pergunta(pergunta, transacoes, historico, perfil, produtos):
    pergunta = pergunta.lower().strip()
    entradas, saidas, saldo, gastos_categoria = calcular_resumo(transacoes)

    if "saldo" in pergunta or "resumo financeiro" in pergunta:
        return (
            f"Seu saldo no período analisado é de R$ {saldo:.2f}.\n\n"
            f"Você teve R$ {entradas:.2f} em entradas e R$ {saidas:.2f} em saídas."
        )

    if "alimentação" in pergunta or "alimentacao" in pergunta:
        total = transacoes[
            (transacoes["categoria"].str.lower() == "alimentacao") &
            (transacoes["tipo"].str.lower() == "saida")
        ]["valor"].sum()
        return f"Você gastou R$ {total:.2f} com alimentação no período analisado."

    if "maior gasto" in pergunta or "gastei mais" in pergunta:
        categoria = gastos_categoria.idxmax()
        valor = gastos_categoria.max()
        return f"Sua categoria com maior gasto foi **{categoria}**, totalizando R$ {valor:.2f}."

    if "reserva de emergência" in pergunta or "reserva de emergencia" in pergunta:
        meta_reserva = None
        for meta in perfil["metas"]:
            if "reserva" in meta["meta"].lower():
                meta_reserva = meta
                break

        if meta_reserva:
            atual = perfil["reserva_emergencia_atual"]
            necessario = meta_reserva["valor_necessario"]
            falta = necessario - atual
            return (
                f"Sua meta de reserva de emergência é R$ {necessario:.2f}.\n\n"
                f"Você já possui R$ {atual:.2f} e ainda faltam R$ {falta:.2f}."
            )

    if "investimento" in pergunta or "produto" in pergunta or "combina comigo" in pergunta:
        recomendados = recomendar_produtos(perfil, produtos)
        if recomendados:
            resposta = "Os produtos mais compatíveis com seu perfil neste momento são:\n\n"
            for p in recomendados:
                resposta += (
                    f"- **{p['nome']}** | categoria: {p['categoria']} | "
                    f"risco: {p['risco']} | aporte mínimo: R$ {p['aporte_minimo']:.2f}\n"
                )
            return resposta
        return "Não encontrei produtos adequados com base nos dados atuais."

    if "histórico" in pergunta or "historico" in pergunta or "atendimento" in pergunta:
        ultimos = historico.tail(3)
        resposta = "Seus últimos atendimentos registrados foram:\n\n"
        for _, row in ultimos.iterrows():
            resposta += f"- {row['data']}: {row['tema']} via {row['canal']}.\n"
        return resposta

    return (
        "Ainda não sei responder isso nesta versão do agente.\n\n"
        "Tente perguntas como:\n"
        "- Qual meu saldo?\n"
        "- Quanto gastei com alimentação?\n"
        "- Qual foi meu maior gasto?\n"
        "- Quanto falta para minha reserva de emergência?\n"
        "- Qual investimento combina comigo?"
    )

st.set_page_config(page_title="Guardião Financeiro IA", page_icon="🤖", layout="wide")

transacoes, historico, perfil, produtos = carregar_dados()
entradas, saidas, saldo, gastos_categoria = calcular_resumo(transacoes)

if "mensagens" not in st.session_state:
    st.session_state.mensagens = [
        {
            "role": "assistant",
            "content": (
                f"Olá, {perfil['nome']}! Eu sou o Guardião Financeiro IA.\n\n"
                "Posso te ajudar com saldo, gastos, metas financeiras, histórico de atendimento e sugestões de produtos."
            )
        }
    ]

st.title("🤖 Guardião Financeiro IA")
st.caption("Assistente virtual financeiro com base em dados simulados do cliente.")

with st.sidebar:
    st.header("Perfil do cliente")
    st.write(f"**Nome:** {perfil['nome']}")
    st.write(f"**Profissão:** {perfil['profissao']}")
    st.write(f"**Renda mensal:** R$ {perfil['renda_mensal']:.2f}")
    st.write(f"**Perfil investidor:** {perfil['perfil_investidor']}")
    st.write(f"**Objetivo principal:** {perfil['objetivo_principal']}")

    st.divider()
    st.subheader("Perguntas rápidas")
    exemplos = [
        "Qual meu saldo?",
        "Quanto gastei com alimentação?",
        "Qual foi meu maior gasto?",
        "Quanto falta para minha reserva de emergência?",
        "Qual investimento combina comigo?",
        "Mostre meu histórico de atendimento"
    ]

    for exemplo in exemplos:
        if st.button(exemplo, use_container_width=True):
            st.session_state.mensagens.append({"role": "user", "content": exemplo})
            resposta = responder_pergunta(exemplo, transacoes, historico, perfil, produtos)
            st.session_state.mensagens.append({"role": "assistant", "content": resposta})
            st.rerun()

    st.divider()
    if st.button("Limpar conversa", use_container_width=True):
        st.session_state.mensagens = [
            {
                "role": "assistant",
                "content": (
                    f"Olá, {perfil['nome']}! Eu sou o Guardião Financeiro IA.\n\n"
                    "Posso te ajudar com saldo, gastos, metas financeiras, histórico de atendimento e sugestões de produtos."
                )
            }
        ]
        st.rerun()

col1, col2, col3 = st.columns(3)
col1.metric("Entradas", f"R$ {entradas:.2f}")
col2.metric("Saídas", f"R$ {saidas:.2f}")
col3.metric("Saldo", f"R$ {saldo:.2f}")

st.subheader("Conversa")

for msg in st.session_state.mensagens:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

pergunta = st.chat_input("Digite sua pergunta financeira aqui...")

if pergunta:
    st.session_state.mensagens.append({"role": "user", "content": pergunta})

    resposta = responder_pergunta(pergunta, transacoes, historico, perfil, produtos)
    st.session_state.mensagens.append({"role": "assistant", "content": resposta})
    st.rerun()

st.subheader("Gastos por categoria")
st.bar_chart(gastos_categoria)