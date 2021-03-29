file = open('test.txt')
# print(file.read(8))

# line = file.read()
# while line != "":
# print(line)
# line = file.read()

for line in file.readlines():
    print(line)
file.close()
