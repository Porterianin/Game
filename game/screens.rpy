# Экранные элементы: HUD, карта и достижения.

init python:
    if "hud" not in config.overlay_screens:
        config.overlay_screens.append("hud")

screen hud():
    frame:
        style_prefix "hud"
        align (0.02, 0.02)
        has vbox
        text "Локация: [current_location]" size 18
        text "Энергия: [player_state['энергия']]" size 16
        text "Возбуждение: [player_state['возбужденность']]" size 16
        text "Сытость: [player_state['сытость']]" size 16
        text "Чистота: [player_state['чистота']]" size 16
        text "Репутация: [player_state['репутация']]" size 16
        text "Деньги: [player_state['деньги']] ₽" size 16

screen location_overlay(current_location):
    tag menu
    modal False
    frame:
        align (0.5, 0.85)
        xsize 800
        has hbox
        spacing 10

        textbutton "Карта города" action Return("map")
        textbutton "Отдохнуть" action Return("rest")
        textbutton "Достижения" action Return("achievements")
        textbutton "Статус" action Return("profile")
        textbutton "Выход" action Return("exit")

    frame:
        align (0.02, 0.2)
        xsize 300
        has vbox
        text "Связи" size 18
        for person, value in relationships.items():
            text "[person]: [value]" size 16

screen character_sheet():
    tag menu
    modal True
    add Solid("#2228")
    frame:
        align (0.5, 0.5)
        xsize 760
        ysize 520
        has vbox
        spacing 8
        text "Профиль Насти" size 26 xalign 0.5
        text player_profile["описание"] size 16
        null height 6
        hbox:
            spacing 20
            vbox:
                text "Характеристики" size 20
                for key, value in player_attributes.items():
                    text "[key.capitalize()]: [value]" size 16
                null height 8
                text "Состояния" size 20
                for key, value in player_state.items():
                    text "[key.capitalize()]: [value]" size 16
            vbox:
                text "Одежда" size 20
                text "[player_profile['текущее_одежда']['название']]" size 16
                text player_profile['текущее_одежда']['описание'] size 14
                if player_profile['текущее_одежда']['эффекты']:
                    text "Эффекты:" size 14
                    for key, value in player_profile['текущее_одежда']['эффекты'].items():
                        text "• [key.capitalize()]: [value]" size 14
                null height 8
                text "Инвентарь" size 20
                if player_profile['инвентарь']:
                    for item in player_profile['инвентарь']:
                        text "- [item['название']]: [item['эффект']]" size 14
                else:
                    text "Рюкзак пуст." size 14
        null height 6
        hbox:
            spacing 20
            vbox:
                text "Прическа" size 20
                text player_profile['прическа'] size 14
            vbox:
                text "Описание тела" size 20
                for key, value in player_profile['тело'].items():
                    text "[key.capitalize()]: [value]" size 14
        textbutton "Закрыть" action Return(None) xalign 0.5

screen city_map(current_location):
    tag menu
    modal True
    add Solid("#1118")
    frame:
        align (0.5, 0.5)
        xsize 600
        ysize 400
        has vbox
        spacing 10
        text "Карта города" size 24 xalign 0.5
        text "Текущая локация: [current_location]" xalign 0.5
        null height 10
        grid 2 2 spacing 10:
            textbutton "Квартира" action Return("home")
            textbutton "Университет" action Return("university")
            textbutton "Аптека" action Return("pharmacy")
            textbutton "Парк" action Return("park")
        null height 10
        textbutton "Закрыть" action Return(None) xalign 0.5

screen achievements_overlay():
    tag menu
    modal True
    add Solid("#2228")
    frame:
        align (0.5, 0.5)
        xsize 700
        ysize 450
        has vbox
        spacing 8
        text "Достижения" size 26 xalign 0.5
        viewport:
            draggable True
            mousewheel True
            xsize 660
            ymaximum 300
            vbox:
                spacing 6
                for key, data in achievements_state.items():
                    frame:
                        has hbox
                        spacing 10
                        text ("✓" if data["unlocked"] else "○") size 20
                        vbox:
                            text data["name"] size 20
                            text data["desc"] size 16
        textbutton "Закрыть" action Return(None) xalign 0.5

style hud_frame:
    background Solid("#ffffffcc")
    padding (8, 8, 8, 8)

style hud_text:
    color "#2a1b28"
