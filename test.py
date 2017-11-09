import json
import time
import csv


def divide(quantity):
    with open('settings.json') as settings_data:
        settings = json.load(settings_data)
    if 100 <= abs(quantity) <= 1000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['1k'])
        else:
            return quantity/int(settings['divide']['1k']-1)
    if 1001 <= abs(quantity) <= 3000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['3k'])
        else:
            return quantity/int(settings['divide']['3k']-1)
    if 3001 <= abs(quantity) <= 6000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['6k'])
        else:
            return quantity/int(settings['divide']['6k']-1)
    if 6001 <= abs(quantity) <= 8000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['8k'])
        else:
            return quantity/int(settings['divide']['8k']-1)
    if abs(quantity) >= 8001:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['10k'])
        else:
            return quantity/int(settings['divide']['10k']-1)


def divide_yesterday(quantity):
    with open('settings.json') as settings_data:
        settings = json.load(settings_data)
    if 100 <= abs(quantity) <= 1000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['1k'])
        else:
            return quantity/int(settings['divide']['1k']-1)
    if 1001 <= abs(quantity) <= 3000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['1k'])
        else:
            return quantity/int(settings['divide']['1k']-1)
    if 3001 <= abs(quantity) <= 6000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['3k'])
        else:
            return quantity/int(settings['divide']['3k']-1)
    if 6001 <= abs(quantity) <= 8000:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['6k'])
        else:
            return quantity/int(settings['divide']['6k']-1)
    if abs(quantity) >= 8001:
        if quantity % 2 == 0:
            return quantity/int(settings['divide']['8k'])
        else:
            return quantity/int(settings['divide']['8k']-1)

data = []

# Read File
try:
    with open('data.json') as json_data:
        d = json.load(json_data)
except EnvironmentError:
    print('JSON File error')
else:
    for json_data in d:
        yesterday_flag = False
        if abs(json_data['quantity']) > 100:
            dtime = str(time.strptime(json_data['date'], "%d/%m/%Y").tm_mday-1) + '/' + \
                    str(time.strptime(json_data['date'], "%d/%m/%Y").tm_mon) + '/' + \
                    str(time.strptime(json_data['date'], "%d/%m/%Y").tm_year)

            yesterday_symbol = (x for x in d if x['date'] == dtime and x['symbol'] == json_data['symbol'])

            # Split Quantity
            json_data['amt'] = divide(json_data['quantity'])
            json_data['split'] = int(json_data['quantity']/json_data['amt'])

            for x in yesterday_symbol:
                if yesterday_flag:
                    break
                else:
                    # If Symbol exist in yesterday , Do Lower Split.
                    yesterday_flag = True
                    json_data['amt'] = divide_yesterday(json_data['quantity'])
                    json_data['split'] = int(json_data['quantity']/json_data['amt'])

            data.append(json_data)

            # Print Data
            print(json_data)

# Enter Date to Export CSV
date_export = input('Enter Date to Export CSV (DD/MM/YYYY format) * Leave blank to get all : ')

with open('Data'+date_export+'.csv', 'w') as csvfile:
    fieldnames = ['date', 'account', 'symbol', 'quantity', 'split', 'amt']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    writer.writeheader()

# If Not blank fill csv by Date
    if date_export:
        for item in data:
            if item['date'] == date_export:
                writer.writerow({'date': item['date'], 'account': item['account'], 'symbol': item['symbol'],
                                 'quantity': item['quantity'], 'split': item['split'], 'amt': item['amt']})
# If Blank Fill All
    else:
        for item in data:
            writer.writerow({'date': item['date'], 'account': item['account'], 'symbol': item['symbol'],
                                 'quantity': item['quantity'], 'split': item['split'], 'amt': item['amt']})