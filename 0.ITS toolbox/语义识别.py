import re # 正则表达式库
import jieba   #分词
import collections # 词频统计库
import numpy as np
import pandas as pd
import networkx as nx  #复杂网络分析库
import matplotlib.pyplot as plt

num=40
G=nx.Graph()
plt.figure(figsize=(20,14))
plt.rcParams['axes.unicode_minus'] = False    # 用来正常显示负号
plt.rcParams['font.sans-serif'] = ['SimHei']   # 用来正常显示中文标签

# 读取文件
fn = open('D:\总的.txt',encoding='utf-8') # 打开文件
string_data = fn.read() # 读出整个文件
fn.close() # 关闭文件

# 文本预处理
pattern = re.compile(u'\t|\.|-|:|;|\)|\(|\?|"') # 定义正则表达式匹配模式
string_data = re.sub(pattern, '', string_data) # 将符合模式的字符去除

# 文本分词
seg_list_exact = jieba.cut(string_data, cut_all = False) # 精确模式分词
object_list = []
# remove_words = list(open('D:666.txt','r',encoding='gbk').read()) # 自定义去除词库
remove_words = list(open('D:666.txt','r',encoding='utf-8').read()) # 自定义去除词库
remove_words.append("\n")
remove_words.append("大后")
print(remove_words)

for word in seg_list_exact: # 循环读出每个分词
    if word not in remove_words: # 如果不在去除词库中
        object_list.append(word) # 分词追加到列表

        # 词频统计
word_counts = collections.Counter(object_list) # 对分词做词频统计
word_counts_top = word_counts.most_common(num) # 获取最高频的词
word = pd.DataFrame(word_counts_top, columns=['关键词','次数'])
print(word)

word_T = pd.DataFrame(word.values.T,columns=word.iloc[:,0])
net = pd.DataFrame(np.mat(np.zeros((num,num))),columns=word.iloc[:,0])

k = 0
#构建语义关联矩阵
for i in range(len(string_data)):
    if string_data[i] == '\n':  #根据换行符读取一段文字
        seg_list_exact = jieba.cut(string_data[k:i], cut_all = False) # 精确模式分词
        object_list2 = []
        for words in seg_list_exact: # 循环读出每个分词
            if words not in remove_words: # 如果不在去除词库中
                object_list2.append(words) # 分词追加到列表
word_counts2 = collections.Counter(object_list2)
word_counts_top2 = word_counts2.most_common(num) # 获取该段最高频的词
word2 = pd.DataFrame(word_counts_top2)
word2_T = pd.DataFrame(word2.values.T,columns=word2.iloc[:,0])
relation = list(0 for x in range(num))
# 查看该段最高频的词是否在总的最高频的词列表中
for j in range(num):
    for p in range(len(word2)):
        if word.iloc[j,0] == word2.iloc[p,0]:
            relation[j] = 1
            break
        #对于同段落内出现的最高频词，根据其出现次数加到语义关联矩阵的相应位置
for j in range(num):
    if relation[j] == 1:
        for q in range(num):
            if relation[q] == 1:
                net.iloc[j, q] = net.iloc[j, q] + word2_T.loc[1, word_T.iloc[0, q]]
    k = i + 1

            # 处理最后一段内容，完成语义关联矩阵的构建


n = len(word)
        # 边的起点，终点，权重
for i in range(n):
    for j in range(i, n):
        G.add_weighted_edges_from([(word.iloc[i, 0], word.iloc[j, 0], net.iloc[i, j])])
print(G.edges())
nx.draw_networkx(G,
                    pos=nx.spring_layout(G),
                    # 根据权重的大小，设置线的粗细
                    width=[float(v['weight'] / 300) for (r, c, v) in G.edges(data=True)],
                    edge_color='orange',
                    # 根据词出现的次数，设置点的大小
                    node_size=[float(net.iloc[i, i] * 6) for i in np.arange(20)],node_color='white'
                    )
plt.axis('off')
#plt.title('助攻表现（常规赛）',fontstyle='oblique')
#plt.savefig('总的.png')
plt.show()
