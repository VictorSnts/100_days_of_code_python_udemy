# Dictionary #########################
# TODO Defining a dictionary
programming_dictionary = {
    "Bug": "An error in a program that prevents the program from running as expected.",
    "Function": "A piece of code that you can easily call over and over again."
}

# TODO Checking dictionary items (By Keys)
# print(programming_dictionary["Bug"])
# print(programming_dictionary["Function"])


# TODO Adding new itens to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again."
# print(programming_dictionary)


# TODO Creating an enpty dictionary
# enpty_dict = {}


# TODO Clearing items from a dictionary
# programming_dictionary = {}


# TODO Editing dictionary items
# programming_dictionary["Bug"] = "New value"
# print(programming_dictionary["Bug"])


# TODO Loop through a dictionary
# for key in programming_dictionary:
#     print(key)  # Printing the keys
#     print(programming_dictionary[key])  # Printing the values
#     print(f"{key}: {programming_dictionary[key]}")  # Printing the keys and the values


# Nesting (Aninhamento) #########################

# TODO Nesting a List in a Dictionary
# travel_log = {
#     "France": ["Paris", "Lille", "Dijon"],
#     "Germany": ["Berlin", "Hamburg", "Stuttgart"],
#     "Brazil": ["Rio de Janeiro", "Bahia", "Fortaleza"]
# }


# Nesting a Dictionary in a Dictionary
# travel_log = {
#     "France": {
#         "cities_visited": [
#             "Paris",
#             "Lille",
#             "Dijon"],
#         "total_visits": 12
#     },
#     "Germany": {
#         "cities_visited": [
#             "Berlin",
#             "Hamburg",
#             "Stuttgart"],
#         "total_visits": 4
#     },
#     "Brazil": {
#         "cities_visited": [
#             "Rio de Janeiro",
#             "Bahia",
#             "Fortaleza"],
#         "total_visits": 3
#     }
# }


# Nesting a Dictionary in a List
# travel_log = [
#     {
#         "country": "France",
#         "cities_visited": ["Paris", "Lille", "Dijon"],
#         "total_visits": 12
#     },
#     {
#         "country": "Germany",
#         "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
#         "total_visits": 4
#     },
#     {
#         "country": "Brazil",
#         "cities_visited": ["Rio de Janeiro", "Bahia", "Fortaleza"],
#         "total_visits": 3
#     }
# ]
# print(travel_log)

starting_dictionary = {
    "a": 9,
    "b": 8,
}

final_dictionary = {
    "a": 9,
    "b": 8,
    "c": 7,
}

final_dictionary["c"] = [1, 2, 3]
