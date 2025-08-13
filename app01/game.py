from loguru import logger
class Player(object):
     def __init__(self,name,health,defense,attack_value,weapon):
          self.name = name
          self.health = health
          self.defense = defense
          self.attack_value = attack_value
          self.weapon = weapon

     def attack(self,player_other):

          # 对象攻击
          if self.attack_value > player_other.defense:
               attack_rulet=(self.attack_value - player_other.defense)
               player_other.health = player_other.health - attack_rulet
               logger.info(f"玩家【{self.name}】对【{player_other.name}】造成了{attack_rulet}点伤害 ")
     def buy_weapon(self):
         pass






player1 = Player('张无忌',100,70,120,100)
player2 = Player('张三丰',100,100,100,100)


player1.attack(player2)
player2.attack(player1)





