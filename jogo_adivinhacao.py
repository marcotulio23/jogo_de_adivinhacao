import streamlit as st
import random

st.set_page_config(page_title="Jogo de Adivinhação", layout="centered")

st.title("🎯 Jogo de Adivinhação")
st.write("Tente adivinhar o número que a máquina escolheu entre 1 e 50!")

# Inicializa variáveis no session_state
if 'numero' not in st.session_state:
    st.session_state.numero = random.randint(1, 50)
    st.session_state.tentativas = 0
    st.session_state.jogo_ativo = True

# Função para reiniciar o jogo
def reiniciar_jogo():
    st.session_state.numero = random.randint(1, 50)
    st.session_state.tentativas = 0
    st.session_state.jogo_ativo = True

# Entrada do palpite
if st.session_state.jogo_ativo:
    palpite = st.number_input("Digite seu palpite:", min_value=1, max_value=50, step=1)
    if st.button("Chutar"):
        st.session_state.tentativas += 1
        if palpite < st.session_state.numero:
            st.warning("O número é maior! 📈")
        elif palpite > st.session_state.numero:
            st.warning("O número é menor! 📉")
        else:
            st.success(f"🎉 Parabéns! Você acertouz após {st.session_state.tentativas} tentativas!")
            st.session_state.jogo_ativo = False

# Botão para reiniciar a qualquer momento
st.button("Reiniciar jogo", on_click=reiniciar_jogo)
