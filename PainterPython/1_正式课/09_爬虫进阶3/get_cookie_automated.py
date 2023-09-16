import browser_cookie3 # pip install browser_cookie3
import requests

url = "https://www.xiaohongshu.com/explore?exSource="
cj = browser_cookie3.chrome() # firefox可以替换为browser_cookie3.firefox()
r = requests.get(url, cookies=cj)
print(r.cookies)

from selenium import webdriver # pip install selenium

driver = webdriver.Chrome()
driver.get("https://www.xiaohongshu.com")

# 等待页面加载完毕
driver.implicitly_wait(10)

# 提取数据
data = driver.find_element("element_id").text

driver.quit()
