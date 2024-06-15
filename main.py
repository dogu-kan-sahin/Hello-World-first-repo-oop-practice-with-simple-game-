from  projectfirst  import Character

hero= Character(health=100,type="human",defence=70,power=50,item="shard")
enemy=Character(health=100,type="ork",defence=70,power=50,item="shard")


while hero.health > 0 and enemy.health > 0:
    hero.attack(enemy)
    if enemy.health > 0:  
        enemy.attack(hero)
    print(f"Hero's remaining health: {hero.health}")
    print(f"Enemy's remaining health: {enemy.health}")
