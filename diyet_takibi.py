import streamlit as st
import pandas as pd

def run():
    st.title('🍽️ Diyet Takibi')

    # Yemek veritabanını yükle
    @st.cache_data(show_spinner=False, ttl=600)
    def yemek_verilerini_yukle():
        df = pd.read_csv("yemek_veritabani_1000plus.csv")
        if 'yağ' in df.columns and 'yag' not in df.columns:
            df = df.rename(columns={'yağ': 'yag'})
        return df

    yemekler_df = yemek_verilerini_yukle()

    # SessionState başlat
    if "gunluk_yemekler" not in st.session_state:
        st.session_state.gunluk_yemekler = []

    st.subheader("🍲 Yemek Seçimi")

    yemek_adi = st.text_input("Yemek ara:")

    filtreli = pd.DataFrame()
    if yemek_adi:
        filtreli = yemekler_df[yemekler_df['yemek_adi'].str.contains(yemek_adi, case=False, na=False)].head(20)

    if not filtreli.empty:
        secim = st.selectbox("Yemek seçin:", filtreli['yemek_adi'].tolist())
        secilen_satir = filtreli[filtreli['yemek_adi'] == secim].iloc[0]

        st.write("**Makro Bilgiler:**")
        st.write(f"Kalori: {secilen_satir['kalori']} kcal")
        st.write(f"Protein: {secilen_satir['protein']} g")
        st.write(f"Karbonhidrat: {secilen_satir['karbonhidrat']} g")
        st.write(f"Yağ: {secilen_satir['yag']} g")

        if st.button("Yemeği Ekle"):
            st.session_state.gunluk_yemekler.append(secilen_satir.to_dict())
            st.success(f"{secim} eklendi!")
    elif yemek_adi:
        st.warning("Aramanıza uygun yemek bulunamadı.")
    else:
        st.info("Lütfen yemek adını girin.")

    st.subheader("📋 Günlük Yemek Listesi")

    gunluk_df = pd.DataFrame(st.session_state.gunluk_yemekler)
    if not gunluk_df.empty:
        st.dataframe(gunluk_df[['yemek_adi', 'kalori', 'protein', 'karbonhidrat', 'yag']])

        st.subheader("📊 Günlük Toplamlar")
        toplamlar = gunluk_df[['kalori', 'protein', 'karbonhidrat', 'yag']].sum()
        st.write(f"Toplam Kalori: {toplamlar['kalori']} kcal")
        st.write(f"Toplam Protein: {toplamar['protein']} g")
        st.write(f"Toplam Karbonhidrat: {toplamlar['karbonhidrat']} g")
        st.write(f"Toplam Yağ: {toplamlar['yag']} g")
    else:
        st.info("Henüz yemek eklenmedi.")
