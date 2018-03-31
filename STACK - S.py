def push(stack):
  if len(stack) < 100:
      n = input('Bведите число. которое хотите добавить')
      stack = stack + [n]
      print('ok')
      return (stack)
  else:
      print("Stack is full")

def pop(listik):
   back(listik)
   listik = listik[:-1]
   return (listik)

def back(my_lis):
   if len(my_lis) > 1:
       print(my_lis[-1])
   elif len(my_lis) == 1:
       print(my_lis[0])
   else:
       print('No elements')


lis =['sabina',7,'serega','proga','magic']

while True:
  print("""
      push - Добавить в стек число.
      pop - Удалить из стека последний элемент.
      back - Вывести значение последнего элемента, не удаляя его из стека.
      size - Вывести количество элементов в стеке.'
      clear - Очистить стек.
      exit - Завершить работу.
   """)
  a = input("Введите вашу команду:")
  if a == 'push':
      lis = push(lis)
  elif a == 'pop':
      lis = pop(lis)
  elif a == 'back':
      back(lis)
  elif a == 'size':
      print(len(lis))
  elif a == 'clear':
      lis=[]
      print(lis)
  elif a == 'exit':
      print('bye')
      break
  else:
      print('Error')