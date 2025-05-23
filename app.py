# app.py
import streamlit as st
from data_loader import initialize_data
from pages.login import login_page
from pages.dashboard import dashboard_page

def main():
    st.set_page_config(
        page_title="Logistix Inventory System",
        page_icon="📦",
        layout="wide"
    )
    
    # Inisialisasi data
    if not initialize_data():
        st.stop()
    
    # Manajemen session state
    if "login_status" not in st.session_state:
        st.session_state.login_status = "not_logged_in"
    
    # Tampilkan halaman sesuai status login
    if st.session_state.login_status == "logged_in":
        dashboard_page()
    else:
        login_page()

if __name__ == "__main__":
    from utils.db import init_db
    init_db()
    main()