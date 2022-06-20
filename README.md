# ruGPT3-bot - телеграмм бот для генерации текста, основанный на  модели ruGPT3 от сбера

### Бот позволяет:

Продолжать тексты на русском и частично на английском языках. Для этого необходимо сформулировать «затравку» - фразу, которую модель допишет.

### Команды бота

1. ``` /help, /info ``` - показывает иформацию об используемых командах
2. ```/activate``` -  включает генерацию текста  
3. ```/deactivate ``` - отключает генерацию текста

Модули программы:
* _main_ - Главный модуль программы. Стартовая точка запуска бота
* _telebot_ - Модуль, в котором происходит создание бота и  обработчики команд
* _rugpt3_ - Модуль c основной функцией генерации текста
* _log_ - Модуль логиррования