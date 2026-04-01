import streamlit as st
import random
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

# --- SAYFA AYARLARI VE TASARIM ---
st.set_page_config(page_title="Bizim Dünyamız", page_icon="💖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fffafa; }
    .ana-baslik { text-align: center; color: #d63031; font-size: 2.2rem; font-weight: bold; margin-bottom: 5px; }
    .timer-box { 
        background-color: white; padding: 25px; border-radius: 20px; 
        border: 1px solid #ff7675; text-align: center; 
        box-shadow: 0px 4px 15px rgba(214, 48, 49, 0.1); margin-bottom: 30px;
    }
    .kupon-karti {
        background: linear-gradient(135deg, #ff7675 0%, #d63031 100%);
        color: white; padding: 20px; border-radius: 15px;
        text-align: center; margin-bottom: 10px;
        border: 2px dashed #ffffff;
    }
    .final-not {
        background-color: #ffffff; padding: 30px; border-radius: 15px;
        text-align: center; font-size: 24px; color: #d63031;
        box-shadow: 0px 10px 25px rgba(214, 48, 49, 0.2);
        border: 2px solid #d63031; margin-top: 20px;
        font-weight: bold; line-height: 1.6;
    }
    /* Devasa Kabul Et Butonu */
    .stButton>button[kind="primary"] {
        background-color: #27ae60 !important; color: white !important;
        font-size: 40px !important; height: 100px !important; width: 100% !important;
        border-radius: 20px !important;
    }
    /* Küçücük Kaçan Buton */
    .stButton>button[kind="secondary"] {
        font-size: 8px !important; height: 20px !important; width: 50px !important;
        background-color: #dfe6e9 !important; border: none !important;
    }
    .stButton>button {
        background-color: #d63031; color: white; border-radius: 25px;
        padding: 10px; width: 100%; border: none; font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. ZAMAN SAYACI (19 Ocak 2024) ---
baslangic = datetime(2024, 1, 19, 0, 0)
simdi = datetime.now()
fark = relativedelta(simdi, baslangic)

st.markdown("<div class='ana-baslik'>❤️ İyi ki Varsın ❤️</div>", unsafe_allow_html=True)
st.markdown(f"""
    <div class='timer-box'>
        <p style='color: #636e72; font-size: 1.1rem; margin-bottom: 5px;'>19 Ocak 2024'ten beri...</p>
        <h2 style='color: #d63031; margin: 0;'>{fark.years} Yıl, {fark.months} Ay, {fark.days} Gün</h2>
        <p style='color: #ff7675; font-weight: bold;'>{fark.hours} Saat, {fark.minutes} Dakika...</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. HAKLILIK SÖZLEŞMESİ (KAÇAN BUTON 2.0) ---
st.subheader("📝 Ömür Boyu Haklılık Sözleşmesi")
st.warning("Nil'in her zaman haklı olduğunu, tüm tartışmaları otomatik olarak kazandığını ve son sözün her zaman Nil'e ait olduğunu kabul ediyorum.")

if 'sozlesme_pos' not in st.session_state:
    st.session_state.sozlesme_pos = 0

col_dev, col_kucuk = st.columns([3, 1])

with col_dev:
    if st.button("KABUL EDİYORUM ✅", kind="primary"):
        st.balloons()
        st.success("Aferin! En doğru kararı verdin. ndmdmsmdmd ❤️")

with [col_kucuk, col_dev, col_dev][st.session_state.sozlesme_pos]:
    if st.button("hayır", key="kacan_sozlesme", kind="secondary"):
        st.session_state.sozlesme_pos = (st.session_state.sozlesme_pos + 1) % 3
        st.toast("Yanlış buton! Tekrar dene... ndmdmsmdmd")
        st.rerun()

st.divider()

# --- 3. BİZİM PLAYLISTİMİZ ---
st.subheader("🎵 Bizim Playlistimiz")
st.markdown('<a href="https://open.spotify.com/playlist/6U7p8uMolo5wVRwp2Vn26h?si=oFJOcedlRx-6786wZrgxaQ" target="_blank" style="display: block; width: 100%; text-align: center; background-color: #1DB954; color: white; padding: 15px; border-radius: 30px; text-decoration: none; font-weight: bold;">🎶 Spotify\'da Dinlemeye Başla 🎶</a>', unsafe_allow_html=True)

st.divider()

# --- 4. SİNİR BOZUCU MÜJDE (Loading Bar) ---
st.subheader("🎁 Çok Büyük Bir Müjde!")
if st.button("🔥 MÜJDEYİ GÖR 🔥"):
    bar = st.progress(0)
    for i in range(1, 101):
        time.sleep(0.04)
        if i == 99: time.sleep(2.0)
        bar.progress(i)
    st.error("HATA: Nil şu an çay içtiği için sürpriz yüklenemedi! ndmdmsmdmd")

st.divider()

# --- 5. TEK KULLANIMLIK KUPONLAR ---
st.subheader("🎟️ Sana Özel Aşk Kuponları")
if 'kuponlar' not in st.session_state:
    st.session_state.kuponlar = {'cay': True, 'film': True, 'sarilma': True, 'yemek': True}

if not any(st.session_state.kuponlar.values()):
    st.markdown("""<div class='final-not'>💌 Sürpriiiiz!<br><br>Sana olan sevgim bu kuponlardan çok daha fazlası. 19 Ocak'tan beri hayatımdaki en güzel şeysin. Seni çok seviyorum! ❤️</div>""", unsafe_allow_html=True)
    st.balloons()
else:
    c1, c2 = st.columns(2)
    with c1:
        if st.session_state.kuponlar['cay']:
            if st.button("Bozdur: ☕️"): st.session_state.kuponlar['cay'] = False; st.rerun()
        if st.session_state.kuponlar['film']:
            if st.button("Bozdur: 🎬"): st.session_state.kuponlar['film'] = False; st.rerun()
    with c2:
        if st.session_state.kuponlar['sarilma']:
            if st.button("Bozdur: 🧸"): st.session_state.kuponlar['sarilma'] = False; st.rerun()
        if st.session_state.kuponlar['yemek']:
            if st.button("Bozdur: 🍕"): st.session_state.kuponlar['yemek'] = False; st.rerun()

st.divider()

# --- 6. CHALLENGER BUCKET LIST ---
st.subheader("🚀 Challenger Bucket List")
items = ["Japonya'da kaybolmak 🇯🇵", "Edinburgh'da yarışmak 🏰", "10 km yürümek 🗺️", "Karlı havada yürüyüş ve çay ☕"]
for item in items:
    if st.checkbox(item): st.balloons()
