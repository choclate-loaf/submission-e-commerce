import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ========================
# Load Data
# ========================
@st.cache_data
def load_data():
    orders = pd.read_csv("data/orders_dataset.csv")
    payments = pd.read_csv("data/order_payments_dataset.csv")
    customers = pd.read_csv("data/customers_dataset.csv")

    # Convert datetime
    orders['order_purchase_timestamp'] = pd.to_datetime(orders['order_purchase_timestamp'], errors='coerce')

    # Merge data
    df = orders.merge(payments, on='order_id')
    df = df.merge(customers, on='customer_id')

    return df

df = load_data()

# ========================
# Title
# ========================
st.title("📊 E-Commerce Dashboard")
st.write("Analisis Tren Penjualan & Segmentasi Pelanggan")

# ========================
# Filter
# ========================
st.sidebar.header("Filter Data")

df['year'] = df['order_purchase_timestamp'].dt.year
year_filter = st.sidebar.selectbox("Pilih Tahun", sorted(df['year'].dropna().unique()))

df = df[df['year'] == year_filter]

# ========================
# KPI
# ========================
total_orders = df['order_id'].nunique()
total_revenue = df['payment_value'].sum()

col1, col2 = st.columns(2)

col1.metric("Total Orders", f"{total_orders:,}")
col2.metric("Total Revenue", f"{total_revenue:,.2f}")

# ========================
# Monthly Trend
# ========================
st.subheader("📈 Tren Bulanan")

df['month'] = df['order_purchase_timestamp'].dt.to_period('M').astype(str)

monthly_orders = df.groupby('month')['order_id'].nunique()
monthly_revenue = df.groupby('month')['payment_value'].sum()

fig, ax = plt.subplots()
monthly_orders.plot(ax=ax, marker='o', label='Orders')
monthly_revenue.plot(ax=ax, marker='o', label='Revenue')

ax.set_title("Tren Order & Revenue")
ax.legend()
st.pyplot(fig)

# ========================
# RFM Analysis
# ========================
st.subheader("👥 RFM Analysis")

import datetime as dt
current_date = df['order_purchase_timestamp'].max()

rfm = df.groupby('customer_id').agg({
    'order_purchase_timestamp': lambda x: (current_date - x.max()).days,
    'order_id': 'count',
    'payment_value': 'sum'
})

rfm.columns = ['Recency', 'Frequency', 'Monetary']

# Plot Frequency
fig2, ax2 = plt.subplots()
sns.histplot(rfm['Frequency'], bins=10, ax=ax2)
ax2.set_title("Distribusi Frequency Pelanggan")

st.pyplot(fig2)

# ========================
# Top Customers
# ========================
st.subheader("🏆 Top Customers")

top_customers = rfm.sort_values(by='Monetary', ascending=False).head(10)

st.dataframe(top_customers)