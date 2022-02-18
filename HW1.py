#Nacteni modulu
from calendar import weekday, day_name
from datetime import date
#Vstupy, vytvoreni promennych
DDay = int(input("Napiš den: "))
MMonth = int(input("Napiš měsíc (číslem): "))
YYear = int(input("Napiš rok: "))
DDate = date(YYear,MMonth,DDay)

#Fce calendar
WWeekDay = weekday(YYear, MMonth, DDay)
NameOfWeekDay = day_name[WWeekDay]

#Vyhodnoceni casu pro cas slovesa
Today = date.today()
if DDate == Today:
    Verb = str("is Today! And Today is")
elif DDate < Today:
    Verb = str("was")
else: 
    Verb = str("will be")

#Vystup
print (f"Day {DDate} {Verb} {NameOfWeekDay}.")
