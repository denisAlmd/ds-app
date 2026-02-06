
from UI.pages.base_page import BasePage

class HomePage(BasePage):

    def get_name(self):
        return "Home"

    def get_description(self):
        return "Welcome to the Data Science App! This is the home page where you can find an overview of the app's features and navigate to different sections."

    def render(self):
        import streamlit as st
        try:            
            st.title("Welcome to the Data Science App!")
            st.write("This is the home page where you can find an overview of the app's features and navigate to different sections.")
            st.divider()
            st.write("Lets get started by selecting a page from the sidebar.")
            st.write("Feel free to send feedback or report issues. mailto: dnis.almeida@gmail.com")

        except Exception as e:
            st.warning(f"Error rendering Home Page: {e}")