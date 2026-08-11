# 🛒 E-Commerce Platform & Delivery Analysis

An interactive **Streamlit dashboard** that analyzes and visualizes **revenue and customer review data** from leading e-commerce and delivery platforms such as **Blinkit**, **Jiomart**, and **Swiggy**.  
This project provides insights into **sales trends, customer sentiments, and platform performance** based on real or simulated data.

---

## 🚀 Features

- 📊 **Revenue Analysis:**  
  Explore total and average revenue trends across multiple platforms.  
  Visualize performance using dynamic charts and filters.

- 💬 **Customer Review Analysis:**  
  Analyze customer feedback and ratings.  
  Understand sentiment distribution and customer satisfaction levels.

- 🧾 **Project Overview:**  
  Get an outline of the project objectives, dataset, and methodology.

- 🧠 **About Section:**  
  Provides background information and contributors’ details.

---

## 🗂️ Project Structure

```
E-Commerce Platform & Delivery Analysis/
│
├── Home.py                       # Main Streamlit entry file
├── .streamlit/
│   └── config.toml               # Streamlit theme configuration
│
├── Images/                       # Platform logos and icons
│   ├── Blinkit.png
│   ├── Blinkit.svg
│   ├── Jiomart.png
│   └── Swiggy.png
│
├── Pages/                        # Multi-page dashboard sections
│   ├── 1_Revenue_Analysis.py
│   ├── 2_Review_Analysis.py
│   ├── 3_Project_Overview.py
│   └── 4_About.py
│
├── Sales/                        # Dataset folder
│   ├── Revenue.csv
│   └── Reviews.csv
│
└── README.md                     # Project documentation (this file)
```

---

## ⚙️ Installation & Setup

### 1. Clone this repository
```bash
git clone https://github.com/<your-username>/Ecommerce_Delivery_Dashboard.git
cd Ecommerce_Delivery_Dashboard
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

If you don’t have a `requirements.txt`, install Streamlit manually:
```bash
pip install streamlit pandas matplotlib
```

### 3. Run the app
```bash
streamlit run Home.py
```

---

## 📈 Technologies Used

- **Python 3**
- **Streamlit** – Web dashboard framework  
- **Pandas** – Data manipulation  
- **Plotly** – Visualization  
- **CSV Datasets** – Revenue and review data  

---

## 📊 Dataset Overview

| File | Description |
|------|--------------|
| `Revenue.csv` | Contains platform-wise sales and revenue data |
| `Reviews.csv` | Includes customer ratings and feedback details |

---

## 🧑‍💻 Contributors

- **Ayandeep Roy** – Developer
- **Ankit Saha** – Developer

---

## 📜 License

This project is open-source and available under the **MIT License**.
