import streamlit as st

st.set_page_config(page_title="FitTakip", layout="wide")

st.sidebar.title("FitTakip | Giriş")
if "oturum" not in st.session_state:
    st.session_state.oturum = False

if not st.session_state.oturum:
    kullanici = st.sidebar.text_input("Kullanıcı Adı")
    sifre = st.sidebar.text_input("Şifre", type="password")
    if st.sidebar.button("Giriş"):
        if kullanici == "admin" and sifre == "1234":
            st.session_state.oturum = True
            st.experimental_rerun()
        else:
            st.sidebar.error("Hatalı giriş.")
    st.stop()
else:
    st.sidebar.success("Giriş yapıldı")
    if st.sidebar.button("Çıkış"):
        st.session_state.oturum = False
        st.experimental_rerun()
