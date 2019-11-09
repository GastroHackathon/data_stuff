#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov  9 17:30:33 2019

@author: drx
"""


from sklearn.neighbors import KNeighborsClassifier  
import pandas as pd
import pickle



    


X_train = training_data.drop('y', axis=1)
y_train = training_data['y']
model = KNeighborsClassifier(n_neighbors=50)  
model.fit(X_train, y_train)

# persistance
modelname = type(model).__name__+'_latest'
pickle.dump(model, open(filename, 'wb'))

def preprocess(dishes):
    data_mockup = pd.read_csv('data/data_mockup.csv')
    country_list = ['Austria', 'Japan', 'China', 'Italy', 'Turkey']
    data_all_dishes = pd.DataFrame()
    for dish in dishes:
        dish_data = data_mockup
        for atribute in dish_data:
            if atribute not in country_list:
                dish_data[atribute] = dish[atribute]
        dish_data[dish['origin']] = True
        data_all_dishes = data_all_dishes.append(dish_data)    
    return data_all_dishes

def predict_choice(user, dishes):
    model = pickle.load(open('data/KNeighborsClassifier_latest'+user['username'], 'rb'))
    data_all_dishes = preprocess(dishes)
    pred_data = data_all_dishes.drop('name', axis = 1)        
    y_hat = model.predict_proba(pred_data)
    data_all_dishes['y'] = y_hat
    data_all_dishes = data_all_dishes.sort_values('y', ascending=False)
    return data_all_dishes.iloc[:3]
    
# creat training data
with open('data/dishes_full.json') as f:
    dishes = json.load(f)

data_all_dishes = preprocess(dishes)
data_all_dishes.shape

data_all_dishes.to_csv('data/training_data_premature.csv')
    
# train model
data_all_dishes = pd.read_csv('data/training_data.csv')
data_all_dishes.columns


y_hat = classifier.predict(X_test)  



modelname = type(model).__name__+'latest'
    
filename = 'data/models/' + league +'/' + years[-1] +'_'+ modelname +'_newest'\n",
print('saved: ', filename)
pickle.dump(model, open(filename, 'wb'))



