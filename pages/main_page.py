# Dependencies
from .base_page import BasePage
from .locators import *

# Main page methods
class MainPage(BasePage):
    def __init__(self, *args, **kwargs):
        super(MainPage, self).__init__(*args, **kwargs)
