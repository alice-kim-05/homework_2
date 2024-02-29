weight=float(input('Вес человека (в фунтах) - ')) / 2.205
height=float(input('Рост человека (в дюймах) - '))*2.54/100
print('ИМТ - ', round(weight/(height**2),2),weight, height)
