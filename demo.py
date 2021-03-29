
print("Hello")
# here are the comments that defined
a = 3
print(a)

Str = "Hello world"
print(Str)

b, c, d = 5, 6.50, "Haroon Hassan"

print("{} {}".format("value is", b))

print(type(b))

print(type(c))

print(type(d))
values = [1, 2, 4, "Haroon", 6]  # List is a data type that allows multiple values and can be different data type

print(values[0])
print(values[2])
print(values[-1])
print(values[1:4])
values.insert(3, "HASSAN")
values.append("Umair")
print(values)

values[3] = "Adeel" # updating
print(values)

del values[1]
print(values)
# Tuple is same as List but immutable
val = (4, 5, "Ahmed", 9)
print(val[0])

# Dictionary
dic = {2: 2, "A": "Haroon", "D": 4, 8: "Hassan"}
print(dic["A"])

# create dictionary at runtime
dict = {}

dict["FirstName"] = "Haroon"
dict["LastName"] = "Hassan"
dict["Gender"] = "Male"
print(dict)

print(dict["LastName"])

Greeting = "Good Morning"
if Greeting == "Good Morning":
    print(" Condition matched")
else:
    print("Condition is not matched")
# print("if else code condition is completed")

obj = (1, 2, 3, 4, 5)
for i in obj:
    print(i*2)
# sum of 1st natural numbers
# range(i,j) -> i to j-1
summation = 0
for j in range(1, 6):
    summation = summation + j
print(summation)

for k in range(1, 10, 2):
    print(k)
print('*****************')
it = 10
while it > 1:
    if it == 9:
        it = it - 1
        continue
    if it == 2:
        break
    print(it)
    it = it - 1
print('While loop execution is done')