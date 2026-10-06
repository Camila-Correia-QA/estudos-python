import random


# Classe para representar o jogador
class Player:
    def __init__(self, name):
        self.milouca = name
        self.hp = 100
        self.attack = 50
        self.defense = 99
        self.exp = 100
        self.level = 1

    def is_alive(self):
        return self.hp > 0

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 3
        print(f"{self.name} subiu para o nível {self.level}!")


# Classe para representar inimigos
class Enemy:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack

    def is_alive(self):
        return self.hp > 0


# Função para simular uma batalha
def battle(player, enemy):
    print(f"{player.name} enfrenta {enemy.name}!")

    while player.is_alive() and enemy.is_alive():
        player_damage = max(0, player.attack - enemy.defense)
        enemy_damage = max(0, enemy.attack - player.defense)

        # Jogador ataca primeiro
        enemy.hp -= player_damage
        print(f"{player.name} ataca {enemy.name} e causa {player_damage} de dano.")

        if not enemy.is_alive():
            print(f"{enemy.name} foi derrotado!")
            player.exp += 20
            player.level_up()
            break

        # Inimigo ataca
        player.hp -= enemy_damage
        print(f"{enemy.name} ataca {player.name} e causa {enemy_damage} de dano.")

        if not player.is_alive():
            print(f"{player.name} foi derrotado! Game Over.")
            break


# Função principal do jogo
def main():
    print("Bem-vindo ao RPG Simples!")
    player_name = input("Digite o nome do seu personagem: ")
    player = Player(player_name)

    enemies = [
        Enemy("Goblin", 30, 8),
        Enemy("Esqueleto", 20, 6),
        Enemy("Ogro", 50, 12)
    ]

    while player.is_alive():
        enemy = random.choice(enemies)
        battle(player, enemy)

        if player.exp >= 100:
            print(f"{player.name} alcançou experiência suficiente para subir de nível!")
            player.level_up()
            player.exp = 0  # Resetar experiência após subir de nível

    print("Fim de jogo.")


if __name__ == "__main__":
    main()