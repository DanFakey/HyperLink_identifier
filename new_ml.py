import sys
import numpy as np
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import csv


def load_data_from_csv(filename):
    data = {'text': [], 'label': []}
    with open(filename, newline='', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            data['text'].append(row['text'])
            data['label'].append(row['label'])
    return data

def train_test_split(data, validation_split=0.1):
    sz = len(data['text'])
    indices = np.arange(sz)
    np.random.shuffle(indices)

    X = [data['text'][i] for i in indices]
    Y = [data['label'][i] for i in indices]
    nb_validation_samples = int(validation_split * sz)

    return {
        'train': {'x': X[:-nb_validation_samples], 'y': Y[:-nb_validation_samples]},
        'test': {'x': X[-nb_validation_samples:], 'y': Y[-nb_validation_samples:]}
    }

def openai():
    data = load_data_from_csv('train_set.csv')
    D = train_test_split(data)
    
    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', SGDClassifier(loss='hinge')),
    ])
    text_clf.fit(D['test']['x'], D['test']['y'])
    predicted = text_clf.predict(D['test']['x'])

    # Начало тестирования программы
    z = input("Введите вопрос без знака вопроса на конце: ")
    
    zz = [z]
    predicted = text_clf.predict(zz)
    print(predicted[0])

if __name__ == '__main__':
    openai()
