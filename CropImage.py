#coding=utf-8
import  xml.dom.minidom
from PIL import Image
import glob


a = glob.glob(r"C:\Users\chiahao_mai\Desktop\Annotation\n02085620-Chihuahua\*")
b = glob.glob(r"C:\Users\chiahao_mai\Desktop\images\n02085620-Chihuahua\*.jpg")
a.sort()
b.sort()

xList = []
yList = []
XList = []
YList = []
for i in range(0,len(a)):
    dom = xml.dom.minidom.parse(a[i])
    root = dom.documentElement

    xmin = root.getElementsByTagName('xmin')
    x = xmin[0]
    xList.append(x.firstChild.data)

    ymin = root.getElementsByTagName('ymin')
    y = ymin[0]
    yList.append(y.firstChild.data)

    xmax = root.getElementsByTagName('xmax')
    X = xmax[0]
    XList.append(X.firstChild.data)

    ymax = root.getElementsByTagName('ymax')
    Y = ymax[0]
    YList.append(Y.firstChild.data)

    im = Image.open(b[i])
    region = im.crop((int(xList[i]), int(yList[i]), int(XList[i]), int(YList[i])))
    region.save("new/02085620_"+ a[i][60:] + "_20180704.jpg")

    fp = open("log.txt", "a")
    fp.write("Chihuahua,02085620_"+ a[i][60:] + "_20180704.jpg," + a[i][70:])
    fp.write('\n')
    fp.close()
