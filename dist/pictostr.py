from PIL import  Image
import  argparse
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
if __name__=='__main__':#为真执行以下语句 为假即被其他.py调用则不执行以下语句
    s1=input("输入图片名：")
    s2=input("输入文件名：")
    s2="C:/Users/FKU/Pictures//"+s2
    main(file_name=s1,out_file_name=s2)








