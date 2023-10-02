import requests

def get_wiki_page_existence(wiki_page_url):
    try:
        response = requests.get(wiki_page_url)
        page_status = 'unknown'

        if response.status_code == 200:
            page_status = "Existe"
        elif response.status_code == 404:
            page_status = "Não existe"

        return f'{wiki_page_url} - {page_status}'

    except requests.RequestException as error:
        return f'{wiki_page_url} - error: {error}'

def main():
    print("Executando de forma sequencial:")

    def gerar_wiki_url(i):
        return f'https://en.wikipedia.org/wiki/{i + 1}'

    wiki_page_urls = [gerar_wiki_url(i) for i in range(50)]

    start_time = time.time()

    for url in wiki_page_urls:
        print(get_wiki_page_existence(url))

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f'Tempo sequencial: {elapsed_time:.2f} segundos')

if __name__ == "__main__":
    import time
    main()