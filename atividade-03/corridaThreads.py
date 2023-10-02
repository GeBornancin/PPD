import threading
import random
import time

def gerar_numero_aleatorio():
    return random.randint(1, 5)

def esperar(segundos):
    time.sleep(segundos)

def realizar_corrida(id_da_thread):
    posicao_atual = 0
    total_passos = 0

    print(f'Thread {id_da_thread} - Iniciando')

    while posicao_atual < 50:
        passos = gerar_numero_aleatorio()
        total_passos += passos
        posicao_atual += passos

        print(f'Vez da Thread {id_da_thread}')
        print(f'Número sorteado: {passos}')
        print(f'Thread {id_da_thread} andou {passos} casas')
        print(f'Posição atual da Thread {id_da_thread}: {posicao_atual}')

        esperar(1)

    print(f'Thread {id_da_thread} - chegou à posição 50! total de passos: {total_passos}')

    return total_passos

def iniciar_corrida():
    num_threads = 2
    threads = []
    resultados = []

    def thread_corrida(id_thread):
        resultado = realizar_corrida(id_thread)
        resultados.append(resultado)

    for i in range(1, num_threads + 1):
        thread = threading.Thread(target=thread_corrida, args=(i,))
        threads.append(thread)
        thread.start()

    for thread in threads:
        thread.join()

    indice_vencedor = resultados.index(min(resultados))
    id_da_thread_vencedora = indice_vencedor + 1
    print(f'A Thread {id_da_thread_vencedora} venceu com {resultados[indice_vencedor]} passos!')

if __name__ == "__main__":
    iniciar_corrida()