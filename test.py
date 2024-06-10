import spacy
from email_validator import validate_email, EmailNotValidError
import idna
import unicodedata


def normalize_domain(domain):
    normalized_domain = unicodedata.normalize('NFC', domain)
    try:
        ascii_domain = idna.encode(normalized_domain).decode('ascii')
    except idna.IDNAError:
        ascii_domain = None
    return ascii_domain


def Parsing(text, flag) -> str:
    nlp = spacy.load("en_core_web_sm")
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
        urls_spacy = [token.text for token in doc if token.like_url]

        with open("TLD_LIST.txt", "r") as file:
            valid_tlds = file.read().lower().split()

        valid_urls = []
        for url in urls_spacy:
            domain = url.split('.')[-1].lower()
            if domain in valid_tlds:
                try:
                    normalized_url = normalize_domain(url)
                    if normalized_url:
                        valid_urls.append(normalized_url)
                except idna.IDNAError:
                    continue
        urls = list(set(valid_urls))
        return urls

    elif flag == 3:
        telegram_accounts = [token.text for token in doc if token.text.startswith('@') and len(token.text) > 5]
        telegram_accounts = list(set(telegram_accounts))
        return telegram_accounts
