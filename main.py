import sklearn
from sklearn import datasets
from sklearn import svm
from sklearn import metrics
from sklearn.neighbors import KNeighborsClassifier

cancer = datasets.load_breast_cancer()

# print(cancer.feature_names)
# print(cancer.target_names)

x = cancer.data
y = cancer.target

x_train, x_test, y_train, y_test = sklearn.model_selection.train_test_split(x, y, test_size= 0.2)


# Use SVC without adding any parameters
# clf = svm.SVC()
# clf.fit(x_train, y_train)
# y_pred = clf.predict(x_test)
# accuracy = metrics.accuracy_score(y_test, y_pred)
# # 87.719298%
# print(format(accuracy, "%"))

# use one kernel: linear with soft/hard margin or poly with degree
clf = svm.SVC(kernel = "linear", C=2)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
# 98.245614%
print(format(accuracy, "%"))

# Use KNN model to classify
clf = KNeighborsClassifier(n_neighbors=9)
clf.fit(x_train, y_train)
y_pred = clf.predict(x_test)
accuracy = metrics.accuracy_score(y_test, y_pred)
# 92.105263%
print(format(accuracy, "%"))


classes = ['malignant', 'benign']