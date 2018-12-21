from collections import Counter
from os import path
import jieba
#jieba.load_userdict(path.join(path.dirname(__file__),'userdict//userdict.txt')) # 导入用户自定义词典

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS
import codecs

stopword_filepath = "./data/tools/stopwords.txt"
stopwords = []

def read_in_stopword():
    global stopwords#读入停用词
    file_obj = codecs.open(stopword_filepath,'r','utf-8')
    while True:
        line = file_obj.readline()
        line=line.strip('\r\n')
        if not line:
            break
        stopwords.append(line)
    file_obj.close()


        
def word_segment(sent,stop = True):

    global  stopwords
    words = list(jieba.cut(sent, cut_all=False)) 
    results = []

    for word in words:
        if word in stopwords and stop:
            continue#去除停用词
        results.append(word)
    finaltext = " ".join(results)
 
    return finaltext

def generate_wordcloud(text):
    '''
    输入文本生成词云,如果是中文文本需要先进行分词处理
    '''
    read_in_stopword()
    seg_list = word_segment(text)
    print("cut word  done.")
    # 设置显示方式
    d=path.dirname(__file__)
    alice_mask = np.array(Image.open(path.join(d, "img/bg.jpg")))
    font_path=path.join(d,"./data/tools/msyh.ttf")
    stopwords = set(STOPWORDS)
    wc = WordCloud(background_color="white",# 设置背景颜色
           max_words=500, # 词云显示的最大词数  
           mask=alice_mask,# 设置背景图片       
           stopwords=stopwords, # 设置停用词
           font_path=font_path, # 兼容中文字体，不然中文会显示乱码
                  )

    # 生成词云 
    wc.generate(seg_list)

    # 生成的词云图像保存到本地
    wc.to_file(path.join(d, "img//alice2.png"))

    # 显示图像
    plt.imshow(wc, interpolation='bilinear')
    # interpolation='bilinear' 表示插值方法为双线性插值
    plt.axis("off")# 关掉图像的坐标
    plt.show()

if __name__ == '__main__':
    
    print("reading files")
    for i in range(1,11):
        text = ""
        filepath = './data/raw/output'+str(i)+'.txt'
        f = open(filepath)
        line = f.readline()
        j = 0
        while(line):
            j += 1
            line = f.readline()
            if j % 100 == 3:
                text += line.strip('\n')
        f.close()

    generate_wordcloud(text)