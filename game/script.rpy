# Основная логика игры и сцены начальных локаций.

# Определяем героиню и базовые переменные.
define n = Character("Настя", color="#c26aa5")

# Характеристики и описания героя.
default player_attributes = {
    "интеллект": 4,
    "ловкость": 3,
    "удача": 5,
    "красота": 7,
    "развращенность": 0,
}

default player_state = {
    "энергия": 70,
    "возбужденность": 10,
    "сытость": 60,
    "чистота": 70,
    "репутация": 10,
    "деньги": 1500,
}

default relationships = {
    "Соседка": 0,
    "Куратор": 0,
    "Провизор из аптеки": 0,
}

default player_profile = {
    "описание": "Молодая блондинка из небольшой деревни, приехавшая поступать в медицинский институт.",
    "прическа": "Длинные светлые волосы, собранные в легкий хвост.",
    "текущее_одежда": {
        "название": "Белое платье с сердечками",
        "описание": "Легкое белое платье с мелким розовым узором, тонкими бретельками и подолом чуть ниже бедра.",
        "эффекты": {"красота": 2, "легкость": 1}
    },
    "инвентарь": [
        {"название": "Красный чемодан", "эффект": "Всё необходимое для жизни в городе"},
        {"название": "Студенческий блокнот", "эффект": "+1 к репутации среди студентов"},
        {"название": "Бюджетный смартфон", "эффект": "Позволяет получать новости и задания"},
    ],
    "тело": {
        "телосложение": "Худощавое, подтянутое.",
        "рост": "170 см",
        "кожа": "Светлая, хорошо ухоженная.",
        "грудь": "Небольшая, аккуратная форма.",
    },
}

default achievements_state = {
    "arrival": {"unlocked": False, "name": "Добро пожаловать!", "desc": "Настя добралась до съемной квартиры."},
    "first_steps": {"unlocked": False, "name": "Первые шаги", "desc": "Посетите любое место в городе впервые."},
}

default current_location = "Квартира"

init python:
    def unlock_achievement(key):
        data = achievements_state.get(key)
        if data and not data["unlocked"]:
            data["unlocked"] = True
            renpy.notify("Достижение получено: {}".format(data["name"]))

label start:
    call prologue

    $ current_location = "Квартира"
    scene expression Solid("#f2e9de")
    with fade

    n "Ну вот я и в большом городе. Съемная квартира пока что выглядит непривычно, но это мой новый дом."
    n "Пора осмотреться и сделать первые шаги к мечте — поступить в медицинский институт."

    $ unlock_achievement("arrival")

    jump home

label home:
    $ current_location = "Квартира"
    scene expression Solid("#f2e9de")
    with fade
    show text "Съемная квартира" at truecenter

    n "Здесь тихо и спокойно. Нужно набраться сил и решить, куда отправиться." 

    call location_loop

label university:
    $ current_location = "Университет"
    scene expression Solid("#dfe7f2")
    with fade
    show text "Главный корпус университета" at truecenter

    n "Коридоры полны абитуриентов. Я должна узнать расписание и подготовиться." 

    $ relationships["Куратор"] += 1
    $ player_state["репутация"] += 1

    call location_loop

label pharmacy:
    $ current_location = "Аптека"
    scene expression Solid("#f2f5df")
    with fade
    show text "Уютная городская аптека" at truecenter

    n "Здесь можно подработать или купить что-то полезное для учебы." 

    $ relationships["Провизор из аптеки"] += 1
    $ player_state["деньги"] -= 50

    call location_loop

label park:
    $ current_location = "Парк"
    scene expression Solid("#e0f2df")
    with fade
    show text "Городской парк" at truecenter

    n "Свежий воздух помогает собраться с мыслями. Может, стоит прогуляться и познакомиться с кем-то?" 

    $ player_state["энергия"] = min(100, player_state["энергия"] + 5)

    call location_loop

label location_loop:
    # Общий цикл выбора действия в текущей локации.
    while True:
        call screen location_overlay(current_location=current_location)
        $ action = _return

        if action == "map":
            call screen city_map(current_location=current_location)
            $ destination = _return
            if destination == "home":
                jump home
            elif destination == "university":
                $ unlock_achievement("first_steps")
                jump university
            elif destination == "pharmacy":
                $ unlock_achievement("first_steps")
                jump pharmacy
            elif destination == "park":
                $ unlock_achievement("first_steps")
                jump park
        elif action == "rest":
            $ player_state["энергия"] = min(100, player_state["энергия"] + 10)
            n "Немного отдыха восстановили силы."
        elif action == "achievements":
            call screen achievements_overlay
        elif action == "profile":
            call screen character_sheet
        elif action == "exit":
            n "Пора сделать перерыв."
            return
        # Возврат в цикл для повторного выбора.


label prologue:
    $ current_location = "Деревня"
    scene expression Solid("#dbe4d0")
    with fade

    n "Настя стояла у поворота на трассу, где старенький автобус вот-вот должен был появиться за горизонтом."
    n "За спиной осталась родная деревня: лес, шум реки и деревянный дом на окраине. Впереди — новый, взрослый, немного страшный мир."

    scene expression Solid("#f3ede7")
    with dissolve
    n "На Насте было легкое белое платье с мелким розовым узором в сердечки, тонкие бретельки и подол чуть ниже бедра."
    n "На ногах — старенькие белые босоножки. В руке — красный чемодан, в котором всё её имущество: одежда, телефон, документы, блокнотик."

    scene expression Solid("#efeae1")
    with dissolve
    n "Девочка из тихой деревни, Настя всегда была примерной. Детсад, школа — отличница."
    n "Отец ушел, когда ей было три. Мама — строгая, но любящая — воспитывала одну. В доме у леса всегда пахло пирогами и мятой."
    n "Но Насте этого стало мало. Она мечтала — вырваться, сбежать, стать взрослой."

    scene expression Solid("#f7f1e8")
    with dissolve
    n "Автобус остановился с глухим шипением. Ветер с дороги резко вздул платье Насте вверх — высоко, почти до талии."
    n "Белые трусики мелькнули перед глазами водителя и двух пассажиров, стоявших у двери."
    n "Настя в ужасе вцепилась в подол, покраснела и юркнула в салон."

    scene expression Solid("#e7edf4")
    with dissolve
    n "Она устроилась у окна, уткнулась в стекло и глубоко вздохнула. Щёки горели, сердце колотилось."
    n "Первый день — и уже позор. А впереди — целая новая жизнь. И кто знает, сколько ещё таких ситуаций её ждёт..."

    return

