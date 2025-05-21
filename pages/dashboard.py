import streamlit as st
from utils.visualization import (
    display_summary_metrics,
    plot_top_products,
    plot_demand_forecast
)
from utils.predictions import get_prediction_data

def dashboard_page():
    """Render the main dashboard page."""
    # Custom CSS
    st.markdown(
        """
        <style>
        .main {
            padding-top: 2rem;
        }
        .stMetric {
            border-radius: 0.5rem;
            padding: 1rem;
            background-color: #f8f9fa;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Sidebar
    with st.sidebar:
        st.title(f"👋 Welcome, {st.session_state.username}")
        st.markdown("---")
        
        if st.button("Logout", type="primary"):
            st.session_state.login_status = "not_logged_in"
            st.rerun()
        
        st.markdown("---")
        st.info("Logistix Inventory System v1.0")
    
    # Main content
    st.title("📊 Inventory Dashboard")
    
    # Load prediction data
    prediction_data = get_prediction_data()
    
    # Display summary metrics
    display_summary_metrics(prediction_data)
    
    # Tabs for different views
    tab1, tab2 = st.tabs(["Overview", "Product Analysis"])
    
    with tab1:
        st.header("Inventory Overview")
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Top Products by Demand")
            plot_top_products(prediction_data)
        
        with col2:
            st.subheader("Demand Forecast")
            selected_product = st.selectbox(
                "Select Product",
                options=prediction_data['nama_stok'].unique(),
                key="product_select"
            )
            plot_demand_forecast(prediction_data, selected_product)
    
    with tab2:
        st.header("Detailed Product Analysis")
        # Add more detailed analysis components here
        st.write("Detailed product analysis coming soon...")