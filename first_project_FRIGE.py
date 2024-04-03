# Импорт необходимых библиотек
from decimal import Decimal
from datetime import datetime as dt
DATE_FORMAT = '%Y-%m-%d'

#Объявляем словарь - список продуктов в холодильнике
goods = {}

# Функция добавления продукта в холодильник
def add(items, title, amount, expiration_date=None):
    if title in items:
        items[title].append({'amount': amount, 'expiration_date': datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date() if expiration_date else None})
    else:
        items[title] = [{'amount': amount, 'expiration_date': datetime.datetime.strptime(expiration_date, '%Y-%m-%d').date() if expiration_date else None}]   
# Функция добавления продукта из текстовой заметки
def add_by_note(items, note):
    title_result = ''
    amount_result = 0
    date_result = ''
    note = note.split()
    if "-" in note[-1]:
        date_result = str(dt.strptime(str(note[-1]), DATE_FORMAT).date()) 
        #if note[-2].replace('.','').isdigit():
        amount_result = Decimal(note[-2]) 
        del note[-1], note[-1]

    elif "-" not in note[-1]:
        date_result = None
        #if note[-2].replace('.','').isdigit():
        amount_result = Decimal(note[-1]) 
        del note[-1]
    title_result = ' '.join(note)
    add(items, title_result, amount_result, date_result)

def find(items, needle):
    #needle = ''
    result_find = []
    for title in items:
        if needle.lower() in title.lower():
             result_find.append(title)
    return result_find     
        

def amount(items, needle):
    products = find(items, needle)
    #print(products)
    result_amount = Decimal('0')
    for i in products:
        #print(title)
        value = items[i]
        #print(value)
        for val in value:
            #print(val)
            result_amount += Decimal(val['amount'])
    return result_amount

import datetime
def expire(items, in_advance_days=0):
    today = datetime.date.today()
    result = []
    for product, details in items.items():
        total_expired = 0
        for detail in details:
            expiration_date = detail['expiration_date']
            if expiration_date != None:
                expiration_date = datetime.datetime.strptime(str(expiration_date), '%Y-%m-%d').date()
                if expiration_date <= today + datetime.timedelta(days=in_advance_days):
                    total_expired += detail['amount']
        if total_expired > 0:
            result.append((product, Decimal(total_expired)))       
    return result
add_by_note(goods, 'молоко 1.5 2023-04-10') 
add_by_note(goods, 'молоко 5.5 2023-04-10') 
add_by_note(goods, 'пельмени 3.5 2024-03-30') 
add_by_note(goods, 'пельмени универсальные 2 2024-04-30') 
add_by_note(goods, 'хлеб 3.5') 
print(expire(goods,))
