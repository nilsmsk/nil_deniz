import streamlit as st
import pandas as pd
import random
import os
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
    .mesaj-kutusu {
        background-color: #ffffff; padding: 35px; border-radius: 15px;
        text-align: center; font-size: 22px; color: #2d3436;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05); margin-top: 15px;
        border-left: 10px solid #d63031;
    }
    .stButton>button {
        background-color: #d63031; color: white; border-radius: 25px;
        padding: 10px; width: 100%; border: none; font-weight: bold;
    }
    .stCheckbox { font-size: 18px; color: #2d3436; }
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

# --- 2. BUCKET LIST (HAYAL LİSTESİ) ---
st.subheader("✈️ Birlikte Yapılacaklar Listesi")
st.write("Gerçekleştirdiğimiz her hayal için bir tık! ❤️")

items = [
    "Tokyo ve Kyoto sokaklarında kaybolmak 🇯🇵",
    "Edinburgh'un tarihi caddelerinde yürümek 🏴󠁧󠁢󠁳󠁣󠁴󠁿",
    "Audi A3 ile plansız bir yolculuğa çıkmak 🚗",
    "En sevdiğimiz şarkıyı bağıra çağıra söylemek 🎤",
    "Mükemmel bir Türk kahvesi eşliğinde gün batımını izlemek ☕"
]

for item in items:
    if st.checkbox(item):
        st.balloons()
        st.toast(f"Harika! Bir hayal daha gerçek oldu: {item}")

st.divider()

# --- 3. MÜZİK KUTUSU (SPOTIFY MODLARI) ---
st.subheader("🎵 Moduna Göre Şarkımız")
st.write("Tıkla ve o anki ruh halimize uygun şarkıyı başlat!")

col_m1, col_m2 = st.columns(2)

with col_m1:
    if st.button("🔥 Enerjimiz Tavan! (Lvbel C5)"):
        st.markdown("[Spotify'da Dinle](https://open.spotify.com/artist/57Z9S0xshO1pWz3B6B3Z9W)")
    
    if st.button("🌟 İkonik Hisset (Lady Gaga)"):
        st.markdown("[Spotify'da Dinle](https://open.spotify.com/artist/1hy7t_FvBXpYh68t76Z7EA)")

with col_m2:
    if st.button("👑 Klasik ve Romantik (Tarkan)"):
        st.markdown("[Spotify'da Dinle](https://open.spotify.com/artist/4X96pEAVS99vI97m9YvIu3)")
        
    if st.button("🚗 Yolculuk Modu"):
        st.markdown("[Favori Listemizi Aç](https://open.spotify.com)")

st.divider()

# --- 4. TEK KULLANIMLIK AŞK KUPONLARI ---
st.subheader("🎟️ Sana Özel Aşk Kuponları")
if 'kuponlar' not in st.session_state:
    st.session_state.kuponlar = {'kahve': True, 'film': True, 'sarilma': True, 'yemek': True}

c1, c2 = st.columns(2)
with c1:
    if st.session_state.kuponlar['kahve']:
        st.markdown("<div class='kupon-karti'><b>☕️ Kahve Ismarlama</b></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: ☕️"):
            st.session_state.kuponlar['kahve'] = False
            st.balloons(); st.rerun()

    if st.session_state.kuponlar['film']:
        st.markdown("<div class='kupon-karti'><b>🎬 Film Seçme Hakkı</b></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: 🎬"):
            st.session_state.kuponlar['film'] = False
            st.balloons(); st.rerun()

with c2:
    if st.session_state.kuponlar['sarilma']:
        st.markdown("<div class='kupon-karti'><b>🧸 Sonsuz Sarılma</b></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: 🧸"):
            st.session_state.kuponlar['sarilma'] = False
            st.balloons(); st.rerun()

    if st.session_state.kuponlar['yemek']:
        st.markdown("<div class='kupon-karti'><b>🍕 Favori Yemek</b></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: 🍕"):
            st.session_state.kuponlar['yemek'] = False
            st.balloons(); st.rerun()
