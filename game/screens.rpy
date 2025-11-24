# -*- coding: utf-8 -*-
# Минимальные экраны проекта без зависимости от сгенерированных GUI-стилей.

# Главное меню с базовым оформлением.
screen main_menu():
    tag menu

    add Solid("#0f0f1a")

    vbox:
        xalign 0.5
        yalign 0.5
        spacing 18

        text config.name size 48 color "#ffffff" outlines [(1, "#000000", 0, 0)]

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

# Экран с диалогом персонажей.
screen say(who, what):
    window:

        vbox:
            spacing 10
            if who:
                text who id "who" size 32 color "#ffd166" outlines [(1, "#000000", 0, 0)]
            text what id "what" size 30 color "#ffffff" outlines [(1, "#000000", 0, 0)]
