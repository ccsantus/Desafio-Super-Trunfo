import random

print("Bem-vindo ao jogo Super Trunfo!")

# Lista de cartas
cartas = [
    {
        "nome": "Dragão Vermelho",
        "ataque": 90,
        "defesa": 70,
        "magia": 60
    },
    {
        "nome": "Cavaleiro de Gelo",
        "ataque": 75,
        "defesa": 85,
        "magia": 50
    },
    {
        "nome": "Feiticeira Sombria",
        "ataque": 60,
        "defesa": 40,
        "magia": 95
    }
]

# Sorteia as cartas
carta_jogador = random.choice(cartas)
carta_maquina = random.choice(cartas)

# Garante que as cartas não sejam iguais
while carta_maquina == carta_jogador:
    carta_maquina = random.choice(cartas)

print("\nSua carta:")
for chave, valor in carta_jogador.items():
    print(f"{chave.capitalize()}: {valor}")

# Jogador escolhe um atributo
atributo = input("\nEscolha um atributo (ataque, defesa ou magia): ").lower()

# Verifica se o atributo é válido
if atributo in ["ataque", "defesa", "magia"]:
    valor_jogador = carta_jogador[atributo]
    valor_maquina = carta_maquina[atributo]

    print(f"\nCarta da máquina: {carta_maquina['nome']}")
    print(f"{atributo.capitalize()} da máquina: {valor_maquina}")
    print(f"Seu
