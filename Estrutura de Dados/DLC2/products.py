from entities.item import Item

productsaaa = [
  {
    "name": "Arroz",
    "l": 1.11,
    "price": 4.75
  },
  {
    "name": "Feijão",
    "l": 1.25,
    "price": 8.0
  },
  {
    "name": "Farinha de Trigo",
    "l": 1.67,
    "price": 5.5
  },
  {
    "name": "Açucar",
    "l": 1.11,
    "price": 3.50
  },
  {
    "name": "Sal",
    "l": 0.46,
    "price": 1.5
  },
  {
    "name": "Oleo de cozinha",
    "l": 0.9,
    "price": 4.5
  },
  {
    "name": "Cafe",
    "l": 1.39,
    "price": 16
  },
  {
    "name": "Leite",
    "l": 1,
    "price": 3.75
  },
  {
    "name": "Manteiga",
    "l": 0.54,
    "price": 11.50
  },
  {
    "name": "Pão",
    "l": 1.75,
    "price": 10
  },
  {
    "name": "Massas",
    "l": 1.33,
    "price": 7.5
  },
  {
    "name": "Enlatados",
    "l": 0.33,
    "price": 6
  },
  {
    "name": "Sabão",
    "l": 0.22,
    "price": 3
  },
  {
    "name": "Papel Higienico",
    "l": 3.24,
    "price": 4.5
  },
  # {
  #   "name": "Novo 1",
  #   "l": 3.54,
  #   "price": 2.5
  # },
  # {
  #   "name": "Novo 2",
  #   "l": 3.241,
  #   "price": 4.54
  # },
  # {
  #   "name": "Novo 3",
  #   "l": 3.54132,
  #   "price": 2.55
  # },
  # {
  #   "name": "Novo 4",
  #   "l": 2.24177,
  #   "price": 1.54
  # },
  # {
  #   "name": "Novo 5",
  #   "l": 4.24177,
  #   "price": 1.54
  # },
  # {
  #   "name": "Novo 6",
  #   "l": 3.24177,
  #   "price": 1.54
  # },
  # {
  #   "name": "Novo 7",
  #   "l": 1.24177,
  #   "price": 1.54
  # },
  # {
  #   "name": "Novo 8",
  #   "l": 2.5,
  #   "price": 1.54
  # },
]

products = [ Item(x["name"], x["price"], x["l"]) for x in productsaaa ]