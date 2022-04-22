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


def validate_homepage_texts_links():
    if driver1.current_url == locators.aos_url or driver1.title == '&nbsp;Advantage Shopping':
        driver1.find_element(By.XPATH, '//*[@id="speakersTxt"]').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '//*[@id="tabletsTxt"]').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '//*[@id="laptopsTxt"]').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '//*[@id="miceTxt"]').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '//*[@id="headphonesTxt"]').is_displayed()
        sleep(0.25)
        print('SPEAKERS,TABLES,HEADPHONES,LAPTOPS and MICE are displayed!')
#  check social media links  +  linkedin
        linkedin = driver1.find_element(By.XPATH, '//*[@id="follow"]/a[3]/img')
        print (f'The linkedin image is displayed: {linkedin.is_displayed()} and is clickable: {linkedin.is_enabled()}')
        driver1.find_element(By.XPATH, '//*[@id="follow"]/a[3]/img').click()
        driver1.switch_to.window(driver1.window_handles[1])
        if driver1.current_url == locators.linkedin_url:
            print('Linkedin link is displayed and clickable!')
            sleep(3)
        else:
            print('Page is not found!')
            driver1.close()
            print('Linkedin link has been closed!')
            driver1.switch_to.window(driver1.window_handles[0])
#    facebook
            facebook = driver1.find_element(By.XPATH, '//*[@id="follow"]/a[1]/img')
            print(f' The Facebook image is displayed: {facebook.is_displayed()} and is clickable: {facebook.is_enabled()}')
            driver1.find_element(By.XPATH, '//*[@id="follow"]/a[1]/img').click()
            driver1.switch_to.window(driver1.window_handles[1])
            if driver1.current_url == locators.facebook_url:
                print('Facebook link is displayed and clickable!')
                sleep(3)
            else:
                print('Page is not found!')
                driver1.close()
                print('Facebook link has been closed!')
                driver1.switch_to.window(driver1.window_handles[0])
#     twitter
                twitter = driver1.find_element(By.XPATH, '//*[@id="follow"]/a[2]/img')
                print(f' The twitter image is displayed: {twitter.is_displayed()} and is clickable: {twitter.is_enabled()}')
                driver1.find_element(By.XPATH, '//*[@id="follow"]/a[2]/img').click()
                driver1.switch_to.window(driver1.window_handles[1])
                if driver1.current_url == locators.twitter_url:
                    print('Twitter link is displayed and clickable!')
                    sleep(3)
                else:
                    print('Page is not found!')
                    driver1.close()
                    print('Twitter link has been closed!')
                    driver1.switch_to.window(driver1.window_handles[0])


def validate_top_nav_menu():
    if driver1.current_url == locators.aos_url or driver1.title == '&nbsp;Advantage Shopping':
        driver1.find_element(By.XPATH, '/html/body/header/nav/div/a/span[1]').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '/html/body/header/nav/ul/li[8]/a').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '/html/body/header/nav/ul/li[7]/a').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '/html/body/header/nav/ul/li[6]/a').is_displayed()
        sleep(0.25)
        driver1.find_element(By.XPATH, '/html/body/header/nav/ul/li[5]/a').is_displayed()
        sleep(0.25)
        print('MAIN LOGO, OUR PRODUCTS, SPECIAL OFFER, POPULAR ITEMS AND CONTACT US are displayed!')


def validate_contact_us_form():
    if driver1.current_url == locators.aos_url or driver1.title == '&nbsp;Advantage Shopping':
        Select(driver1.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[1]/div/sec-view[1]/div/select')).select_by_visible_text("Laptops")
        sleep(0.25)
        Select(driver1.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[1]/div/sec-view[2]/div/select')).select_by_visible_text("HP Pavilion 15z Laptop")
        sleep(0.25)
        driver1.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[1]/div/sec-view[3]/div/input').send_keys(locators.email)
        sleep(0.25)
        driver1.find_element(By.XPATH, '//*[@id="supportCover"]/div[2]/sec-form/div[2]/div/sec-view/div/textarea').send_keys(locators.phone_number)
        sleep(0.25)
        driver1.find_element(By.XPATH, '//*[@id="send_btnundefined"]').click()
        sleep(0.25)
        if driver1.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/p').is_displayed():
            sleep(0.25)
            print('MAIN LOGO,SPEAKERS,TABLES,HEADPHONES,LAPTOPS and MICE are displayed!')
            if driver1.find_element(By.XPATH, '//*[@id="registerSuccessCover"]/div/a').click():
                sleep(0.25)
                print('CONTINUE SHOPPING button is clickable and displayed!')


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

validate_homepage_texts_links()

validate_top_nav_menu()

validate_contact_us_form()

create_new_account()

validate_user_login()

log_out()

log_in()

log_out1()

tearDown()