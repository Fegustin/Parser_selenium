from selenium import webdriver
from Parser_selenium.modal import Question


class ProgParser:
    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_tests_page()
        self.parse_question_page()

    def go_to_tests_page(self):
        self.driver.get('https://proghub.ru/tests')
        slide_elements = self.driver.find_elements_by_class_name('carousel__card')

        for i in slide_elements:
            lang_link = i.get_attribute('href')

            if self.lang in lang_link:
                language = lang_link.split('/')[-1]
                self.driver.get('https://proghub.ru/t/' + language)
                self.driver.find_element_by_tag_name('button').click()
                break

    def parse_question_page(self):
        question = Question()
        self.fill_question_text(question)
        print(question)

    def fill_question_text(self, question):
        question_text_elm = self.driver.find_element_by_xpath('//*[@id="__next"]/div[2]/div[1]/div[1]/h3[1]')
        question_text = question_text_elm




def main():
    driver = webdriver.Chrome()
    parser = ProgParser(driver, 'python')
    parser.parse()


if __name__ == '__main__':
    main()
