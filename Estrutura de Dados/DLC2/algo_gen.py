from entities.individual import Individual
from entities.item import Item
from products import products

BAG_VOLUME = 0
items = []

for i in products:
  items.append(Item(i.get('name'), i.get('price'), i.get('l')))


fIndividual = Individual(items, BAG_VOLUME, 0)

print(fIndividual.get_solution_rating())