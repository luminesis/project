[app]

# Название твоего приложения
title = Dorm Chef

# Имя пакета
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

# Указываем Buildozer брать готовый SDK прямо с сервера GitHub (это отменяет скачивание и ошибку с aidl)
android.sdk_path = /usr/local/lib/android/sdk
android.ndk_path = /usr/local/lib/android/sdk/ndk/25b
android.api = 31
android.min_api = 21

[buildozer]
log_level = 2
warn_on_root = 1
