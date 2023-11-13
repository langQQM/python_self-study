import os
file_path=os.path.join("user","bob", "st.txt")
print("file_path:"+file_path)
#output:
#file_path:user\bob\st.txt

st=open("st.txt","w")
st.write("Hi from python")
st.close()

# write
with open("st2.txt","w") as f:
    f.write("Hi from python!")
    f.write("\n")
    f.write("abcdef")

# read
with open("st2.txt", "r") as f:
    print(f.read())
# Hi from python!
# abcdef

my_list=list()
with open("st2.txt", "r") as f:
    my_list.append(f.read())
print(my_list)
# ['Hi from python!\nabcdef']

my_list2=list()
with open("st2.txt", "r") as f:
    ctx=f.readline()
    while ctx is not None and ctx !="":
        my_list2.append(ctx)
        ctx=f.readline()

print(my_list2)
# ['Hi from python!\n', 'abcdef']