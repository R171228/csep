def compound_interest(principle,rate,year):
    if year<=0:
        return principle
    else:
        return compound_interest(principle+principle*rate/100,rate,year-1)
principle=int(input("enter amount:"))
rate=int(input("enter the rate:"))
year=int(input("enter the years:"))
amount=compound_interest(principle,rate,year)
print(amount)
