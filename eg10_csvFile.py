import csv

with open("test.csv", "w") as f:
    w=csv.writer(f,delimiter=",")
    w.writerow(["one", "tow", "three"])
    w.writerow(["four", "five", "six"])
# one	tow	  three	
# four	five  six


with open("test.csv", "r") as f:
    r=csv.reader(f, delimiter=",")
    # print(r)
    for row in r:
        if r is None or r =="":
            continue
        print(",".join(row))

# one,tow,three
# four,five,six
