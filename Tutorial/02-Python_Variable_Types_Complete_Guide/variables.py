#variables types and their operations in python

#Int Integers
age = 25

#Examples
int_a = age + 2
int_b = age - 2
int_c = age * 2
int_d = age / 2
print("int_a:",int_a)
print("int_b:",int_b)
print("int_c:",int_c)
print("int_d:",int_d)

#Float
price = 29.99

#Examples
float_a = age + 2
float_b = age - 2
float_c = age * 2
float_d = age / 2
print("float_a:",float_a)
print("float_b:",float_b)
print("float_c:",float_c)
print("float_d:",float_d)

#String
name = "alice"

#Examples
print(f"{name} is {age} years old.")
print("First Letter of String Sequence:",name[0])
print("Slicing",name[0:3])

#Boolean
is_online = False

#Examples
if is_online == True:
    print(f"{name} is Online.")
else:
    print(f"{name} is Offline.")


#List
jobs = ["programmer","doctor", "teacher"]

#Examples
print(f"{name} is a {jobs[0]}")
jobs.append("Engineer")
jobs.remove("programmer")

#Tuple
dimensions = (1920 , 1080)

#Example
print("First Element:",dimensions[0])
print("Second Element:",dimensions[1])

#Set
unique_items = {1,2,3,4,5}

#Examples
unique_items.add(6)
unique_items.discard(3)

#Dictionary
person = {
    "name":"Alice",
    "age":25,
    "job":"programmer"
}

#Examples
print(f"{person["name"]} is {person['age']} years old and is a {person['job']}.")
person["city"] = "New York"

#None
result = None

#Examples
if result == None:
    print("There is no result.")
else:
    print(f"result is {result}")

#Range
range = range(10)

#Examples
for i in range:
    print(i)

#Bytes
bytes_data = b"hello"

#Examples
print("bytes_data:",bytes_data)

#Bytes array
bytes_array = bytearray(5)

#Examples
print("bytes_array:",bytes_array)

#Frozen Set
frozen_set = frozenset([1, 2, 3])

#Examples
print("frozen_set:",frozen_set)

#Complex Number
comp_num = 3 + 4j

#Examples
print("Real Part:",comp_num.real)
print("Imaginary Part:",comp_num.imag)
print("Conjugate:",comp_num.conjugate())

#Type conversion

#Int to String
age = str(25)
print("Type of age:",type(age))

#String to Int
age = int("25")
print("Type of age:",type(age))
print(float(age) + 2)

#Int to Float
age = float(25)
print("Type of age:",type(age))