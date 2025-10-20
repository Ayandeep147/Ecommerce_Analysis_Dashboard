import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Review Analysis", page_icon="📝", layout="wide")
st.title("📝 Review Analysis")

st.subheader("""
Explore customer perceptions and delivery performance metrics here. 
This analysis focuses on identifying top-performing platforms in terms of speed, service quality, 
accuracy, and city-wise popularity based on review data.
""")


# ----------------------
# Load data
# ----------------------
@st.cache_data
def load_data(path="../Sales/Reviews.csv"):
    df = pd.read_csv(path)
    # Ensure numeric columns
    df['Customer Service Rating'] = pd.to_numeric(df['Customer Service Rating'], errors='coerce').fillna(0)
    df['Delivery Time (min)'] = pd.to_numeric(df['Delivery Time (min)'], errors='coerce').fillna(0)
    df['Order Accuracy'] = pd.to_numeric(df['Order Accuracy'], errors='coerce').fillna(0)
    df['Product Availability'] = pd.to_numeric(df['Product Availability'], errors='coerce').fillna(0)
    return df

df_review = load_data("../Sales/Reviews.csv")  # change path if needed

# ----------------------
# Sidebar filters
# ----------------------
st.sidebar.header("Filters")
platforms = sorted(df_review['Agent Name'].dropna().unique())
selected_platforms = st.sidebar.multiselect("Platform", platforms, default=platforms)

locations = sorted(df_review['Location'].dropna().unique())
selected_locations = st.sidebar.multiselect("Location", locations, default=locations)

df = df_review[(df_review['Agent Name'].isin(selected_platforms)) & 
               (df_review['Location'].isin(selected_locations))]

# ----------------------
# KPIs
# ----------------------
st.subheader("Key Metrics")

if len(selected_platforms) == 1:
    agent = selected_platforms[0]

    avg_time = df_review[df_review['Agent Name'] == agent]['Delivery Time (min)'].mean()
    formatted_time = f"{int(avg_time)} min {int((avg_time - int(avg_time)) * 60)} sec"

    avg_rating = df_review[df_review['Agent Name'] == agent]['Customer Service Rating'].mean()

    order_acc = df_review[df_review['Agent Name'] == agent]['Order Accuracy'].mean() * 100
    product_avail = df_review[df_review['Agent Name'] == agent]['Product Availability'].mean() * 100

    # Create 4 columns to show metrics in a single line
    col1, col2, col3, col4 = st.columns(4)

    col1.metric(label=f"Avg Delivery Time ({agent})", value=formatted_time)
    col2.metric(label=f"Avg Customer Rating ({agent})", value=f"{avg_rating:.1f} ⭐")
    col3.metric(label=f"Order Accuracy ({agent})", value=f"{order_acc:.1f}%")
    col4.metric(label=f"Product Availability ({agent})", value=f"{product_avail:.1f}%")

else:
    st.info("⚠️ Select a single agent to view Key Metrics.")


# ----------------------
# Average Delivery Time chart
# ----------------------
st.subheader("Average Delivery Time per Platform")
if df.empty:
    st.info("⚠️ No data available to display Average Delivery Time. Please adjust filters.")
else:
    avg_delivery_df = df.groupby('Agent Name')['Delivery Time (min)'].mean().reset_index()
    avg_delivery_df['Formatted Time'] = avg_delivery_df['Delivery Time (min)'].apply(
        lambda x: f"{int(x)} min {int((x - int(x))*60)} sec"
    )
    fig_delivery = px.bar(
        avg_delivery_df,
        x='Agent Name',
        y='Delivery Time (min)',
        text='Formatted Time',
        title="Average Delivery Time per Platform",
        color='Agent Name'
    )
    fig_delivery.update_traces(textposition='inside', textfont_color='white', textfont_size=16)
    st.plotly_chart(fig_delivery, use_container_width=True)

# ----------------------
# Most Used Platform per Location
# ----------------------
st.subheader("Platform Usage per Location")

df_filtered = df.copy()

if df_filtered.empty:
    st.info("⚠️ No data available for the selected filters.")

# Only show this section if all 3 platforms are selected
elif len(selected_platforms) == 3:   # assuming your filter variable is selected_agents
    if len(selected_locations) > 1:
        # Multiple locations → show only most used platform per location
        most_used_platform = (
            df_filtered.groupby('Location')['Agent Name']
            .agg(lambda x: x.value_counts().idxmax())
            .reset_index()
        )
        most_used_platform.columns = ['Location', 'Most Used Platform']

        fig_sunburst = px.sunburst(
            most_used_platform,
            path=['Location', 'Most Used Platform'],
            color='Most Used Platform',
            color_discrete_sequence=px.colors.qualitative.Set3
        )
        st.plotly_chart(fig_sunburst, use_container_width=True)

    else:
        # Single location → show all platforms with percentages
        location = selected_locations[0]
        df_loc = df_filtered[df_filtered['Location'] == location]
        platform_counts = df_loc['Agent Name'].value_counts().reset_index()
        platform_counts.columns = ['Platform', 'Count']
        platform_counts['Percentage'] = (platform_counts['Count'] / platform_counts['Count'].sum()) * 100

        # Sunburst chart
        fig_sunburst = px.sunburst(
            platform_counts,
            path=['Platform'],          # single level sunburst
            values='Percentage',
            title=f"Platform Usage in {location}",
            color='Platform',
            color_discrete_sequence=px.colors.qualitative.Set3,
            hover_data={'Count': True, 'Percentage': ':.1f'}
        )

        # Add text inside slices
        fig_sunburst.update_traces(
            texttemplate='%{label}<br>%{value:.1f}%',
            textinfo='label+value',
            insidetextfont=dict(color='white', size=16)
        )

        st.plotly_chart(fig_sunburst, use_container_width=True)

else:
    st.info("ℹ️ Platform usage chart is available only when all 3 platforms are selected.")

    


# ----------------------
# Avg Customer Feedback Heatmap
# ----------------------
st.subheader("Average Customer Feedback per Platform & Location")
if df.empty:
    st.info("⚠️ No data available to display Customer Feedback. Please adjust filters.")
else:
    avg_feedback = df.groupby(['Location','Agent Name'])['Customer Service Rating'].mean().reset_index()
    fig_heatmap = px.density_heatmap(
        avg_feedback,
        x='Agent Name',
        y='Location',
        z='Customer Service Rating',
        color_continuous_scale='RdYlGn',
    )
    fig_heatmap.update_layout(yaxis=dict(autorange="reversed"), height=600,coloraxis_colorbar_title="Avg Rating ⭐")
    st.plotly_chart(fig_heatmap, use_container_width=True)

# ----------------------
# Order Accuracy & Product Availability per Platform
# ----------------------
st.subheader("Order Accuracy & Product Availability per Platform")
if df.empty:
    st.info("⚠️ No data available to display Order Accuracy & Product Availability. Please adjust filters.")
else:
    # Aggregate per platform and convert 0-1 to %
    order_product = df.groupby('Agent Name')[['Order Accuracy','Product Availability']].mean().reset_index()
    order_product['Order Accuracy'] = order_product['Order Accuracy'] * 100
    order_product['Product Availability'] = order_product['Product Availability'] * 100

    order_product_melted = order_product.melt(
        id_vars='Agent Name', 
        value_vars=['Order Accuracy','Product Availability'], 
        var_name='Metric', 
        value_name='Percentage'
    )

    fig_order = px.bar(
        order_product_melted,
        x='Agent Name',
        y='Percentage',
        color='Metric',
        barmode='group',
        text='Percentage',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    fig_order.update_traces(texttemplate='%{text:.1f}%', textposition='inside', textfont_color='white')
    st.plotly_chart(fig_order, use_container_width=True)



