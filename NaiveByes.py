import numpy as np

from collections import Counter, defaultdict
 
def occurrences(list1):
    no_of_examples = len(list1)
    prob = dict(Counter(list1))
    for key in prob.keys():
        prob[key] = prob[key] / float(no_of_examples)
    return prob

def naive_bayes(training, outcome, new_sample):
    classes     = np.unique(outcome)
    rows, cols  = np.shape(training)
    likelihoods = {}
    for cls in classes:
        likelihoods[cls] = defaultdict(list)
 
    class_probabilities = occurrences(outcome)
 
    for cls in classes:
        row_indices = np.where(outcome == cls)[0]
        subset      = training[row_indices, :]
        r, c        = np.shape(subset)
        for j in range(0,c):
            likelihoods[cls][j] += list(subset[:,j])
 
    for cls in classes:
        for j in range(0,cols):
             likelihoods[cls][j] = occurrences(likelihoods[cls][j])
    print(likelihoods)
    results = {}
    for cls in classes:
         class_probability = class_probabilities[cls]
         for i in range(0,len(new_sample)):
             relative_values = likelihoods[cls][i]
             if new_sample[i] in relative_values.keys():
                 class_probability *= relative_values[new_sample[i]]
             else:
                 class_probability *= 0
             results[cls] = class_probability
    print(results)
    a=(results[0]/(results[0]+results[1]))*100
    b=(results[1]/(results[0]+results[1]))*100
    print(a)
    print(b)

import numpy as np
training = np.asarray(((1,1,0,0),
                       (1,1,0,1),
                       (0,1,0,0),
                       (2,2,0,0),
                       (2,0,1,0),
                       (2,0,1,1),
                       (0,0,1,1),
                       (1,2,0,0),
                      (1,0,1,0),
                      (2,2,1,0),
                      (1,2,1,1),
                      (0,2,0,1),
                      (0,1,1,0),
                      (2,2,0,1)));
 
outcome = np.asarray((0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 1, 1, 1, 0))
new_sample = np.asarray((2,1,1,0))
naive_bayes(training, outcome, new_sample)

#weather=['Rainy','Rainy','Overcast','Sunny','Sunny','Sunny','Overcast','Rainy','Rainy',
'Sunny','Rainy','Overcast','Overcast','Sunny']
#temp=['Hot','Hot','Hot','Mild','Cool','Cool','Cool','Mild','Cool','Mild','Mild','Mild','Hot','Mild']
#humidity=['High','High','High','High','Normal','Normal','Normal','High','Normal','Normal','Normal','High','Normal','High']
#windy=['F','T','F','F','F','T','T','F','F','F','T','T','F','T']
#type(weather)
#le = preprocessing.LabelEncoder()
# Converting string labels into numbers.
#weather_encoded=le.fit_transform(weather)
#print(weather_encoded)
#type(weather_encoded)
#temp_encoded=le.fit_transform(temp)
#humidity_encoded=le.fit_transform(humidity)
#windy_encoded=le.fit_transform(windy)
#play=['N','N','Y','Y','Y','N','Y','N','Y','Y','Y','Y','Y','N']
#label_encoded=le.fit_transform(play)
