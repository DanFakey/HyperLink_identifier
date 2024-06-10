import requests
import idna

def load_allowed_domains(url):
    response = requests.get(url)
    if response.status_code == 200:
        return response.text.splitlines()
    else:
        raise Exception("Не удалось загрузить список доменов")

def is_domain_allowed(domain, allowed_domains):
    try:
        punycode_domain = idna.encode(domain).decode('ascii')
    except idna.IDNAError:
        return False
    return punycode_domain in allowed_domains

def main():
    allowed_domains_url = 'https://data.iana.org/TLD/tlds-alpha-by-domain.txt'
    allowed_domains = load_allowed_domains(allowed_domains_url)
    user_domain = input("Введите домен: ").strip()
   
    if is_domain_allowed(user_domain, allowed_domains):
        print("Домен разрешен")
    else:
        print("Домен не разрешен")

if __name__ == "__main__":
    main()