# a = 35
# b = 55
# c = 55
# # if a > b and a< c :
# #     print("second biggeest", a)
# # elif b > a and b <c:
# #     print( "second biggeest", b)
# # else:
# #     print("second biggeest", c)

# maxNum = max(a,b,c)
# minNum = min(a,b,c)
# second_max =  a+b+c - maxNum + minNum



#
n = 145
digit = 0
li= []
sumFact = 0
fact = 1

while n>=1:
  digit = n%10
  n = n//10
  li.append(digit)

for num in li:
  for i in range(1, num+1):
    fact = fact


