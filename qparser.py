from selenium import webdriver


class ProgParser:
    def __init__(self, driver, lang):
        self.driver = driver
        self.lang = lang

    def parse(self):
        self.go_to_tests_page()
        self.parse_que

    def go_to_tests_page(self):
        self.driver.get('https://proghub.ru/tests')
        slide_elements = self.driver.find_elements_by_class_name('carousel__card')

        for i in slide_elements:
            lang_link = i.get_attribute('href')

            if self.lang in lang_link:
                language = lang_link.split('/')[-1]
                self.driver.get('https://proghub.ru/t/' + language)
                break



def main():
    driver = webdriver.Chrome()
    parser = ProgParser(driver, 'Python')
    parser.parse()


if __name__ == '__main__':
    main()
