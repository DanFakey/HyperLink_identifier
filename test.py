import re
import spacy



def Parsing(text, flag):
    nlp = spacy.load("en_core_web_sm")

    email_pattern = re.compile(r'\b[a-zA-Zа-яА-Я0-9_.+-]+@[a-zA-Zа-яА-Я0-9-]+\.[a-zA-Zа-яА-Я]{2,}\b')
    url_pattern = re.compile(r'\b((https?://)?([^\s]+?\.[^\s]+))\b')
    telegram_pattern = re.compile(r'\B@[a-zA-Z0-9_]{5,}\b')
    
    doc = nlp(text)

    if flag == 1:
        emails_spacy = [token.text for token in doc if token.like_email]
        emails_regex = email_pattern.findall(text)
        emails = list(set(emails_spacy + emails_regex))
        print("Emails:", emails)
    elif flag == 2:
        # urls_spacy = [token.text for token in doc if token.like_url]
        urls_regex = url_pattern.findall(text)
        with open("TLD_LIST.txt", "r") as file:
            valid_tlds = file.read().lower()

        urls_filtered = [url[0] for url in urls_regex if url[0].split('.')[-1] in valid_tlds]
        urls = list(set(urls_filtered))
        print("URLs:", urls)
    elif flag == 3:
        telegram_accounts = telegram_pattern.findall(text)
        telegram_accounts = list(set(telegram_accounts))
        print("Telegram Accounts:", telegram_accounts)

        