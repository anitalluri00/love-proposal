# app.py
import streamlit as st
from PIL import Image
import base64
import os

# --- Config ---
st.set_page_config(page_title="A Question for Yashwitha 💌", page_icon="❤️", layout="centered")

# Paths (change if you keep a different structure)
PHOTO_PATH = "assets/photos/yashwitha.jpg"   # <-- place your image here
YOUR_PHOTO_PATH = "assets/photos/you.jpg"    # optional
AUDIO_PATH = "assets/audio/proposal_song.mp3"  # optional

# Helper to load image safely
def load_image(path):
    if os.path.exists(path):
        return Image.open(path)
    return None

# Optional audio loader
def load_audio(path):
    if os.path.exists(path):
        with open(path, "rb") as f:
            return f.read()
    return None

# Heart animation CSS + HTML
HEART_CSS = """
<style>
:root {
  --heart-size: 40px;
}
.love-container{
  text-align:center;
  margin-top: 10px;
}
.heart {
  display:inline-block;
  width:var(--heart-size);
  height:var(--heart-size);
  position:relative;
  transform: rotate(-45deg);
  margin: 0 6px;
  animation: float 3s ease-in-out infinite;
  opacity: 0.95;
}
.heart::before,
.heart::after{
  content: "";
  width: var(--heart-size);
  height: var(--heart-size);
  border-radius: 50%;
  background: linear-gradient(135deg,#ff5f6d,#ffc371);
  position:absolute;
  top:0;
  left:0;
}
.heart::before { left: 50%; transform: translateX(-50%); }
.heart::after  { top: -50%; transform: translateY(50%); left: 0; }
@keyframes float {
  0% { transform: translateY(0) rotate(-45deg) scale(1); }
  50% { transform: translateY(-18px) rotate(-45deg) scale(1.06); }
  100% { transform: translateY(0) rotate(-45deg) scale(1); }
}

/* Blinking text */
.propose {
  font-family: "Georgia", serif;
  font-size: 1.6rem;
  letter-spacing: 0.2px;
  animation: pulse 2.8s infinite;
  color: #6b2232;
  margin-top: 8px;
}
@keyframes pulse {
  0% { opacity: 0.95; transform: scale(1); }
  50% { opacity: 1; transform: scale(1.02); }
  100% { opacity: 0.95; transform: scale(1); }
}

/* Card-like container */
.proposal-card {
  background: linear-gradient(180deg, rgba(255,255,255,0.9), rgba(255, 245, 245,0.9));
  border-radius: 12px;
  padding: 18px;
  box-shadow: 0 6px 24px rgba(107,34,50,0.08);
}
</style>
"""

# Page header
st.markdown("<h1 style='text-align:center; margin-bottom:6px;'>For Chinthala Yashwitha</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; margin-top: -10px; color: #6b2232;'>A little digital note — with a big heart.</p>", unsafe_allow_html=True)

# Main container
st.markdown("<div class='proposal-card'>", unsafe_allow_html=True)

# Load and display Yashwitha's photo
img = load_image(PHOTO_PATH) or load_image("/mnt/data/WhatsApp Image 2025-11-11 at 06.38.58.jpeg")
if img:
    st.image(img, caption="Chinthala Yashwitha", use_column_width=True)
else:
    st.warning("No photo found. Add one at: `assets/photos/yashwitha.jpg` (or update PHOTO_PATH).")

# Love symbols + animated hearts
st.markdown(HEART_CSS, unsafe_allow_html=True)
st.markdown("""
<div class="love-container">
  <div class="heart"></div>
  <div class="heart"></div>
  <div class="heart"></div>
</div>
""", unsafe_allow_html=True)

# Romantic message (you can edit the text)
message_md = """
<div style="text-align:center; margin-top:12px;">
  <p class="propose">Yashwitha — you made the ordinary glow. Will you be the reason I smile every day?</p>
</div>
"""
st.markdown(message_md, unsafe_allow_html=True)

# Interactive buttons
col1, col2, col3 = st.columns([1,1,1])
with col1:
    if st.button("Say 'Yes' 💍"):
        st.balloons()
        st.success("You made my world. Thank you, Yashwitha. ❤️")
with col2:
    if st.button("Ask again ✉️"):
        st.info("One more time with feeling... I promise it's sincere.")
with col3:
    if st.button("Not yet 💬"):
        st.warning("I understand. I'll always respect your feelings.")

# Optionally show your photo (if you added one)
your_img = load_image(YOUR_PHOTO_PATH)
if your_img:
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.subheader("From me —")
    st.image(your_img, width=220)

# Optional audio playback
audio_bytes = load_audio(AUDIO_PATH)
if audio_bytes:
    st.markdown("<hr/>", unsafe_allow_html=True)
    st.audio(audio_bytes, format="audio/mp3")

# Footer / instructions
st.markdown("</div>", unsafe_allow_html=True)
st.info("To change the text, edit `message_md` in `app.py`. To change photo, replace the image in `assets/photos/` and commit.")
