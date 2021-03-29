# ItemsInCart = 0

# if ItemsInCart != 2: # raise Exception("Product cart item is not match")
    # pass


# assert(ItemsInCart == 0)

try:
    with open('testlog.txt', 'r') as reader:
        reader.read()

except:
    print("This is except block in python")

try:
    with open('test.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)