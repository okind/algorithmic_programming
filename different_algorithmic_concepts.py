# HashTable = array
import collections
# if key space = [0 .. 9]
# a[key] = value
# studends = string[10]
# class Student:
#     firstName = string
#     lastName = string
#     age = int
#     country = string
#     university = string
#     photo = array of bytes
# student = Student[10]
# O(1)

# all studens in the world
# there is no id of student
# key = country + city + street + house number + apartment number + first name + last name + age
# key = string
# HashMap<key, value>
# HashMap<String, Student> students = new HashMap<String, Student>()
# println(students.get(country + city + street + house number + apartment number + first name + last name + age).university)
# 1M students
# size(student) = 1MB
# size(students) = 1M * 1MB = 1TB (can keep in memory)
# size of key 1000 bytes, 30 ^ 1000 = 3 * 10 ^ 10000
# O(N)

# key space = [0 .. n-1], n = 10^1000; or key is string
# need to store 100 elements
# HashTable = array of size 100, key space = [0 .. 99], index = hash_function(key) [0..99]
# array of size 100: a[hash_function(key)] = value
# limitations: needs to increase size of hash table; collisions
# O(1) - constant time
# Solution for collisions: array of lists

# Basic data types
"""Create a list of strings and print the list"""

list_of_strings = ["Hello", "World", "I", "am", "learning", "Python"]
for w in list_of_strings:
    print(w)

# create a list of different data types and print the list
list_of_different_data_types = ["Hello", 1, 2.5, True]
# create range of numbers from 0 to 9 with step 2 and print the list
range_of_numbers = range(0, 10, 2)
print(range_of_numbers)
# access each element of the range of numbers and print it
# acess 2 element of the range of numbers and print it
print(range_of_numbers[2])
# access last element of the range of numbers and print it
print(range_of_numbers[-1])


list_of_strings.append("!")

# create a dictionary with 3 key-value pairs
dictionary = {"key1": "value1", "key2": "value2", "key3": "value3"}
# access value by key and print it

# access all keys and print them
for key in dictionary:
    print(key)
print("aceess value 1: " + dictionary.get("key1"))

# create a set of random numbers from 0 to 100
set_of_random_numbers = set()
for i in range(0, 100):
    set_of_random_numbers.add(i)
set_of_random_numbers.remove(34)

# create named  tuple with 3 fields
Point = collections.namedtuple("Point", ["x", "y", "z"])


# create collections.userlist
user_list = collections.UserList()
# initiate userlist with list of strings
user_list = collections.UserList(["Hello", "World"])
user_list.insert(0, "I")
sorted(user_list, reverse=True)


# create a simple class with one method
class SimpleClass:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name
