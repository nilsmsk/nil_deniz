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
    /* Playlist Butonu Özel Stili */
    .playlist-btn {
        display: block; width: 100%; text-align: center;
        background-color: #1DB954; color: white; padding: 15px;
        border-radius: 30px; text-decoration: none; font-weight: bold;
        font-size: 1.2rem; margin: 20px 0;
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

# --- 2. BİZİM PLAYLISTİMİZ ---
st.subheader("🎵 Bizim Playlistimiz")
st.markdown('<a href="https://open.spotify.com/playlist/6U7p8uMolo5wVRwp2Vn26h?si=oFJOcedlRx-6786wZrgxaQ" target="_blank" class="playlist-btn">🎶 Spotify\'da Dinlemeye Başla 🎶</a>', unsafe_allow_html=True)

st.divider()

# --- 3. CHALLENGER BUCKET LIST ---
st.subheader("🚀 Gerçekten Yapmamız Gerekenler")
items = [
    "Japonya'da tek bir kelime bilmeden kaybolup yolu bulmak 🇯🇵",
    "Edinburgh Kalesi'nin en tepesine kadar yarışarak çıkmak 🏰",
    "Hiç bilmediğimiz bir şehirde sadece haritaya bakarak 10 km yürümek 🗺️",
    "Tüm gün sadece en sevdiğimiz şarkılar eşliğinde araba sürmek 🚗",
    "Karlı bir havada dışarıda buz gibi bir yürüyüş sonrası sıcacık çaylarımızı içmek ☕"
]

for item in items:
    if st.checkbox(item):
        st.balloons()
        st.toast(f"Meydan okuma tamamlandı! ✅")

st.divider()

# --- 4. TEK KULLANIMLIK AŞK KUPONLARI ---
st.subheader("🎟️ Sana Özel Aşk Kuponları")
if 'kuponlar' not in st.session_state:
    st.session_state.kuponlar = {'cay': True, 'film': True, 'sarilma': True, 'yemek': True}

c1, c2 = st.columns(2)
with c1:
    if st.session_state.kuponlar['cay']:
        st.markdown("<div class='kupon-karti'><b>☕️ Tavşan Kanı Çay Ismarlama</b><br><small>Nil tarafından özenle demlenir.</small></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: ☕️", key="k1"):
            st.session_state.kuponlar['cay'] = False
            st.balloons(); st.rerun()

    if st.session_state.kuponlar['film']:
        st.markdown("<div class='kupon-karti'><b>🎬 Film Seçme Hakkı</b></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: 🎬", key="k2"):
            st.session_state.kuponlar['film'] = False
            st.balloons(); st.rerun()

with c2:
    if st.session_state.kuponlar['sarilma']:
        st.markdown("<div class='kupon-karti'><b>🧸 Sonsuz Sarılma</b></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: 🧸", key="k3"):
            st.session_state.kuponlar['sarilma'] = False
            st.balloons(); st.rerun()

    if st.session_state.kuponlar['yemek']:
        st.markdown("<div class='kupon-karti'><b>🍕 Favori Yemek</b></div>", unsafe_allow_html=True)
        if st.button("Kuponu Bozdur: 🍕", key="k4"):
            st.session_state.kuponlar['yemek'] = False
            st.balloons(); st.rerun()
