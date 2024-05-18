import re

def find_urls(text):
    # Регулярное выражение для поиска URL
    url_pattern = r'\bhttps?://\S+\b'
    # Находим все совпадения
    urls = re.findall(url_pattern, text)
    return urls

def find_emails(text):
    # Регулярное выражение для поиска адресов электронной почты
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    # Находим все совпадения
    emails = re.findall(email_pattern, text)
    return emails

def convert_to_hyperlinks(text, urls, emails):
    # Заменяем найденные URL на гиперссылки
    for url in urls:
        text = text.replace(url, f'<a href="{url}">{url}</a>')
    # Заменяем найденные адреса электронной почты на гиперссылки
    for email in emails:
        text = text.replace(email, f'<a href="mailto:{email}">{email}</a>')
    return text

def process_text(text):
    # Находим URL и адреса электронной почты
    urls = find_urls(text)
    emails = find_emails(text)
    # Преобразуем их в гиперссылки
    processed_text = convert_to_hyperlinks(text, urls, emails)
    return processed_text


