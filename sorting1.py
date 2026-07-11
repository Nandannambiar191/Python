"""UnderstandingLinearSearch"""
"""# Program for searching an element using Linear Search
# Function to search for an element"""

def search(arr, n, x):
    for i in range(0, n):
        if (arr[i] == x):
            return i
    return -1
arr = [2, 3, 4, 10, 40]
x = 10
n = len(arr)
result = search(arr, n, x)
if (result == -1):
    print("Element is not present in array")
else:
    print("Element is present at index", result)

"""FindingDuplicates"""
"""Write a program to find the duplicate of an item in an array"""

tour_locations = [ "New York City", "Los Angeles", "Bangkok", "Istanbul", "London", "New York City", "Toronto" ]
target_city = "New York City"
def linear_search(search_list, target_value):
    matches = []
    for idx in range(len(search_list)):
        if search_list[idx] == target_value:
            matches.append(idx)
    if not matches:
        raise ValueError(("{} is not in the list".format(target_value)))
    else:
        return matches
tour_stops = linear_search(tour_locations, target_city)