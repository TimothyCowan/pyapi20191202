import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driverpath = r'C:\Users\Student\Desktop\chromedriver.exe'  # Optional argument, if not specified will search path.
driver = webdriver.Chrome(executable_path=driverpath)
driver.get('https://www.dominos.com/en/pages/order/#!/locations/search/')
# time.sleep(8)
input()
click_delivery = driver.find_element_by_xpath('//*[@id="locationSearchForm"]/div/div[1]/label[2]/span[1]/img')
click_delivery.click()
input()
click_delivery = driver.find_element_by_xpath('//*[@id="Postal_Code_Sep"]')
click_delivery.click()
click_delivery.send_keys('98499' + Keys.RETURN)
input()
click_delivery = driver.find_element_by_xpath('//*[@id="locationsResultsPage"]/div/div[2]/div[1]/div[2]/div/div[2]/div/a')
click_delivery.click()
input()
click_delivery = driver.find_element_by_xpath('//*[@id="entree-BuildYourOwn"]/a/div[2]/h2')
click_delivery.click()
input()
click_delivery = driver.find_element_by_xpath('//*[@id="toppings"]')
click_delivery.click()
input()
click_delivery = driver.find_element_by_xpath('// *[ @ id = "stepUpsell"] / div / button[1] / span')
click_delivery.click()
finshed = "y"
while finshed == 'y':
    pizza_select = (input('please type 1:pepperoni only,  2:pineapple w/ ham,  3:pepperoni w/ bacon'))
    print()
    click_delivery = driver.find_element_by_xpath('// *[ @ id = "sizeCrust"]')
    click_delivery.click()
    if pizza_select == '1':
        print()
        click_delivery = driver.find_element_by_xpath(
            '// *[ @ id = "toppingsWrapper"] / div / div / div[1] / div / div / div[1] / div[4] / label / input')
        click_delivery.click()
        print()
        click_delivery = driver.find_element_by_xpath('// *[ @ id = "pizzaSummaryInColumn"] / div[1] / div[2] / div[2] / button')
        click_delivery.click()
        finshed = input("Yes to order more or no to continue")
    if pizza_select == '2':
        click_delivery = driver.find_element_by_xpath(
            '//*[@id="toppingsWrapper"]/div/div/div[2]/div/div/div[1]/div[8]/label/input')
        click_delivery.click()
        print()
        click_delivery = driver.find_element_by_xpath(
            '//*[@id="toppingsWrapper"]/div/div/div[1]/div/div/div[1]/div[1]/label/input')
        click_delivery.click()
        print()
        click_delivery = driver.find_element_by_xpath('// *[ @ id = "pizzaSummaryInColumn"] / div[1] / div[2] / div[2] / button')
        click_delivery.click()
        finshed = input("Yes to order more or no to continue")
    if pizza_select == '3':
        click_delivery = driver.find_element_by_xpath(
            '// *[ @ id = "toppingsWrapper"] / div / div / div[1] / div / div / div[1] / div[4] / label / input')
        click_delivery.click()
        print()
        click_delivery = driver.find_element_by_xpath(
            '// *[ @ id = "toppingsWrapper"] / div / div / div[1] / div / div / div[2] / div[3] / label / input')
        click_delivery.click()
        print()
        click_delivery = driver.find_element_by_xpath('// *[ @ id = "pizzaSummaryInColumn"] / div[1] / div[2] / div[2] / button')
        click_delivery.click()
        finshed = input("Yes to order more or no to continue")

# search_box.send_keys('98387')
# search_box.submit()
time.sleep(5)
input("Enter to exit")
driver.quit()
