import os

from selene import  have, be

from selenium.webdriver.common.by import By


class PracticeFormPage:
    def __init__(self, browser):
        self.browser = browser
        self.base_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), '..', 'tests', 'resources')
        )

    def open(self):
        self.browser.open('https://demoqa.com/automation-practice-form')
        self.browser.driver.execute_script("$('#fixedban').remove()") # Для удаления баннеров
        self.browser.driver.execute_script("$('footer').remove()")    # Для удаления баннеров
        return self

    def fill_personal_info(self, first_name, last_name, email, phone):
        self.browser.element('#firstName').type(first_name)
        self.browser.element('#lastName').type(last_name)
        self.browser.element('#userEmail').type(email)
        self.browser.element('[name=gender][value=Male]+label').click()
        self.browser.element('#userNumber').type(phone)
        return self

    def set_date_of_birth(self, month, year, day):
        self.browser.element('#dateOfBirthInput').click()
        self.browser.element('.react-datepicker__month-select').click()
        self.browser.element(f'[value="{month}"]').click()
        self.browser.element('.react-datepicker__year-select').click()
        self.browser.element(f'[value="{year}"]').click()
        self.browser.element(f'.react-datepicker__day--0{day}').click()
        return self

    def fill_subjects(self, *values):
        for subject in values:
            self.browser.element('#subjectsInput').type(subject).press_enter()

        return self

    def set_hobbies(self, *values):
        # for value in values:
        #     browser.element(f'[for^="hobbies-checkbox"][label="{value}"]').click()
        for value in values:
            self.browser.element(
                (By.XPATH, f'//label[starts-with(@for, "hobbies-checkbox") and contains(text(), "{value}")]')).click()

        return self

    def upload_picture(self, picture):
        file_path = os.path.join(self.base_path, picture)
        self.browser.element('#uploadPicture').send_keys(file_path)

        return self

    def set_current_address(self, value):
        self.browser.element('#currentAddress').type(value)
        return self

    def select_state(self, value):
        self.browser.element('#state').click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def select_city(self, value):
        self.browser.element('#city').click()
        self.browser.all('[id^=react-select][id*=option]').element_by(
            have.exact_text(value)
        ).click()
        return self

    def submit(self):
        self.browser.element('#submit').press_enter()
        return self
    
    def should_have_registered(self, full_name, email, gender, phone, date_of_birth, subject, hobbies, avatar, current_address, city):
        self.browser.element('.modal-content').should(be.visible)
        self.browser.element('.modal-title').should(have.exact_text('Thanks for submitting the form'))
        self.browser.element('.table').all('td').even.should(
            have.exact_texts(
                full_name, 
                email, 
                gender,
                phone, 
                date_of_birth, 
                subject,
                hobbies,
                avatar,
                current_address,
                city
            )
        )