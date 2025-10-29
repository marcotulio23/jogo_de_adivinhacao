import streamlit as st
import random

# Título e instruções
st.title("🎯 JOGO DE ADIVINHAÇÃO")
st.write("Seja bem-vindo(a) ao meu primeiro jogo em Python!")
st.write("Objetivo: Tentar acertar o número que o programa selecionou aleatoriamente entre 1 e 50")
st.write('---')

# Inicializar número secreto e tentativas usando sessão do Streamlit
if 'numero' not in st.session_state:
    st.session_state.numero = random.randint(1, 50)
    st.session_state.tentativas = 0
    st.session_state.jogo_finalizado = False

# Input do jogador
palpite = st.number_input("Insira seu palpite:", min_value=1, max_value=50, step=1)

# Botão para tentar adivinhar
if st.button("Tentar") and not st.session_state.jogo_finalizado:
    st.session_state.tentativas += 1

    if palpite == st.session_state.numero:
        st.success(f"🎉 Parabéns, você acertou o número após {st.session_state.tentativas} tentativas!")
        st.session_state.jogo_finalizado = True
    elif palpite < st.session_state.numero:
        st.info("O número é maior!")
    else:
        st.info("O número é menor!")

# Botão para reiniciar o jogo
if st.button("Reiniciar Jogo"):
    st.session_state.numero = random.randint(1, 50)
    st.session_state.tentativas = 0
    st.session_state.jogo_finalizado = False
    st.experimental_rerun()
