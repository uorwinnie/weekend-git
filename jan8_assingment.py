#Guess the number
import random
r=random.randint(1,99)
while 1:
  guess=int(input('Guess a number between 0 and 100 : '))
  if guess<r:
    print('Too low')
  elif guess>r:
    print('Too high')
  else:
    print('Correct!')
    break

#Summing numbers from a list
result=0
list=[1,2,3,4,5,6,7,8]
for i in list:
    result+=i
print(result)

#Secret Language conversion
vocab=input('Write down something : ')
vowel=['a','e','i','o','u']
f=vocab[0]
if f in vowel:
  print(vocab+'way')
else:
  print(vocab[1:]+vocab[0]+'ay')

#[First, Last] list
mylist = [1,2,3,4,5]
mylist2 = ['a','b','c','d']
print([mylist[0],mylist[-1]])
print([mylist2[0],mylist2[-1]])

#Hobbies list
hobby=['Cooking','Travelling']
user=input('What is your fav hobby?')
hobby.append(user.title())
hobby.sort()
print(hobby)

#Delete unfavorite subjects
sub=['Myanmar','English','Mathematics','Chemistry','Physics','Biology']
print(sub)
dislike=input('Subject you don\'t like : ')
del sub[sub.index(dislike)]
print(sub)