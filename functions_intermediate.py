# question 1
# changing values in the dictionaries and lists below
def updating_values(list_1, list_2, list_3, list_4):
    list_1[1][0] = 15
    list_2[0]["last_name"] = "Bryant"
    list_3["soccer"][0] = "Andres"
    list_4[0]["y"] = 30
    return list_1, list_2, list_3, list_4


x = [[5, 2, 3], [10, 8, 9]]
students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'}
]
sports_directory = {
    'basketball': ['Kobe', 'Jordan', 'James', 'Curry'],
    'soccer': ['Messi', 'Ronaldo', 'Rooney']
}
z = [{'x': 10, 'y': 20}]

y = updating_values(x, students, sports_directory, z)
print(y)


# question 2
# iterate through a list of dictionaries and print their keys and values
def iterateDictionary(some_list):
    for i in some_list:
        for key in i:
            print(key + " - " + i[key] + ", ", end=" ")
        print()


students = [
    {'first_name':  'Michael', 'last_name': 'Jordan'},
    {'first_name': 'John', 'last_name': 'Rosales'},
    {'first_name': 'Mark', 'last_name': 'Guillen'},
    {'first_name': 'KB', 'last_name': 'Tonel'}
]
iterateDictionary(students)
# should output: (it's okay if each key-value pair ends up on 2 separate lines;
# bonus to get them to appear exactly as below!)

# question 3
# will print values associated with given key in the list of dictionaries
def iterateDictionary2(key_name, some_list):
    for i in some_list:
        print(i[key_name])

iterateDictionary2("first_name", students)
iterateDictionary2("last_name", students)

# question 4
# iterate through a dictionary with list values
def printInfo(some_dict):
    for key in some_dict:
        print("----------------")
        print(len(some_dict[key]), key.upper())
        for value in some_dict[key]:
            print(value)
        


dojo = {
    'locations': ['San Jose', 'Seattle', 'Dallas', 'Chicago', 'Tulsa', 'DC', 'Burbank'],
    'instructors': ['Michael', 'Amy', 'Eduardo', 'Josh', 'Graham', 'Patrick', 'Minh', 'Devon']
}
printInfo(dojo)
