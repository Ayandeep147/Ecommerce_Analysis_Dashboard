import streamlit as st

# Page title
st.title("📊 Project Overview")
st.markdown("---")

# Project Introduction
st.subheader("About the Project")
st.write("""
The **E-Commerce Platform & Delivery Performance Analysis** project provides a comprehensive overview of 
two critical aspects of an online delivery ecosystem — **Revenue Performance** and **Customer Review Analysis**.

The goal is to identify key business trends, performance gaps, and improvement opportunities 
across multiple platforms such as **Zomato**, **Swiggy**, and **Blinkit**.  
By analyzing both **financial metrics** and **customer experience data**, this project aims to give 
a complete understanding of how each platform performs in different regions.
""")

st.markdown("---")

# Dataset Overview
st.subheader("📂 Datasets Used")
st.write("""
1. **Revenue Dataset** – Contains data related to sales, transactions, and platform-wise revenue across locations.  
   Includes columns like: *Platform, Location, Total Orders, Revenue,Product Category* etc.

2. **Review Dataset** – Focuses on customer feedback and service quality.  
   Includes columns like: *Agent Name, Location, Delivery Time, Service Rating, Order Accuracy, Product Availability,* etc.
""")

st.markdown("---")

# Tools and Technologies
st.subheader("🛠️ Tools & Technologies Used")
st.write("""
- **Python** – For data cleaning, aggregation, and preprocessing.  
- **Pandas** – For data handling and KPI calculation.  
- **Plotly Express** – For creating interactive visualizations and insights.  
- **Streamlit** – For building and deploying the interactive dashboard interface.  
- **Excel / CSV** – As the primary data sources for analysis.
""")

st.markdown("---")

# Key Insights
st.subheader("📈 Key Insights from Analysis")
st.write("""
- **Zomato** received the highest customer satisfaction ratings overall.  
- **Swiggy** showed the **fastest delivery times**, but had slightly lower order accuracy.  
- **Blinkit** performed strongly in **specific high-demand locations**, contributing to revenue spikes.  
- **Product Availability** was the strongest driver of positive reviews.  
- **Weekend orders** recorded **higher order volumes** but also more **delivery delays**.  
- Locations with consistent agent performance showed **higher repeat customer rates**.
""")

st.markdown("---")

# Recommendations
st.subheader("💡 Suggested Solutions & Business Recommendations")
st.write("""
- Enhance **inventory management systems** to improve product availability and reduce order cancellations.  
- Conduct **agent training programs** focused on improving order accuracy and customer communication.  
- Utilize **predictive scheduling** to optimize agent distribution during high-demand hours and weekends.  
- Implement **real-time feedback tracking** to respond quickly to poor customer experiences.  
- Focus marketing and promotions on **locations with strong performance metrics** to maximize revenue growth.  
- Regularly monitor **delivery KPIs and satisfaction metrics** using automated dashboards.
""")

st.markdown("---")

# Navigation
st.info("👉 Use the sidebar to explore detailed **Revenue Analysis** and **Review Analysis** sections.")
