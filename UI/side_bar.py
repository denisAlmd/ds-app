import streamlit as st
from managers.page_manager import PageManager

class SideBar:

    def __init__(self):
        self.render_side_bar()

    def render_side_bar(self):
        try:
            st.sidebar.title("Navigation")
            pages = PageManager.get_pages()
            page_names:list[str] = [page().get_name() for page in pages]
            selected_page_name: str = st.sidebar.radio("Go to", page_names)

            for page in pages:
                if page().get_name() == selected_page_name:
                    page().render()
                    break
        except Exception as e:
            raise Exception(f"Error rendering side bar: {e}")