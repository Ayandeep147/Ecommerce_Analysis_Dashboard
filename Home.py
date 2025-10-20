import streamlit as st

st.set_page_config(page_title="E-commerce Dashboard", page_icon="🛒", layout="wide")

# --- Title section ---
st.title("🛒 E-commerce Performance Dashboard")
st.subheader("Analyze revenue trends and customer reviews across platforms")
st.write("Select a section below to explore:")

# --- Navigation buttons ---
col1, col2, col3, col4, col5 = st.columns([1, 2, 2, 2, 1])

with col2:
    if st.button("📊 Revenue Analysis", use_container_width=True):
        st.switch_page("1_Revenue_Analysis")

with col3:
    if st.button("⭐ Review Analysis", use_container_width=True):
        st.switch_page("2_Review_Analysis")

with col4:
    if st.button("📘 Project Overview", use_container_width=True):
        st.switch_page("3_Project_Overview")

# --- Spacer before footer ---
st.write("")
st.write("")
st.write("---")

# --- Footer message ---
st.markdown("### 💡 Delivering insights from top online platforms for smarter business growth")
st.caption("Powered by data from leading E-commerce apps.")

# --- Platform logos (pure Streamlit way) ---
colA, colB, colC = st.columns(3)

with colA:
    st.image("Images/Jiomart.png", width=110)
    #st.caption("JioMart")

with colB:
    st.image("Images/Swiggy.png", width=130)
    #st.caption("Swiggy")

with colC:
    st.image("Images/Blinkit.svg", width=100)
    #st.caption("Blinkit")

