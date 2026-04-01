import streamlit as st
import pandas as pd
import random
import os
import time
from datetime import datetime
from dateutil.relativedelta import relativedelta

# --- SAYFA AYARLARI VE TASARIM ---
st.set_page_config(page_title="Sadece Biz", page_icon="❤️", layout="centered")

st.markdown("""
    <style>
    .stApp { background-color: #fffafa; }
    .ana-baslik { text-align: center; color: #d63031; font-size: 2.2rem; font-weight: bold; margin-bottom: 5px; }
    .timer-box { 
        background-color: white; 
        padding: 25px; 
        border-radius: 20px; 
        border: 1px solid #ff7675; 
        text-align: center; 
        box-shadow: 0px 4px 15px rgba(214, 48, 49, 0.1);
        margin-bottom: 30px;
    }
    .mesaj-kutusu {
        background-color: #ffffff;
        padding: 35px;
        border-radius: 15px;
        text-align: center;
        font-size: 22px;
        color: #2d3436;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.05);
        margin-top: 20px;
        border-left: 5px solid #d63031;
    }
    .stButton>button {
        background-color: #d63031;
        color: white;
        border-radius: 25px;
        padding: 10px;
        width: 100%;
        border: none;
    }
    </style>
    """, unsafe_allow_html=True)

# --- 1. ZAMAN SAYACI (27 Ocak 2024) ---
baslangic = datetime(2024, 1, 27, 0, 0)
simdi = datetime.now()
fark = relativedelta(simdi, baslangic)

st.markdown("<div class='ana-baslik'>❤️ İyi ki Varsın ❤️</div>", unsafe_allow_html=True)

st.markdown(f"""
    <div class='timer-box'>
        <p style='color: #636e72; font-size: 1.1rem; margin-bottom: 10px;'>27 Ocak 2024'ten beri...</p>
        <h2 style='color: #d63031; margin: 0;'>{fark.years} Yıl, {fark.months} Ay, {fark.days} Gün</h2>
        <p style='color: #ff7675; font-weight: bold; margin-top: 5px;'>{fark.hours} Saat ve {fark.minutes} Dakikadır seninleyim.</p>
    </div>
    """, unsafe_allow_html=True)

# --- 2. AŞK NOTLARI VERİTABANI ---
DOSYA = "notlar.csv"
if not os.path.exists(DOSYA):
    varsayilan = pd.DataFrame([
        {"Not": "Gülüşün, tüm karmaşık denklemlerin en güzel çözümü gibi."},
        {"Not": "Seninle geçen her dakika, ömrümün en değerli yatırımı."},
        {"Not": "En stresli anlarımda bile senin sesin benim huzur alanım."},
        {"Not": "Geleceğe dair kurduğum her hayalin başrolünde sen varsın."},
        {"Not": "Seninleyken zamanın nasıl geçtiğini gerçekten anlamıyorum."}
    ])
    varsayilan.to_csv(DOSYA, index=False)

df = pd.read_csv(DOSYA)

# --- 3. İNTERAKTİF BÖLÜM ---
st.write("")
if 'su_anki_not' not in st.session_state:
    st.session_state.su_anki_not = "Sana söylemek istediğim bir şey var... 👇"

if st.button("✨ Kalbimden Bir Not Oku ✨"):
    st.session_state.su_anki_not = random.choice(df['Not'].tolist())
    st.balloons()

st.markdown(f"<div class='mesaj-kutusu'>\"{st.session_state.su_anki_not}\"</div>", unsafe_allow_html=True)

st.divider()

# --- 4. YENİ NOT EKLEME (GİZLİ) ---
with st.expander("🤫 Gelecekte Okuyacağı Notları Ekle"):
    with st.form("yeni_not_formu", clear_on_submit=True):
        yeni = st.text_area("Ona bir sevgi sözü bırak:")
        if st.form_submit_button("Notu Sisteme Kaydet"):
            if yeni:
                yeni_df = pd.DataFrame([{"Not": yeni}])
                df = pd.concat([df, yeni_df], ignore_index=True)
                df.to_csv(DOSYA, index=False)
                st.success("Bu not artık listemizde, bir gün karşısına çıkacak!")
