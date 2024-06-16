import requests
import idna
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import SGDClassifier
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score
import csv
import re
import spacy
from email_validator import validate_email, EmailNotValidError
import idna
import unicodedata


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
        print("Это почта")
        result = Parsing(text, 1)
    elif predicted == "Ссылка":
        print("Это ссылка")
        result = Parsing(text, 2)
    elif predicted == "Телеграм":
        print("Это телеграм")
        result = Parsing(text, 3)
    elif predicted == "ВК":
        print("Это ВК")
        
            
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
    telegram_pattern = re.compile(r'\B@[a-zA-Z0-9_]{5,}\b')    
    doc = nlp(text)

    if flag == 1:
        emails_spacy = [token.text for token in doc if token.like_email]

        valid_emails = []
        for email in emails_spacy:
            try:
                v = validate_email(email)
                normalized_domain = normalize_domain(v['domain'])
                if normalized_domain:
                    local_part = v['local']
                    valid_emails.append(f"{local_part}@{normalized_domain}")
            except EmailNotValidError:
                continue
        return valid_emails
    elif flag == 2:
        # urls_spacy = [token.text for token in doc if token.like_url]
        valid_tlds = run_check_domain(text)
        if valid_tlds:
            return text
        else:
            return
    elif flag == 3:
        telegram_accounts = telegram_pattern.findall(text)
        print(telegram_accounts)
        telegram_accounts = list(set(telegram_accounts))
        print(telegram_accounts)
        return telegram_accounts
        

def load_allowed_domains(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.lower().splitlines()
    else:
        raise Exception("Не удалось загрузить список доменов")

def is_domain_allowed(domain, allowed_domains):
    try:
        punycode_domain = idna.encode(domain).decode('ascii')
    except idna.IDNAError:
        return False
    return punycode_domain in allowed_domains

def check_domain(url, user_domain):
    allowed_domains = load_allowed_domains(url)
    return is_domain_allowed(user_domain, allowed_domains)

def run_check_domain(user_domain) -> bool:
    allowed_domains_url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
    return check_domain(allowed_domains_url, user_domain)


def normalize_domain(domain):
    # Normalize domain using NFC
    normalized_domain = unicodedata.normalize('NFC', domain)
    try:
        # Convert to ASCII using IDNA
        ascii_domain = idna.encode(normalized_domain).decode('ascii')
    except idna.IDNAError:
        ascii_domain = None
    return ascii_domain
