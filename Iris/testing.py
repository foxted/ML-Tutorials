import numpy as np
import pydotplus
from sklearn import tree
from sklearn.datasets import load_iris
from sklearn.externals.six import StringIO

# initial data
iris = load_iris()
test_idx = [0, 50, 100]

# prepare training data
train_target = np.delete(iris.target, test_idx)
train_data = np.delete(iris.data, test_idx, axis=0)

# prepare testing data
test_target = iris.target[test_idx]
test_data = iris.data[test_idx]

# train decision tree
clf = tree.DecisionTreeClassifier()
clf.fit(train_data, train_target)

# compare test data with prediction
print test_target
print clf.predict(test_data)

# visualization
dot_data = StringIO()
tree.export_graphviz(clf,
                     out_file=dot_data,
                     feature_names=iris.feature_names,
                     class_names=iris.target_names,
                     filled=True, rounded=True,
                     impurity=False)

graph = pydotplus.graph_from_dot_data(dot_data.getvalue())
graph.write_pdf("iris.pdf")

print test_data[1], test_target[1]
print iris.feature_names, iris.target_names
