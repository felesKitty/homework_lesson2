user_month = int(input('Enter number of your favourite month and you will see it"s name: '))

months_in_dict = {1: 'January', 2: 'February', 3: 'March', 4: 'April',
              5: 'May', 6: 'June', 7: 'July', 8: 'August', 9: 'September',
              10: 'October', 11: 'November', 12: 'December'}

list_of_months = ['January', 'February', 'March', 'April', 'May', 'June', 'July',
                  'August', 'September', 'October', 'November', 'December']

if user_month in months_in_dict:
    print(f'{user_month} - this is {list_of_months[user_month - 1]}')