# -*- coding: utf-8 -*-
import time

link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"

def test_caheck_ability_add_to_basket(browser):
    browser.get(link)
    time.sleep(30)
    basket = browser.find_element_by_css_selector(".btn-add-to-basket")
    assert basket, "Button to add an item to basket doesnt find!"