# Number of items: 3  Price of item: 100  Price of item: 35.56  Price of item: 3.24  Total price for 3 items is $124.92
print("calculation of price ")
total = 0
count = 0
price_of_item = input("please input price,enter q to start calculate:")
while price_of_item != "q":
    price = float(price_of_item)
    total += price
    count += 1
    price_of_item = input("please input price,enter q to start calculate:")
if count == 0:
    result = 0

else:
    result = total
if result < 100:
    print("not enough $100")
else:
    print("number of items:" + str(count))
    print("total price for " + str(count) + " is " + str(result * 0.9))
