import csv
import jieba
import pandas as pd
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn import metrics
import joblib

data = []
data_label = []
#讀入 分詞 轉換格式
with open('bgdata.csv', 'r',encoding='UTF-8') as csv_file:
    csv_reader = csv.reader(csv_file)
    for r in csv_reader:
        data.append([' '.join(jieba.cut(r[1]))])
        data_label.append(r[0])
df = pd.DataFrame(data, columns=['article'])
df['label'] = data_label

#切分測資
data_train,data_test,data_label_train,data_label_test = train_test_split(df['article'], df['label'], test_size=0.2)
#轉換器
vectorizer = CountVectorizer()
data_train = vectorizer.fit_transform(data_train)
data_test = vectorizer.transform(data_test)
joblib.dump(vectorizer, 'vectorizer.pkl')

#邏輯
BGmodel = LogisticRegression()
BGmodel.fit(data_train, data_label_train)

#測
pred = BGmodel.predict(data_test)
s = metrics.accuracy_score(data_label_test, pred)
print("準確率:%0.3f" % s)


joblib.dump(BGmodel, 'BGmodel.pkl')

