image maine_menu = "gui/main_menu[persistent.number].jpg"


define невідомий = Character("???", color = "#ffffff")

define павка = Character("Павка", color = "#80ed99")

define інкі = Character("Інкі", color = "#ffea00")

define лайя = Character("Куратор Лайя", color = "ff0a54")

define робі = Character("Робі", color = "6c757d")

define демон = Character("Демон сумніву", color = "#ffbe0b")

define кімната = Character("Кімната 116", color = "#2196f3")

define гучномовець = Character("Гучномовець", color = "#ff0a54")

define йербі = Character("Йербі", color = "C27664")

define генто = Character("Генто", color = "#C69749")

define батько = Character("Батько", color = "#009EFF")

define мама = Character("Мама", color = "#F8F988")

define суйра = Character("Суйра", color = "#FEA1BF")


define автовідповідач = Character("Автовідповідач", color = "#153462")

define пасажирка = Character("Пасажирка", color = "#F273E6")

define перевіряючий = Character("Перевіряючий", color = "#FAD6A5")


define голос = Character("Голос", color = "6900C6")
define голос1 = Character("Голос 1", color = "fb8500")
define голос2 = Character("Голос 2", color = "f25c54")
define хлопець1 = Character("Хлопець 1", color = "E14D2A")
define хлопець2 = Character("Хлопець 2", color = "7DE5ED")
init:
    transform shaking:
        linear 0.1 xoffset -2 yoffset 2
        linear 0.1 xoffset 3 yoffset -3
        linear 0.1 xoffset 2 yoffset -2
        linear 0.1 xoffset -3 yoffset 3
        linear 0.1 xoffset 0 yoffset 0
        repeat
init:
    $ timer_range = 0
    $ timer_jump = 0
    $ persistent.ending = "Ending 1"

stop music
default відносини_лайя = 0
default відносини_інкі = 0

default непомітність = 0
default швидкість = 0

default покора_лайі = 0

default годіум_інкі = False
default лайка_інкі = False
default шок_інкі = False
default обіцянка_інкі = False

default втеча_годіум = False

default вулиця = False
default брама = False
