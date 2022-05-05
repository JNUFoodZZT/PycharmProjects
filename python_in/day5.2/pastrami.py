sandwish_orders = ['pastrami','fat_pork','beef','pastrami','chicken','pastrami']
print('pastrami is over ,sorry')
finished_orders = []
while True:
    if 'pastrami' in sandwish_orders:
        finished_orders.append(sandwish_orders.pop())
    else:
        break
print(finished_orders)
print(sandwish_orders)

