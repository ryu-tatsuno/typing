import csv
import matplotlib.pyplot as plt
import numpy as np
import os

class Quiz:
    #モード選択
    def quiz(self):
        print('モードを選んでください\n1.単語　2.短文　3.ランダム　4.折れ線グラフ表示　5.終了')
        self.select = int(input('>> '))

    #グラフ表示の選択
    def graph_quiz(self):
        print('正答率の折れ線グラフを表示します。')
        print('表示したいグラフを選んでください\n1.単語グラフ　2.短文グラフ　3.ランダムグラフ　4.グラフの削除　5.グラフ終了')
        self.graph_select = int(input('>> '))

    #削除するグラフの選択


    #CSVからデータを読み込んで折れ線グラフを表示
    def show_tango_graph(self):
        scores = []
        try:
            with open('seitouritsu_tango.csv', mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    scores.append(float(row[0]))
        except FileNotFoundError:
            print('ファイルがありません')

        #グラフ描画
        if scores:
            plt.xlim(0,10) #グラフ10回分表示
            plt.xticks(np.arange(0, 11, step=1)) #目盛りを1刻み
            plt.ylim(0,10) #点数10回分表示
            plt.yticks(np.arange(0, 11, step=1)) #目盛りを1刻み
            plt.plot(range(1, len(scores) + 1), scores, marker='o', linestyle='-', color='b')
            plt.title('Hit')
            plt.xlabel('Number of practices')
            plt.ylabel('Score')
            plt.grid(True)
            plt.show()
        else:
            print("正答率のデータがありません。")

    #CSVからデータを読み込んで折れ線グラフを表示
    def show_tanbun_graph(self):
        scores = []
        try:
            with open('seitouritsu_tanbun.csv', mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    scores.append(float(row[0]))
        except FileNotFoundError:
            print('ファイルがありません')

        #グラフ描画
        if scores:
            plt.xlim(0,10) #グラフ10回分表示
            plt.xticks(np.arange(0, 11, step=1))#目盛りを1刻み
            plt.ylim(0,10) #点数10回分表示
            plt.yticks(np.arange(0, 11, step=1)) #目盛りを1刻み
            plt.plot(range(1, len(scores) + 1), scores, marker='o', linestyle='-', color='b')
            plt.title('正答率の推移')
            plt.xlabel('練習回数')
            plt.ylabel('点数')
            plt.grid(True)
            plt.show()
        else:
            print("正答率のデータがありません。")

    #CSVからデータを読み込んで折れ線グラフを表示
    def show_mix_graph(self):
        scores = []
        try:
            with open('seitouritsu_mix.csv', mode='r', encoding='utf-8') as file:
                reader = csv.reader(file)
                for row in reader:
                    scores.append(float(row[0]))
        except FileNotFoundError:
            print('ファイルがありません')

        #グラフ描画
        if scores:
            plt.xlim(0,10)#グラフ10回分表示
            plt.xticks(np.arange(0, 11, step=1)) #目盛りを1刻み
            plt.ylim(0,10) #点数10回分表示
            plt.yticks(np.arange(1, 11, step=1)) #目盛りを1刻み
            plt.plot(range(1, len(scores) + 1), scores, marker='o', linestyle='-', color='b')
            plt.title('正答率の推移')
            plt.xlabel('練習回数')
            plt.ylabel('点数')
            plt.grid(True)
            plt.show()
        else:
            print("正答率のデータがありません。")




    #ファイルが存在するか確認してから削除
    def delete_csv(self,file_path):
        if os.path.exists(file_path):
            os.remove(file_path)
            print(f"{file_path} を削除しました")
        else:
            print(f"{file_path} が見つかりません")