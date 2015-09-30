init -50 python:   
    class Char: ### Шаблон для статов персонажей
        def __init__(self,fname,name,age,hp,hpmax,mp,mpmax,sp,spmax,str,will,agil,spd,endr,willp,int):
            self.fname = fname # Фамилия
            self.name = name   # Имя
            self.age = age      # Возраст
            self.hp = hp        # Хит поинты
            self.hpmax = hpmax    # Максимальное кол-во хитпоинтов
            self.mp = mp         #  Мана
            self.mpmax = mpmax    # Максимум маны
            self.sp = sp          # Очки выносливости
            self.spmax = spmax     # Максимум их же
            self.str = str         # Сила
            self.will = will       # Воля
            self.agil = agil       # Ловкость
            self.spd = spd         # Скорость
            self.endr = endr       # Выносливость
            self.willp = willp      # Сила воли
            self.int = int          # Интеллект
            
label init_start:         ###СЮДА ВВОДИМ ПЕРЕМЕННЫЕ
    # Статы нашего героя
    python:
        hero = Char("Харитонов", "Игорь", 42, 100, 100, 100, 100, 100, 100, 10, 10, 10, 10, 10, 10, 10)
        
    # Наличка
    $ money = 50000
    
    # Счет в банке
    $ archem_bank = 3545295
    
    # Переменная, отражающая, что герой находится в реальном мире    
    $ real_world = "True"
    
    # Задаем время
    $ day = 1
    $ month = 3
    $ year = 2010
    $ hour = 10
    $ minute = 0     
                
return