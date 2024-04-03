'''# 导入必要的包
import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver

# 指定 ChromeDriver 可执行文件的路径
path = r'C:\\Program Files\\Google\\Chrome\\Application\\chrome_proxy.exe'
# 创建一个 Service 对象
service = Service(path)
# 使用指定的可执行文件路径创建一个 Chrome 浏览器实例
browser = webdriver.Chrome(service=service)

def getDriver():
    options = webdriver.ChromeOptions()
    options.add_argument("--disable-extensions")
    options.add_argument("--disable-gpu")
    #options.add_argument("--no-sandbox") # linux only
    options.add_experimental_option("excludeSwitches", ["enable-automation"])
    options.add_experimental_option("useAutomationExtension", False)
    driver = webdriver.Chrome(options=options)
    driver.execute_cdp_cmd("Network.enable", {})
    driver.execute_cdp_cmd("Network.setExtraHTTPHeaders", {"headers": {"User-Agent": "browserClientA"}})
    driver.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": """
            Object.defineProperty(navigator, 'webdriver', {
                get: () => undefined
            })
        """
    })
    return driver

driver = getDriver()
# 指定要在浏览器中打开的 URL
# 指定要在浏览器中打开的 URL
url = "https://www.jd.com"

# 在浏览器中打开指定的 URL
browser.get(url)

# 获取已打开页面的源代码 HTML 内容
content = browser.page_source

# 将页面源代码内容打印到控制台
print(content)

# 检查文件夹是否存在，不存在则创建
folder_path = './文件/'
os.makedirs(folder_path, exist_ok=True)
# 将页面源代码内容保存到本地文件
with open('./文件/jd_page.html', 'w', encoding='utf-8') as file:
    file.write(content)

# 关闭浏览器
browser.quit()
'''

# 导入必要的包
import os
import time

import bs4
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
# 指定 ChromeDriver 可执行文件的路径
path = 'chromedriver.exe'

# 使用指定的可执行文件路径创建一个 Chrome 浏览器实例
browser = webdriver.Chrome(path)

# 指定要在浏览器中打开的 URL
url = "https://www.bilibili.com/v/popular/history/"

# 等待 5 秒钟

# 在浏览器中打开指定的 URL
browser.get(url)
time.sleep(5)
# 等待页面中的某个元素加载完毕，最多等待 10 秒钟
wait = WebDriverWait(browser, 10)
# element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'card-item')))

# 获取已打开页面的源代码 HTML 内容
content = browser.page_source

# 将页面源代码内容打印到控制台
print(content)

# 检查文件夹是否存在，不存在则创建
folder_path = './文件/'
os.makedirs(folder_path, exist_ok=True)
# 将页面源代码内容保存到本地文件
with open('./文件/bilibili_page.html', 'w', encoding='utf-8') as file:
    file.write(content)
# 提取视频标题、UP主、播放量和弹幕量
element = wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'video-card')))
for i in range(2):
    # 查找视频卡片元素
    video_card = browser.find_element(By.CLASS_NAME, 'video-card')

    # 提取视频标题
    video_title = video_card.find_element(By.CLASS_NAME, 'video-name').text.strip()

    # 提取UP主
    up_name = video_card.find_element(By.CLASS_NAME, 'up-name__text').text.strip()

    # 提取播放量
    playback = video_card.find_element(By.CLASS_NAME, 'play-text').text.strip()

    # 提取弹幕量
    barrage = video_card.find_element(By.CLASS_NAME, 'like-text').text.strip()
    # 打印提取的信息
    print("视频标题:", video_title)
    print("UP主:", up_name)
    print("播放量:", playback)
    print("弹幕量:", barrage)

# 关闭浏览器
browser.quit()
# 使用 Beautiful Soup 解析页面源代码
bs = bs4.BeautifulSoup(content, 'html.parser')
datas = bs.find_all('div', class_='card-item')

# 提取数据并保存到 txt 文件中
output_file = './文件/bilibili_data.txt'
with open(output_file, 'w', encoding='utf-8') as file:
    for data in datas:
        item = {}  # 创建字典来保存数据
        item['video_title'] = data.find('a', class_='video-card__content').text
        item['title'] = data.find('p', class_='video-card__info').text
        item['up_name'] = data.find('span', class_='up-name__text').text
        item['playback'] = data.find('span', class_='play-text').text
        item['barrage'] = data.find('span', class_='line-text').text
        item['logo'] = data.find('span', class_='history-hint').text
        if data.find('span', class_='inq'):
            item['selogen'] = data.find('span', class_='inq').text
        else:
            item['selogen'] = ""

        # 将字典中的数据写入文件
        file.write(str(item) + '\n')

print(f"数据已保存到文件: {output_file}")