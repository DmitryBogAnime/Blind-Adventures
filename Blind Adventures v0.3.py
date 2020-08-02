import random, sys, os

monstr_spis = [['Скелет', 'Хрустит костями'], ['Зомби', 'Жутко воняет'], ['Гоблин', 'Хочет твои деньги'], ['Гигантский паук', 'Сколько у него глаз!?'], ['Скорпион', 'Ядовитое жало'], ['Жук носорог', 'Жук с рогом'], ['Оживший шаман', 'У него есть 2 посоха'], ['Маленький демон', 'Маленький и устрашающий'], ['Леприкон', 'Ворует ваши чувства'], ['Мутировавший червь', 'Фууу....'], ['Водный элементаль', 'Очень мокрый'], ['Земляной элементаль', 'Оживашая грязь'], ['Огненный элементаль', 'Горячий как раскаленная лава'], ['Ветряной элементаль', 'Бушует как торнадо'], ['Гремлин', 'Не обливайте водой!'], ['Вампир', 'Высосет из тебя все соки'], ['Марадёр', 'Ограбит вас в любой момент'], ['Огромный крот', 'Слепой как и вы'], ['Огромная личинка', 'Массивная и упитаная'], ['Устрашающая тень', 'Ваще вооброжение в темноте не имеет придела'], ['Главарь марадёров', 'Упровляет марадёрами'], ['Жирная крыса', 'Если укусит то будет плохо'], ['Странный огонёк', 'Огонёк но не воняет гарью'], ['Злая фея', 'Винкс приняли ислам?'], ['Кентавр', 'Полу-человек, полу-лошадь'], ['К0д0вый1м0нстр1', 'Состоит из цыфр и букв'], ['Жадный гризли', 'Не хочет отдовать мёд'], ['Чумной доктор', 'Может заклювать'], ['Детёнышь огненного дракона', 'Рыгает огнем'], ['Детёнышь ледяного дракона', 'Рыгает льдом'], ['Старый волшебник', 'Может колдовать'], ['Электрический угорь', 'Бьётся током'], ['Оборотень', 'Волк или ауф?'], ['Пират', 'Ну что матросы'], ['Капитан пиратов', 'Свистать всех на вверх!']]
spis_food = ['Странный гриб', 'Светящийся фрукт', 'Маленький гриб', 'Воняющий овощ', 'Твёрдый фрукт', 'Огромный фрукт', 'Холодная сосулька', 'Тухлое мясо', 'Сырое мясо', 'Желеобразный напиток', 'Странная смесь', 'Клюкву', 'Кокос', 'Тыкву', 'Виноград', 'Дыню', 'Арбуз', 'Манго', 'Грей фрукт', 'Мандарин', 'Картофель', 'Заваренный дошик', 'Незаваренный дошик', 'Яблоко', 'Перец', 'Редиска', 'Щавель', 'Интересный цветок', 'Киви', 'Апельсин', 'Помидор', 'Огурец', 'Петрушка', 'Укроп', 'Нектарин', 'Персик', 'Сливу', 'Ежевику', 'Малину', 'Клубнику', 'Миндаль', 'Брокколи', 'Капусту', 'Фасоль', 'Горох', 'Морковь', 'Кукурузу', 'Берёзовый сок', 'Жёлудь', 'Грецкий орех', 'Арахис', 'Воду', 'Холодный кофе', 'Холодный зелёный чай', 'Холодный красный чай', 'Холодный черный чай', 'Холодное какао', 'Энергетик', 'Банка колы', 'Банка фанты', 'Банка спрайта', 'Твёрдое печенье', 'Сушенный фрукт', 'Конфету', 'Халву']
class Player:
    typs = 'player'
    def __init__(self, stats):
        #self.sost = sost #Дружелюбно, Нейтрально, Агресивно
        name,lvl, max_hp, hp ,dmg, exp = stats
        self.name = name
        self.lvl = int(lvl)
        self.hp = int(hp)
        self.dmg = int(dmg)
        self.exp = float(exp)
        self.max_hp = int(max_hp)
    def expUP(self, ex):
        print(f'Вы получили {ex} опыта')
        self.exp += ex
        while self.exp >= 1000 * 0.5 * self.lvl:
            self.exp -=1000 * 0.5 * self.lvl
            self.dmg += 1.5
            self.max_hp += 1
            self.hp = self.max_hp
            self.lvl+=1
            print(f'Вы повысили уровень, теперь он равен: {self.lvl}')
    def healUP(self, heal):
        if heal > 0:
            print(f'Вы отхилились на {heal}')
        elif heal < 0:
            print(f'Вы получили {abs(heal)} урона')
        else:
            print('Ничего не произошло')
        if (self.hp+heal) >= self.max_hp:
            self.hp = self.max_hp
        else:
            self.hp+=heal
            if self.hp<1:
                death('ваш обед')
class Monster:
    typs = 'monster'
    def __init__(self, name,lvl, hp, dmg, exp):
        self.name = name
        self.lvl = lvl
        self.hp = hp
        self.dmg = dmg
        self.exp = exp
########Меню################
def menu():
    print('1)Информация')
    print('2)Сделать ход')
    print('3)Сохранить')
    print('4)')
    action = input()
    if action == '1':
        info(igrok)
    elif action == '2':
        sobit()
    elif action == '3':
        save_game(igrok)
    elif action == '4':
        pass
    else:
        pass
    print('--'*27)
def sobit():
    r = random.randint(1,10)
    if r in [3,4,5,6,7,8]:
        monster_battle()
    elif r in [1,2]:
        found_food()
    else:

        print('Вы ничего не нашли и никого не встретили')
        pass
def battle_menu(m):
    while True:
        print(f'На против вас "{m.name[0]}"')
        print(f'1)Информация о "{m.name[0]}"')
        print(f'2)Информация о "{igrok.name}"')
        print('3)Сражаться')
        print('4)Убежать')
        action = input()
        if action == '1':
            info(m)
        elif action == '2':
            info(igrok)
        elif action == '3':
            hit_monster(m)
            if m.hp > 0:
                hit_player(m)
            else:
                print(f'{m.name[0]} мёртв')
                igrok.expUP(m.exp)
                break
        elif action == '4':
            if random.randint(1,100) > 75:
                print("Вы убежали")
                break
            else:
                print("Вы не смогли скрыться")
                hit_player(m)
                pass
        else:
            pass
        print('--'*27)
########Меню################
def hit_monster(m):
    m.hp-= igrok.dmg
def hit_player(m):
    igrok.hp-= m.dmg
    if igrok.hp <=0:
        death(m)
def death(m):
    try:
        print(f'Вас убил {m.name[0]}')
    except:
        print(f'Вас убил {m}')
    file.close()
    os.remove(os.path.join(os.path.abspath(os.path.dirname(__file__)), 'data.txt'))
    input()
    sys.exit()
def food_eat():
    r = random.randint(1,10)
    if r in [1, 2]:
        a = random.randint(50, 300)
        igrok.expUP(a)
    elif r in [3, 4, 5]:
        igrok.healUP(random.randint(1, 4))

    elif r in [6, 7, 8]:
        igrok.healUP(random.randint(-3, -1))
    else:
        print('Ничего не произошло')
####СОБЫТИЯ###########
def monster_battle():
    lvl = random.randint(1, 6)
    mons = Monster(random.choice(monstr_spis), lvl, lvl+random.randint(0, 3), int(lvl/2)+random.randint(1, 3), random.randint(50, 100)*lvl)
    battle_menu(mons)
def found_food():
    f = random.choice(spis_food)
    while True:
        print(f'Вы нашли {f}')
        print('Что вы хотите с ним сделать?')
        print(f'1)Употребить {f}')
        print(f'2)Выкинуть {f}')
    #    print('3)Забрать')
        choice_p = input()
        if choice_p == '1':
            print(f'Вы употребили {f}')
            food_eat()
            break
        elif choice_p == '2':
            print(f'Вы выкинули {f}')
            break
        else:
            pass
####СОБЫТИЯ###########
def save_game(obj):
    file = open('data.txt', 'w')
    file.write(obj.name+'\n'+str(obj.lvl)+'\n'+str(obj.max_hp)+'\n'+str(obj.hp)+'\n'+str(obj.dmg)+'\n'+str(obj.exp))
    file.close()
def info(obj):
    print('----------Информация----------')
    print(f'Имя: {obj.name[0]}')
    print(f'Уровень: {obj.lvl}')
    if obj.typs == 'player':
        print(f'Жизней: {obj.hp}/{obj.max_hp}')
    else:
        print(f'Жизней: {obj.hp}')
    print(f'Урон: {obj.dmg}')
    if obj.typs == 'player':
        print(f'Опыт: {int(obj.exp)}/{int(1000 * 0.5 * obj.lvl)}')
    else:
        print(f'Опыта за убийство: {int(obj.exp)}')
    if obj.typs == 'monster':
        print(f'{obj.name[1]}')
try:
    file = open('data.txt', 'r')
    t = file.read()
    igrok = Player(str(t).split('\n'))
except FileNotFoundError:
    print('Введите имя игрока:')
    nm = input()
    igrok = Player([nm, 1,10 ,10,2,0])
    file = open('data.txt', 'w')
    save_game(igrok)
print('--'*27)
while True:
    menu()
input()
