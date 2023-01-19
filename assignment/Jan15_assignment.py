#Digit Counting
def num(digit):
  count=0
  for i in str(digit):
    count+=1
  return count
num(12345)

#Bigger Sum
def bigger_sum(a,b,c):
  empty=[]
  for i in a,b,c:
    empty.append(i)
  lar=max(empty)
  empty.remove(lar)
  sec_lar=max(empty)
  result=(lar**2)+(sec_lar**2)
  return result
bigger_sum(3,0,2)

#Leap Years
def is_leap_year(year):
  if year % 4==0 and (year % 400 ==0 or year%100!=0):
    return True
  else:
    return False
is_leap_year(2100)

#Area of Circle
import math 
def area_of_circle(radius):
  answer=math.pi * (radius ** 2)
  return answer
area_of_circle(3)


