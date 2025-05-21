import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns

def display_summary_metrics(data):
    """Display summary metrics cards."""
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.metric("Total Products", len(data['nama_stok'].unique()))
    
    with col2:
        pasti_dibeli = data[data['kategori'] == 'Pasti Dibeli'].shape[0]
        st.metric("Products to Buy", pasti_dibeli)
    
    with col3:
        st.metric("Prediction Days", 30)

def plot_top_products(data):
    """Plot top products by predicted demand."""
    top_products = data.groupby('nama_stok')['predicted_quantity'].sum().nlargest(5)
    
    fig, ax = plt.subplots(figsize=(10, 4))
    sns.barplot(x=top_products.values, y=top_products.index, palette="Blues_d", ax=ax)
    ax.set_xlabel("Total Predicted Quantity")
    ax.set_title("Top 5 Products by Demand")
    st.pyplot(fig)

def plot_demand_forecast(data, product_name):
    """Plot demand forecast for a specific product."""
    product_data = data[data['nama_stok'] == product_name].sort_values('tanggal')
    
    fig, ax = plt.subplots(figsize=(10, 4))
    ax.plot(product_data['tanggal'], product_data['predicted_quantity'], label='Predicted')
    ax.fill_between(
        product_data['tanggal'],
        product_data['lower_bound'],
        product_data['upper_bound'],
        alpha=0.2,
        label='Confidence Range'
    )
    ax.set_xlabel("Date")
    ax.set_ylabel("Quantity")
    ax.set_title(f"Demand Forecast for {product_name}")
    ax.legend()
    st.pyplot(fig)