import os  
import sys 
import re
from sklearn import feature_extraction  
from sklearn.feature_extraction.text import TfidfTransformer  
from sklearn.feature_extraction.text import CountVectorizer  

chiffre=re.compile("\d+")
ordonnance=dict()
jury=open("phrases.txt", "r", encoding="utf-8").read()
jour=open("contraste.txt", "r", encoding="utf-8").read()

if __name__ == "__main__":  
    results=open("jury.txt", "w", encoding="utf-8")
    corpus=[jury,#第一类文本切词后的结果 
       jour]#第二类文本的切词结果  
        
    vectorizer=CountVectorizer()#该类会将文本中的词语转换为词频矩阵，矩阵元素a[i][j] 表示j词在i类文本下的词频  
    transformer=TfidfTransformer()#该类会统计每个词语的tf-idf权值  
    tfidf=transformer.fit_transform(vectorizer.fit_transform(corpus))#第一个fit_transform是计算tf-idf，第二个fit_transform是将文本转为词频矩阵  
    word=vectorizer.get_feature_names()#获取词袋模型中的所有词语  
    weight=tfidf.toarray()#将tf-idf矩阵抽取出来，元素a[i][j]表示j词在i类文本中的tf-idf权重  
    for j in range(len(word)):
        if (weight[0][j] > 0.001) and (weight[1][j] < 0.001) and (word[j] in jury) and not (chiffre.match(word[j])):
            ordonnance[word[j]] = weight[0][j]
    for k,v in sorted(ordonnance.items(), key=lambda t:t[1], reverse=True):
        results.write(k+"\t"+str(v)+'\n')
        print(k+"\t"+str(v)+'\n')
      
    results.close()