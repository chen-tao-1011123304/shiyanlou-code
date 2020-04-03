class Game(object):
    """这是一个游戏类"""

    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @classmethod
    def show_top_score(cls):
        print('游戏最高分{0}'.format(cls.top_score))

    @staticmethod
    def show_help():
        print('僵尸走进房间')

    def start_game(self):
        print('{0}开始游戏'.format(self.player_name))

        Game.top_score = 999


Game.show_help()

Game.show_top_score()

game = Game('小明')
game.start_game()


Game.show_top_score()





