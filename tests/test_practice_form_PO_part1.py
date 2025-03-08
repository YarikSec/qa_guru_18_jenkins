import allure


from allure_commons.types import Severity
from pages.practice_form_page import PracticeFormPage




@allure.tag("web")
@allure.severity(Severity.CRITICAL)
@allure.label("owner", "YAQA")
@allure.feature("Задание по jenkins")
@allure.story("Проверяем заполнение формы на сайте")
@allure.link("https://github.com", name="Testing")
def test_practice_form(setup_browser):
    browser = setup_browser
    practice_form = PracticeFormPage(browser)
    
    # WHEN
    with allure.step('Заполняем форму'):
        with allure.step('Открываем форму'):
            practice_form.open()
        with allure.step('Заполняем персональные данные'):
            practice_form.fill_personal_info(
                first_name='Ivan',
                last_name='Ivanov',
                email='ivan@example.com',
                phone='1234567890'
            )
        with allure.step('Устанавливаем дату рождения'):
            practice_form.set_date_of_birth(month='1', year='1990', day='05')
        with allure.step('Заполняем предметы'):
            practice_form.fill_subjects('Maths', 'English')
        with allure.step('Выбираем хобби'):
            practice_form.set_hobbies('Sports', 'Music')
        with allure.step('Загружаем изображение'):
            practice_form.upload_picture('test.jpg')
        with allure.step('Указываем адрес'):
            practice_form.set_current_address('Санкт-Петербург')
        with allure.step('Выбираем штат'):
            practice_form.select_state('NCR')
        with allure.step('Выбираем город'):
            practice_form.select_city('Delhi')
        with allure.step('Отправляем форму'):
            practice_form.submit()

    # THEN
    with allure.step('Проверяем регистрацию'):
        practice_form.should_have_registered(
            full_name='Ivan Ivanov',
            email='ivan@example.com',
            gender='Male',
            phone='1234567890',
            date_of_birth='05 February,1990',
            subject='Maths, English',
            hobbies='Sports, Music',
            avatar='test.jpg',
            current_address='Санкт-Петербург',
            city='NCR Delhi'
        )