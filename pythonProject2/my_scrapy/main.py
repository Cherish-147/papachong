from tkinter import *
from my_tk import My_tk  # 导入自定义的My_tk类


class MyScrapyWindow(My_tk): #创建MyScrapyWindow类
    def __init__(self,tk): #MyScrapyWindow类的构造方法（必须要有一个self参数
        super().__init__(tk)
        # super() 首先找到父类（就是类 My_tk），
        # 然后把类 MyScrapyWindow 的对象转换为类 My_tk 的对象


def begin():
    root = Tk()  # 获取用户在 Tk中输入的 值，并存储为root
    MyScrapyWindow(root)  # 使用 MyScrapyWindow 解析存储的root 内容
    root.mainloop()  # 窗口进入循环（为什么啊？）

# 如果该脚本被直接运行，调用 begin 函数启动应用程序
if __name__ == '__main__':  # 判断当前脚本是否为主程序入口
    begin()  # 调用begin函数，启动程序
