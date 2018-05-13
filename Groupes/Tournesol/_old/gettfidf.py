
# coding: utf-8

# In[5]:

from sklearn import feature_extraction
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer
from lxml import etree


# In[18]:

def gettfidf(fichier):
    with open(fichier,'r') as f:
        tree = etree.parse(f)
        textes = tree.xpath('//text')
        text = []
        dictfidf={}
        values=[]
        featuress=[]
        for t in textes:
            text.append(t.text)
        vectorizer=CountVectorizer()
        transformer=TfidfTransformer()
        tfidf=transformer.fit_transform(vectorizer.fit_transform(text))
        word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
        weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
        for i in range(len(weight)):#打印每类文本的tf-idf词语权重，第一个for遍历所有文本，第二个for便利某一类文本下的词语权重  
            for j in range(len(word)):  
                if not weight[i][j] ==0:
                    dictfidf[weight[i][j]]=word[j]
        values = sorted(dictfidf.keys(),reverse=True)[:20]
        for v in values :
            if not dictfidf[v] =='de':
                featuress.append(dictfidf[v])
        return featuress



# In[ ]:



