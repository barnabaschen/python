# coding:utf-8
import time
import os
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys

path = os.path.abspath("./actuateModel")+"/IEDriverServer.exe"

option = webdriver.IeOptions()
option.add_argument('headless')

driver = webdriver.Ie(executable_path=path)
# url = "http://192.168.14.249/portal/"
url = "https://account.cnblogs.com/signin?returnUrl=http%3a%2f%2fi.cnblogs.com%2f"

driver.get(url=url)

button = driver.find_element_by_xpath("//button[@id='submitBtn']")
driver.find_element_by_xpath("//input[@name='LoginName']").send_keys("you name")
driver.find_element_by_xpath("//input[@name='Password']").send_keys("you password")

# text = driver.find_element_by_xpath("//input[@name='LoginName']").get_attribute("value")
# print(text)
button.submit()

cookie1 = driver.get_cookies()

time.sleep(6)

href = driver.find_element_by_xpath("//div[@id='blog_title']/a").get_attribute("href")
# driver.add_cookie(cookie1[0])
driver.get(url=href)

# 实例化鼠标对象 鼠标移入标签事件
action = ActionChains(driver)
# 鼠标移动到该元素上，鼠标悬停,等待下拉框元素可见
ele = driver.find_element_by_xpath("//div[@class='dropdown'][3]")
action.move_to_element(ele).perform()

# href1 = driver.find_element_by_xpath("//div[@class='dropdown'][3]/div[@class='dropdown-content']/a[@class='menu'][1]").get_attribute("href")

# driver.get(href1)

time.sleep(3)

# href2 = driver.find_element_by_xpath("//div[@id='ipython']/iframe").get_attribute("src")
#
# driver.get(href2)
#
# href3 = driver.find_element_by_xpath("//tbody/tr[4]/td/a").get_attribute("href")
#
# driver.get(href3)


url1 = driver.find_element_by_xpath("//a[@id='blog_nav_admin']").get_attribute("href")

driver.get(url1)

url2 = driver.find_element_by_xpath("//div[@id='left_nav']/ul/li[1]/a").get_attribute("href")

driver.get(url2)

time.sleep(3)

driver.find_element_by_xpath("//input[@id='Editor_Edit_txbTitle']").send_keys("八戒你瘦了！")

# 缺换到iframe框架里面去了。
# iframe = driver.find_element_by_xpath("//iframe[@id='Editor_Edit_EditorBody_ifr']")
# driver.switch_to.window(iframe)

content = '八戒你瘦了！测试python selenium。'
js = '''
    document.querySelector("iframe#Editor_Edit_EditorBody_ifr").contentWindow.document.querySelector("body#tinymce").innerText="{}";
    '''.format(content)
driver.execute_script(js)

# driver.find_element_by_xpath("//body[@id='tinymce']/p")
# 切换回来。跳出如上的iframe
# driver.switch_to.parent_frame()

# 选中input 按钮
driver.find_element_by_xpath("//input[@id='Editor_Edit_APOptions_Advancedpanel1_cklCategories_15']").click()

# 提交事件触发

driver.find_element_by_xpath("//input[@name='Editor$Edit$lkbPost']").send_keys(Keys.ENTER)
time.sleep(6)
print("————发布成功——————")