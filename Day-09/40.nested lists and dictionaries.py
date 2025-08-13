capitals = {
    "france" : "paris",
    "germany" : "berlin"
}

#nested list in dictionary
travel_log = {
    "france" : ["paris","little","dijon"],
    "germany" : ["stuttart", "berlin"]
}
print(travel_log["france"][0])


#nested list
nested_list =["a","b",["c","d"]]
print(nested_list[2][1])

#list in dictionary nested in dictionary
travel_logg = {
    "france": {
    "num_times_visited":8,
    "cities_visited" : ["paris","little","dijon"]
    },
    "germany" : {
        "cities_visited": ["stuttart", "berlin"],
        "total_visits" : 5
    },
}
print(travel_logg["germany"]["cities_visited"][0])