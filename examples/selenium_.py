from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


'''
    Przykład wypisania tytułu strony.
'''
def example_1():
    print('Example 1')
    url = 'https://example.com'

    driver = webdriver.Firefox()
    driver.get(url)

    print(f'Website title: {driver.title}')

    time.sleep(2)
    driver.quit()


'''
    Przykład przykład podstawowej nawigacji po stronie
    oraz wprowadzania danych.
'''
def example_2():
    print('Example 2')
    url = 'https://www.selenium.dev/documentation/'

    driver = webdriver.Firefox()
    driver.get(url)

    button = driver.find_element(By.CLASS_NAME, 'DocSearch-Button-Placeholder')
    button.click()

    time.sleep(.5)

    input = driver.find_element(By.TAG_NAME, 'input')
    input.clear()

    # input.send_keys('Python') w tym przypadku nie sprawdza się,
    # gdyż nie wywołuje podpowiedzi wyszukiwania na stronie
    for c in 'Python':
        input.send_keys(c)
        time.sleep(0.05)

    input.send_keys(Keys.RETURN)

    time.sleep(5)
    driver.quit()


if __name__ == "__main__":
    example_1()
    example_2()
