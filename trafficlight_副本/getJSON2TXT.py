from importlib.resources import contents
import json
from turtle import width
from jsonpath import jsonpath
import os



def json2txt(pic_path,labels_types_path,title):
    with open(labels_types_path, encoding="utf-8")as labels:    
        list_id = []
        pyth_list_labels = json.load(labels)
        for i in range(len(pyth_list_labels)):
            list_id.append(pyth_list_labels[i]["id"])
    with open(pic_path, encoding="utf-8")as fp:
        pyth_list = json.load(fp)
        res = eval(pyth_list.get('rectTool').replace('true','True').replace('false', 'False'))
        W = res.get("width")
        H = res.get("height")
        items = res.get('step_1').get('result')
        features =  [(item['x'], item['y'], item['width'], item['height'], item['attribute']) for item in items]
        
        
        file = open(title+".txt","w")
        for f in features:
            x = f[0]
            y = f[1]
            w = f[2]
            h = f[3]
            id = f[4]
            #拉框图片中心点x坐标并进行归一化
            a1 = (w/2+x)/W
            #拉框图片中心点y坐标并进行归一化
            a2 = (h/2+y)/H
            #拉框图片宽度进行归一化
            a3 = w/W
            #拉框图片高度进行归一化
            a4 = h/H
            for i in range(len(list_id)):
                if id == list_id[i]:  
                    file.write(str(i)+" "+str(a1)+" "+str(a2)+" "+str(a3)+" "+str(a4)+"\n")
        file.close()



labels_types_path ="/Users/xixi/Downloads/yolov5/data/example/labels.json"
lables_json_path = "/Users/xixi/Downloads/yolov5/data/example/labelsjson"
path_list = os.listdir(lables_json_path)

#store_path = "/Users/xixi/Downloads/yolov5/data/labels_/labelstxt"
for p in path_list:
    title = p.rstrip(".json")
    json2txt((lables_json_path+"/"+p),labels_types_path,title)
