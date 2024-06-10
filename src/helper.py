import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import csv
import re
import spacy

def process_input(input_text):
    result = openai(input_text)

    result_label = result_label.config(text=f"Результат: {result}")

def openai(text) -> str:
    data = load_data_from_csv('train_set.csv')
    D = train_test_split(data)
    
    text_clf = Pipeline([
        ('tfidf', TfidfVectorizer()),
        ('clf', SGDClassifier(loss='hinge')),
    ])
    text_clf.fit(D['test']['x'], D['test']['y'])
    predicted = text_clf.predict(D['test']['x'])
    
    
    zz = [text]
    predicted = text_clf.predict(zz)
    result = ""

    if predicted == "Почта":
        print("here 1")
        result = Parsing(text, 1)
    elif predicted == "Ссылка":
        print("here 2")
        result = Parsing(text, 2)
    elif predicted == "Телеграм":
        print("here 3")
        result = Parsing(text, 3)
            
    return result 

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
    
def Parsing(text, flag) -> str:
    nlp = spacy.load("en_core_web_sm")

    email_pattern = re.compile(r'\b[a-zA-Zа-яА-Я0-9_.+-]+@[a-zA-Zа-яА-Я0-9-]+\.[a-zA-Zа-яА-Я]{2,}\b')
    url_pattern = re.compile(r'\b((https?://)?([^\s]+?\.[^\s]+))\b')
    telegram_pattern = re.compile(r'\B@[a-zA-Z0-9_]{5,}\b')
    
    doc = nlp(text)

    if flag == 1:
        emails_spacy = [token.text for token in doc if token.like_email]
        emails_regex = email_pattern.findall(text)
        emails = list(set(emails_spacy + emails_regex))
        return emails
    elif flag == 2:
        # urls_spacy = [token.text for token in doc if token.like_url]
        urls_regex = url_pattern.findall(text)
        with open("TLD_LIST.txt", "r") as file:
            valid_tlds = file.read().lower()

        urls_filtered = [url[0] for url in urls_regex if url[0].split('.')[-1] in valid_tlds]
        urls = list(set(urls_filtered))
        return urls
    elif flag == 3:
        telegram_accounts = telegram_pattern.findall(text)
        print(telegram_accounts)
        telegram_accounts = list(set(telegram_accounts))
        print(telegram_accounts)
        return telegram_accounts
        