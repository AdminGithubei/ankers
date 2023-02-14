from selenium import webdriver
import time

# create a new Chrome browser instance
browser = webdriver.Chrome(options=webdriver.ChromeOptions().add_argument('--no-sandbox'))


# navigate to the Google account creation page
browser.get('https://accounts.google.com/signup/v2/webcreateaccount?hl=en&flowName=GlifWebSignIn&flowEntry=SignUp')

# fill out the registration form with random data
browser.find_element_by_name('firstName').send_keys('John')
browser.find_element_by_name('lastName').send_keys('Doe')
browser.find_element_by_name('Username').send_keys('johndoe1234')
browser.find_element_by_name('Passwd').send_keys('password123')
browser.find_element_by_name('ConfirmPasswd').send_keys('password123')
browser.find_element_by_name('BirthDay').send_keys('01')
browser.find_element_by_name('BirthYear').send_keys('2000')

# submit the form and wait for the account to be created
browser.find_element_by_id('accountDetailsNext').click()
time.sleep(5)

# get the username and password from the confirmation page
username = browser.find_element_by_css_selector('.whsOnd.zHQkBf').text
password = browser.find_element_by_css_selector('.zQJV3e.k0tWj.IYewr').text

# print the login credentials
print('Username:', username)
print('Password:', password)

# close the browser
browser.quit()
