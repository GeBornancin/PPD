import multiprocessing
import requests

def verificar_pagina_wiki_existente(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return f'{url} - Existe'
        elif response.status_code == 404:
            return f'{url} - Não existe'
        else:
            return f'{url} - Desconhecido'
    except requests.RequestException as error:
        return f'{url} - Erro: {error}'

def worker_function(url, result_queue):
    result = verificar_pagina_wiki_existente(url)
    result_queue.put(result)

def main():
    print("Executando em paralelo:")

    wiki_page_urls = [f'https://en.wikipedia.org/wiki/{i + 1}' for i in range(50)]
    start_time = time.time()

    result_queue = multiprocessing.Queue()
    processes = []

    for url in wiki_page_urls:
        process = multiprocessing.Process(target=worker_function, args=(url, result_queue))
        processes.append(process)
        process.start()

    for process in processes:
        process.join()

    results = []
    while not result_queue.empty():
        result = result_queue.get()
        results.append(result)

    for result in results:
        print(result)

    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f'Tempo em paralelo: {elapsed_time:.2f} segundos')

if __name__ == "__main__":
    import time
    main()