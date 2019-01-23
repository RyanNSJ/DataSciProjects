## 2. Generating Data That Contains Nonlinearity ##

from mpl_toolkits.mplot3d import Axes3D
from sklearn.datasets import make_moons
import pandas as pd
import matplotlib.pyplot as plt

data = make_moons(n_samples=100, random_state=3, noise=0.04)

features = pd.DataFrame(data[0])
labels = pd.Series(data[1])

fig = plt.figure(figsize=(8,8))
ax = fig.add_subplot(111, projection="3d")
ax.scatter(features[0], features[1], labels, cmap=labels)
ax.set_xlabel('x1')
ax.set_ylabel('x2')
ax.set_zlabel('y')

## 4. Training A Neural Network Using Scikit-learn ##

from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
np.random.seed(8)

data = make_moons(100, random_state=3, noise=0.04)
features = pd.DataFrame(data[0])
labels = pd.Series(data[1])
features["bias"] = 1

shuffled_index = np.random.permutation(features.index)
shuffled_data = features.loc[shuffled_index]
shuffled_labels = labels.loc[shuffled_index]
mid_length = int(len(shuffled_data)/2)
train_features = shuffled_data.iloc[0:mid_length]
test_features = shuffled_data.iloc[mid_length:len(shuffled_data)]
train_labels = shuffled_labels.iloc[0:mid_length]
test_labels = shuffled_labels.iloc[mid_length: len(labels)]

nn_model = MLPClassifier(hidden_layer_sizes=(1,), activation="logistic")
nn_model.fit(train_features,train_labels)
nn_predictions = nn_model.predict(test_features)
nn_accuracy = accuracy_score(test_labels,nn_predictions)

log_model = LogisticRegression()
log_model.fit(train_features,train_labels)
log_predictions = log_model.predict(test_features)
log_accuracy = accuracy_score(test_labels,log_predictions)



print(log_accuracy)
print(nn_accuracy)


## 5. Hidden Layer With Multiple Neurons ##

np.random.seed(8)
shuffled_index = np.random.permutation(features.index)
shuffled_data = features.loc[shuffled_index]
shuffled_labels = labels.loc[shuffled_index]
mid_length = int(len(shuffled_data)/2)
train_features = shuffled_data.iloc[0:mid_length]
test_features = shuffled_data.iloc[mid_length:len(shuffled_data)]
train_labels = shuffled_labels.iloc[0:mid_length]
test_labels = shuffled_labels.iloc[mid_length: len(labels)]

neurons = [1, 5, 10, 15, 20, 25]
accuracies = []

for num in neurons:
    nn_model = MLPClassifier(hidden_layer_sizes=(num,), activation="logistic")
    nn_model.fit(train_features,train_labels)
    nn_predictions = nn_model.predict(test_features)
    nn_accuracy = accuracy_score(test_labels,nn_predictions)
    accuracies.append(nn_accuracy)
    
print(accuracies)

## 6. Multiple Hidden Layers ##

neurons = [1, 5, 10, 15, 20, 25]
nn_accuracies = []

for num in neurons:
    nn = MLPClassifier(hidden_layer_sizes=(num,num), activation="relu",  max_iter=1000)
    nn.fit(train_features,train_labels)
    prediction = nn.predict(test_features)
    accuracy = accuracy_score(test_labels,prediction)
    nn_accuracies.append(accuracy)

print(nn_accuracies)