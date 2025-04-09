
import random

# Lista de cartas com atributos
cartas = [
    {"nome": "Dragão", "força": 10, "velocidade": 7, "inteligência": 6},
    {"nome": "Fênix", "força": 6, "velocidade": 9, "inteligência": 8},
    {"nome": "Unicórnio", "força": 5, "velocidade": 6, "inteligência": 10},
    {"nome": "Grifo", "força": 8, "velocidade": 8, "inteligência": 7},
    {"nome": "Minotauro", "força": 9, "velocidade": 5, "inteligência": 4},
    {"nome": "Cérbero", "força": 8, "velocidade": 6, "inteligência": 5}
]

# Função para escolher carta aleatória
def escolher_carta():
    return random.choice(cartas)

# Função para comparar as cartas com base no atributo escolhido
def comparar_cartas(carta1, carta2, atributo):
    if carta1[atributo] > carta2[atributo]:
        return "Você venceu!"
    elif carta1[atributo] < carta2[atributo]:
        return "Você perdeu!"
    else:
        return "Empate!"

# Início do jogo
print("=== Super Trunfo ===")
carta_jogador = escolher_carta()
carta_pc = escolher_carta()

# Garante que as cartas não sejam iguais
while carta_pc == carta_jogador:
    carta_pc = escolher_carta()

print("\nSua carta:")
for atributo, valor in carta_jogador.items():
    print(f"{atributo.capitalize()}: {valor}")

atributo = input("\nEscolha um atributo para competir (força, velocidade, inteligência): ").lower()

print("\nCarta do computador:")
for atributo_pc, valor_pc in carta_pc.items():
    print(f"{atributo_pc.capitalize()}: {valor_pc}")

resultado = comparar_cartas(carta_jogador, carta_pc, atributo)
print("\nResultado:", resultado)
