total_mark=int(input('Your mark:'))
if total_mark>=80 and total_mark<=100:
    print('Grade-A')
elif total_mark>=60 and total_mark<80:
    print('Grade-B')
elif total_mark>=40 and total_mark<60:
    print('Grade-C')
else:
    print('Fail')