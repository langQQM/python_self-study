shows=["Apple", "Peach", "Watermelon"]
for show in shows:
    print(show)

# continue
for i in range(1,6):
    if i==3:
        continue
    print(i)

# break
for j in range(0,100):
    print(j)
    break

# while example01
qs=["what is your name?",
    "what is your fav. color?",
    "what is your quest?"]
n=0
while True:
    print("type q to quit")
    a=input(qs[n])
    if a=="q":
        break
    n=(n+1)%len(qs)

# while example02
while input("y or n?")!="n":
    for i in range(1,6):
        print(i)
