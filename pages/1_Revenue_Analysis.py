# pages/1_Revenue_Analysis.py
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Revenue Analysis", page_icon="💰", layout="wide")
st.title("💰 Revenue Analysis")
st.subheader("""
Analyze revenue distribution across categories and platforms here. 
This dashboard showcases category contributions, total earnings, 
and platform-wise revenue performance for a clear financial overview.
""")



# -------------------------
# 1) Load data (cached)
# -------------------------
@st.cache_data
def load_data(path="../Sales/Revenue.csv"):
    df = pd.read_csv(path)
    # ensure numeric column for revenue
    if 'Order Value (INR)' in df.columns:
        df['Order Value (INR)'] = pd.to_numeric(df['Order Value (INR)'], errors='coerce').fillna(0)
    # ensure Order ID is string (so count works)
    if 'Order ID' in df.columns:
        df['Order ID'] = df['Order ID'].astype(str)
    # parse date if present
    if 'Order Date' in df.columns:
        df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')
    return df

# Change this path if your CSV is elsewhere
DATA_PATH = "../Sales/Revenue.csv"

try:
    df_sales = load_data(DATA_PATH)
except FileNotFoundError:
    st.error(f"Data file not found at `{DATA_PATH}`. Put `Revenue.csv` in the `Sales/` folder or update the path.")
    st.stop()

# -------------------------
# 2) Sidebar filters
# -------------------------
st.sidebar.header("Filters")

if 'Platform' in df_sales.columns:
    platform_options = sorted(df_sales['Platform'].dropna().unique())
    selected_platforms = st.sidebar.multiselect("Platform", options=platform_options, default=platform_options)
else:
    platform_options = []
    selected_platforms = []

df = df_sales.copy()
if selected_platforms:
    df = df[df['Platform'].isin(selected_platforms)]

# -------------------------
# 3) KPIs
# -------------------------
st.subheader("KPI Summary")
total_revenue = df['Order Value (INR)'].sum() if 'Order Value (INR)' in df.columns else 0
avg_order_value = df['Order Value (INR)'].mean() if 'Order Value (INR)' in df.columns else 0
total_orders = df['Order ID'].count() if 'Order ID' in df.columns else len(df)

c1, c2, c3 = st.columns(3)
c1.metric("Total Revenue", f"₹{total_revenue:,.0f}")
c2.metric("Average Order Value", f"₹{avg_order_value:,.2f}")
c3.metric("Total Orders", f"{total_orders:,}")

# -------------------------
# 4) Total Orders per Platform (bar)
# -------------------------
st.header("\n")
st.subheader("Total Orders (per Platform)")
if {'Platform', 'Order ID'}.issubset(df.columns):
    orders_table = df.groupby('Platform')['Order ID'].count().sort_values(ascending=False).reset_index(name='Total Orders')
    fig_orders = px.bar(orders_table, x='Platform', y='Total Orders', text='Total Orders',color='Platform')
    fig_orders.update_traces(texttemplate='%{text:,}', textposition='outside')
    st.plotly_chart(fig_orders, use_container_width=True)
else:
    st.info("Requires `Platform` and `Order ID` columns to show Total Orders chart.")

# -------------------------
# 5) Platform-wise Sales (horizontal bar)
# -------------------------
st.header('\n')
st.subheader("Platform-wise Total Sales")
if {'Platform', 'Order Value (INR)'}.issubset(df.columns):
    platform_sales = df.groupby('Platform')['Order Value (INR)'].sum().reset_index()
    platform_sales['Total Sales (INR, Lakh)'] = (platform_sales['Order Value (INR)'] / 100000).round(2)
    platform_sales = platform_sales.sort_values('Total Sales (INR, Lakh)', ascending=False)
    fig_sales = px.bar(platform_sales, x='Total Sales (INR, Lakh)', y='Platform', orientation='h',
                       text='Total Sales (INR, Lakh)', color='Platform')
    fig_sales.update_traces(texttemplate='%{text:.2f}', textposition='outside')
    st.plotly_chart(fig_sales, use_container_width=True)
else:
    st.info("Requires `Platform` and `Order Value (INR)` columns to show Platform Sales.")


# -------------------------
# Most & Least Ordered Category per Platform
# -------------------------
st.header('\n')
st.subheader("Most & Least Ordered Category per Platform")

if {'Platform', 'Product Category', 'Order ID'}.issubset(df.columns):
    # Count orders per platform and category
    cat_count = df.groupby(['Platform', 'Product Category'])['Order ID'].count().reset_index(name='Orders')
    
    # Compute total orders per platform
    cat_count['Platform Total'] = cat_count.groupby('Platform')['Orders'].transform('sum')
    
    # Compute % contribution per category
    cat_count['Percentage'] = (cat_count['Orders'] / cat_count['Platform Total'] * 100).round(2)
    
    # Most ordered per platform
    top = cat_count.loc[cat_count.groupby('Platform')['Percentage'].idxmax()]
    top = top[['Platform', 'Product Category', 'Orders', 'Percentage']].rename(
        columns={'Product Category':'Top Category', 'Orders':'Top Orders', 'Percentage':'Top %'}
    )
    
    # Least ordered per platform
    bottom = cat_count.loc[cat_count.groupby('Platform')['Percentage'].idxmin()]
    bottom = bottom[['Platform', 'Product Category', 'Orders', 'Percentage']].rename(
        columns={'Product Category':'Bottom Category', 'Orders':'Bottom Orders', 'Percentage':'Bottom %'}
    )
    
    # Combine top & bottom
    most_least = pd.merge(top, bottom, on='Platform')
    
    # Display table
    st.table(most_least)
    
    # Stacked bar chart showing percentage breakdown for visual comparison
    chart_cat = px.bar(
        cat_count,
        x='Platform',
        y='Percentage',
        color='Product Category',
        title='Category Breakdown per Platform (Percentage)',
        text='Percentage',
        barmode='stack'
    )
    chart_cat.update_traces(texttemplate='%{text:.2f}%', textposition='inside', textfont_size=14, textfont_color='white')
    chart_cat.update_layout(yaxis_title='Percentage', xaxis_title='Platform', legend_title='Product Category', height=500)
    
    st.plotly_chart(chart_cat, use_container_width=True)
    
else:
    st.info("Requires `Platform`, `Product Category`, and `Order ID` columns to show most/least ordered categories.")



# -------------------------
# 7) Revenue per Order (scatter + table)
# -------------------------
st.header('\n')
st.subheader("Revenue per Order By Platform (INR)")
if {'Platform', 'Order Value (INR)', 'Order ID'}.issubset(df.columns):
    total_by_platform = df.groupby('Platform').agg({
        'Order Value (INR)': 'sum',
        'Order ID': 'count'
    }).rename(columns={'Order Value (INR)': 'Total Sales (INR)', 'Order ID': 'Total Orders'})
    total_by_platform['Revenue per Order (INR)'] = (total_by_platform['Total Sales (INR)'] / total_by_platform['Total Orders']).round(2)
    rpo = total_by_platform.reset_index().sort_values('Revenue per Order (INR)', ascending=False)
    fig_rpo = px.scatter(rpo, x='Platform', y='Revenue per Order (INR)', size='Revenue per Order (INR)',
                         hover_name='Platform', size_max=80,color='Platform')
    st.plotly_chart(fig_rpo, use_container_width=True)
    st.dataframe(rpo[['Platform', 'Total Orders', 'Total Sales (INR)', 'Revenue per Order (INR)']])
else:
    st.info("Requires `Platform`, `Order Value (INR)`, and `Order ID` columns to show Revenue per Order.")

# -------------------------
# 8) Category contribution to overall sales (grouped bar chart)
# -------------------------
st.header('\n')
st.subheader("Category Contribution % per Platform")

if {'Platform', 'Product Category', 'Order Value (INR)'}.issubset(df.columns):
    # Group sales by Platform and Product Category
    category_sales = df.groupby(['Platform', 'Product Category'])['Order Value (INR)'].sum()

    # Compute % contribution of each category to the total per platform
    category_contribution = (category_sales / category_sales.groupby(level=0).transform('sum') * 100).round(1)

    # Reset index for plotting
    category_contribution = category_contribution.reset_index(name='Contribution (%)')

    # Create grouped bar chart
    chart_category = px.bar(
        category_contribution,
        x='Platform',
        y='Contribution (%)',
        color='Product Category',
        barmode='group',
        text='Contribution (%)'
    )

    # Style labels and layout
    chart_category.update_traces(
        textposition='outside',
        textfont_color='white',
        textfont_size=11
    )

    chart_category.update_layout(
        yaxis_title='Contribution (%)',
        xaxis_title='Platform',
        legend_title='Product Category',
        height=500
    )

    st.plotly_chart(chart_category, use_container_width=True)
    st.dataframe(category_contribution.sort_values(['Platform', 'Contribution (%)'], ascending=[True, False]))
else:
    st.info("Requires `Platform`, `Product Category`, and `Order Value (INR)` columns to show category contribution.")


