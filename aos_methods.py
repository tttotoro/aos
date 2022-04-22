from selenium import webdriver
from time import sleep
import datetime
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import Select
import aos_locators as locators

s = Service(executable_path='C:/tools/chromedriver.exe')
driver1 = webdriver.Chrome(service=s)


def setUp():
    driver1.maximize_window()
    driver1.implicitly_wait(30)
    driver1.get(locators.aos_url)
    if driver1.current_url == locators.aos_url:  # and driver1.title == '&nbsp;Advantage Shopping':
        print(f'Wow!You successfully launched URL: {driver1.current_url}')
        print('Page Title:', {driver1.title})
        print(f'We are at the main page!')
    else:
        print(f'we are NOT at the main page --- need to check ur code')
        driver1.close()
        driver1.quit()


def create_new_account():
    if driver1.current_url == locators.aos_url or driver1.title == '&nbsp;Advantage Shopping':
        driver1.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver1.find_element(By.LINK_TEXT, 'CREATE NEW ACCOUNT').click()
        sleep(2)
    if driver1.current_url == locators.aos_register_url or driver1.title == '&nbsp;Advantage Shopping':
        driver1.find_element(By.NAME, 'usernameRegisterPage').send_keys(locators.new_username)
        sleep(2)
        driver1.find_element(By.NAME, 'emailRegisterPage').send_keys(locators.email)
        sleep(2)
        driver1.find_element(By.NAME, 'passwordRegisterPage').send_keys(locators.password)
        sleep(2)
        driver1.find_element(By.NAME, 'confirm_passwordRegisterPage').send_keys(locators.password)
        sleep(2)
        driver1.find_element(By.NAME, 'first_nameRegisterPage').send_keys(locators.first_name)
        sleep(2)
        driver1.find_element(By.NAME, 'last_nameRegisterPage').send_keys(locators.last_name)
        sleep(2)
        driver1.find_element(By.NAME, 'phone_numberRegisterPage').send_keys(locators.phone_number)
        sleep(2)
        Select(driver1.find_element(By.NAME, 'countryListboxRegisterPage')).select_by_visible_text("Canada")
        sleep(2)
        driver1.find_element(By.NAME, 'addressRegisterPage').send_keys(locators.address)
        sleep(2)
        driver1.find_element(By.NAME, 'cityRegisterPage').send_keys(locators.city)
        sleep(2)
        driver1.find_element(By.NAME, 'state_/_province_/_regionRegisterPage').send_keys(locators.state_province_region)
        sleep(2)
        driver1.find_element(By.NAME, 'postal_codeRegisterPage').send_keys(locators.postal_code)
        sleep(2)
        driver1.find_element(By.NAME, 'i_agree').click()
        sleep(2)
        driver1.find_element(By.ID, 'register_btnundefined').click()
        sleep(2)


def validate_user_login():
    if driver1.current_url == locators.aos_url:
        sleep(1)
        print(f'New Account created successfully with username: {locators.new_username}')
        print(f'New Account fullname is: {locators.full_name}')
        print(f'New Account address is: {locators.address1}')
    else:
        print(f'New Account not created successfully. Please verify all the required fields (*) are completed.')


def log_out():
    driver1.find_element(By.ID, "menuUserLink").click()
    sleep(2)
    driver1.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(2)


def log_in():
    if driver1.current_url == locators.aos_url or driver1.title == '&nbsp;Advantage Shopping':
        driver1.find_element(By.ID, 'menuUser').click()
        sleep(2)
        driver1.find_element(By.NAME, 'username').send_keys(locators.new_username)
        sleep(2)
        driver1.find_element(By.NAME, 'password').send_keys(locators.password)
        sleep(2)
        driver1.find_element(By.ID, 'sign_in_btnundefined').click()
        sleep(2)
    if driver1.current_url == locators.aos_url:
        sleep(1)
        print(f'New User log in successfully with username: {locators.new_username}')


def log_out1():
    driver1.find_element(By.ID, "menuUserLink").click()
    sleep(2)
    driver1.find_element(By.XPATH, '//*[@id="loginMiniTitle"]/label[3]').click()
    sleep(2)


def tearDown():
    if driver1 is not None:
        print(f'--------------------------------------')
        print(f'Test Completed at: {datetime.datetime.now()}')
        driver1.close()
        driver1.quit()


setUp()

create_new_account()

validate_user_login()

log_out()

log_in()

log_out1()

tearDown()