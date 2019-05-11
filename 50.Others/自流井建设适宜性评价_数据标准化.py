import arcpy


# 富顺
fc = 'U:/富顺数据/fushun.gdb/a富顺数据获取标准化0427'
fields = ['MJ', 'GC', 'PX', 'PD', 'HL', 'SJ', 'BP', 'SJX', 'LD', 'SD']
# 标准化矩阵
data = [
     [553.25, 1490.90, 3504.95, 7831.116],  # 0面积
     [279.434, 285.101, 287.86, 393.527],  # 1平均高程
     [3.399, 4.821, 5.957, 6.864],  # 2平均坡向
     [8.807, 12.078, 13.294, 16.565],  # 3平均坡度
     [4177.933, 6087.827, 8950.625, 13241.7564],  # 4河流最近距离
     [809.805, 960.582, 1756.723, 5960.600],  # 5山脚最近距离
     [1835.47, 4713.27, 9225.30, 16299.63],  # 6变坡线最近距离
     [2805.23, 3869.35, 6605.57, 13641.26],  # 7山脊线最近距离
     [1261.154, 3424.58586, 7135.818, 13502.207],  # 8林地
     [4706.065, 6910.927, 10867.213, 17966.159]  # 9湿地
 ]
print(len(data))

# 自流井
# fc = 'U:\自流井建设适宜性评价分析数据.gdb/a自流井数据标准化20190427'
# fields = ['MJ', 'GC', 'PX', 'PD', 'HL', 'SJ', 'BP', 'SJX', 'LD', 'SD']
# #           0    1    2      3     4     5     6     7      8      9
# # 标准化矩阵
# data = [
#     [2135, 12282, 61250, 297572],  # 0面积
#     [352, 378, 387, 413],  # 1平均高程
#     [3.9, 4.9, 5.3, 6.3],  # 2平均坡向
#     [5.6, 8.6, 14.1, 24.5],  # 3平均坡度
#     [0.168, 0.236, 0.404, 0.817],  # 4河流最近距离
#     [0.0333, 0.1617, 0.6566, 2.5641],  # 5山脚最近距离
#     [0.0994, 0.1435, 0.2426, 0.4651],  # 6变坡线最近距离
#     [0.08042, 0.09204, 0.17244, 0.72846],  # 7山脊线最近距离
#     [0.00441, 0.02388, 0.10975, 0.48851],  # 8林地
#     [0.076507, 0.098225, 0.174733, 0.444244]  # 9湿地
#  ]
# print(len(data))


# 更新数据

for i in range(len(data)):
    with arcpy.da.UpdateCursor(fc, fields) as cursor:
        for row in cursor:
            print(row)
            if row[i] <= data[i][0]:
                row[i] = 1
            elif data[i][0] < row[i] <= data[i][1]:
                row[i] = 2
            elif data[i][1] < row[i] <= data[i][2]:
                row[i] = 3
            elif data[i][2] < row[i] <= data[i][3]:
                row[i] = 4
            elif row[i] > data[i][3]:
                row[i] = 5
            cursor.updateRow(row)
    print('success')





