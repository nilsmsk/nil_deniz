import streamlit as st
import pandas as pd
import random
import os
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
    .stButton>button {
        background-color: #d63031; color: white; border-radius: 25px;
        padding: 10px; width: 100%; border: none; font-weight: bold;
    }
    /* Kaçan Buton Alanı */
    .kacan-alan {
        height: 200px;
        position: relative;
        border: 1px dashed #fab1a0;
        border-radius: 15px;
        margin: 20px 0;
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
        <p style='color: #ff7675; font-weight: bold;'>{fark.hours} Saat, {fark.minutes} Dakika, {simdi.second} Saniye...</p>
        <p style='color: #b2bec3; font-size: 0.9rem;'>Nil seni her saniye daha çok seviyor.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KAÇAN BUTON ŞAKASI (TRICKY QUESTION) ---
st.subheader("🧐 Hayati Bir Soru")
st.write("Lütfen dürüstçe cevap ver:")
st.info("Dünyanın en tatlı, en zeki ve en muhteşem sevgilisi Nil mi?")

# Butonun konumunu session_state'de tutalım
if 'btn_pos' not in st.session_state:
    st.session_state.btn_pos = 0

# Buton her tıklandığında (veya sayfa her yüklendiğinde) yer değiştirecek
# Streamlit yapısı gereği butona 'yaklaşınca' değil, her etkileşimde kaçacak
col_a, col_b, col_c = st.columns([1, 1, 1])

# Kaçan Buton Mantığı
with [col_a, col_b, col_c][st.session_state.btn_pos]:
    if st.button("EVET! 😍", key="kacan_evet"):
        st.session_state.btn_pos = (st.session_state.btn_pos + 1) % 3
        st.toast("Hoppa! Yakalayamazsın ki ndmdmsmdmd")
        st.rerun()

with col_b:
    if st.button("Tabii ki Evet! ✨", key="sabit_evet"):
        st.balloons()
        st.success("Doğru cevap! Mühendislik analizleri de bunu doğruluyor. ❤️")

st.divider()

# --- 3. BİZİM PLAYLISTİMİZ ---
st.subheader("🎵 Bizim Playlistimiz")
st.markdown('<a href="https://open.spotify.com/playlist/6U7p8uMolo5wVRwp2Vn26h?si=oFJOcedlRx-6786wZrgxaQ" target="_blank" style="display: block; width: 100%; text-align: center; background-color: #1DB954; color: white; padding: 15px; border-radius: 30px; text-decoration: none; font-weight: bold;">🎶 Spotify\'da Dinlemeye Başla 🎶</a>', unsafe_allow_html=True)

st.divider()

# --- 4. CHALLENGER BUCKET LIST ---
st.subheader("🚀 Challenger Bucket List")
items = [
    "Japonya'da tek bir kelime bilmeden yolu bulmak 🇯🇵",
    "Edinburgh Kalesi'nin en tepesine kadar yarışarak çıkmak 🏰",
    "Hiç bilmediğimiz bir şehirde 10 km yürümek 🗺️",
    "Karlı havada yürüyüş sonrası sıcacık çaylar ☕"
]
for item in items:
    if st.checkbox(item):
        st.balloons()

st.divider()

# --- 5. SİNİR BOZUCU LOADING ---
st.subheader("🎁 Çok Büyük Bir Müjde!")
if st.button("🔥 MÜJDEYİ GÖR 🔥"):
    bar = st.progress(0)
    for i in range(1, 101):
        time.sleep(0.03)
        if i == 99: time.sleep(1.5)
        bar.progress(i)
    st.error("HATA: Nil şu an çay içiyor, sürpriz yüklenemedi! ndmdmsmdmd")

st.divider()

# --- 6. TEK KULLANIMLIK KUPONLAR ---
st.subheader("🎟️ Aşk Kuponları")
if 'kuponlar' not in st.session_state:
    st.session_state.kuponlar = {'cay': True, 'film': True, 'sarilma': True, 'yemek': True}

c1, c2 = st.columns(2)
with c1:
    if st.session_state.kuponlar['cay']:
        if st.button("Kuponu Bozdur: ☕️"):
            st.session_state.kuponlar['cay'] = False; st.balloons(); st.rerun()
    if st.session_state.kuponlar['film']:
        if st.button("Kuponu Bozdur: 🎬"):
            st.session_state.kuponlar['film'] = False; st.balloons(); st.rerun()
with c2:
    if st.session_state.kuponlar['sarilma']:
        if st.button("Kuponu Bozdur: 🧸"):
            st.session_state.kuponlar['sarilma'] = False; st.balloons(); st.rerun()
    if st.session_state.kuponlar['yemek']:
        if st.button("Kuponu Bozdur: 🍕"):
            st.session_state.kuponlar['yemek'] = False; st.balloons(); st.rerun()
