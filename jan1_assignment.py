#assignment1
name=input('What is your name?')
num=int(input('Put a number:'))
if num<10:
    for item in range(num):
        print(name)
else:
    for j in range(3):
        print('Number is too high.')

#assignment2
total=0
for i in range(5):
    n=int(input('Put a number:'))
    ans=input("Do you want that number included? (y)es or (n)o:")
    if ans=='y':
        total+=n
print('Total result:',total)

#assignment3
up_d=input("Choose a direction 'Up' or 'Down' :")
if up_d=='Up':
    num=int(input('Maximum number: '))
    for i in range(1,num+1):
        print(i)
elif up_d=='Down':
    num=int(input('A number under 20: '))
    for i in range(20,num-1,-1):
        print(i)
else:
    print('I don\'t understand.')

#assignment4
amount=int(input('How many people do you want to invite?'))
if amount<10 and amount>0:
    for i in range(amount):
        name=input('What is the person\'s name?')
        print(f'{name} has been invited.')
elif amount>=10:
    print('Too many people.')
else:
    print('Stop this nonsense!')