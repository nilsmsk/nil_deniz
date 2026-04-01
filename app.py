import streamlit as st
import random
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

# --- SAYFA AYARLARI ---
st.set_page_config(page_title="Bizim Dünyamız", page_icon="💖", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fffafa; }
    .ana-baslik { text-align: center; color: #d63031; font-size: 2.2rem; font-weight: bold; }
    .timer-box { 
        background-color: white; padding: 25px; border-radius: 20px; 
        border: 1px solid #ff7675; text-align: center; 
        box-shadow: 0px 4px 15px rgba(214, 48, 49, 0.1); margin-bottom: 30px;
    }
    .kupon-karti {
        background: linear-gradient(135deg, #ff7675 0%, #d63031 100%);
        color: white; padding: 20px; border-radius: 15px;
        text-align: center; margin-bottom: 10px; border: 2px dashed #ffffff;
    }
    .final-not {
        background-color: #ffffff; padding: 30px; border-radius: 15px;
        text-align: center; font-size: 22px; color: #d63031;
        border: 2px solid #d63031; margin-top: 20px; font-weight: bold;
    }
    /* Devasa Buton */
    div.stButton > button:first-child {
        background-color: #d63031; color: white; border-radius: 25px;
        font-weight: bold; width: 100%;
    }
    /* Kabul Et Butonu Özel */
    .kabul-btn button {
        background-color: #27ae60 !important; font-size: 30px !important; height: 80px !important;
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
        <p style='color: #636e72;'>19 Ocak 2024'ten beri...</p>
        <h2 style='color: #d63031; margin: 0;'>{fark.years} Yıl, {fark.months} Ay, {fark.days} Gün</h2>
        <p style='color: #ff7675; font-weight: bold;'>{fark.hours} Saat, {fark.minutes} Dakika...</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. HAKLILIK SÖZLEŞMESİ (KAÇAN BUTON) ---
st.subheader("📝 Haklılık Sözleşmesi")
st.write("Nil'in her zaman haklı olduğunu kabul ediyor musun?")

if 'kacan_pos' not in st.session_state:
    st.session_state.kacan_pos = 0

c1, c2 = st.columns([2, 1])
with c1:
    if st.button("EVET, KABUL EDİYORUM ✅", key="dev_evet"):
        st.balloons()
        st.success("Doğru karar! ndmdmsmdmd")

with [c2, c1, c1][st.session_state.kacan_pos]:
    if st.button("hayır", key="kacan_hayir"):
        st.session_state.kacan_pos = (st.session_state.kacan_pos + 1) % 3
        st.rerun()

st.divider()

# --- 3. PLAYLIST ---
st.subheader("🎵 Bizim Playlistimiz")
st.link_button("🎶 Spotify'da Dinlemeye Başla 🎶", "https://open.spotify.com/playlist/6U7p8uMolo5wVRwp2Vn26h?si=oFJOcedlRx-6786wZrgxaQ")

st.divider()

# --- 4. SİNİR BOZUCU MÜJDE ---
st.subheader("🎁 Çok Büyük Bir Müjde!")
if st.button("🔥 MÜJDEYİ GÖR 🔥"):
    bar = st.progress(0)
    for i in range(1, 101):
        time.sleep(0.03)
        if i == 99: time.sleep(1.5)
        bar.progress(i)
    st.error("HATA: Nil şu an çay içiyor, sürpriz yüklenemedi! ndmdmsmdmd")

st.divider()

# --- 5. KUPONLAR ---
st.subheader("🎟️ Sana Özel Aşk Kuponları")
if 'kuponlar' not in st.session_state:
    st.session_state.kuponlar = {'cay': True, 'film': True, 'sarilma': True, 'yemek': True}

if not any(st.session_state.kuponlar.values()):
    st.markdown("<div class='final-not'>💌 Sürpriiiiz!<br>Seni 19 Ocak'tan beri her şeyden çok seviyorum. İyi ki varsın! ❤️</div>", unsafe_allow_html=True)
    st.balloons()
else:
    col_k1, col_k2 = st.columns(2)
    with col_k1:
        if st.session_state.kuponlar['cay']:
            if st.button("Bozdur: ☕️"): st.session_state.kuponlar['cay'] = False; st.rerun()
        if st.session_state.kuponlar['film']:
            if st.button("Bozdur: 🎬"): st.session_state.kuponlar['film'] = False; st.rerun()
    with col_k2:
        if st.session_state.kuponlar['sarilma']:
            if st.button("Bozdur: 🧸"): st.session_state.kuponlar['sarilma'] = False; st.rerun()
        if st.session_state.kuponlar['yemek']:
            if st.button("Bozdur: 🍕"): st.session_state.kuponlar['yemek'] = False; st.rerun()
