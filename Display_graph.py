from Quiz import Quiz
from Gra_dele import Gra_dele

y = Quiz()
z = Gra_dele()

#グラフを表示するプログラム
class Display_graph:
    def graph_disply(self):
        while True:
            try:
                y.graph_quiz()#グラフの選択肢の表示
                if y.graph_select == 1:
                    y.show_tango_graph() #単語グラフ表示

                elif y.graph_select == 2:
                    y.show_tanbun_graph() #短文グラフ表示

                elif y.graph_select == 3:
                    y.show_mix_graph() #ランダムグラフ表示

                elif y.graph_select == 4:
                    z.gra_dele_quiz() #グラフ削除

                elif y.graph_select == 5:
                    break

                else:
                    print('=====================\n１～５で入力してください\n=====================')
            except ValueError:
                print('=====================\n番号を入れてください\n=====================')