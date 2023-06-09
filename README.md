# Автор
**Иванова Мария, 13 гр.**

# Предмет 
Компьютерная графика. Лабораторная работа 3. Реализация алгоритмов и методов обработки изображений

# Запуск приложения
Чтобы запустить приложение следует скачать и запустить [main.exe](https://github.com/MaryIv76/kg2023-labrabota3-ImageProcessingMethods/blob/main/main.exe)

# Установка приложения
1. Клонировать репозиторий

```
git clone https://github.com/MaryIv76/kg2023-labrabota3-ImageProcessingMethods
```

2. Установить pyinstaller
```
pip install pyinstaller
```

3. Создать exe файл
```
pyinstaller --onefile -w main.py
```

# Необходимые библиотеки
```
pip install numpy
```
```
pip install Pillow
```
```
pip install opencv-python
```

# Описание
Данное приложение является графическим приложением, написанным на Python.

Приложение способно обрабатывать графические изображения с помощью следующих методов:

Нелинейные фильтры, основанные на порядковых статистиках:
* Фильтр минимума
* Фильтр максимума
* Медианный фильтр

Методы глобальной пороговой обработки:
* Метод Отсу
* Метод глобальной пороговой обработки с выбором порога c использованием Triangle method

Метод адаптивной пороговой обработки

В папке [img](https://github.com/MaryIv76/kg2023-labrabota3-ImageProcessingMethods/tree/main/img) можно найти картинки для тестирования методов.
