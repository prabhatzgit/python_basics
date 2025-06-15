capitals = {
    "France" : "Paris",
    "Germany" : "Berlin"
}

# Nested list in dictionary

travel_log = {
    "France" : ["Paris", "Little", "Dijon"],
    "Germany" : ["Stuttgart", "Berlin"]
}

print(travel_log)
print(travel_log["France"])
print(travel_log["France"][1])

nested_list = ["A","B",["C","D"]]
print(nested_list[2])
print(nested_list[2][0])
print(nested_list[2][1])

cities = {
    "Bangalore" : {
        "places_visited": ["E City","ITPL","White field","Indira Nagar","JP Nagar"],
        "num_times_visited": 8
    },
    "Vizag" : {
    "places_visited": ["Gajuwaka", "Hanumantwaka", "NAD"],
    "num_times_visited": 10
    },
}

print(cities["Vizag"])
print(cities["Vizag"]["places_visited"])
print(cities["Vizag"]["places_visited"][2])