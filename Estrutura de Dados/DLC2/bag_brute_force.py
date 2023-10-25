from products import products
import itertools
import timeit as time

BAG_VOLUME = 10
ALL_COMBINATIONS = []

start = time.default_timer()

for i in range(1, len(products)):
  combinations = list(itertools.combinations(products, i))
  all_combinations_by_range = []
  for y in combinations:
    sumL = 0
    sumP = 0
    for z in y:
      sumL += z['l']
      sumP += z['price']
    all_combinations_by_range.append({
      # "combinations": combinations,
      "liter": sumL,
      "price": sumP
    })
  ALL_COMBINATIONS.append(all_combinations_by_range)

max_price = 0
comb = any
for y in ALL_COMBINATIONS:
  for x in y:
    if x['price'] > max_price and BAG_VOLUME > x['liter']:
      max_price = x['price']
      comb = x


print({
  "comb": comb,
  "products": len(products),
  "time": time.default_timer() - start
})

