from UI.pages.base_page import BasePage
from UI.pages.home.home_page import HomePage

class PageManager:
    
    _pages: list[type[BasePage]] = [
        HomePage,
        ]

    @classmethod
    def get_pages(cls) -> list[type[BasePage]]:
        return cls._pages
    
    @classmethod
    def register_page(cls, page: type[BasePage]) -> type[BasePage]:
        if page not in cls._pages:
            cls._pages.append(page)
        return page
    
    @classmethod
    def unregister_page(cls, page: type[BasePage]) -> None:
        if page in cls._pages:
            cls._pages.remove(page)

    @classmethod
    def get_pagge_instances(cls) -> list[BasePage]:
        return [page() for page in cls._pages]