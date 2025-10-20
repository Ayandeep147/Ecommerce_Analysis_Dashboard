import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="About Me | Ayan Roy", page_icon="👨‍💻")

# --- TITLE ---
st.title("👨‍💻 About the Developer")
st.write("---")

# --- INTRODUCTION ---
st.subheader("Hi, I'm Ayandeep Roy!")
st.write("""
I'm a B.Tech Computer Science and Engineering fresher passionate about **data analytics**, **AI-driven insights**, and **creative problem solving**.  
I enjoy turning datasets into meaningful visual stories that reveal real-world patterns and decisions.
""")

# --- SKILLS ---
st.write("---")
st.subheader("🧠 Skills & Tools")
st.write("""
- 💻 Python (Pandas, Plotly, NumPy)
- 📊 Data Visualization & Analysis
- 🧾 MySQL
- ⚡ Streamlit Dashboarding
- 🧩 Problem Solving
""")


# --- CONTACT INFO ---
st.write("---")
st.subheader("📫 Get in Touch")
col1, col2 = st.columns(2)
with col1:
    st.write("""
    - 📧 Email: ayandeeproy460@example.com 
    """)
with col2:
    st.write("""
    - 💼 LinkedIn: [linkedin.com/in/ayandeeproy](https://linkedin.com/in/ayandeep-roy-874176244)
    - 📍 Location: India
    """)



