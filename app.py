import streamlit as st
from pages.login import login_page
from pages.dashboard import dashboard_page

def main():
    st.set_page_config(
        page_title="Logistix Inventory System",
        page_icon="📦",
        layout="wide"
    )
    
    # Initialize session state
    if "login_status" not in st.session_state:
        st.session_state.login_status = "not_logged_in"
    
    # Show the appropriate page based on login status
    if st.session_state.login_status == "logged_in":
        dashboard_page()
    else:
        login_page()

if __name__ == "__main__":
    main()