s_hrs=[12,1,2,3,4,5,6,7,8,9,10,11]
m_hrs=int(input('Put your hour:'))
a=s_hrs[m_hrs%12]
if m_hrs>=12 and m_hrs<24:
    print(a,'PM')
else:
    print(a,'AM')