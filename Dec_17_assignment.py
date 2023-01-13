mark=int(input('How many mark did you get?'))
if mark>100 or mark<0:
    print('Don\'t talk nonsense!')
else:
    if mark==100:
        print('Excellent! Perfectly A')
    elif mark>=80 and mark<100:
        print('You got Grade A. Good job!')
    elif mark<80 and mark>=60:
        print('You got Grade B. Keep trying!')
    elif mark<=59 and mark>=40:
        print('You got C. Congrats, you passes the exam. Fighting!')
    elif mark<=39 and mark>=1:
        print('Sorry, dear..you didn\'t pass the exam. You got D.')
    if mark!=0:
        print('Be happy! You didn\'t get zero at least.')
    else:
        print('You got zero! Try to pass the exam next time!'.upper())