class hud():
    def __init__(self, health, money, population):
        self.health = health
        self.money = money
        self.population = population

    def hospital():
        self.health += 100
        self.population += 200
        self.money -= 1000
        printHud(self.health, self.population, self.money)

    
    def printHud(h, p, m):
        writeText(f'Health: {h}%   Population: {p}   Money:  ${m} ', get_font2(30), GOLD, _VARS['surf'], 1000, 50) 