
class Character:
  def __init__(self, name, hp):
    self.name = name
    self.hp = hp
    
  def get_hp(self):
    return self.hp
    
  def yell(self):
    print("AHHHHHHHH")
    
tom = Character("tom", 10)

tom.yell()


