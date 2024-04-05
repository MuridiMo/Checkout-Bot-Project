import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import Select
from tld import get_tld

# for using Chrome
browser = webdriver.Chrome ('C:/webdrivers/chromedriver.exe')

chrome_driver_location = ('C:/webdrivers/chromedriver.exe')

def add_to_cart(url):
    """
    Adds the item to the cart.
    :param url: THe product page url
    :return: Null
    """
    # For Bestbuy Digital PS5 Page
    #browser.get("https://www.bestbuy.com/site/sony-playstation-5-digital-edition-console/6430161.p?skuId=6430161")
    browser.get(url)
    buy_button = False
    while not buy_button:

        try:
            # if this works then  the button is not open
            browser.find_element_by_class_name("btn-disabled")

            # button isnt open restart script
            print("button isnt ready")

            # refresh page after a delay
            time.sleep(.5)
            browser.refresh()

        except:
            add_to_cart_btn = browser.find_element_by_class_name("btn-primary")

            # click the button and end script
            print("Button was clicked.")
            add_to_cart_btn.click()
            buy_button = True
    return buy_button


def check_out(url, email=None, password=None):
    """
    This function goes to the cart and checks out
    string:param url: the URL of the product page
    bool:param sign_in: Whether the user wants to sign in
    :return:
    """

    res = get_tld(url, as_object=True)  # Get the root as an object
    cart_url = "https://www."+res.fld+"/cart"
    browser.get(cart_url)
    print("added to cart")

    try:
        check_out_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, "btn-primary")))
        check_out_btn.click()
    except TimeoutException:
        browser.refresh()

    if email is not None and password is not None:
        # Fill in User and password fields
        try:
            # Make sure the webpage is loaded
            email_element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.NAME, 'fld-e')))
            email_element.click()
            email_element.send_keys(email)
        except TimeoutException:
            browser.refresh()
        password_element = browser.find_element_by_name('fld-p1')
        password_element.click()
        password_element.send_keys(password)

        sign_in_btn = browser.find_element_by_class_name('btn-secondary')
        sign_in_btn.click()
        print("Signed in")
        return "Signed In"

    else:
        # Continue as guest
        try:
            guest_btn = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'guest')))
            guest_btn.click()
            print("continuing as guest")
            return "Guest"
        except TimeoutException:
            browser.refresh()


def fill_shipping_info(user_email, user_phone):
    print("proceeding to checkout")
    try:
        email_element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, 'user.emailAddress')))
        email_element.click()
        email_element.send_keys(user_email)
    except TimeoutException:
        browser.refresh()

    phone_element = browser.find_element_by_id('user.phone')
    phone_element.click()
    phone_element.send_keys(user_phone)

    proceed_to_payment = browser.find_element_by_class_name("btn-secondary")
    proceed_to_payment.click()
    print("Shipping Info Submitted")


def processing_payment(user_card_number, user_expiration_month, user_expiration_year, user_cvv, user_first_name,
                       user_last_name, user_street_address, user_apt_number, user_city, user_state, user_zipcode, ):
    try:
        card_number_element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.ID, "optimized-cc-card-number")))
        card_number_element.click()
        card_number_element.send_keys(user_card_number)
    except TimeoutException:
        browser.refresh()

    expiration_month = Select(browser.find_element_by_name("expiration-month"))
    expiration_month.select_by_value(user_expiration_month)

    expiration_year = Select(browser.find_element_by_name("expiration-year"))
    expiration_year.select_by_value(user_expiration_year)

    cvv_element = browser.find_element_by_id("credit-card-cvv")
    cvv_element.click()
    cvv_element.send_keys(user_cvv)

    billing_first_name = browser.find_element_by_id("payment.billingAddress.firstName")
    billing_first_name.click()
    billing_first_name.send_keys(user_first_name)

    billing_last_name = browser.find_element_by_id("payment.billingAddress.lastName")
    billing_last_name.click()
    billing_last_name.send_keys(user_last_name)

    street_address_element = browser.find_element_by_id("payment.billingAddress.street")
    street_address_element.click()
    street_address_element.send_keys(user_street_address)
    hide_suggestions_element = browser.find_element_by_class_name("autocomplete__toggle")
    hide_suggestions_element.click()

    city_element = browser.find_element_by_id("payment.billingAddress.city")
    city_element.click()
    city_element.send_keys(user_city)

    state_element = Select(browser.find_element_by_id("payment.billingAddress.state"))
    state_element.select_by_value(user_state)

    zipcode_element = browser.find_element_by_id("payment.billingAddress.zipcode")
    zipcode_element.click()
    zipcode_element.send_keys(user_zipcode)

    print("Payment Info Submitted")

    check_out_button = browser.find_element_by_class_name("btn-primary")
    check_out_button.click()

    print("Success!")








def main():
    url = "https://www.bestbuy.com/site/apple-20w-usb-c-power-adapter-white/6437121.p?skuId=6437121"
    sign_in=False
    user_email = "Myemail@gmail.com"
    user_email2 = " "
    user_pass = " "
    user_phone = "(555)555-5555"
    user_card_number = "1234-1234-1233-1111"
    user_expiration_month = "12"
    user_expiration_year = "2024"
    user_cvv = "333"
    user_first_name = "John"
    user_last_name = "Doe"
    user_street_address = "1111 house st"
    user_apt_number = " "
    user_city = "Detroit"
    user_state = "MI"
    user_zipcode = "12312"

    add_to_cart(url)
    check_out_type = check_out(url, email=user_email2, password=user_pass)
    if check_out_type == "Guest":
        fill_shipping_info(user_email, user_phone)
        processing_payment(user_card_number, user_expiration_month, user_expiration_year, user_cvv, user_first_name,
                           user_last_name, user_street_address, user_apt_number, user_city, user_state, user_zipcode, )
    else:
        try:
            place_order_element = WebDriverWait(browser, 5).until(EC.presence_of_element_located((By.CLASS_NAME, 'btn-primary')))
            place_order_element.click()
        except TimeoutException:
            browser.refresh()




if __name__ == "__main__":
    main()

# SOLD OUT ELEMENT
# <button class="btn btn-disabled btn-lg btn-block add-to-cart-button" disabled ="" type="button" data-sku-id="6430161" style="padding:0 8px".Sold Out</button>


# Instock ELEMENT
# <button class="btn btn-primary btn-lg btn-block btn-leading-ficon add-to-cart-button" type="button" data-sku-id="6430161" style="padding:0 8px"><svg aria-hidden="true" role="img" viewBox="0 0


