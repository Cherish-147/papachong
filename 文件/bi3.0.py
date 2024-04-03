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

# 循环获取所有ul元素的class="card-list"
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
# 定位大 div 元素
card_list_container = driver.find_element(By.CLASS_NAME, "card-list")

# 在大 div 元素内部定位视频名称元素并获取文本内容
a_tags = card_list_container.find_elements(By.TAG_NAME, "a")

# 查找具有特定 class 的图片元素
images = driver.find_elements(By.CSS_SELECTOR, 'img.lazy-image.cover-picture__image')

video_names = card_list_container.find_elements(By.CLASS_NAME, "video-name")
up_names = card_list_container.find_elements(By.CLASS_NAME, "up-name__text")

play_texts = card_list_container.find_elements(By.CLASS_NAME, "play-text")
like_texts = card_list_container.find_elements(By.CLASS_NAME, "like-text")
history_hint = card_list_container.find_elements(By.CLASS_NAME, "history-hint")
# 定位所有的 a 标签元素
# a_tags = card_list_container.find_elements(By.TAG_NAME, "a")

# 获取链接地址和图片地址
# 打印每个 a 标签的 href 属性值
#
# 3.0
# for a_tag in a_tags:
#     href = a_tag.get_attribute("href")
#     print("链接:", href)
# 3.0

# 2.0
# for video_name in video_names:
#     print(video_name.text)
# for up_name in video_names:
#     print(up_name.text)
# 2.0


# 3.0
# for video_name, up_name, play_text, like_text, hint in zip(video_names, up_names, play_texts, like_texts, history_hint):
#     print("视频名称:", video_name.text)
#     print("UP主名称:", up_name.text)
#     print("播放量:", play_text.text)
#     print("点赞数:", like_text.text)
#     print("历史提示:", hint.text)
#     print("-----------------------------")
#     3.0
for a_tag,img_elements, video_name, up_name, play_text, like_text, hint in zip(a_tags,images, video_names, up_names, play_texts, like_texts, history_hint):
    href = a_tag.get_attribute("href")
    src = img_elements.get_attribute("data-src")  # 获取图片链接
    if src.startswith("//"):  # 检查链接是否以双斜杠开头
        src = "https:" + src  # 如果是，则添加https:

    print("链接:", href)
    print("图片链接:", src)
    print("视频名称:", video_name.text)
    print("UP主名称:", up_name.text)
    print("播放量:", play_text.text)
    print("点赞数:", like_text.text)
    print("历史提示:", hint.text)
    print("-----------------------------")

# 打开一个文本文件用于写入
with open("bilibili_data.txt", "w", encoding="utf-8") as f:
    for a_tag, img_element, video_name, up_name, play_text, like_text, hint in zip(a_tags, images, video_names,
                                                                                   up_names, play_texts, like_texts,
                                                                                   history_hint):
        href = a_tag.get_attribute("href")
        src = img_element.get_attribute("data-src")  # 获取图片链接
        if src.startswith("//"):  # 检查链接是否以双斜杠开头
            src = "https:" + src  # 如果是，则添加https:

        f.write("链接: {}\n".format(href))
        f.write("图片链接: {}\n".format(src))
        f.write("视频名称: {}\n".format(video_name.text))
        f.write("UP主名称: {}\n".format(up_name.text))
        f.write("播放量: {}\n".format(play_text.text))
        f.write("点赞数: {}\n".format(like_text.text))
        f.write("历史提示: {}\n".format(hint.text))
        f.write("-----------------------------\n")

# 创建一个空的 DataFrame 用于存储数据
data = {
    '链接': [],
    '图片链接': [],
    '视频名称': [],
    'UP主名称': [],
    '播放量': [],
    '点赞数': [],
    '历史提示': []
}

# 将数据存储到 DataFrame 中
for a_tag, img_element, video_name, up_name, play_text, like_text, hint in zip(a_tags, images, video_names, up_names,
                                                                               play_texts, like_texts, history_hint):
    href = a_tag.get_attribute("href")
    src = img_element.get_attribute("data-src")  # 获取图片链接
    if src.startswith("//"):  # 检查链接是否以双斜杠开头
        src = "https:" + src  # 如果是，则添加https:

    data['链接'].append(href)
    data['图片链接'].append(src)
    data['视频名称'].append(video_name.text)
    data['UP主名称'].append(up_name.text)
    data['播放量'].append(play_text.text)
    data['点赞数'].append(like_text.text)
    data['历史提示'].append(hint.text)

df = pd.DataFrame(data)

# 将 DataFrame 写入 Excel 文件
df.to_excel("bilibili_data.xlsx", index=False)

'''数据库
CREATE DATABASE IF NOT EXISTS blibli;
USE blibli
;

CREATE TABLE IF NOT EXISTS videos (
    id INT AUTO_INCREMENT PRIMARY KEY,
    link VARCHAR(255),
    image_link VARCHAR(255),
    video_name VARCHAR(255),
    up_name VARCHAR(255),
    play_count VARCHAR(255),
    like_count VARCHAR(255),
    history_hint VARCHAR(255)
);
数据库'''
import mysql.connector
from mysql.connector import Error

try:
    # 连接到MySQL数据库
    conn = mysql.connector.connect(
        host='localhost',
        user='root',  # 替换为你的MySQL用户名
        password='123456',  # 替换为你的MySQL密码
        database='blibli'
    )

    # 检查数据库是否成功连接
    if conn.is_connected():
        cursor = conn.cursor()

        # 准备SQL插入语句
        insert_stmt = (
            "INSERT INTO videos (link, image_link, video_name, up_name, play_count, like_count, history_hint) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s)"
        )

        # 假设'data'是你的数据列表
        for href, src, video_name, up_name, play_text, like_text, history_hint in zip(
                data['链接'], data['图片链接'], data['视频名称'], data['UP主名称'], data['播放量'], data['点赞数'],
                data['历史提示']
        ):
            # 数据准备
            data_tuple = (href, src, video_name, up_name, play_text, like_text, history_hint)

            # 执行SQL语句
            cursor.execute(insert_stmt, data_tuple)

        # 提交到数据库执行
        conn.commit()
        print(f"{cursor.rowcount} rows were inserted.")

except Error as e:
    print("Error while connecting to MySQL", e)
finally:
    # 检查连接是否打开
    if conn.is_connected():
        cursor.close()
        conn.close()
        print("MySQL connection is closed")

# 关闭浏览器
driver.quit()



