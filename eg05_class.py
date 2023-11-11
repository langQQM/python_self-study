class Data:
    def __init__(self) -> None:
        self.nums=[1,2,3,4,5]
    
    def change_data(self,index,n):
        self.nums[index]=n

    def __repr__(self) -> str:
        res=""
        for item in self.nums:
            res+=","+str(item)
        return "nums="+res[1:]
    

data_one=Data()
data_one.nums[0]=100
print(data_one.nums)

data_two=Data()
data_two.change_data(0,200)
print(data_two.nums)

data_three=Data()
data_three.change_data(1,200)
print(data_three)

print(data_one is data_one)
print(data_one is data_two)


class Positive:
    
    def __init__(self,number) -> None:
        self.num=number
    # 魔法方法 
    def __add__(self, other):
        return abs(self.num+other.num)

x=Positive(-20)
y=Positive(10)
print(x+y)
