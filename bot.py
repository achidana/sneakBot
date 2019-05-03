import webbrowser
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--headless')

# browser = webdriver.Chrome('./chromedriver', options=chrome_options)
browser = webdriver.Chrome('./chromedriver')
browser.implicitly_wait(10)


####################

# url = 'https://www.nike.com/launch/t/air-jordan-1-high-travis-scott/'

####################

test = "//li//button[text()[contains(.,'M          9')]]"
sizeM9 = "//li//button[text()[contains(.,'M 9')]]"
size9 = "//li//button[text()[contains(.,'9')]]"
addCartText = "//button[text()='ADD TO CART']"
addCartAttribute = "//button[@data-qa='add-to-cart']"
cartNumber = "//span[contains(@data-qa,'cart-count-jewel')][contains(.,'1')]"
payPal = "//img[contains(@alt,'PayPal')]"

url = 'https://www.nike.com/launch/t/blazer-mid-77-vintage-sail-white/'
browser.fullscreen_window()
browser.get(url)


def pickSizeAndToCart():
    try:
        mySize = browser.find_element_by_xpath(sizeM9)
    except:
        print('trying 9')
        mySize = browser.find_element_by_xpath(size9)

    mySize.click()
    try:
        addToCart = browser.find_element_by_xpath(addCartAttribute)
    except:
        print('trying by attribute')
        addToCart = browser.find_element_by_xpath(addCartText)
    # action = ActionChains(browser)
    # action.move_to_element(addToCart).click()
    # ActionChains(browser).move_to_element(addToCart)
    try:
        addToCart.click()
        x = browser.find_element_by_xpath(cartNumber)
        print(x)
        return True
    except:
        return False

addToCart = pickSizeAndToCart()

while not addToCart:
    print('in loop')
    addToCart = pickSizeAndToCart()

checkoutLink = browser.find_element_by_xpath("//a[contains(@href,'cart')]")
checkoutLink.click()


payPalLink = WebDriverWait(browser, 20).until(EC.element_to_be_clickable((By.XPATH,  payPal))).click()

# payPalLink.click()

browser.get_screenshot_as_file('sample.png')
# print('succ')
