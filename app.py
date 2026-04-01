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
        <p style='color: #b2bec3; font-size: 0.9rem;'>Nil seni her geçen gün daha çok seviyor.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. KAÇAN HAYIR BUTONU ŞAKASI ---
st.subheader("🧐 Küçük Bir Soru")
st.write("Beni seviyor musun?")

if 'hayir_pos' not in st.session_state:
    st.session_state.hayir_pos = 0

col_evet, col_bos, col_hayir = st.columns([1, 1, 1])

with col_evet:
    if st.button("EVET! 😍", key="net_evet"):
        st.balloons()
        st.success("Ben de seni çok seviyorum! ❤️")

with [col_hayir, col_bos, col_evet][st.session_state.hayir_pos]:
    if st.button("Hayır 😜", key="kacan_hayir"):
        st.session_state.hayir_pos = (st.session_state.hayir_pos + 1) % 3
        st.toast("Yakalayamazsın ki! ndmdmsmdmd")
        st.rerun()

st.divider()

# --- 3. BİZİM PLAYLISTİMİZ ---
st.subheader("🎵 Bizim Playlistimiz")
st.markdown('<a href="https://open.spotify.com/playlist/6U7p8uMolo5wVRwp2Vn26h?si=oFJOcedlRx-6786wZrgxaQ" target="_blank" style="display: block; width: 100%; text-align: center; background-color: #1DB954; color: white; padding: 15px; border-radius: 30px; text-decoration: none; font-weight: bold;">🎶 Spotify\'da Dinlemeye Başla 🎶</a>', unsafe_allow_html=True)

st.divider()

# --- 4. SİNİR BOZUCU MÜJDE (Loading Bar) ---
st.subheader("🎁 Çok Büyük Bir Müjde!")
if st.button("🔥 MÜJDEYİ GÖR 🔥", key="mujde_btn"):
    bar = st.progress(0)
    for i in range(1, 101):
        time.sleep(0.04)
        if i == 99: time.sleep(2.0) # Tam burada sinirler bozulur
        bar.progress(i)
    st.error("HATA: Nil şu an çay içtiği için sürpriz yüklenemedi! Lütfen daha sonra (belki 100 yıl sonra) tekrar deneyiniz. ndmdmsmdmd")

st.divider()

# --- 5. TEK KULLANIMLIK KUPONLAR VE FİNAL NOTU ---
st.subheader("🎟️ Sana Özel Aşk Kuponları")
st.write("Tüm kuponları bitirdiğinde gizli bir mesaj açılacak... 👀")

if 'kuponlar' not in st.session_state:
    st.session_state.kuponlar = {'cay': True, 'film': True, 'sarilma': True, 'yemek': True}

# Eğer tüm kuponlar kullanıldıysa final notunu göster
if not any(st.session_state.kuponlar.values()):
    st.markdown("""
        <div class='final-not'>
            💌 Tebrikler! Tüm kuponları başarıyla bitirdin.<br><br>
            Sana olan sevgim bu kuponlardan çok daha fazlası. 19 Ocak'tan beri hayatımdaki en güzel şeysin. 
            Seninle her anım, her çayımız ve her hayalimiz benim için paha biçilemez. Seni çok seviyorum! ❤️
        </div>
    """, unsafe_allow_html=True)
    st.balloons()
else:
    c1, c2 = st.columns(2)
    with c1:
        if st.session_state.kuponlar['cay']:
            st.markdown("<div class='kupon-karti'><b>☕️ Çay Ismarlama</b></div>", unsafe_allow_html=True)
            if st.button("Bozdur: ☕️"):
                st.session_state.kuponlar['cay'] = False; st.rerun()
        if st.session_state.kuponlar['film']:
            st.markdown("<div class='kupon-karti'><b>🎬 Film Seçme Hakkı</b></div>", unsafe_allow_html=True)
            if st.button("Bozdur: 🎬"):
                st.session_state.kuponlar['film'] = False; st.rerun()
    with c2:
        if st.session_state.kuponlar['sarilma']:
            st.markdown("<div class='kupon-karti'><b>🧸 Sonsuz Sarılma</b></div>", unsafe_allow_html=True)
            if st.button("Bozdur: 🧸"):
                st.session_state.kuponlar['sarilma'] = False; st.rerun()
        if st.session_state.kuponlar['yemek']:
            st.markdown("<div class='kupon-karti'><b>🍕 Favori Yemek</b></div>", unsafe_allow_html=True)
            if st.button("Bozdur: 🍕"):
                st.session_state.kuponlar['yemek'] = False; st.rerun()

st.divider()

# --- 6. CHALLENGER BUCKET LIST ---
st.subheader("🚀 Challenger Bucket List")
items = ["Japonya'da kaybolmak 🇯🇵", "Edinburgh'da yarışmak 🏰", "10 km yürümek 🗺️", "Karlı havada yürüyüş ve çay ☕"]
for item in items:
    if st.checkbox(item):
        st.balloons()
