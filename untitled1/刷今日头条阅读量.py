import time
import requests

from selenium import webdriver


def refresh_html(jianshu_url):
    firefoxdriver ="C:\Program Files\Mozilla Firefox\firefox.exe"
    browser = webdriver.firefox(firefoxdriver)
    browser.get(jianshu_url)
    while True:
        time.sleep(1)
        browser.refresh()

if __name__ == '__main__':
        url = 'https://www.toutiao.com/a6744255163768242692/'
        try:
            refresh_html(url)
        except:
            refresh_html(url)