#'''中文分词'''
#import jieba

##全模式
#seg1 = jieba.cut('我来自新疆乌鲁木齐水磨沟区',cut_all = True)             #cut_all=True 为全模式（输出为：我 来自 自新 新疆 乌鲁木齐 水磨 水磨沟 水磨沟区）
#print(' '.join(seg1))
##精确模式（默认）
#seg2 = jieba.cut('（），，，我来自新疆乌鲁木齐水磨沟区',cut_all = False)             #cut_all=False 为精确模式（输出为：我 来自 新疆 乌鲁木齐 水磨沟区）
#print(' '.join(seg2))


##搜索引擎模式
#seg3 = jieba.cut_for_search('张三硕士毕业于重庆邮电大学计算机科学与技术学院，后在美国斯坦福大学深造')
#print(','.join(seg3))
#print(list(seg3))

#for i in jieba.cut('我来自新疆乌鲁木齐水磨沟区',cut_all = True):             #jieba.cut()和jieba.cut_for_search()返回是个generator
    
#    print(i)


#'''统计词频'''
#from collections import Counter 

##打开文件
#content = open(r'F:\python_work\WordsCloud\pachong.txt',encoding = 'utf-8').read()

##获取分词频率前10的词
#c1 = Counter(content).most_common(10)           #输出包含字符
#print(c1)

#con_words = [x for x in jieba.cut(content) if len(x) > 2]           #利用jieba分离词，并找出大于2的词组
#c2 = Counter(con_words).most_common(10)
#print(c2)

##添加用户自定义字典
#text = '欧阳建国是创新办主任也是欢聚时代公司云计算方面的专家'
#print(','.join(jieba.cut(text)))                            #输出为：欧阳,建国,是,创新,办,主任,也,是,欢聚,时代,公司,云,计算,方面,的,专家

##jieba.load_userdict()添加词组
#jieba.load_userdict(r'F:\python_work\WordsCloud\user_dict.txt')
#print(','.join(jieba.cut(text)))                            #输出为：欧阳建国,是,创新办,主任,也,是,欢聚时代,公司,云计算,方面,的,专家




'''词云图'''
from wordcloud import WordCloud ,STOPWORDS      #STOPWORDS根据词频计算需要
import matplotlib.pyplot as plt
import jieba
from PIL import Image
from scipy.misc import imread
from collections import Counter                 #根据词频需要counter计算词频

'''根据文本生成词云'''
text = open(r'F:\python_work\WordsCloud\pachong.txt',encoding = 'utf-8')
#将文件分词做成列表
mylist = list(text)
word_list = [' '.join(jieba.cut(sentence)) for sentence in mylist]
#将列表中的元素用空格连接便于词频计算
new_text = ' '.join(word_list)

#设置字体
font_path = r'C:\Windows\Fonts\simkai.ttf'
#设置背景图片
mask = imread(r'F:\python_work\WordsCloud\apchong.png')
#设置背景图片颜色
background_color = 'white'
#设置最大词数
max_words = 2000
wordcloud = WordCloud(font_path = font_path,
                      mask = mask,
                      background_color = background_color,
                      max_words = max_words).generate(new_text)             #generate()根据文本生成词云图
#对图像进行处理
plt.imshow(wordcloud)
#关闭坐标轴
plt.axis('off')
plt.show()

#保存图像
wordcloud.to_file(r'F:\python_work\WordsCloud\\词云图片_文本.png')

'''根据词频生成词云图片'''
#分词
con_word = [x for x in jieba.cut(new_text) if len(x) >= 2]
#统计词频
frequencies = Counter(con_word).most_common()
#将词频转换为字典
frequencies = dict(frequencies)
wordcloud1 = WordCloud(font_path = font_path,
                      mask = mask,
                      background_color = background_color,
                      max_words = max_words).fit_words(frequencies)             #fit_words（）根据词频生成词云

#对图像进行处理
plt.imshow(wordcloud1)
#关闭坐标轴
plt.axis('off')
plt.show()

#保存图像
wordcloud1.to_file(r'F:\python_work\WordsCloud\\词云图片_词频.png')

#import matplotlib.pyplot as plt
#from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS
#import jieba
#import numpy as np
#from PIL import Image
#def wordyun():
# #导入背景图   
#backgrim=np.array(Image.open("C:\\Users\SAMSUNG\PycharmProjects\practice0829\qqzon\\bg.jpg"))
# #导入文本文件   text=open("C:\\Users\SAMSUNG\PycharmProjects\practice0829\qqzon\\1154540719worldcloud.txt",encoding='utf-8').read()
#    #jieba分词
#    wordlist = jieba.cut(text, cut_all=True)
#    wl = " ".join(wordlist)
##设置参数
#    wordcloud=WordCloud(
#        background_color='white',  #背景颜色
#        mask=backgrim ,   #背景图片
#        max_words = 300,  # 设置最多现实的词数
#        stopwords=STOPWORDS,  # 设置停用词
#        max_font_size=200,    # 设置字体最大值
#        font_path='C:/Users/Windows/fonts/STXINGKA.TTF',#设置字体，路径在电脑内
#        width=1600,
#        height=1000,
#        random_state=30,  # 设置有多少种随机生成状态，即有多少种配色方案
#        # scale=.5
#    ).generate(text)
##改变字体颜色
#    image_colors = ImageColorGenerator(backgrim)
##展示词云
#    plt.imshow(wordcloud)
##是否显示想x，y坐标
#    plt.axis("off")
#    plt.show()
##写入文件
#    wordcloud.to_file('py_book1.png')  # 把词云保存下
#wordyun()