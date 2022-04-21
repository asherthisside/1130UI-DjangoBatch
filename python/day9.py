f = open("intro.txt", "r")
# print(f.read(12))
# print(f.read(4))
# print(f.read(20))
# print(f.read())
# print(f.read())
# print(f.readline())
# print(f.readline())
# lines = f.readlines()
# for i in lines:
#     print(i)
# f.close()

# f1 = open("data.txt", "w")
# f1.write("This is the text that we wrote using the write method")
# f1.write("\nWriting one more line")

# f1.close()

# f2 = open("data.txt", "a")
# f2.write("...\nThis is the 3rd Line.")
# f2.write("\nThere are 4 lines in this file")

# f2.close()

# tell function - Used to print out the current location of the pointer
# f3 = open("copy.txt", "r")
# print(f3.tell())
# print(f3.readline())
# print(f3.tell())
# print(f3.readline())
# print(f3.tell())
# print(f3.readline())
# print(f3.tell()) 

# seek function - used to seek the pointer backward or forward
# f3.seek(0)
# print(f3.readline())
# f3.seek(0)
# print(f3.readline())

# data = f3.read()
# print(type(data))
# print(data.index('Deepak'))
# f3.seek(104)
# print(f3.readline())
# f3.seek(data.index('Deepak') + 4)
# print(f3.readline())
# f3.seek(12)
# print(f3.readline())
# f3.seek(40)
# print(f3.readline())

# f3.close()

# with open("myIntro.txt", "r") as f:
#     data = f.read()
#     print(data)

# print(f.read())

with open("office.jpg", "rb") as f2:
    # print(f2.read())
    image_data = f2.read()


with open("newImage.jpg", "wb") as f3:
    f3.write(image_data)