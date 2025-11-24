#!/usr/bin/env bash
set -euo pipefail

# Скрипт для локальной проверки запуска проекта через Ren'Py.
# Использование:
#   RENPY_HOME=/path/to/renpy ./scripts/run-local.sh [command]
# Где [command] — одно из: lint (по умолчанию), launch, both.

PROJECT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)
RENPY_HOME="${RENPY_HOME:-}"
COMMAND="${1:-lint}"

if [[ -z "$RENPY_HOME" ]]; then
  echo "[Ошибка] Укажите путь к каталогу Ren'Py через переменную RENPY_HOME." >&2
  exit 1
fi

RENPY_BIN="$RENPY_HOME/renpy.sh"
if [[ ! -x "$RENPY_BIN" ]]; then
  echo "[Ошибка] Не найден исполняемый файл renpy.sh по пути: $RENPY_BIN" >&2
  exit 1
fi

run_lint() {
  echo "[Инфо] Запуск lint для проекта в $PROJECT_DIR" >&2
  "$RENPY_BIN" "$PROJECT_DIR" lint
}

run_launch() {
  echo "[Инфо] Запуск игры (launch) для проекта в $PROJECT_DIR" >&2
  "$RENPY_BIN" "$PROJECT_DIR" launch
}

case "$COMMAND" in
  lint)
    run_lint
    ;;
  launch)
    run_launch
    ;;
  both)
    run_lint
    run_launch
    ;;
  *)
    echo "[Ошибка] Неизвестная команда: $COMMAND (доступно: lint, launch, both)" >&2
    exit 1
    ;;
esac
