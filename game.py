


class Game:
  def __init__(self,gameid, gamename):
    self.gameid = gameid
    self.gamename = gamename

  def list(self):
    #print(str(self.gameid)+ ". "+self.gamename)
    return str(str(self.gameid)+ ". "+self.gamename)


game1=Game(1,"csgo")
game2=Game(2,"witch it!")
game3=Game(3,"cod19")

games_id=[game1.gameid,game2.gameid,game3.gameid]

games_name=[game1.gamename,game2.gamename,game3.gamename]

games_list=[game1.list(),game2.list()]

games_list.append(game3.list())

