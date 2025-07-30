from Count import Count

#csvに書き込むプログラム
class Draw:
    def question_tango(self):
        for i in range(self.total_questions):
            question = self.mix.tango()
            print(f'問題: {question}')
            youserinput = input('入力してください: ')
            self.count.count_score(question, youserinput) #正答率のカウント
        score = self.count.total_score(self.total_questions)
        self.count.save_score_tango_csv(score) #CSVに正答率を記録

    def question_short_sentence(self):
        for i in range(self.total_questions):
            question = self.mix.short_sentence()
            print(f'問題: {question}')
            youserinput = input('入力してください: ')
            self.count.count_score(question, youserinput) #正答率のカウント
        score = self.count.total_score(self.total_questions)
        self.count.save_score_tanbun_csv(score) #CSVに正答率を記録

    def question_mix(self):
        for i in range(self.total_questions):
            question = self.mix.mix()
            print(f'問題: {question}')
            youserinput = input('入力してください: ')
            self.count.count_score(question, youserinput) #正答率のカウント
        score = self.count.total_score(self.total_questions)
        self.count.save_score_mix_csv(score)  # CSVに正答率を記録