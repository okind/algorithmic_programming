#HashTable = array
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
    #HashMap<key, value>
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

    
    
    
