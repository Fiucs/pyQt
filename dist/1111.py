# coding:utf-8
'''app = QApplication(sys.argv)
win = QWidget()
win.resize(450,450)
win.move(0,300)
win.setWindowTitle('你大爷的，在这里')
win.show()
sys.exit(app.exec_())'''
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QCoreApplication
from pictostr import *
import sys
from pictureT import *
from PIL import  Image
import  argparse
from PyQt5.QtWidgets import   QFileDialog
ascii_char = list("$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")+list(
    "'1234567  "
)
##ascii_char=list("****************************                                  ")

def get_char(r,g,b,alpha=256):
    if alpha==0:
        return " "
    gray=(2126*r+7125*g+722*b)/10000
    x =int((gray/256)*len(ascii_char))
    return ascii_char[x]
def write_file(out_file_name,content):
    with open(out_file_name,"w+") as f:
        f.write(content)
def main(width=100,height=100,file_name="test.png",out_file_name="out_file1.txt"):#图片格式
    text=""
    ts=Image.open(file_name)
    wh=ts.size
    print(wh)
    print(wh[0],wh[1])
    #ts=ts.transpose(Image.FLIP_TOP_BOTTOM)
    ts=ts.resize((width,height),Image.NEAREST)#Image.NEAREST图片低质量
    for j in range(width):
        for i in range(height):
            content=ts.getpixel((i,j))
            text=text+get_char(*content)
        text+="\n"
    print(text)
    write_file(out_file_name,text)

class my_ui(Ui_hello):
    s1="s1"
    s2="s2"
    def __init__(self,MainWindow):
        super().setupUi(MainWindow)
        super().retranslateUi(MainWindow)
        self.pushButton.clicked.connect(self.get_n_)
        self.pushButton_3.clicked.connect(self.r_value)
        self.pushButton_2.clicked.connect(QCoreApplication.instance().quit)
        self.pushButton_4.clicked.connect(self.pic_add)
        self.pushButton_5.clicked.connect(self.str_add)
    def pic_add(self):

        picadd = QFileDialog.getOpenFileName(self.centralwidget, "选取文件", "./", "all (*);; (.txt);;img (*.png *.jpg)")
        self.s1=picadd[0]
        self.lineEdit.setText(self.s1)
        print(self.s1)
    def str_add(self):
        stradd = QFileDialog.getOpenFileName(self.centralwidget, "选取文件", "./", "all (*);; (.txt);;img (*.png *.jpg)")
        self.s2=stradd[0]
        self.strnameinp.setText(self.s2)
        print(self.s2)
    def get_n_(self):
        self.strnameinp.textChanged.connect(self.pt_n)

    def pt_n(self):
        self.s2=self.strnameinp.text()
        self.s1=self.lineEdit.text()



    def r_value(self):
        print(self.s1)
        #s1=(self.pt_n())[0]
        #s2=(self.pt_n())[1]
        main(file_name=self.s1,out_file_name=self.s2)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    widget = QtWidgets.QMainWindow()
    ui = my_ui(widget)
    widget.show()
    sys.exit(app.exec_())