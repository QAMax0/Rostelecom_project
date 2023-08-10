# project_Rostelecom:
    Реализация page object-а

# Что проверяют тесты? 
1) Валидность полей регистрации, сообщений 
валидации при неверном вводе данных в поля регистрации. 
2) Авторизацию с валидными данными по требованиям.
3) Наличие слогана ЛК "Ростелеком ID"
4) Кликабельность ссылок на странице авторизации.



# Настройка проекта:
    1. Создаем виртуапльное окружение командой:
        python -m venv venv
    2. Активируем виртуальное окружение командой (MacOS/Linux):
        source venv/bin/activate
       для Windows другая команда:
        \env\Scripts\activate.bat
    3. Установка зависимостей:
        pip install -r requirements.txt
    4. Настроить в IDE(Pycharm) текущий интерпритатор, выбрав текущее вертуальное окружение

# Запуск тестов:
    Нажмите на зеленую стрелочку слева от названия теста, если она вдруг не появилась, 
    значит вы не установили библиотеку pytest. Установите командой: pip install pytest.
