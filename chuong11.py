#11.1
""" 
độ dài danh sách a là 3
độ dài danh sách b là 2
độ dài danh sách c là 0
độ dài danh sách d là 2
"""


#11.2
teams = [['Steven', 'Neena', 'Lex', 'Alexander', 'Bruce'], ['David', 'Jack', 'Bill', 'Tom', 'Mike'], ['Alexander', 'Adam', 'Payam', 'Kevin', 'Sigal', 'Mike']]
print(teams[2][1])



#11.3
List_of_animals =  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo'] 
n = input(" I want to find")
print("List of animals :  ['ant', 'bear', 'cat', 'dog', 'elephant', 'fish', 'goat', 'hippo']")
print("Number of animals",len(List_of_animals))
if n in List_of_animals:
    print("There is ",n,"list of animals")
else:
    print("There isn't ",n,"list of animals")



#11.5
list=[]
x=int(input("Nhập giá trị:"))
list.append(x)
i=1
while i==1:
          y=int(input("Tiếp tục nhập giá trị? 1:Có, 0:Không"))
          if y==1:
                  x=int(input("Nhập giá trị:"))
                  list.append(x)
          elif y==0:
                  break
print("list:",list)
sum=0
for num in list:
        sum+=num
print("Tổng các giá trị trong list:",sum)
x=int(input("Nhập giá trị cần tìm:"))
find = x in list
if find=="True":
        print(x,"xuất hiện",list.count(x),"lần trong list")
for i in list:
        if i>x:
          print(x,"không lớn hơn tất cả các số trong list")
          break
new_list=[]
for i in list:
        if i>x:
               new_list.append(i)
print("Các số lớn hơn",x,"trong list:",new_list)   




#11.4
list = []
while True:
  value = int(input("Nhập giá trị: "))
  list.append(value)
  choice = int(input("Tiếp tục nhập giá trị? 1: Có, 0: Không "))
  if choice == 0:
    break
print("List: ", list)
total = sum(list)
print("Tổng các giá trị trong list: ", total)
x = int(input("Nhập vào giá trị cần tìm x: "))
if x in list:
  count = list.count(x)
  print("{} xuất hiện {} lần trong list".format(x, count))
else:
  print("{} không xuất hiện trong list".format(x))
if x > max(list):
  print("{} lớn hơn tất cả các số trong list".format(x))
else:
  print("{} không lớn hơn tất cả các số trong list".format(x))
  greater_list = [num for num in list if num > x]
  print("Các số lớn hơn {} trong list: {}".format(x, greater_list))


#11.8   
def has_lucky_number(nums):
  for num in nums:
    if num % 7 == 0:
      return True
  return False
nums = [2, 6, 7, 9]
print(has_lucky_number(nums))