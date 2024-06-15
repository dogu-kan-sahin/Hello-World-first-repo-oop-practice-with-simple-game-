class Character:

    charactertype={"ork":1.2,"human":1.3}
    itemtype={"raptor":50,"shard":44}

    def __init__(self,health,type,defence,power,item):
        self.health=health
        self.type=type
        self.defence=defence
        self.power=power
        self.item=item
      
           
    def attack(self,target):
        target.health+=target.defence-self.power*self.charactertype[self.type]-self.itemtype[self.item]
        target.health=max(target.health,0)
        return target.health

