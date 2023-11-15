# list
fruit=["Apple", "Orange", "Pear"]
fruit.append("Banana")
fruit.append("Peach")
print(fruit)

random=[]
random.append(True)
random.append(100)
random.append(1.1)
random.append("Hello")
print(random)

# pop方法移除列表最后一个元素
colors=["blue","green","yellow"]
print(colors)
item=colors.pop()
print(item)
print(colors)

color2=["orange","pink","black"]
print(colors+color2)

print("green" in colors)
print(len(colors))


# tuple
my_tuple=tuple()
print(my_tuple)

my_tuple2=()
print(my_tuple2)

rndm=("M.Jackson", 1958, True)
print(rndm)

print(rndm[0])


# dictionary
my_dict=dict()
print(my_dict)

my_dict2={}
print(my_dict2)

facts=dict()
facts["Bill"]="Gates"
print(facts["Bill"])

fruits={"Apple":"Red", "Banana":"Yellow"}
print(fruits)

bill=dict({"Bill Gates":"charitable"})
print("Bill Gates" in  bill)

books={"Dracula":"Stoker",
       "1984":"Orwell",
       "The Trial":"Kafka"}
del books["1984"]
print(books)


# 容器嵌套
lists=[]
rap=["Kanye West",
     "Jay Z",
     "Eminem",
     "Nas"]
rock=["Bob Dylan",
      "The Beatles",
      "Led Zeppelin"]
djs=["Zeds Dead",
     "Tiesto"]

lists.append(rap)
lists.append(rock)
lists.append(djs)
# lists.append(djs)
print(lists)
print(lists[1])

ny={"locations":(40.7128,
                 74.0059),
    "celebs":["W. Allen",
              "Jay Z",
              "K. Bacon"],
    "facts":{"state":"NY",
             "country":"America"
    }
}
print(ny)










