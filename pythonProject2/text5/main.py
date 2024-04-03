
import requests
from bs4 import BeautifulSoup


class MyScrapyWindow(My_tk):
    def __init__(self,tk):
        super().__init__(tk)

def begin():
    root = Tk()
    MyScrapyWindow(root)
    root.mainloop()

if __name__ == '__main__':
    begin()