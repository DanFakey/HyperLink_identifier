from telegram.ext import Updater, MessageHandler, filters
import re
import requests

# Функция для обработки текста, распознавания интернет-идентификаторов и преобразования их в гиперссылки


def is_valid_domain(domain):
    try:
        response = requests.head(f"http://{domain}")
        return response.status_code == 200
    except requests.exceptions.RequestException:
        return False


def process_text(text):
    # Регулярное выражение для поиска URL
    url_pattern = r'\bhttps?://(?:www\.)?[\w\.-]+\.\w+\b'
    # Находим все совпадения URL
    urls = re.findall(url_pattern, text)
    # Заменяем найденные URL на гиперссылки
    for url in urls:
        text = text.replace(url, f'<a href="{url}">{url}</a>')

    # Регулярное выражение для поиска адресов электронной почты
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b'
    # Находим все совпадения адресов электронной почты
    emails = re.findall(email_pattern, text)
    # Заменяем найденные адреса электронной почты на гиперссылки
    for email in emails:
        text = text.replace(email, f'<a href="mailto:{email}">{email}</a>')

    # Регулярное выражение для поиска доменных имен
    domain_pattern = r'\b(?:[A-Za-z0-9-]+\.)+[A-Za-z]{2,}\b'
    # Находим все совпадения доменных имен
    domains = re.findall(domain_pattern, text)
    # Проверяем каждое доменное имя и преобразуем его в гиперссылку, если домен существует
    for domain in domains:
        # Проверяем, является ли домен существующим
        if is_valid_domain(domain):
            text = text.replace(domain, f'<a href="http://{domain}">{domain}</a>')

    return text





# Функция, которая будет вызываться при получении сообщения
def echo(update, context):
    # Получаем текст сообщения
    message_text = update.message.text
    # Обрабатываем текст и преобразуем интернет-идентификаторы в гиперссылки
    processed_text = process_text(message_text)
    # Отправляем обработанный текст обратно пользователю
    update.message.reply_text(processed_text, parse_mode='HTML')




# Точка входа в программу
def main():
    # Токен вашего бота
    token = '7164511724:AAFnspZPP0JmXaC7RVWgPBN7ibxzVnlSerU'
    # Создаем обновлятор, который будет получать обновления от Telegram
    updater = Updater(token, use_context=True)
    # Получаем диспетчер для регистрации обработчиков
    dispatcher = updater.dispatcher
    # Регистрируем обработчик для текстовых сообщений
    text_handler = MessageHandler(filters.text & ~filters.command, echo)
    dispatcher.add_handler(text_handler)
    # Запускаем бота
    updater.start_polling()
    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()


# Запускаем главную функцию
if __name__ == '__main__':
    main()
