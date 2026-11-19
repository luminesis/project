[app]

# Название твоего приложения
title = Dorm Chef

# Имя пакета (латиницей, без пробелов)
package.name = dormchef

# Твой домен
package.domain = org.dorm

# Путь к исходному коду (точка означает текущую папку, где лежит main.py)
source.dir = .

# Какие файлы включать в проект
source.include_exts = py,png,jpg,kv,atlas

# Главный файл программы
source.main_file = main.py

# Версия
version = 0.1

# Список зависимостей
requirements = python3,kivy

# Целевая платформа Android
orientation = portrait
fullscreen = 0
android.permissions = INTERNET

[buildozer]
log_level = 2
warn_on_root = 1
