
label scene_eight:
    scene погоня with dissolve
    play music "audio/Сцена 8/Прискорене серцебиття.mp3" fadeout 1
    "{i}Ноги самі несуть мене геть"

    "{i}Кудись подалі від того клятого автомату"

    "{i}Подалі від цього страшного голосу"

    play music "audio/Сцена 7/Тривога.mp3" fadeout 1

    гучномовець "ТРИВОГА! ТРИВОГА! РОЗХОДЬТЕСЯ ПО СВОЇХ ДОМІВКАХ І ЧЕКАЙТЕ НА ПЕРЕВІРЯЮЧИХ. ЗАБОРОНЕНО ЗАЛИШАТИ ОАЗУ, ДОКИ ДИВЕРСАНТА НЕ БУДЕ ЗНАЙДЕНО"

    "{i}Але від нього неможливо втекти. Він лунає з кожного кута, з кожної стіни"

    "{i}Час зупинитись і подумати. Доки я не накоїла дурниць"

    menu:
        "Зупинитись":
            "{i}Фух. Час видохнути і зібратись з думками"

    play music "audio/Сцена 7/ТемаПередВтечею.mp3" fadeout 3

    "{i}Копи, напвено, вже дістались до того трансконнектору"

    if відносини_інкі < 2:
        "{i}Інкі, напевно, вже навела їх на мій слід"

        "{i}Значить, часу в мене небагато"

    if відносини_інкі >= 2:
        "{i}Сподіваюсь, Інкі зможе їх затримати. Це дасть мені трохи часу"

        "{i}Дякую тобі, подруго. Сподіваюсь, з тобою все буде гаразд"

    "{i}Що ж мені робити?"

    menu:
        "Лайя!":
            "{i}Точно, Лайя!"

    "{i}Це він втягнув мене у все це! 'Просто збираємо інформацію' - а як же! От негідник!"

    "{i}Але він згадував якісь адреси... Треба пригадати…"

    "{i}Згадала! Він казав про вулицю Чисту, будинок 2, і чоловіка в капелюсі…"

    "{i}А ще про південно-східну браму, біля якої я повинна буду його зустріти"

    "{i}До брами далеко. Але якщо транспортери ще літають, я зможу застрибнути на один з них і доїхати прямо до неї"

    "{i}Вилиця Чиста всього в двох кварталах звідси. Але щось мені підказує, що прямувати пішки буде небезпечніше"

    "{i}Куди мені слід вирушити?"

    menu:
        "Бігти на вулицю":
            $вулиця = True
            "{i}Хто знає, що може статися зі мною у транспортері?"
            "{i}Пішки в мене більше шансів втекти. До того ж це зовсім недалеко"
        "Прямувати до брами":

            $брама = True
            "{i}Лайя повинен зараз бути біля брами. Значить, слід вирушати туди"
            "{i}До того ж, це ближче до вихіду з міста"


    if відносини_інкі < 2:
        play sound "audio/Сцена 8/Звук Робота.mp3"
        перевіряючий "Охопити періметр. Обшукатий кожен будинок. Злочинець не міг втекти далеко"
        "{i}Дідько! Копи вже майже тут"
        stop sound fadeout 3


        $ time = 5
        $ timer_range = 5
        $ timer_jump = 'proval'

        show screen countdown
        menu:
            "Бігти не озираючись":
                hide screen countdown
                $ непомітність = непомітність - 1
                $ швидкість = швидкість + 2
                "{i}Не підведіть мене ніженьки!"
                "{i}Нехай спробують наздогнати!"


    if відносини_інкі >= 2:
        "{i}Тривога не стихає, але копів ще не чути. В мене є трохи часу для роздумів. Як саме мені краще пересуватись містом?"

        play sound "audio/Сцена 8/Звук Таймера.mp3"

        menu:
            "Бігти не озираючись ":
                stop sound fadeout 3
                $ непомітність = непомітність - 1
                $ швидкість = швидкість + 2
                "{i}Не підведіть мене ніженьки!"
                "{i}Нехай спробують наздогнати!"
            "Залишатися в тіні":
                stop sound fadeout 3
                $ непомітність = непомітність + 2
                $ швидкість = швидкість - 1
                "{i}Я знаю це місто як свої п'ять пальців"
                "{i}Тут неподалік є завулок, через нього можна прослизнути непоміченою"
            "Спробувати змішатись з натовпом":
                stop sound fadeout 3
                $ непомітність = непомітність + 1
                $ швидкість = швидкість + 1
                "{i}Якщо пристану до от тої групки вживачів, то зможу вислизнути з вулиці непоміченою"
                "{i}Вони настількі обдовбані, що навіть не розуміють, що відбувається"

    play sound "audio/Сцена 8/Звук Робота.mp3"
    перевіряючий "Охопити періметр. Обшукатий кожен будинок. Злочинець не міг втекти далеко"
    "Як же вчасно я пішла з вулиці!"
    stop sound fadeout 4

    "{i}Позаду чутно неприємне металеве трискотіння Перевіряючих"
    play sound "audio/Сцена 8/Звук Важкої Металевої Брами.mp3"
    "{i}Буквально за моєю спиною зачиняється велика металева брама"
    "{i}Вулицю перекрито, всі, хто на ній залишилися, будуть ретельно перевірені і проскановані"
    "{i}Я не раз бачила таке. Коли ми викликали копів, щоб затримати вандалів"
    "{i}Але я ніколи ще не ВТІКАЛА від копів!"
    stop sound fadeout 3
    if вулиця == True:
        jump street
    if брама == True:
        jump brama

label street:
    "{i}Чиста вулиця наліво від мене. Три хвилини бігом"
    "{i}Я вже бачу верхній край того клятого бігборду, про який казав Лайя"
    "{i}Він стоїть прямо на мурі, що відділяє Оазу від решти міста"
    "{i}До нього можна спробувати піднятись крутими вуличними сходами, що піднімаються проміж будинків"
    "{i}Або ж видертися на дах комплексу апартаментів. В ньому напевно є ліфт, хоча пересування ним може привернути багато зайвої уваги"
    play music "audio/Сцена 8/Звук Тривога.mp3"
    гучномовець "ТРИВОГА! ТРИВОГА!"

    "{i}Клятий гучномовець продовжує голосити"
    "{i}Дуже скоро цю вулицю теж перекриють. Нема часу на зволікання"
    play sound "audio/Сцена 8/Звук Таймера.mp3"

    menu:
        "Бігти навпростець":
            stop sound fadeout 3
            $ непомітність = непомітність + 1
            $ швидкість = швидкість - 1
            play sound "audio/Сцена 8/Звук Важкої Металевої Брами.mp3"
            "{i}Клац! Ледь встигла. Брама зачинилась прямо за мною"
            "{i}Далі - по сходах наверх, на мур, що відділяє Оазу від периферії"
            "{i}Після підйому в мене ледь вистачає дихання. Це місто явно проектували не для піших прогулянок"
        "Пройти крізь комплекс":
            stop sound fadeout 3
            $ непомітність = непомітність - 1
            $ швидкість = швидкість + 1

            "{i}Дах комплексу стоїть впритул до мура"
            "{i}Зсередини комплекс виглядає як розшурханий мурашник"
            "{i}Мешканці зі здивуванням і острахом зиркають на мене зі своїх осель. Хтось з них, напевно, вже доповідає копам…"
            "{i}Ну що ж, проте хоча б скористаюсь ліфтом!"

        "Кінець гри при таймері":
            play sound "audio/Сцена 8/Звук Важкої Металевої Брами.mp3"

            "{i}Клац! Брама прямо переді мною зачиняється. Через секунду Перевіряючи вийдуть із своїх капсул"
            "{i}Схоже, вибору в мене тепер немає - доведеться йти крізь комплекс"

            play sound "audio/Сцена 8/Звук Таймера.mp3"

            menu:
                "Пройти крізь комплекс":
                    stop sound fadeout 3
                    $ непомітність = непомітність - 1
                    $ швидкість = швидкість + 1

                    "{i}Дах комплексу стоїть впритул до мура"
                    "{i}Зсередини комплекс виглядає як розшурханий мурашник"
                    "{i}Мешканці зі здивуванням і острахом зиркають на мене зі своїх осель. Хтось з них, напевно, вже доповідає копам…"
                    "{i}Ну що ж, проте хоча б скористаюся ліфтом!"
                "ПРОВАЛ":
                    play sound "audio/Сцена 8/Звук Робота.mp3"
                    перевіряючий "Підозрювана локалізована. Ініціюю процедуру захоплення"
                    stop sound fadeout 1
                    "{i}Ну от і все. На цьому моя історія закінчується..."
                    jump scene_eight

    scene погоня_2 with dissolve

    "{i}Нарешті, я на Чистій вулиці"
    "{i}Найдовша вулиця під Куполом. Вона обгинає всю Оазу одним великим кільцем"
    "{i}Одне велике, нескінченне кільце. На внутрішній стороні - сотні будинків, що туляться один на одного, наче якісь органічні нарости"
    "{i}Зовні - обрив, що відділяє Оазу від периферії. А тих, хто має все - від тих, хто не має нічого"
    "{i}Але зараз не час для екскурсій"
    "{i}Ось він - біг борд, під яким на мене повинен чекати чоловік в капелюсі"
    "{i}Але…"

    if непомітність >=3 :
        "{i}Жодної людини в капелюсі. Ні чоловіків, ні жінок"
        "{i}Лайя, щоб тобі!"
        "{i}Ніякого чоловіка в капелюсі ніколи не було. Ніхто не чекав на мене, щоб передати перепустку з цього проклятого міста"
        "{i}Мене підставили, використали як пішака, і кинули на призволяще"
        "{i}А я, наївна дурепа, повірила в казки про життя поза Куполом…"

        play music "audio/Сцена 8/Звук Тривога.mp3"

        гучномовець "УВАГА! ВСІ ГРОМАДЯНИ, ЩО ПЕРЕБУВАЮТЬ НА ВУЛИЦІ ПІД ЧАС ЗАГАЛЬНОЇ ТРИВОГИ ПІДЛЯГАЮТЬ НЕГАЙНІЙ ПЕРЕВІРЦІ! НЕ НАМАГАЙТЕСЯ ЧИНИТИ ОПІР!"
        "{i}Вже ніхто не прийде мене рятувати…"
        "{i}Ось і все, Павко, час прощатися настав"
        stop music fadeout 1
        play sound "audio/Сцена 8/Далекий Вибух.mp3"

        "{i}Що це в дідька ще таке?"
        "..."
        "{i}Гучномовець обривається на півслові"
        play sound "audio/Сцена 8/Близький Вибух.mp3"
        "{i}За першим вибухом чутно ще один, ближче і гучніше"
        stop sound fadeout 2
        "{i}За першим вибухом чутно ще один, ближче і гучніше"
        menu:
            "Бігти в укриття":
                "Чорт його знає, де тут безпечне укриття"
                "Машинально забігаю в комплекс апартаментів. Принаймні, тут мене не зачепить уламками"
                jump scene_eight_end
    if непомітність < 3 :
        "{i}На мене вже чекають"
        "{i}Але це не чоловік в капелюсі"

        play sound "audio/Сцена 8/Звук Робота.mp3"

        перевіряючий "Громадянко! Залишайтесь на місці. Ви підозрюєтесь у державній зраді"

        stop sound fadeout 3
        "{i}Клятий робот вже висадилився на дах і наближається до мене"
        "{i}Здається, я була недостатньо обережною. Але що робити тепер?"

        play sound "audio/Сцена 8/Звук Таймера.mp3"

        menu:
            "Тікати назад":
                павка "А як же, не дочекаєшся!"
                "{i}Я прослизаю вниз по сходах до того, як ця бляшанка схопить мене по руках і ногах своїми металевими щупальцями"
                play sound "audio/Сцена 8/Далекий Вибух.mp3"
                "..."
                "{i}Що це в дідька таке?"
                play sound "audio/Сцена 8/Близький Вибух.mp3"
                "{i}За першим вибухом чутно ще один, ближче і гучніше"
                stop sound fadeout 2
                "{i}За першим вибухом чутно ще один, ближче і гучніше"
                "{i}Сподіваюсь, стіни будинку захистять мене від уламків"

            "Стояти на місці":
                "{i}Ще нікому не вдавалося втекти від Перевіряючого. Ці машини були створені спеціально для того, щоб ефективно ловити втікачів"
                "{i}Але це не означає, що мої справи безнадійні. Треба тільки правильно підібрати момент"
                "{i}Робот наближається впритул до мене. Ще секунда - і він зв'яже мої кінцівки своїми щупальцями"


                play sound "audio/Сцена 8/Звук Таймера.mp3"
                menu:
                    "Застосувати електрошокер":
                        play sound "audio/Сцена 8/Звук Електрошокера.mp3"
                        павка "Ось тобі, потворо!"
                        stop sound fadeout 3
                        "{i}Це був останній заряд електрошокеру, але який постріл!"

                        "{i}Робот з декілька разів дригається від потужного заряду, потім з металевим скавучанням падає на землю"
                        "{i}Можливо я і не врятуюсь сьогодні, але до чого ж приємно було вмазати цьому опудалу!"

                        play sound "audio/Сцена 8/Далекий Вибух.mp3"
                        "..."
                        "{i}Що це в дідька таке?"
                        play sound "audio/Сцена 8/Близький Вибух.mp3"
                        "{i}За першим вибухом чутно ще один, ближче і гучніше"
                        stop sound fadeout 2
                        menu:
                            "Бігти в укриття":
                                "{i}Чорт його знає, де тут безпечне укриття"
                                "{i}Машинально забігаю в комплекс апартаментів. Принаймні, тут мене не зачепить уламками"
                                jump scene_eight_end
                    "ПРОВАЛ":
                        "{i}Доки я зволікаю, металева тварюка перелітає на декілька метрів ближче. Тепер годі і думати про втечу"
                        play sound "audio/Сцена 8/Звук робота.mp3"
                        перевіряючий "Підозрювану захоплено. Вводжу заспокійливе і починаю процедуру перевірки"
                        stop sound fadeout 1
                        "{i}Ну от і все. На цьому моя історія закінчується…"
                        jump scene_eight

label proval:
    #	*роботичний металевий скрегіт*
    перевіряючий "Підозрювана локалізована. Ініціюю процедуру захоплення"
    "Ну от і все. На цьому моя історія закінчується…"
    #	[КІНЕЦЬ. ПРОГРАШ]
label brama:
    scene фон

label scene_eight_end:
        stop music fadeout 3
        невідомий "Не рухайся"
        play sound "audio/Сцена 8/Звук Боротьби Придушений Зойк.mp3"
        stop music fadeout 3
        "..."
        "{i}Чиїсь сильні руки міцно охоплюють мене і підіймають над землею"
        "{i}Я намагаюсь кричати, але за секунду горло слабне, а очі застилає темрява"
        "{i}Прощавай, світ"
        stop sound
        "..."
        jump scene_nine
        #"ДЯКУЮ ЗА ГРУ В ДЕМО)) ЦЕ ПОКИ 7.5 СЦЕНА З 13+ ПИШІТЬ СВОЇ ЗАУВАЖЕННЯ ТА ПРОПОЗИЦІЇ!!"