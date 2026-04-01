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
        <p style='color: #ff7675; font-weight: bold; font-size: 1.2rem;'>{fark.hours} Saat, {fark.minutes} Dakika...</p>
        <p style='color: #b2bec3; font-size: 0.9rem;'>Nil seni her saniye daha çok seviyor.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. AŞK NOTLARI ---
notlar_listesi = [
    "Gülüşün, Nil'in çözmeye çalıştığı tüm denklemlerden daha güzel bir sonuç. ❤️",
    "19 Ocak 2024'ten beri kalbimdeki en güzel yer senin.",
    "Seninle içilen o bol köpüklü Türk kahvelerinin tadı başka hiçbir şeyde yok. ☕",
    "Tokyo ve Kyoto hayallerimizi gerçekleştireceğimiz günü iple çekiyorum. ✈️",
    "Kodak kameramın vizöründen gördüğüm en kusursuz manzara sensin. 📸",
    "Senin zekan ve kalbin, Nil'in hayatındaki en büyük şans.",
    "En stresli lab raporlarında bile senin desteğin bana güç veriyor.",
    "Seninle arabada şarkı söyleyerek yaptığımız yolculuklar favori anılarım. 🚗",
    "Hangi dilde söylersem söyleyeyim, seni sevmek kelimelere sığmıyor.",
    "Nil'in hayatına girdiğin o günden beri her şey çok daha anlamlı. ❤️"
]

st.subheader("💌 Kalbimden Sana...")
if 'mesaj' not in st.session_state:
    st.session_state.mesaj = "Butona bas ve Nil'den bir not oku... 👇"

if st.button("✨ Yeni Bir Not Oku ✨"):
    st.session_state.mesaj = random.choice(notlar_listesi)
    st.balloons()

st.markdown(f"<div class='mesaj-kutusu'>\"{st.session_state.mesaj}\"</div>", unsafe_allow_html=True)

st.write("")
st.divider()

# --- 3. TEK KULLANIMLIK AŞK KUPONLARI ---
st.subheader("🎟️ Sana Özel Aşk Kuponları")
st.write("Dikkat: Bu kuponlar 'Bozdur' denildiği an yok olur! ❤️")

# Kuponların durumunu hafızada tutalım
if 'kuponlar' not in st.session_state:
    st.session_state.kuponlar = {
        'kahve': True,
        'film': True,
        'sarilma': True,
        'yemek': True
    }

col1, col2 = st.columns(2)

with col1:
    if st.session_state.kuponlar['kahve']:
        st.markdown("<div class='kupon-karti'><b>☕️ Kahve Ismarlama</b><br><small>Nil tarafından özenle yapılır.</small></div>", unsafe_allow_html=True)
        if st.button("Kuponu Kullan: ☕️", key="k1"):
            st.session_state.kuponlar['kahve'] = False
            st.snow()
            st.toast("Kupon kullanıldı ve yok oldu! Kahven hazırlanıyor. ❤️")
            st.rerun()

    if st.session_state.kuponlar['film']:
        st.markdown("<div class='kupon-karti'><b>🎬 Film Seçme Hakkı</b><br><small>Bu akşam kumanda tamamen sende!</small></div>", unsafe_allow_html=True)
        if st.button("Kuponu Kullan: 🎬", key="k2"):
            st.session_state.kuponlar['film'] = False
            st.snow()
            st.toast("Kupon kullanıldı ve yok oldu! Filmi seçme sırası sende. 😊")
            st.rerun()

with col2:
    if st.session_state.kuponlar['sarilma']:
        st.markdown("<div class='kupon-karti'><b>🧸 Sonsuz Sarılma</b><br><small>Günün her anında geçerlidir.</small></div>", unsafe_allow_html=True)
        if st.button("Kuponu Kullan: 🧸", key="k3"):
            st.session_state.kuponlar['sarilma'] = False
            st.snow()
            st.toast("Kupon kullanıldı! Nil hemen yanına geliyor. ❤️")
            st.rerun()

    if st.session_state.kuponlar['yemek']:
        st.markdown("<div class='kupon-karti'><b>🍕 Favori Yemek</b><br><small>Akşam ne yeneceğine sen karar ver.</small></div>", unsafe_allow_html=True)
        if st.button("Kuponu Kullan: 🍕", key="k4"):
            st.session_state.kuponlar['yemek'] = False
            st.snow()
            st.toast("Kupon kullanıldı! Menü tamamen sende. 🍕")
            st.rerun()

# Eğer hiç kupon kalmadıysa
if not any(st.session_state.kuponlar.values()):
    st.info("💡 Tüm kuponlarını kullandın! Ama Nil'in sevgisi sınırsız. Sayfayı yenilersen kuponlar geri gelir. 😉")
