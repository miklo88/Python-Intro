"""
Dictionaries are Python's implementation of associative arrays.
There's not much different with Python's version compared to what
you'll find in other languages (though you can also initialize and
populate dictionaries using comprehensions just like you can with
lists!).

The docs can be found here:
https://docs.python.org/3/tutorial/datastructures.html#dictionaries

For this exercise, you have a list of dictionaries. Each dictionary
has the following keys:
 - lat: a signed integer representing a latitude value
 - lon: a signed integer representing a longitude value
 - name: a name string for this location
"""
#this is a list with dictionaries in it as elements.
waypoints = [
    {
        "lat": 43,
        "lon": -121,
        "name": "a place"
    },
    {
        "lat": 41,
        "lon": -123,
        "name": "another place"
    },
    {
        "lat": 43,
        "lon": -122,
        "name": "a third place"
    }
]

# Add a new waypoint to the list
# YOUR CODE HERE
# just goofin and seeing all my key pairs in the dictionary.
# print(waypoints)
# print(waypoints[0])
# print(waypoints[1])
# print(waypoints[2]) 
#adding another key value pair to a dictionary.
# to update a dictionary you'll use update(). this is a list tho so we used append.
waypoints.append({"lat": 44, "lon": 52, "name":"casita"})
# print(waypoints)
# print(waypoints[3])
# adding to a list, and i neeed to specify what exactly i'm adding

# Modify the dictionary with name "a place" such that its longitude
# value is -130 and change its name to "not a real place"
# Note: It's okay to access the dictionary using bracket notation on the
# waypoints list.
# YOUR CODE HERE
# print(waypoints[0])
a = {"name":"not a place"}
waypoints[0].update(a)
# print(waypoints[0])

# Write a loop that prints out all the field values for all the waypoints
# YOUR CODE HERE
# x = waypoints[3].values()
# # print(x)
for i in waypoints:
    print(i.values())

