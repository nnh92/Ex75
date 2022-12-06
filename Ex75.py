def Print_List(s):
    s = s.split()
    for index, value in enumerate(s):
        print(index, value)

s = open('Ex75/Ex75.inp', 'r').read()

Print_List(s)