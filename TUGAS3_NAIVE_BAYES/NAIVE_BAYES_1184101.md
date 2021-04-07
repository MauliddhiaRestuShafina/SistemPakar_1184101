# Sistem Pakar_1184101_Mauliddhia Restu Shafina

# Naive Bayes
Untuk tugas kali ini membahas mengenai Naive Bayes. Memiliki fungsi untuk mengklasifikasi peluang terjadinya sesuatu berdasarkan data yang dimiliki. Pada kali ini, membahas mengenai wine. Untuk datasetnya langsung import dari sklearn dan memiliki 13 fitur diantaranya adalah alcohol, malic_acid, ash, alcalinity_of_ash, magnesium, total_phenols, flavanoids, nonflavanoid_phenols, proanthocynains, color_intensity, hue, od280/od315_of_diluted_wines, proline.
# from sklearn import datasets
Digunakan untuk mengimport dataset dari sklearn
# from sklearn.model_selection import train_test_split
Digunakan untuk mengimport train_test_split dari sklearn.model_sselecetion
# from sklearn.naive_bayes import GaussianNB
Digunakan untuk mengimport GaussianNB dari sklearn.naive_bayes
# from sklearn import metrics
Digunakan untuk mengimport metrics dari sklearn
# wine = datasets.load_wine()
Untuk meload datatset wine
# print("Features: ", wine.feature_names)
Untuk mecetak features yang ada 13
# print("Labels: ", wine.target_names)
Mencetak jenis label wine (class_0, class_1, Class_2)
# wine.data.shape
Mencetak data dengan shape
# print (wine.data[0:5])
Mencetak data wine 0:5
# print (wine.target)
mencetak label wine (0: class_0, 1: class_1, 2: class_2
#Import fungsi train_test_split
Pisahkan set data menjadi set training dan set testing, seperti dibawah ini
# X_train, X_test, y_train, y_test = train_test_split(wine.data, wine.target, test_size=0.3,random_state=109) # 70% training and 30% test
# gnb = GaussianNB()
Digunakan untuk pengklasifikasian GaussianNB
# gnb.fit(X_train, y_train)
Digunakan untuk mencoba model menggunakan set data training
# y_pred = gnb.predict(X_test)
Digunakan untuk prediksi respon untuk set data testing
# print("Accuracy:",metrics.accuracy_score(y_test, y_pred))
Mencetak seberapa sering pengklasifikasian benar pada akurasi model
# output
Hasil dari pembahasan diatas menggunakan metode Naive Bayes adalah mendefinisikan wine. untuk 0 mendefinisikan layaknya wine untuk dikonsumsi dan 1 mendefinisikan wine tidak laya untuk dikonsumsi. 
