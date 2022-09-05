"""

Домашнее задание №1

Цикл for: Продажи товаров

* Дан список словарей с данными по колличеству проданных телефонов
  [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
  ]
* Посчитать и вывести суммарное количество продаж для каждого товара
* Посчитать и вывести среднее количество продаж для каждого товара
* Посчитать и вывести суммарное количество продаж всех товаров
* Посчитать и вывести среднее количество продаж всех товаров
"""

def determine_sum_for_each(product_list):
  """
  Считает суммарное количество продаж для каждого товара
  """
  for item in product_list:
    item['sum'] = sum(item['items_sold'])
    


def determine_avg_for_each(product_list):
  """
  Считает среднее количество продаж для каждого товара
  """
  for item in product_list:
    item['avg'] = int(sum(item['items_sold'])/len(item['items_sold']))
    

def determine_sum_for_all(product_list):
  """
  Считает суммарное количество продаж всех товаров
  """
  accum = 0
  for item in product_list:
    accum += sum(item['items_sold'])

  return accum


def determine_avg_for_all(product_list):
  """
  Считает среднее количество продаж всех товаров
  """
  accum = 0; counter = 0
  for item in product_list:
    accum += sum(item['items_sold'])
    counter += len(item['items_sold'])

  return int(accum/counter)


def main():
    """
    Эта функция вызывается автоматически при запуске скрипта в консоли
    В ней надо заменить pass на ваш код
    """
    product_list = [
    {'product': 'iPhone 12', 'items_sold': [363, 500, 224, 358, 480, 476, 470, 216, 270, 388, 312, 186]}, 
    {'product': 'Xiaomi Mi11', 'items_sold': [317, 267, 290, 431, 211, 354, 276, 526, 141, 453, 510, 316]},
    {'product': 'Samsung Galaxy 21', 'items_sold': [343, 390, 238, 437, 214, 494, 441, 518, 212, 288, 272, 247]},
    ]

    print('\nПосчитать и вывести суммарное количество продаж для каждого товара')
    determine_sum_for_each(product_list)

    for item in product_list:
      print(f"Продукт {item['product']}, сумма продаж = {item['sum']}")
        
    
    print('\nПосчитать и вывести среднее количество продаж для каждого товара')
    determine_avg_for_each(product_list)
    
    for item in product_list:
      print(f"Продукт {item['product']}, среднее количество продаж = {item['avg']}")
    

    print('\nПосчитать и вывести суммарное количество продаж всех товаров')
    print(f"Cуммарное количество продаж всех товаров = {determine_sum_for_all(product_list)}")


    print('\nПосчитать и вывести среднее количество продаж всех товаров')
    print(f"Среднее количество продаж всех товаров = {determine_avg_for_all(product_list)}")



if __name__ == "__main__":
    main()
