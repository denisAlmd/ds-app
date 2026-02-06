import streamlit as st
from UI.side_bar import SideBar

PAGE_CONFIG: dict = {
    "page_title": "Data Science App",
    "layout": "wide",
    "initial_sidebar_state": "expanded",
    "page_icon": "📊"
}

def configure_page():
    st.set_page_config(**PAGE_CONFIG)

def main():
    configure_page()
    try:
        SideBar()
    except Exception as e:
        st.error(f"Error initializing the app: {e}")

if __name__ == "__main__":
    main()