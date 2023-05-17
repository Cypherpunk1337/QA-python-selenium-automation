from generator.generator import generate_person
from pages.base_page import BasePage
from locators.form_page_locators import FormPageLocators as Locators
from selenium.webdriver.common.keys import Keys
import time


class FormPage(BasePage):
    def fill_fields_and_submit(self):
        picture_path = (r'C:\Users\0xFFFFFFFF\Downloads\5fz_MWLq6Xo_11zon.jpg')
        person = generate_person()
        self.remove_footer()
        self.element_is_visible(Locators.FIRST_NAME).send_keys(person.first_name)
        self.element_is_visible(Locators.LAST_NAME).send_keys(person.last_name)
        self.element_is_visible(Locators.EMAIL).send_keys(person.email)
        self.element_is_visible(Locators.GENDER).click()
        self.element_is_visible(Locators.MOBILE).send_keys(person.mobile)
        subject = self.element_is_visible(Locators.SUBJECTS)
        subject.send_keys(person.subject)
        subject.send_keys(Keys.RETURN)
        self.element_is_visible(Locators.HOBBIES).click()
        self.element_is_visible(Locators.PICTURE).send_keys(picture_path)
        self.element_is_visible(Locators.CURRENT_ADDRESS).send_keys(person.current_address)
        self.element_is_visible(Locators.SUBMIT).click()
        self.element_is_visible(Locators.RESULT_TABLE)
        return person
    
    def form_result(self):
        result_list = self.elements_are_visible(Locators.RESULT_TABLE)

        results_text = [i.text for i in result_list]

        return results_text