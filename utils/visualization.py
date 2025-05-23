import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.ticker import MaxNLocator
import matplotlib.cm as cm

def display_summary_metrics(data):
    """Display summary metrics cards."""
    col1, col3 = st.columns(2)
    
    with col1:
        st.metric("Total Products", len(data['nama_stok'].unique()))
    
    # with col2:
    #     pasti_dibeli = data[data['kategori'] == 'Pasti Dibeli'].shape[0]
    #     st.metric("Products to Buy", pasti_dibeli)
    
    with col3:
        st.metric("Prediction Days", 30)

def plot_top_products(data):
    """Plot top products by predicted demand."""
    # Get top 10 products (changed from 5 to match your desired output)
    top_products = data.groupby('nama_stok')['predicted_quantity'].sum().nlargest(5).reset_index()
    
    # Create figure with specified size
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Create barplot with proper styling
    sns.barplot(
        data=top_products,
        x='predicted_quantity',
        y='nama_stok',
        hue='nama_stok',
        palette='viridis',
        legend=False,
        dodge=False,
        ax=ax
    )
    
    # Set labels and title (corrected method names)
    ax.set_title('Top 10 Produk dengan Prediksi Demand Tertinggi (30 Hari ke Depan)', pad=20)
    ax.set_xlabel('Total Predicted Quantity')
    ax.set_ylabel('Nama Produk')
    
    # Grid and styling
    ax.grid(axis='x', linestyle='--', alpha=0.7)
    ax.xaxis.set_major_locator(MaxNLocator(integer=True))
    
    # Remove spines
    sns.despine(right=True, top=True)
    
    # Display in Streamlit
    st.pyplot(fig)

def plot_demand_forecast(data, product_name):
    """Plot demand forecast for a specific product."""
    product_data = data[data['nama_stok'] == product_name].sort_values('tanggal')
    
    fig, ax = plt.subplots(figsize=(12, 6))
    
    # Plot main prediction line
    ax.plot(
        product_data['tanggal'], 
        product_data['predicted_quantity'], 
        label='Predicted',
        linewidth=2,
        color="#0057E3"
    )
    
    # Plot confidence interval
    ax.fill_between(
        product_data['tanggal'],
        product_data['lower_bound'],
        product_data['upper_bound'],
        alpha=0.2,
        label='Confidence Range',
        color="#0062FF"
    )
    
    # Set labels and title
    ax.set_xlabel("Date", fontsize=12)
    ax.set_ylabel("Quantity", fontsize=12)
    ax.set_title(f"Demand Forecast for {product_name}", fontsize=14, pad=20)
    
    # Customize ticks and grid
    ax.tick_params(axis='both', which='major', labelsize=10)
    ax.grid(axis='y', linestyle='--', alpha=0.5)
    
    # Add legend
    ax.legend(fontsize=10)
    
    # Remove right and top spines
    sns.despine(right=True, top=True)
    
    # Display in Streamlit
    st.pyplot(fig)
