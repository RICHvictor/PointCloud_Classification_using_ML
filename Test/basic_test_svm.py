# encoding=utf-8

#####################
# basic_test_svm.py #
#####################

from sklearn import preprocessing
from sklearn.externals import joblib
import numpy as np  
from sklearn import metrics

# load data for testing
feature_matrix = np.loadtxt('/media/shao/TOSHIBA EXT/data_object_velodyne/feature_matrix_with_label/test/r_0.16.txt')
print('the shape of the loaded feature matrix is ', feature_matrix.shape)

# feature scaling and normalizing
np.random.shuffle(feature_matrix)
data = feature_matrix[:, :-1]
target = feature_matrix[:, -1]
# scaler = preprocessing.MaxAbsScaler(copy=False)
scaler = preprocessing.StandardScaler(copy=False)
scaler.fit_transform(data)
normalizer = preprocessing.Normalizer(norm='l2', copy=False)
normalizer.fit_transform(data)

# load the trained model
clf = joblib.load('/home/shao/文档/VSCodeWS/Masterarbeit_Code/PointCloud_Classification/Training/svm.pkl')

# prediction / test
y_pred = clf.predict(data)
score = metrics.accuracy_score(target, y_pred)
print('accuracy score = ', score)
conf_matrix = metrics.confusion_matrix(target, y_pred, [0,1,2,3,4])
print('confusion matrix = ', conf_matrix)
recall = metrics.recall_score(target, y_pred, average='weighted')
print('recall score = ', recall)
precision = metrics.precision_score(target, y_pred, average='weighted')
print('precision score = ', precision)