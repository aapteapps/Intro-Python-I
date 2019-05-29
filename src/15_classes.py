# Make a class LatLon that can be passed parameters `lat` and `lon` to the
# constructor


class LatLon:
    def __init__(self, lat, lon):
        self.lat = lat
        self.lon = lon

    def __repr__(self):
        return "<LatLon lat:%s lon:%s>" % (self.lat, self.lon)

    def __str__(self):
        return "From str method of LatLon: lat is %s, lon is %s" % (self.lat, self.lon)
        
# Make a class Waypoint that can be passed parameters `name`, `lat`, and `lon` to the
# constructor. It should inherit from LatLon. Look up the `super` method.

class Waypoint(LatLon):
    def __init__(self, lat, lon, name):
        super().__init__(lat, lon)
        self.name = name
    
    def __repr__(self):
        return "<Waypoint name:%s>" % (self.name)

    def __str__(self):
        return "From str method of Waypoint: name is %s" % (self.name)


# Make a class Geocache that can be passed parameters `name`, `difficulty`,
# `size`, `lat`, and `lon` to the constructor. What should it inherit from?

class Geocache(Waypoint):
    def __init__(self, lat, lon, name, difficulty, size):
        super().__init__(lat, lon, name)
        self.difficulty = difficulty
        self.size = size

    def __repr__(self):
        return "<Geocache difficulty:%s size:%s>" % (self.difficulty, self.size)

    def __str__(self):
        return "From str method of Geocache: difficulty is %s, size is %s" % (self.difficulty, self.size)

# Make a new waypoint and print it out: "Catacombs", 41.70505, -121.51521

waypoint = Waypoint(41.70505, -121.51521, "Catacombs")
attrs = vars(waypoint)

# Without changing the following line, how can you make it print into something
# more human-readable? Hint: Look up the `object.__str__` method
print(waypoint)
print (', '.join("%s: %s" % item for item in attrs.items()))
print()

# Make a new geocache "Newberry Views", diff 1.5, size 2, 44.052137, -121.41556

geocache = Geocache(44.052137, -121.41556, "Newberry Views", 1.5, 2)
attrs = vars(geocache)

# Print it--also make this print more nicely
print(geocache)
print (', '.join("%s: %s" % item for item in attrs.items()))
