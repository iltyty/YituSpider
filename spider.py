import json
import time

from child import Child

from lxml import etree
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support import expected_conditions as EC


START_URL = 'https://medical-saas.yitutech.com/boneage/#/'

USERNAME = 'szet@boneageyitiji'
PASSWORD = 'szet123456'


def save_cookie(cookie: dict, filename='cookie.json'):
    with open(filename, 'w') as f:
        json.dump(cookie, f)


def login(driver: WebDriver):
    _ = WebDriverWait(driver, 50, 1).until(
        EC.presence_of_element_located((By.ID, 'username'))
    )

    usr_input = driver.find_element_by_id('username')
    usr_input.send_keys(USERNAME)
    pwd_input = driver.find_element_by_id('password')
    pwd_input.send_keys(PASSWORD)
    time.sleep(5)

    btn = driver.find_element_by_xpath('//button')
    btn.click()

    save_cookie(driver.get_cookies()[0])


def get_cookie_from_file(filename='cookie.json'):
    with open(filename, 'r') as f:
        return json.load(f)


def get_all_detail_urls(driver: WebDriver) -> list[str]:
    driver.get(START_URL)
    # login(driver)
    res: list[str] = []

    cookie = get_cookie_from_file()
    driver.add_cookie(cookie)
    driver.get(START_URL)
    
    DETAIL_XPATH = '//div[@class="ant-table-body"]//tbody//tr'
    NEXT_BTN_XPATH = '//li[@class=" ant-pagination-next"]//a[@class="ant-pagination-item-link"]'

    for _ in range(49):
        _ = WebDriverWait(driver, 5, 1).until(
            EC.presence_of_element_located((By.XPATH, DETAIL_XPATH))
        )

        hrefs = driver.find_elements_by_xpath(DETAIL_XPATH)
        hrefs = [href.get_attribute('data-row-key') for href in hrefs]
        hrefs = ['{}result/{}'.format(START_URL, href) for href in hrefs]

        if len(hrefs):
            res.extend(hrefs)

        try:
            next_page = driver.find_element_by_xpath(NEXT_BTN_XPATH)
            driver.execute_script('arguments[0].click()', next_page)
        except NoSuchElementException:
            print('Reach the final page.')
            break

        time.sleep(2)

    with open('urls.txt', 'w') as f:
        for url in res:
            f.write('{}\n'.format(url))

    return res


def get_all_urls_from_file(filename='urls.txt'):
    res: list[str] = []

    with open(filename, 'r') as f:
        line = f.readline()
        res.append(line)

    return res



def init_driver() -> WebDriver:
    options = webdriver.ChromeOptions()
    prefs = {
        'profile.managed_default_content_settings.images': 2
    }
    options.add_experimental_option('prefs', prefs)
    # return webdriver.Chrome(options=options)
    return webdriver.Chrome()


def get_all_children(browser: WebDriver, urls: list[str]):
    res: list[Child] = []

    for url in urls:
        url = url.strip()
        browser.get(url)
        child = get_one_child(browser)
        res.append(child)

    return res


def get_one_child(browser: WebDriver):
    tree = etree.HTML(browser.page_source)

    name = tree.xpath(Child.NAME_XPATH)[0].strip()
    exam_id = tree.xpath(Child.EXAM_ID_XPATH)[0].strip()
    gender = tree.xpath(Child.GENDER_XPATH)[0].strip()
    child_id = tree.xpath(Child.CHILD_ID_XPATH)[0].strip()
    age = tree.xpath(Child.AGE_XPATH)[0].strip()
    date = tree.xpath(Child.DATE_XPATH)[0].strip()

    return Child(
        name=name,
        exam_id=exam_id,
        gender=gender,
        child_id=child_id,
        age=age,
        date=date,
        rus_bone='',
        c_bone='',
        zh_bone='',
        img_bone=''
    )


def main():
    browser = init_driver()
    # urls = get_all_detail_urls(browser)
    urls = get_all_urls_from_file()
    res = get_all_children(browser, urls)


main()