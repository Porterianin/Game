# -*- coding: utf-8 -*-
# Минимальный шаблон сценария Ren'Py.

# Определяем персонажей.
define e = Character("Эйлин")

label start:
    # Устанавливаем базовую сцену и приветствие.
    scene black
    e "Добро пожаловать в новый проект Ren'Py!"

    return
