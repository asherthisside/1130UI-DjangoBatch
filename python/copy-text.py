f = open("myIntro.txt", "r")
# data = f.read()
# # print(data)

# f.close()

f1 = open("copy.txt", "w")
# f1.write(data)

for line in f.readlines():
    # print(line)
    f1.write(line)
