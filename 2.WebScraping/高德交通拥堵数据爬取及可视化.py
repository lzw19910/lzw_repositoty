import requests
import pandas as pd
import time
import numpy as np
import folium
import webbrowser
from folium.plugins import HeatMap


def get_GaoDeData():
    url='https://trp.autonavi.com/assets/data/data2.txt'
    response=requests.get(url)
    datas=response.text
    count=datas.split("&")
    print(len(count))
    temp=[]
    for i in range(len(count)-1):
        wzy=count[i].split(",")
        x=float(wzy[0])
        y=float(wzy[1])
        z=int(wzy[2])
        temp.append([x,y,z])

    map_osm = folium.Map(location=[35,110],zoom_start=10)    #绘制Map，开始缩放程度是5倍
    HeatMap(temp).add_to(map_osm)  # 将热力图添加到前面建立的map里
    file_path = r"高德交通大数据地图可视化.html"
    map_osm.save(file_path)     # 保存为html文件
    webbrowser.open(file_path)  # 默认浏览器打开

    df=pd.DataFrame(temp)
    now = time.strftime("%Y-%m-%d-%H_%M_%S",time.localtime(time.time()))
    df.to_csv('GaoDe'+now+'.txt',mode='a',index = False,header=None)


if __name__ =='__main__':
    get_GaoDeData()