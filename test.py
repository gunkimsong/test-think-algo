import json
import time
import csv

data = []
# Read File
try:
    with open('data.json') as json_data:
        d = json.load(json_data)
    with open('settings.json') as settings_data:
        settings = json.load(settings_data)
except EnvironmentError:
    print('JSON File error')


def divide(quantity):
    arg = []
    if 100 <= abs(quantity) <= 1000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['1k']))
            arg.append(int(settings['divide']['1k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['1k']-1))
            arg.append(int(settings['divide']['1k']-1))
            return arg
    if 1001 <= abs(quantity) <= 3000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['3k']))
            arg.append(int(settings['divide']['3k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['3k']-1))
            arg.append(int(settings['divide']['3k']-1))
            return arg
    if 3001 <= abs(quantity) <= 6000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['6k']))
            arg.append(int(settings['divide']['6k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['6k']-1))
            arg.append(int(settings['divide']['6k']-1))
            return arg
    if 6001 <= abs(quantity) <= 8000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['8k']))
            arg.append(int(settings['divide']['8k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['8k']-1))
            arg.append(int(settings['divide']['8k']-1))
            return arg
    if abs(quantity) >= 8001:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['10k']))
            arg.append(int(settings['divide']['10k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['10k']-1))
            arg.append(int(settings['divide']['10k']-1))
            return arg


def divide_yesterday(quantity):

    arg = []
    if 100 <= abs(quantity) <= 1000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['1k']))
            arg.append(int(settings['divide']['1k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['1k']-1))
            arg.append(int(settings['divide']['1k'])-1)
            return arg
    if 1001 <= abs(quantity) <= 3000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['1k']))
            arg.append(int(settings['divide']['1k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['1k']-1))
            arg.append(int(settings['divide']['1k']-1))
            return arg
    if 3001 <= abs(quantity) <= 6000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['3k']))
            arg.append(int(settings['divide']['3k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['3k']-1))
            arg.append(int(settings['divide']['3k']-1))
            return arg
    if 6001 <= abs(quantity) <= 8000:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['6k']))
            arg.append(int(settings['divide']['6k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['6k']-1))
            arg.append(int(settings['divide']['6k']-1))
            return arg
    if abs(quantity) >= 8001:
        if quantity % 2 == 0:
            arg.append(quantity/int(settings['divide']['8k']))
            arg.append(int(settings['divide']['8k']))
            return arg
        else:
            arg.append(quantity/int(settings['divide']['8k']-1))
            arg.append(int(settings['divide']['8k']-1))
            return arg


for json_data in d:
    yesterday_flag = False
    if abs(json_data['quantity']) > 100:
        dtime = str(time.strptime(json_data['date'], "%d/%m/%Y").tm_mday-1) + '/' + \
                str(time.strptime(json_data['date'], "%d/%m/%Y").tm_mon) + '/' + \
                str(time.strptime(json_data['date'], "%d/%m/%Y").tm_year)

        yesterday_symbol = (x for x in d if x['date'] == dtime and x['symbol'] == json_data['symbol'])

        for x in yesterday_symbol:
            if yesterday_flag:
                break
            else:
                yesterday_flag = True

        if yesterday_flag:
            split_arg = divide(json_data['quantity'])
        else:
            split_arg = divide_yesterday(json_data['quantity'])

        for num in range(0, split_arg[1]):
            tmp_data = {}
            tmp_data['date'] = json_data['date']
            tmp_data['time'] = settings['timeslot'][str(split_arg[1])][num]
            tmp_data['account'] = json_data['account']
            tmp_data['symbol'] = json_data['symbol']
            tmp_data['quantity'] = split_arg[0]
            data.append(tmp_data)


with open('Data.csv', 'w') as csvfile:
    fieldnames = ['date', 'time', 'account', 'symbol', 'quantity']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

    for item in data:
        writer.writerow({'date': item['date'], 'time': item['time'], 'account': item['account'], 'symbol': item['symbol'],
                             'quantity': item['quantity']})