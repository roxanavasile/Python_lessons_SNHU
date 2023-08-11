#collect user input
input_month = input()
input_day = int(input())

#progarm data
days = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31]
months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November',' December']
winter = ['January', 'February', 'March']
spring = ['April', 'May', 'June']
summer = ['July', 'August', 'September']
autumn = ['October', 'November', 'December']

#validate user input
if (input_month not in months) or (input_day not in days):
    print('Invalid')
else:
    if input_month in winter:
        season = 'Winter'
    elif input_month in spring:
        season = 'Spring'
    elif input_month in summer:
        season = 'Summer'
    elif input_month in autumn:
        season = 'Autumn'
       
    if (input_month == 'March') and (input_day > 19):
        season = 'Spring'
    elif (input_month == 'June') and (input_day > 20):
        season = 'Summer'
    elif (input_month == 'September') and (input_day > 21):
        season = 'Autumn'
    elif (input_month == 'December') and (input_day > 20):
        season = 'Winter'

if (input_month in ('September', 'April', 'June', 'November')) and (input_day > 30):
    print('Invalid')
else:
    print(season)


