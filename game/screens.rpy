# -*- coding: utf-8 -*-
# Минимальные экраны проекта без зависимости от сгенерированных GUI-стилей.

# Главное меню с базовым оформлением.
screen main_menu():
    tag menu

    add Solid("#0d1321")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 18

        text config.name size 48 color "#ffd166" outlines [(1, "#000000", 0, 0)]
        text "Версия [config.version]" size 22 color "#e6e6e6"
        text "Городская песочница о студентке мединститута" size 24 color "#ffffff"

        textbutton "Начать игру":
            action Start()
            text_size 32
            text_color "#ffffff"
            text_hover_color "#ffd166"

        textbutton "Загрузить":
            action ShowMenu("load")
            text_size 28
            text_color "#ffffff"
            text_hover_color "#ffd166"

        textbutton "Настройки":
            action ShowMenu("preferences")
            text_size 28
            text_color "#ffffff"
            text_hover_color "#ffd166"

        textbutton "Выход":
            action Quit(confirm=True)
            text_size 28
            text_color "#ffffff"
            text_hover_color "#ffd166"

# Панель характеристик и локации для режима песочницы.
screen hud():
    layer "overlay"

    frame:
        background Solid("#1b2433cc")
        xalign 0.02
        yalign 0.02
        padding (16, 12)
        has vbox

        text "Локация: [current_location]" size 22 color "#ffd166"
        text "Деньги: [katya_money] ₽" size 20 color "#e6e6e6"

        hbox:
            spacing 10
            for key, value in katya_stats.items():
                frame:
                    background Solid("#101827")
                    padding (8, 6)
                    vbox:
                        text key size 18 color "#c0d6ff"
                        text str(value) size 18 color "#ffffff"

        if relations:
            text "Отношения:" size 18 color "#ffd166" top_padding 6
            for name, score in relations.items():
                text "[name]: [score]" size 18 color "#ffffff"

# Экран с диалогом персонажей.
screen say(who, what):
    use hud

    window:
        background Solid("#0d1321c0")
        xfill True
        yminimum 180

        vbox:
            spacing 10
            if who:
                text who id "who" size 32 color "#ffd166" outlines [(1, "#000000", 0, 0)]
            text what id "what" size 30 color "#ffffff" outlines [(1, "#000000", 0, 0)]
