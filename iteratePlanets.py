#List of Planets
planet_list = ["Mercury", "Mars"]

planet_list.append("Jupiter")
planet_list.append("Saturn")
planet_list.extend(["Uranus", "Neptune"])
planet_list.insert(2, "Earth")
planet_list.insert(3, "Venus")
planet_list.append("Pluto")
rocky_planets = planet_list[0:4]
planet_list.__delitem__(-1)

#List of Spacecraft

spacecrafts = [
    ("Pioneer 10", "Jupiter"),
    ("Pioneer 11", "Jupiter"),
    ("Voyager 2", "Jupiter"),
    ("Cassini", "Saturn"),
    ("Viking", "Mars")
]

#Iterate over planets
for planet in planet_list:
    for craft in spacecrafts:
        if craft[1] == planet:
            print(craft[0],"visited", craft[1])