import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# 设置 Chrome 选项
options = webdriver.ChromeOptions()
options.add_argument('--headless')  # 无头模式，不打开浏览器窗口
options.add_argument('--disable-gpu')  # 禁用GPU加速

# 启动 Chrome 浏览器
driver = webdriver.Chrome(options=options)

# 访问网页
url = "https://www.bilibili.com/v/popular/history/"
driver.get(url)

# 等待页面加载完成
wait = WebDriverWait(driver, 10)
wait.until(EC.presence_of_element_located((By.CLASS_NAME, "flow-loader")))

# 循环获取所有ul元素的class="card-list" # 要这个就不要下面的，这个是什么都爬

# while True:
#     try:
#         # 找到所有具有class="card-list"的ul元素
#         ul_elements = driver.find_elements(By.CSS_SELECTOR, ".flow-loader .card-list")
#
#         # 输出找到的ul元素
#         for ul in ul_elements:
#             print(ul.get_attribute("outerHTML"))  # 输出整个ul元素的HTML代码
#
#         # 模拟下滑操作，触发加载更多内容
#         driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
#
#         # 等待新内容加载完成
#         wait.until(EC.presence_of_element_located((By.CLASS_NAME, "flow-loader")))
#
#     except Exception as e:
#         print("Error:", e)
#         break
# 上面要这个就不要下面的，这个是什么都爬
# 定位大 div 元素
card_list_container = driver.find_element(By.CLASS_NAME, "card-list")

# 在大 div 元素内部定位视频名称元素并获取文本内容
# 定位所有的 a 标签元素
a_tags = card_list_container.find_elements(By.TAG_NAME, "a")
# images = card_list_container.find_elements(By.TAG_NAME, "img")
video_names = card_list_container.find_elements(By.CLASS_NAME, "video-name")
up_names = card_list_container.find_elements(By.CLASS_NAME, "up-name__text")

play_texts = card_list_container.find_elements(By.CLASS_NAME, "play-text")
like_texts = card_list_container.find_elements(By.CLASS_NAME, "like-text")
history_hint = card_list_container.find_elements(By.CLASS_NAME, "history-hint")


for a_tag, video_name, up_name, play_text, like_text, hint in zip(a_tags, video_names, up_names, play_texts, like_texts, history_hint):
    href = a_tag.get_attribute("href")
    print("链接:", href)
    print("视频名称:", video_name.text)
    print("UP主名称:", up_name.text)
    print("播放量:", play_text.text)
    print("点赞数:", like_text.text)
    print("历史提示:", hint.text)
    print("-----------------------------")

# 打开一个记事本文件用于写入
with open("bilibili_data.txt.txt", "w", encoding="utf-8") as f:
    for a_tag, video_name, up_name, play_text, like_text, hint in zip(a_tags, video_names, up_names, play_texts, like_texts, history_hint):
        href = a_tag.get_attribute("href")
        f.write("链接: {}\n".format(href))
        f.write("视频名称: {}\n".format(video_name.text))
        f.write("UP主名称: {}\n".format(up_name.text))
        f.write("播放量: {}\n".format(play_text.text))
        f.write("点赞数: {}\n".format(like_text.text))
        f.write("历史提示: {}\n".format(hint.text))
        f.write("-----------------------------\n")

# 创建一个空的 DataFrame 用于存储数据
data = {
    '链接': [],
    '视频名称': [],
    'UP主名称': [],
    '播放量': [],
    '点赞数': [],
    '历史提示': []
}

# 将数据存储到 DataFrame 中
for a_tag, video_name, up_name, play_text, like_text, hint in zip(a_tags, video_names, up_names, play_texts, like_texts, history_hint):
    data['链接'].append(a_tag.get_attribute("href"))
    data['视频名称'].append(video_name.text)
    data['UP主名称'].append(up_name.text)
    data['播放量'].append(play_text.text)
    data['点赞数'].append(like_text.text)
    data['历史提示'].append(hint.text)

df = pd.DataFrame(data)

# 将 DataFrame 写入 Excel 文件
df.to_excel("bilibili.xlsx", index=False)
# 关闭浏览器
driver.quit()



