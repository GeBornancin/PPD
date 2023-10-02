import xmlrpc.server
import random

def jogar(escolha_usuario):
    resultado = ""
    escolha_computador = random.choice(['pedra', 'papel', 'tesoura'])

    if escolha_usuario == escolha_computador:
        resultado = "empate"
        return escolha_computador, resultado
    elif (
        (escolha_usuario == 'pedra' and escolha_computador == 'tesoura') or
        (escolha_usuario == 'papel' and escolha_computador == 'pedra') or
        (escolha_usuario == 'tesoura' and escolha_computador == 'papel')
    ):
        resultado = "Você venceu!"
        return escolha_computador, resultado
    else:
        resultado = "Computador venceu!"
        return escolha_computador, resultado

server = xmlrpc.server.SimpleXMLRPCServer(("localhost", 8000))

server.register_function(jogar, "jogar")

print("Servidor RPC rodando na porta 8000")

try:
    server.serve_forever()
finally:
    server.server_close()