import requests  # requests将库导入python
import tkinter as tk  # tkinter库导入后命名为tk
import tkinter.messagebox  # tkinter中的messagebox 将库导入python
from bs4 import BeautifulSoup  # BeautifulSoup中的bs4导入python

url = ''
html = ''


def getHTML():
    global url, html  # global将全局变量中的url和html改成下面的赋值
    url = entry_url.get()
    text_req_header.delete('1.0', 'end')
    text_res_header.delete('1.0', 'end')
    text_res_html.delete('1.0', 'end')
    if url == '':
        tk.messagebox.showerror("错误", '网页路径为空')
        return
    try:
        response = requests.get(url)
        req_headers = ''
        res_headers = ''
        req_headers += 'method:' + response.request.method + '\n'
        for key, value in response.request.headers.items():
            req_headers += key + ':' + value + '\n'
        for key, value in response.headers.items():
            res_headers += key + ':' + value + '\n'
        text_req_header.insert(tk.END, req_headers)
        text_res_header.insert(tk.END, res_headers)
        text_res_html.insert(tk.END, response.text)
        html = response.text
    except:
        print('error')


def getPoetry():
    text_get_poetry.delete('1.0', 'end')
    soup = BeautifulSoup(html, 'html.parser')
    contents = soup.findAll(class_='view_text')
    get_html_poetrys = ''
    for value in contents:
        get_html_poetrys += value.find('h2').text + '\n'
        get_html_poetrys += value.find('p').text + '\n'
    text_get_poetry.insert(tk.END, get_html_poetrys)


window = tk.Tk()
window.title('初识爬虫')
window.geometry('800x1000')

label_url = tk.Label(window, text='url: ')
label_url.place(x=10, y=10)
entry_url = tk.Entry(window, width=30)
entry_url.place(x=40, y=10)

button_get_html = tk.Button(window, text='获取网页', command=getHTML)
button_get_html.place(x=10, y=50)

label_req = tk.Label(window, text='请求头信息：')
label_req.place(x=10, y=90)
text_req_header = tk.Text(window, height=10, width=40)
text_req_header.place(x=10, y=120)

label_res = tk.Label(window, text='响应头信息：')
label_res.place(x=10, y=290)
text_res_header = tk.Text(window, height=10, width=40)
text_res_header.place(x=10, y=320)

label_html = tk.Label(window, text='响应网页代码：')
label_html.place(x=10, y=490)
text_res_html = tk.Text(window, height=30, width=40)
text_res_html.place(x=10, y=520)

button_get_poetry = tk.Button(window, text='爬取古诗', command=getPoetry)
button_get_poetry.place(x=400, y=10)
text_get_poetry = tk.Text(window, height=30, width=40)
text_get_poetry.place(x=400, y=60)

window.mainloop()

if __name__ == '__main__':
    print('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
