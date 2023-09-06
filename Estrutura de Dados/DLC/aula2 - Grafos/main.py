from graph import Graph
from vertex import Vertex

my_graph = Graph()

cities = [
  {
    "name":"Arad",
    "neighbours": [
      {"name": "Zerind", "weight": 75},
      {"name": "Sibiu", "weight": 140},
      {"name": "Timisoara", "weight": 118}
    ]
  },
  {
    "name": "Bucharest",
    "neighbours": [
      {"name": "Urziceni", "weight": 85},
      {"name": "Giurgiu", "weight": 90},
      {"name": "Fagaras", "weight": 211},
      {"name": "Pitesti", "weight": 90}
    ]},
  {
    "name":"Craiova",
    "neighbours": [
      {"name": "Pitesti", "weight": 138},
      {"name": "Rimnicu Vilcea", "weight": 146},
      {"name": "Dobreta", "weight": 120}
    ]
  },
  {
    "name":"Dobreta",
    "neighbours": [
      {"name": "Craiova", "weight": 120},
      {"name": "Mehadia", "weight": 75}
    ]
  },
  {
    "name": "Eforie",
    "neighbours": [
      {"name": "Hirsova", "weight": 86}
    ]
  }, 
  {
    "name": "Fagaras",
    "neighbours": [
      {"name": "Bucharest", "weight": 211},
      {"name": "Sibiu", "weight": 99}
    ]
  },
  {
    "name": "Giurgiu",
    "neighbours": [
      {"name": "Bucharest", "weight": 90}
    ]
  }, 
  {
    "name":"Hirsova",
    "neighbours": [
      {"name": "Eforie", "weight": 86},
      {"name": "Urziceni", "weight": 98}
    ]
  },
  {
    "name":"Iasi",
    "neighbours": [
      {"name": "Vaslui", "weight": 92},
      {"name": "Neamt", "weight": 87}
    ]
  }, 
  {
    "name":"Lugoj",
    "neighbours": [
      {"name": "Mehadia", "weight": 70},
      {"name": "TImisoara", "weight": 111}
    ]
  },
  {
    "name":"Mehadia",
    "neighbours": [
      {"name": "Lugoj", "weight": 70},
      {"name": "Dobreta", "weight": 75}
    ]
  },
  {
    "name": "Neamt",
    "neighbours": [
      {"name": "Iasi", "weight": 87}
    ]
  },
  {
    "name":"Oradea",
    "neighbours":[
      {"name": "Zerind", "weight": 71},
      {"name": "Sibiu", "weight": 151}
    ]
  }, 
  {
    "name":"Pitesti",
    "neighbours": [
      {"name": "Craiova", "weight": 138},
      {"name": "Rimnicu Vilcea", "weight": 97},
      {"name": "Bucharest", "weight": 101}
    ]
  }, 
  {
    "name":"Rimnicu Vilcea",
    "neighbours": [
      {"name": "Pitesti", "weight": 97},
      {"name": "Sibiu", "weight": 80},
      {"name": "Craiova", "weight": 146}
    ]
  }, 
  {
    "name":"Sibiu",
    "neighbours": [
      {"name": "Fagaras", "weight": 99},
      {"name": "Rimnicu Vilcea", "weight": 80},
      {"name": "Oradea", "weight": 151},
      {"name": "Arad", "weight": 140}
    ]
  }, 
  {
    "name":"Timisoara",
    "neighbours": [
      {"name": "Arad", "weight": 118},
      {"name": "Lugoj", "weight": 111}
    ]
  },
  {
    "name":"Urziceni",
    "neighbours": [
      {"name": "Bucharest", "weight": 85},
      {"name": "Hirsova", "weight": 98},
      {"name": "Vaslui", "weight": 142}
    ]
  },
  {
    "name":"Vaslui",
    "neighbours": [
      {"name": "Urziceni", "weight": 142},
      {"name": "Iasi", "weight": 92}
    ]
  },
  {
    "name":"Zerind",
    "neighbours":[
      {"name": "Oradea", "weight": 71},
      {"name": "Arad", "weight": 75}
    ]
  }
]

for city in cities:
    # print(city)
    for neighbour in city.get("neighbours"):
        my_graph.add_vertex(city.get("name"))
        my_graph.add_vertex(neighbour.get("name"))

        my_graph.add_connection(
            city.get("name"),
            neighbour.get("name"),
            neighbour.get("weight")
        )

# print(my_graph.search("Arad", "Bucharest"))

print(my_graph.search_dfs())
