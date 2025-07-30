import csv

class Count:
    def __init__(self):
        self.seikou = 0  # 合格数の初期化

    def count_score(self, question, youserinput):
        if question == youserinput: #合否の判定
            print('合格')
            self.seikou += 1 #合格数をプラス１
        else:
            print('失敗')

    def total_score(self, total_questions):
        score = self.seikou / total_questions
        print(f'正答率は {self.seikou}/{total_questions}です')
        self.seikou = 0
        return score

        # 単語正答率をCSVに保存
    def save_score_tango_csv(self, score):
        with open('seitouritsu_tango.csv', mode='a', newline='',encoding='utf-8') as file:
            writer = csv.writer (file)
            writer.writerow([score * 10])

        # 短文正答率をCSVに保存
    def save_score_tanbun_csv(self, score):
        with open('seitouritsu_tanbun.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([score *10])

        # ミックス正答率をCSVに保存
    def save_score_mix_csv(self, score):
        with open('seitouritsu_mix.csv', mode='a', newline='', encoding='utf-8') as file:
            writer = csv.writer(file)
            writer.writerow([score * 10])