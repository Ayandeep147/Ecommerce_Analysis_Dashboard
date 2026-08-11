import streamlit as st

# --- PAGE SETUP ---
st.set_page_config(page_title="About Us", page_icon="👨‍💻")

# --- TITLE ---
st.title("👨‍💻 About the Team")
st.write("---")

# --- INTRODUCTION ---
st.subheader("Hi, I'm Ayandeep Roy!")
st.write("""
I'm a B.Tech Computer Science and Engineering fresher passionate about **data analytics**, **AI-driven insights**, and **creative problem solving**.  
I enjoy turning datasets into meaningful visual stories that reveal real-world patterns and decisions.
""")

st.subheader("Hi, I'm Ankit Saha!")
st.write("""
I'm a B.Tech Computer Science and Engineering fresher passionate about **web development**.  
I enjoy creating UI which makes it easy for people to navigate.
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
    - 📧 Email: ayandeeproy460@gmail.com 
    """)
    st.write("""
    - 📧 Email: sahaankit2204@gmail.com 
    """)
    
with col2:
    st.write("""
    - 💼 LinkedIn: [linkedin.com/in/ayandeeproy](https://linkedin.com/in/ayandeep-roy-874176244)
    - 💼 LinkedIn: [linkedin.com/in/ankitsaha](https://www.linkedin.com/in/ankit-saha-a06699254/)
    - 📍 Location: India
    """)



