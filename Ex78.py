def List_PT_Le(s):
    ds = [i for i in s if i%2 != 0]
    return ds

s = map(int,input('Nhap DS: ').split())

print(List_PT_Le(s))
