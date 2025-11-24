## Общие настройки игры «Приключения в большом городе».
init -1 python:
    config.name = "Приключения в большом городе"
    config.version = "0.1.0"
    config.window_title = config.name
    # Отключаем подтверждение выхода, чтобы избежать вызова отсутствующего layout.yesno_prompt
    # в nightly-сборках Ren'Py 8.5.x.
    config.quit_action = Quit(confirm=False)

# Цветовая схема по умолчанию достаточно спокойная, подчеркивающая повседневный характер игры.
define gui.accent_color = "#e6a8d7"
