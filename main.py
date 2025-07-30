from Question import Question
from Quiz import Quiz
from Name import Name
from Display_graph import Display_graph

quest = Question()
quiz = Quiz()
dis = Display_graph()

print('<<タイピング練習>>')
yourname = input('名前を入れてください>>')
print(Name(yourname)) #名前入力
while True:
    try:
        quiz.quiz() #選択肢の表示
        if quiz.select == 1:
            print('単語練習')
            input('開始するにはEnterを押してください')
            quest.question_tango() #単語の出題

        elif quiz.select == 2:
            print('短文練習')
            input('開始するにはEnterを押してください')
            quest.question_short_sentence() #短文の出題

        elif quiz.select == 3:
            print('ランダム練習')
            input('開始するにはEnterを押してください')
            quest.question_mix() #ランダムの出題

        elif quiz.select == 4: #グラフ表示
            dis.graph_disply()

        elif quiz.select == 5:
            print('プログラムを終了します。')
            break

        else:
            print('=====================\n１～５で入力してください\n=====================')

    except ValueError:
        print('=====================\n番号を入れてください\n=====================')