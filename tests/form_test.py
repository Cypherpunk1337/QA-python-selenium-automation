from pages.form_page import FormPage


class TestFormPage:
    def test_form(self, driver):
        form_page = FormPage(driver, 'https://demoqa.com/automation-practice-form')
        form_page.open()
        person = form_page.fill_fields_and_submit()
        result = form_page.form_result()
        print(person)
        print(result)
        assert f'{person.first_name} {person.last_name}' == result[0], 'Result First name and Last name from are not equal to input data'
        assert person.email == result[1], 'Result Email is not equal to input data'
        assert person.current_address == result[8], 'Result Address is not equal to input data'
        assert person.mobile == result[3], 'Result Mobile is not equal to input data'
        assert person.subject == result[5], 'Result Subject is not equal to input data'