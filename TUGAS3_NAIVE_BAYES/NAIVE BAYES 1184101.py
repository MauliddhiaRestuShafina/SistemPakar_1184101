# -*- coding: utf-8 -*-
"""
Created on Wed Apr  7 11:43:40 2021

@author: Asus VIVOBOOK
"""

from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn import metrics

#Load dataset
wine = datasets.load_wine()

# print nama dari 13 fitur
print("Features: ", wine.feature_names)

# print jenis label anggur (class_0, class_1, class_2)
print("Labels: ", wine.target_names)

# print data dengan shape
wine.data.shape

print (wine.data[0:5])

# print label anggur (0: Class_0, 1: class_2, 2: class_2)
print (wine.target)

# Impor fungsi train_test_split

# Pisahkan set data menjadi set pelatihan dan set pengujian
X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109) # 70% training and 30% test

# Membuat Pengklasifikasi Gaussian
gnb = GaussianNB()

# Mencoba model menggunakan set pelatihan
gnb.fit(X_train, y_train)

#Prediksi respons untuk set data pengujian
y_pred = gnb.predict(X_test)

# Akurasi Model, seberapa sering pengklasifikasi benar
print("Accuracy:",metrics.accuracy_score(y_test, y_pred))