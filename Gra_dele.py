from Quiz import Quiz
q = Quiz()

class Gra_dele:
    def gra_dele_quiz(self):
        while True:
            try:
                print('削除するグラフを選んでください')
                print('1.単語グラフ　2.短文グラフ　3.ランダムグラフ　4.グラフ削除終了')
                graph_delete_select = int(input('>> '))
                if graph_delete_select == 1:
                    q.delete_csv('seitouritsu_tango.csv')#単語グラフ削除
                elif graph_delete_select == 2:
                    q.delete_csv('seitouritsu_tanbun.csv')#短文グラフ削除
                elif graph_delete_select == 3:
                    q.delete_csv('seitouritsu_mix.csv')#ランダムグラフ削除
                elif graph_delete_select == 4:#グラフ削除終了
                    break

                else:
                    print('=====================\n１～４で入力してください\n=====================')
            except ValueError:
                print('=====================\n番号を入れてください\n=====================')