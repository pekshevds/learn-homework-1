"""

Домашнее задание №1

Условный оператор: Сравнение строк

* Написать функцию, которая принимает на вход две строки
* Проверить, является ли то, что передано функции, строками. 
  Если нет - вернуть 0
* Если строки одинаковые, вернуть 1
* Если строки разные и первая длиннее, вернуть 2
* Если строки разные и вторая строка 'learn', возвращает 3
* Вызвать функцию несколько раз, передавая ей разные праметры 
  и выводя на экран результаты

"""

def determine(str1, str2):
  
  """
  Функция определяет результат сравнения двух строк по различным критериям
  """

  if not (isinstance(str1, str) and isinstance(str2, str)):
    return 0
  
  if str1 == str2:
    return 1
  
  if len(str2) > len(str1):
    return 2

  if str2 == 'learn':
    return 3

def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    print(determine('my happy string', 1))
    print(determine(1.2, 'my happy string'))
    print(determine([], 1))
    print(determine('my happy string', 'my happy string'))
    print(determine('learn', 'my happy string'))
    print(determine('some string', 'learn'))
    
    
if __name__ == "__main__":
    main()
