from selenium.webdriver.common.by import By
from random import randint

class FormPageLocators:
    FIRST_NAME = (By.CSS_SELECTOR, '#firstName')
    LAST_NAME = (By.CSS_SELECTOR, '#lastName')
    EMAIL = (By.CSS_SELECTOR, '#userEmail')
    GENDER = (By.CSS_SELECTOR, f'label[for="gender-radio-{randint(1,3)}"' )
    MOBILE = (By.CSS_SELECTOR, '#userNumber')
    SUBJECTS = (By.CSS_SELECTOR, '#subjectsInput')
    HOBBIES = (By.CSS_SELECTOR, f'label[for="hobbies-checkbox-{randint(1,3)}"' )
    PICTURE = (By.CSS_SELECTOR, '#uploadPicture')
    CURRENT_ADDRESS = (By.CSS_SELECTOR, '#currentAddress')
    STATE = (By.CSS_SELECTOR, '#react-select-3-input')
    CITY = (By.CSS_SELECTOR, '#react-select-4-input')
    SUBMIT = (By.CSS_SELECTOR, '#submit')

    RESULT_TABLE = (By.XPATH, '//div[@class="table-responsive"]//td[2]')