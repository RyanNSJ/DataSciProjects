## 1. Introduction ##

# Let's say this is your running history for the past week
# For each day, it records whether or not you ran, and whether or not you were tired
days = [["ran", "was tired"], ["ran", "was not tired"], ["didn't run", "was tired"], ["ran", "was tired"], ["didn't run", "was not tired"], ["ran", "was not tired"], ["ran", "was tired"]]

# Let's say we want to use Bayes' theorem to calculate the odds that you were tired, given that you ran
# This is P(A)
prob_tired = len([d for d in days if d[1] == "was tired"]) / len(days)
# This is P(B)
prob_ran = len([d for d in days if d[0] == "ran"]) / len(days)
# This is P(B|A)
prob_ran_given_tired = len([d for d in days if d[0] == "ran" and d[1] == "was tired"]) / len([d for d in days if d[1] == "was tired"])

# Now we can calculate P(A|B)
prob_tired_given_ran = (prob_ran_given_tired * prob_tired) / prob_ran

print("Probability of being tired given that you ran: {0}".format(prob_tired_given_ran))

## 2. Overview of Naive Bayes ##

# Here's our data, but with "woke up early" or "didn't wake up early" added
days = [["ran", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was tired", "didn't wake up early"], ["didn't run", "was tired", "woke up early"], ["ran", "was not tired", "didn't wake up early"], ["ran", "was tired", "woke up early"]]

# We're trying to predict whether or not you were tired on this day
new_day = ["ran", "didn't wake up early"]

def calc_y_probability(y_label, days):
    return len([d for d in days if d[1] == y_label]) / len(days)

def calc_ran_probability_given_y(ran_label, y_label, days):
    return len([d for d in days if d[1] == y_label and d[0] == ran_label]) / len(days)

def calc_woke_early_probability_given_y(woke_label, y_label, days):
    return len([d for d in days if d[1] == y_label and d[2] == woke_label]) / len(days)

denominator = len([d for d in days if d[0] == new_day[0] and d[2] == new_day[1]]) / len(days)
# Plug all the values into our formula
# Multiply the class (y) probability, and the probability of the x-values occurring given that class
prob_tired = (calc_y_probability("was tired", days) * calc_ran_probability_given_y(new_day[0], "was tired", days) * calc_woke_early_probability_given_y(new_day[1], "was tired", days)) / denominator

prob_not_tired = (calc_y_probability("was not tired", days) * calc_ran_probability_given_y(new_day[0], "was not tired", days) * calc_woke_early_probability_given_y(new_day[1], "was not tired", days)) / denominator

# Make a classification decision based on the probabilities
classification = "was tired"
if prob_not_tired > prob_tired:
    classification = "was not tired"
print("Final classification for new day: {0}. Tired probability: {1}. Not tired probability: {2}.".format(classification, prob_tired, prob_not_tired))

## 7. A Faster Way to Make Predictions ##

from sklearn.naive_bayes import MultinomialNB
from sklearn.feature_extraction.text import CountVectorizer
from sklearn import metrics

# Generate counts from text using a vectorizer  
# We can choose from other available vectorizers, and set many different options
# This code performs our step of computing word counts
vectorizer = CountVectorizer(stop_words='english', max_df=.05)
train_features = vectorizer.fit_transform([r[0] for r in reviews])
test_features = vectorizer.transform([r[0] for r in test])

# Fit a Naive Bayes model to the training data
# This will train the model using the word counts we computed and the existing classifications in the training set
nb = MultinomialNB()
nb.fit(train_features, [int(r[1]) for r in reviews])

# Now we can use the model to predict classifications for our test features
predictions = nb.predict(test_features)

# Compute the error
# It's slightly different from our model because the internals of this process work differently from our implementation
fpr, tpr, thresholds = metrics.roc_curve(actual, predictions, pos_label=1)
print("Multinomal naive bayes AUC: {0}".format(metrics.auc(fpr, tpr)))