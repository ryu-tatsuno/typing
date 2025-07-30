import random

class Mix:
    def tango(self):  # 単語出題
        with open('tango.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)  # ランダムに選択
            return random_line.strip()

    def short_sentence(self):  # 短文出題
        with open('tanbun.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)  # ランダムに選択
            return random_line.strip()

    def mix(self):  # ランダム出題
        with open('mix.txt', 'r', encoding='utf-8') as file:
            lines = file.readlines()
            random_line = random.choice(lines)  # ランダムに選択
            return random_line.strip()
