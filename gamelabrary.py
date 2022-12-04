from game import Game, games_list, games_id, games_name


class Library(Game):
    def __init__(self,id,games_list):
        self.userid=id
        self.games_list=games_list

    def listgames(self):
        for i in self.games_list:
            print(i)

userid=1 #根据用户id获取其对应的库
user_library=Library(userid,games_list)
print("***************************************")
print("您的游戏库:(请输入游戏id进行游玩或其他操作)")
user_library.listgames()
print("***************************************")
print(games_id)

option_game=eval(input())

if option_game in games_id:
    print("***************************************")
    print(games_name[option_game])
    print("1.本地游玩")
    print("2.远程畅玩")
    print("3.游戏社区")
    print("***************************************")
    option_model=input()
    if option_model==1:
        print("开始游玩"+games_name[option_game])
        print("读取游戏文件中。。。")
    #elif option_model==2:



