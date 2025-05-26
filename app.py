
import streamlit as st
import diyet_takibi
import egzersiz_takibi
import olcum_takibi
import plan_takvimi
import diyet_analizi
import veri_aktarimi

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
            st.rerun()
        else:
            st.sidebar.error("Hatalı giriş.")
    st.stop()
else:
    st.sidebar.success("Giriş yapıldı")
    if st.sidebar.button("Çıkış"):
        st.session_state.oturum = False
        st.rerun()

    sayfa = st.sidebar.selectbox("Sayfa Seçin", [
        "Diyet Takibi",
        "Egzersiz Takibi",
        "Vücut Ölçüm Takibi",
        "Haftalık Plan",
        "Haftalık Diyet Analizi",
        "Veriler Dışa Aktarımı"
    ])

    if sayfa == "Diyet Takibi":
        diyet_takibi.run()
    elif sayfa == "Egzersiz Takibi":
        egzersiz_takibi.run()
    elif sayfa == "Vücut Ölçüm Takibi":
        olcum_takibi.run()
    elif sayfa == "Haftalık Plan":
        plan_takvimi.run()
    elif sayfa == "Haftalık Diyet Analizi":
        diyet_analizi.run()
    elif sayfa == "Veriler Dışa Aktarımı":
        veri_aktarimi.run()
