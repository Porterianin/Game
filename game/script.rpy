# Основная логика игры и сцены начальных локаций.

# Определяем героиню и базовые переменные.
define n = Character("Настя", color="#c26aa5")

default player_stats = {
    "энергия": 70,
    "репутация": 10,
    "деньги": 1500,
}

default relationships = {
    "Соседка": 0,
    "Куратор": 0,
    "Провизор из аптеки": 0,
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
    $ player_stats["репутация"] += 1

    call location_loop

label pharmacy:
    $ current_location = "Аптека"
    scene expression Solid("#f2f5df")
    with fade
    show text "Уютная городская аптека" at truecenter

    n "Здесь можно подработать или купить что-то полезное для учебы." 

    $ relationships["Провизор из аптеки"] += 1
    $ player_stats["деньги"] -= 50

    call location_loop

label park:
    $ current_location = "Парк"
    scene expression Solid("#e0f2df")
    with fade
    show text "Городской парк" at truecenter

    n "Свежий воздух помогает собраться с мыслями. Может, стоит прогуляться и познакомиться с кем-то?" 

    $ player_stats["энергия"] = min(100, player_stats["энергия"] + 5)

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
            $ player_stats["энергия"] = min(100, player_stats["энергия"] + 10)
            n "Немного отдыха восстановили силы."
        elif action == "achievements":
            call screen achievements_overlay
        elif action == "exit":
            n "Пора сделать перерыв."
            return
        # Возврат в цикл для повторного выбора.

