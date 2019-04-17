#coding:utf-8
#根据jpglist.txt中的数据，结合annotation文件，
#以<class_name> <left> <top> <right> <bottom> [<difficult>]格式读出
import os
from xml.dom.minidom import parse
import xml.dom.minidom
jpglist_dir = "C:\Users\Liupu\Desktop\learn\jpglist.txt"
annotation_dir = "C:\Users\Liupu\Desktop\learn\Annotations"
with open(jpglist_dir,'r') as f1:
    lines = f1.readlines()
    print(lines)
    for line in lines:
        num = line[0:6] #截取第i位到第i+6位的字符
        print(num)
        #os.mknod(num +".txt")
        with open(num +".txt",'a+') as newfile:
            #print("*****%s"%num)
            new_dir= annotation_dir +"\\"+ num + ".xml"
            DOMTree = xml.dom.minidom.parse(new_dir)
            collection = DOMTree.documentElement
            objects =  collection.getElementsByTagName("object")
            for object in objects:
                class_name = object.getElementsByTagName('name')[0].childNodes[0].data
                left = object.getElementsByTagName('xmin')[0].childNodes[0].data
                top = object.getElementsByTagName('ymin')[0].childNodes[0].data
                right = object.getElementsByTagName('xmax')[0].childNodes[0].data
                bottom = object.getElementsByTagName('ymax')[0].childNodes[0].data
                dif = object.getElementsByTagName('difficult')[0].childNodes[0].data
                if dif == "0":
                    newfile.write(class_name+" "+left+" "+top+" "+right+" "+bottom+"\n")
                else:
                    newfile.write(class_name+" "+left+" "+top+" "+right+" "+bottom+" "+"difficult"+"\n")
                






            
                                            
                    
                    
            
            
        
