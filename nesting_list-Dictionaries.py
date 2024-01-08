#example
#{
    #key1: [list],
    #key2: {Dict}},
#}

#Nesting

capitals = {
    "France": "Paris",
    "Germany": "Berlin"
}

#Nesting a list

travel_log = {
    "France" : ["Paris", "Lille", "Dijon"],
    "Germany" : ["Berlin", "Hamburg", "Stuttgart"]
}

#Nesting list in the list

sample = ["A", "B", ["C", "D"]]

#Nesting Dictionary in Dictionary

#example
#{
    #key1: [list],
    #key2: {Dict}},
#}

travel_log = {
    "France" : {"cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 15},
    "Germany" : {"cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10}
}
print(travel_log)

#[{
    #key1: [list],
    #key2: {Dict}},
#},
#{
    #key3 : value,
    #key4: value,
#}]

#Nesting Dictionary in a List

travel_bog = [
    {"Country": "France",  "cities_visited": ["Paris", "Lille", "Dijon"], "total_visits": 15},
    {"Country": "Germany", "cities_visited": ["Berlin", "Hamburg", "Stuttgart"], "total_visits": 10}
]
print(travel_bog)

travel_jog = [
    {
        "Country": "France",
        "cities_visited": ["Paris", "Lille", "Dijon"],
        "total_visits": 15
     },
    {
        "Country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 10
    },
]
print(travel_jog)