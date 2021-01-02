# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 23:25:07 2020

@author: moham
"""

import time
from selenium import webdriver
# for using Chrome
browser = webdriver.Chrome ('C:/webdrivers/chromedriver.exe')

# For Bestbuy Digital PS5 Page
browser.get("https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161")

buyButton=False

while not buyButton:
        
        try:
            #if this works then  the button is not pytopen
            addToCartBtn = addButton = browser.find_element_by_class_name("btn-disabled")
            
            #button isnt open restart script
            print("button isnt ready")
            
            #refresh page after a delay
            time.sleep(1)
            browser.refresh(1)
            
        except:
                
                
                addToCartBtn = addButton = browser.find_element_by_class_name("btn-primary")
                
                #click the button and end script
                print("Button was clicked.")
                addToCartBtn.click()
                buyButton = True
                
# SOLD OUT ELEMENT
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled ="" type="button" data-sku-id="6430161" style="padding:0 8px".Sold Out</button>


# Instock ELEMENT
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" data-sku-id="6430161" style="padding:0 8px"><svg aria-hidden="true" role="img" viewBox="0 0
