import jieba
from sklearn.model_selection import train_test_split
import joblib
import os
model = joblib.load('BGmodel.pkl')
vectorizer = joblib.load('vectorizer.pkl')
while 1 :
    text = input('請輸入要判斷的粉絲專業內文:')
    if text!='@@':
        text_cut = [' '.join(jieba.cut(text))]
        p = vectorizer.transform(text_cut)
        pp = model.predict(p)
        if pp[0]=='1':
            print('這偏綠')
        elif pp[0]=='0':
            print('這偏藍')
    elif text=='@@':
        os._exit()
