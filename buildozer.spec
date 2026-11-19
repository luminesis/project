[app]

# Название твоего приложения
title = Dorm Chef

# Имя пакета (латиницей, без пробелов)
package.name = dormchef

# Твой домен
package.domain = org.dorm

# Путь к исходному коду
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

# Фиксируем стабильные версии SDK, чтобы избежать ошибок лицензий и сборки
android.api = 31
android.min_api = 21
android.sdk = 31
android.ndk = 25b

[buildozer]
log_level = 2
warn_on_root = 1
