import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

try:
    escolha = input("Escolha: pedra, papel ou tesoura: ")

    resultado = proxy.jogar(escolha)
    escolha_computador, resultado_jogo = resultado

    print(resultado_jogo)
    print("Computador escolheu", escolha_computador)
    print("Você escolheu", escolha)

except ValueError as e:
    print("Erro:", e)
except Exception as e:
    print("Erro", e)