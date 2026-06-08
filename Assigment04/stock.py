#stock store
items=['chocolate','kurkure','biscuits','maggie','chicken','colddrink','Banana','Rice_bag','Orange','cake']
stock={
    'chocolate':10,
    'kurkure':8,
    'biscuits':9,
    'maggie':14,
    'chicken':8,
    'colddrink':4,
    'Banana':13,
    'Rice_bag':23,
    'Orange':7,
    'cake':13
}
print("Stock which is less than 10: ")
for item in items:
    if stock[item]<10:
        print(item,":",stock[item])    