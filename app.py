import streamlit as st
import pandas as pd

st.set_page_config(page_title="History Kids Pro", layout="wide")

# 🎨 PREMIUM UI
st.markdown("""
<style>
body {
    background: linear-gradient(135deg,#0f2027,#203a43,#2c5364);
}
h1, h2, h3 {
    color: gold;
}
.card {
    background: rgba(255,255,255,0.1);
    padding:20px;
    border-radius:15px;
    margin:10px;
    backdrop-filter: blur(10px);
    transition:0.3s;
}
.card:hover {
    transform: scale(1.05);
}
</style>
""", unsafe_allow_html=True)

# 🌍 TITLE
st.title("🌍 World History Learning Platform")
st.write("👶 Learn History in Easy Way | Ashu Mehara")

# 📂 CATEGORY SELECT
category = st.sidebar.selectbox("Choose Category", [
    "World History",
    "Indian History",
    "Temple History"
])

# =========================
# 🌍 WORLD HISTORY
# =========================
if category == "World History":

    st.header("🌍 World History (Kids Friendly)")

    st.image("https://upload.wikimedia.org/wikipedia/commons/a/a3/WW2_collage.png")

    st.markdown("""
### 👶 Easy Explanation:
- World history means duniya ke bade events
- Different countries ka development
- Wars, revolutions aur discoveries

### 🧠 Important Points:
👉 Ancient Civilizations (Egypt, Mesopotamia)  
👉 Medieval Period (Kings, Empires)  
👉 Modern History (Wars, Technology)  
👉 World Wars changed the world  
👉 Countries became independent  

### 🎥 Video Learning
""")

    st.video("https://www.youtube.com/watch?v=NbuUW9i-mHs")

# =========================
# 🇮🇳 INDIAN HISTORY
# =========================
elif category == "Indian History":

    st.header("🇮🇳 Indian History")

    st.image("https://upload.wikimedia.org/wikipedia/commons/1/1d/Mohenjo-daro.jpg")

    st.markdown("""
### 👶 Easy Explanation:
- India ki history bahut purani hai
- Different empires rule karte the

### 🧠 Important Points:
👉 Indus Valley Civilization (planned cities)  
👉 Maurya Empire (Ashoka)  
👉 Gupta Empire (Golden Age)  
👉 Mughal Empire (Akbar)  
👉 British Rule  
👉 1947 Independence  

### 🎥 Video
""")

    st.video("https://www.youtube.com/watch?v=xyz")

# =========================
# 🛕 TEMPLE HISTORY
# =========================
elif category == "Temple History":

    st.header("🛕 Indian Temple History")

    col1, col2 = st.columns(2)

    with col1:
        st.image("https://upload.wikimedia.org/wikipedia/commons/1/1e/Kailasa_temple_ellora.jpg")
        st.markdown("""
### 🛕 Kailash Temple
👉 Ek hi rock se bana  
👉 Ellora caves me hai  
👉 Shiv ji ko dedicate  
        """)

    with col2:
        st.image("https://upload.wikimedia.org/wikipedia/commons/4/4a/Konark_Sun_Temple.jpg")
        st.markdown("""
### ☀️ Konark Sun Temple
👉 Rath shape temple  
👉 Sun God ko dedicate  
👉 Odisha me hai  
        """)

    st.markdown("""
### 👶 Easy Explanation:
- Temples pehle small the
- Baad me bade aur beautiful ban gaye

### 🧠 Temple Styles:
👉 Nagara (North India)  
👉 Dravida (South India)  
👉 Vesara (Mixed)  
""")

    st.video("https://www.youtube.com/watch?v=xyz")

# =========================
# 🎮 QUIZ SYSTEM
# =========================
st.header("🎮 Quick Quiz")

quiz = [
    ("World War 2 kab hua?", ["1914","1939","2000"], 1),
    ("India kab independent hua?", ["1947","2000","1800"], 0),
    ("Kailash Temple kaha hai?", ["Delhi","Ellora","Mumbai"], 1)
]

score = 0

for q, options, ans in quiz:
    st.write(q)
    user = st.radio("Choose answer", options, key=q)
    if st.button("Submit "+q):
        if options.index(user) == ans:
            st.success("Correct 🎉")
            score += 1
        else:
            st.error("Wrong ❌")

st.write("Your Score:", score)

# =========================
# 📊 LEARNING PROGRESS
# =========================
st.header("📊 Progress Chart")

data = pd.DataFrame({
    "Topic":["World","India","Temple"],
    "Progress":[80,60,70]
})

st.bar_chart(data.set_index("Topic"))
