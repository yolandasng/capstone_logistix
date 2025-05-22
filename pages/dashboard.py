import streamlit as st
from utils.visualization import (
    display_summary_metrics,
    plot_top_products,
    plot_demand_forecast
)
from utils.predictions import get_prediction_data

def dashboard_page():
    """Render the main dashboard page with centered compact layout."""
    # Custom CSS for centering and compact design
    st.markdown(
        """
        <style>
        /* Center all headers and content */
        .stApp > div > div > div > div > div {
            max-width: 800px;
            margin: 0 auto;
        }
        /* Compact metrics cards */
        .stMetric {
            padding: 0.5rem !important;
            margin: 0.2rem !important;
        }
        /* Compact select box */
        .stSelectbox > div {
            width: 50%;
            margin: 0 auto;
        }
        /* Remove extra padding */
        .main .block-container {
            padding-top: 0.5rem;
            padding-bottom: 1rem;
        }
        /* Compact tabs */
        .stTabs [data-baseweb="tab-list"] {
            gap: 0.5rem;
        }
        .stTabs [data-baseweb="tab"] {
            padding: 0.5rem 1rem;
            font-size: 0.9rem;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Sidebar (unchanged)
    with st.sidebar:
        st.title(f"👋 Welcome, {st.session_state.username}")
        st.markdown("---")
        if st.button("Logout", type="primary"):
            st.session_state.login_status = "logged_in"
            st.rerun()
        st.markdown("---")
        st.info("Logistix Inventory System v1.0")
    
    # Main content - Centered layout
    with st.container():
        st.title("Inventory Dashboard")
        
        # Summary metrics
        prediction_data = get_prediction_data()
        display_summary_metrics(prediction_data)
        
        # Tabs - Compact version
        tab1, tab2 = st.tabs(["Overview", "Product Analysis"])
        
        with tab1:
            st.header("Inventory Overview", divider='gray')
            
            # Top Products - Centered and compact
            st.subheader("Top Products by Demand", anchor='center')
            plot_top_products(prediction_data)
            
            # Demand Forecast - Centered and compact
            st.subheader("Demand Forecast", anchor='center')
            cols = st.columns([1, 3, 1])
            with cols[1]:
                selected_product = st.selectbox(
                    "Select Product",
                    options=prediction_data['nama_stok'].unique(),
                    key="product_select",
                    label_visibility="collapsed"
                )
            plot_demand_forecast(prediction_data, selected_product)
        
        with tab2:
            st.header("Detailed Product Analysis", divider='gray')
            st.write("Coming soon...")