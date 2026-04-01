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
        text-align: center; margin-bottom: 15px;
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

# --- 1. ZAMAN SAYACI (Güncellendi: 19 Ocak 2024) ---
baslangic = datetime(2024, 1, 19, 0, 0)
simdi = datetime.now()
fark = relativedelta(simdi, baslangic)

st.markdown("<div class='ana-baslik'>❤️ İyi ki Varsın ❤️</div>", unsafe_allow_html=True)

st.markdown(f"""
    <div class='timer-box'>
        <p style='color: #636e72; font-size: 1.1rem; margin-bottom: 5px;'>19 Ocak 2024'ten beri...</p>
        <h2 style='color: #d63031; margin: 0;'>{fark.years} Yıl, {fark.months} Ay, {fark.days} Gün</h2>
        <p style='color: #ff7675; font-weight: bold; font-size: 1.2rem;'>{fark.hours} Saat, {fark.minutes} Dakika...</p>
        <p style='color: #b2bec3; font-size: 0.9rem;'>Her saniye seninle daha güzel.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. GENİŞLETİLMİŞ AŞK NOTLARI ---
notlar_listesi = [
    "Gülüşün, çözmeye çalıştığım tüm denklemlerden daha güzel bir sonuç. ❤️",
    "19 Ocak 2024'ten beri kalbimdeki en güzel yer senin.",
    "Seninle içilen o bol köpüklü Türk kahvelerinin tadı başka hiçbir şeyde yok. ☕",
    "Tokyo ve Kyoto hayallerimizi gerçekleştireceğimiz günü iple çekiyorum. ✈️",
    "Kodak kameramın vizöründen gördüğüm en kusursuz manzara sensin. 📸",
    "Senin zekan ve kalbin, hayatımın en mükemmel mühendislik harikası.",
    "En stresli lab raporlarında bile senin desteğin bana güç veriyor.",
    "Seninleyken zamanın nasıl geçtiğini anlamayacak kadar çok seviyorum seni.",
    "Sadece sevgilim değil, en iyi dostum olduğun için teşekkür ederim.",
    "Bakışlarındaki o sıcaklık, dünyadaki en güvenli limanım.",
    "Seninle arabada şarkı söyleyerek yaptığımız yolculuklar favori anılarım. 🚗",
    "Hayatımın en doğru 'Evet'i seninle bu yola çıkmaktı.",
    "Senin her başarında seninle gurur duymayı çok seviyorum.",
    "Hangi dilde söylersem söyleyeyim, seni sevmek kelimelere sığmıyor.",
    "Seninle geçireceğimiz daha binlerce harika günümüz olsun. ❤️"
]

st.subheader("💌 Kalbimden Sana...")
if 'mesaj' not in st.session_state:
    st.session_state.mesaj = "Butona bas ve senin için hazırladığım notlardan birini oku... 👇"

if st.button("✨ Yeni Bir Not Oku ✨"):
    st.session_state.mesaj = random.choice(notlar_listesi)
    st.balloons()

st.markdown(f"<div class='mesaj-kutusu'>\"{st.session_state.mesaj}\"</div>", unsafe_allow_html=True)

st.write("")
st.divider()

# --- 3. DİJİTAL AŞK KUPONLARI ---
st.subheader("🎟️ Sana Özel Aşk Kuponları")
st.write("Dilediğin an kullanabileceğin, reddedilemez hakların!")

col1, col2 = st.columns(2)

with col1:
    st.markdown("<div class='kupon-karti'><b>☕️ Kahve Ismarlama</b><br><small>Merve tarafından özenle yapılır.</small></div>", unsafe_allow_html=True)
    if st.button("Kuponu Kullan: ☕️"):
        st.snow()
        st.toast("Kupon kullanıldı! Kahveler benden. ❤️")

    st.markdown("<div class='kupon-karti'><b>🎬 Film Seçme Hakkı</b><br><small>Bu akşam kumanda tamamen sende!</small></div>", unsafe_allow_html=True)
    if st.button("Kuponu Kullan: 🎬"):
        st.snow()
        st.toast("Kupon kullanıldı! Filmi sen seçiyorsun. 😊")

with col2:
    st.markdown("<div class='kupon-karti'><b>🧸 Sonsuz Sarılma</b><br><small>Günün her anında geçerlidir.</small></div>", unsafe_allow_html=True)
    if st.button("Kuponu Kullan: 🧸"):
        st.snow()
        st.toast("Kupon kullanıldı! Hemen yanındayım. ❤️")

    st.markdown("<div class='kupon-karti'><b>🍕 Favori Yemek</b><br><small>Akşam ne yeneceğine sen karar ver.</small></div>", unsafe_allow_html=True)
    if st.button("Kuponu Kullan: 🍕"):
        st.snow()
        st.toast("Kupon kullanıldı! Menü sende. 🍕")

st.info("💡 Not: Bu kuponlar dijitaldir ve her zaman geçerlidir! ❤️")
