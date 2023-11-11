author="Kafka"
print(author[2])
print(author[-1])

print("way"*3)

print("We hold these truths.".upper())
print("GO AWAY.".lower())
print("four score and ...".capitalize())


# 格式化
author="William"
born="1897"
print("{} was born in {}.".format(author, born))

str="I jumped over the puddle. It was 12 feet!"
print(str.split("."))
for item in str.split("."):
    print(item)


first_three="abc"
result="+".join(first_three)
print(result)
print(" ".join(first_three))

s="     The dog   "
print(s)
print(s.strip())

equ="All animal are equal."
equ=equ.replace("a","@")
print(equ)

print("Cat" in "Cat in the hat.")
print("Potter" not in "Harry")

print("she said \"Surely\"")
print("she said 'Surely'")
print('she said "Surely"')

print("line1\nline2\nline3")


fict=["Tol",
      "Camus",
      "Orwell",
      "Huxley"]
print(fict[0:2]) #半闭半开