# OOP for fun ٩(◕‿◕)۶ #

Сборник небольших игр, разработанных с помощью ООП. <br>
Периодически пополняю, если приходит вдохновение (｡◕‿◕｡)


## Стек ##
+ Python 3.10.10
+ ООП
+ Git

## Список содержимого ##
1. камень, ножницы, бумага
2. создаем таски
3. умножай в уме (доводится до ума)
4. конфигурационный менеджер
5. эмулятор корзины онлайн-магазина с оплатой и чеком

## Описание функционала некоторых файлов ##
4. конфигурационный менеджер: <br>
Простой конфигурационный менеджер для приложения. <br>
Класс AppConfig предоставляет метод для загрузки конфигурации из JSON-файла и получает значения конкретных параметров.<br>
В классе AppConfig реализовано следующее: 
- метод load_config, который загружает конфигурацию из указанного JSON-файла,
- метод get_config, который принимает ключ и возвращает соответствующее значение из загруженной конфигурации. Если ключ не найден, метод возвращает None. <br>
Файл 'app_config.json' находится в корне директории.
Реализована возможность вызова перечисленных методов как через класс, так и через экземпляр.

## Для пользования репозиторием локально ##
Скачайте проект с SSH:
```python
git clone git@github.com:Mary8jk/OOP-for-fun.git
```

Enjoy!
