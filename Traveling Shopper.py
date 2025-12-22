def buy_items(funds, items):
    exchange_rates= {"USD":10000, "EUR":11000, "GBP": 12500, "JPY":70, "CAD": 7500}
##multiplied the given exchange rate table by 10,000
##For currency calculations,  converting everything into scaled integers to avoid floating-point precision errors

    money = int(float(funds[0])*exchange_rates[funds[1]])
    count=0
    for price, currency in items:
        cost = int(float(price)*exchange_rates[currency])

        if money>=cost:
            money-=cost
            count+=1
        else:
            break
    if count ==len(items):
        return "Buy them all!"
    else:
        return f"Buy the first {count} items."
