import streamlit as st
import pandas as pd
import random
import os
import time

# --- SAYFA AYARLARI VE TASARIM ---
st.set_page_config(page_title="Seni Seviyorum Çünkü...", page_icon="💌", layout="centered")

st.markdown("""
    <style>
    .ana-baslik { text-align: center; color: #d63031; font-size: 2.5rem; font-weight: bold; }
    .alt-metin { text-align: center; color: #636e72; font-size: 1.1rem; margin-bottom: 30px; }
    .mesaj-kutusu {
        background-color: #ffeaa7;
        padding: 40px;
        border-radius: 20px;
        text-align: center;
        font-size: 24px;
        font-style: italic;
        color: #2d3436;
        box-shadow: 5px 5px 15px rgba(0,0,0,0.1);
        margin-top: 20px;
        margin-bottom: 30px;
        border-left: 8px solid #fdcb6e;
    }
    .stButton>button {
        background-color: #ff7675;
        color: white;
        font-size: 20px;
        font-weight: bold;
        border-radius: 30px;
        padding: 10px;
        width: 100%;
        border: none;
        transition: 0.3s;
    }
    .stButton>button:hover { background-color: #d63031; }
    .polaroid {
        background-color: white; padding: 10px; padding-bottom: 20px;
        box-shadow: 3px 3px 10px rgba(0,0,0,0.2); text-align: center;
        margin-bottom: 15px;
    }
    </style>
    """, unsafe_allow_html=True)

# --- VERİTABANI: AŞK NOTLARI ---
DOSYA = "ask_notlari.csv"

if not os.path.exists(DOSYA):
    # Senin için birkaç başlangıç cümlesi ekledim, bunları o okuyacak!
    varsayilan_mesajlar = pd.DataFrame([
        {"Mesaj": "Gülüşün, çözmeye çalıştığım en zor diferansiyel denklemden bile daha büyüleyici."},
        {"Mesaj": "Seninle geçirdiğim her an, Kodak kameramın vizöründen gördüğüm en kusursuz manzara gibi."},
        {"Mesaj": "27 Ocak 2024'te hayatıma girdiğinden beri her günüm bir öncekinden daha güzel."},
        {"Mesaj": "En sıkıcı ve yorucu günlerde bile sesini duymak tüm stresimi alıp götürüyor."},
        {"Mesaj": "Birlikte arabada şarkı söyleyerek yaptığımız o yolculukları hiçbir şeye değişmem."},
        {"Mesaj": "Bana her baktığında gözlerinde bulduğum o sıcaklığı çok seviyorum."}
    ])
    varsayilan_mesajlar.to_csv(DOSYA, index=False)

df = pd.read_csv(DOSYA)

# --- ANA EKRAN ---
st.markdown("<div class='ana-baslik'>💌 Seni Seviyorum Çünkü...</div>", unsafe_allow_html=True)
st.markdown("<div class='alt-metin'>Bugün sana olan hislerimi duymaya hazır mısın?</div>", unsafe_allow_html=True)

# Butona basıldığında rastgele bir mesaj seçme mantığı
if 'gunun_mesaji' not in st.session_state:
    st.session_state.gunun_mesaji = "👇 Kutuyu açmak için aşağıdaki butona tıkla! 👇"

if st.button("✨ Bugünün Sebebini Göster ✨"):
    with st.spinner("Kalbimden geçenler taranıyor..."):
        time.sleep(1) # Gerçekçilik katmak için 1 saniyelik tatlı bir bekleme süresi
        st.session_state.gunun_mesaji = random.choice(df['Mesaj'].tolist())
        st.balloons()

# Mesaj Kutusu Görünümü
st.markdown(f"<div class='mesaj-kutusu'>\"{st.session_state.gunun_mesaji}\"</div>", unsafe_allow_html=True)

st.divider()

# --- VINTAGE FOTOĞRAF ALBÜMÜ ---
st.subheader("📸 Film Rulosundan Kalanlar")
st.write("Sanki eski bir kameradan çıkmış gibi, en güzel anılarımız...")

col1, col2 = st.columns(2)

with col1:
    st.markdown("""
        <div class='polaroid'>
            <img src='https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=400&auto=format&fit=crop' width='100%'/>
            <p style='margin-top:10px; font-family:cursive; color:#2d3436;'>27 Ocak 2024 ❤️</p>
        </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
        <div class='polaroid'>
            <img src='https://images.unsplash.com/photo-1522673607200-164d1b6ce486?q=80&w=400&auto=format&fit=crop' width='100%'/>
            <p style='margin-top:10px; font-family:cursive; color:#2d3436;'>Sonsuza dek...</p>
        </div>
    """, unsafe_allow_html=True)

st.info("💡 Not: Yukarıdaki fotoğraflar şu an temsilidir. GitHub'a kendi fotoğraflarınızı yükleyip kodun içine kendi linklerinizi koyabilirsiniz!")

# --- MERVE'NİN GİZLİ BÖLMESİ (Sadece senin not eklemen için) ---
st.write("")
st.write("")
with st.expander("🤫 Gizli Bölme (Sadece Not Eklemek İçin)"):
    st.write("Buradan sisteme sürekli yeni sürpriz mesajlar ekleyebilirsin. O butona bastıkça senin yeni eklediklerini görecektir.")
    with st.form("mesaj_ekle", clear_on_submit=True):
        yeni_not = st.text_area("Yeni bir 'Seni seviyorum çünkü...' sebebi yaz:")
        if st.form_submit_button("Sisteme Gizle"):
            if yeni_not:
                yeni_row = pd.DataFrame([{"Mesaj": yeni_not}])
                df = pd.concat([df, yeni_row], ignore_index=True)
                df.to_csv(DOSYA, index=False)
                st.success("Notun başarıyla eklendi! Artık rastgele karşısına çıkabilir.")
                st.rerun()
