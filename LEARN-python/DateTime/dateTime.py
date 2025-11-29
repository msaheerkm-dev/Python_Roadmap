#date time library
import datetime as dt

# print current date and time
print(dt.datetime.now())

# print current date only
print(dt.date.today())

# print current time only
now=dt.datetime.now()
print(now.time())

# rearanging using strftime()
print("Current Time:", now.strftime("%d/%m/%Y"))

# date calculations 
x=dt.datetime(2027,5,7)
y=dt.datetime(2025,5,7)
dif=x-y
print(dif)

end=dt.datetime.now()
dif=end-now
print(dif)
print('\n')