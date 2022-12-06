def Day_Giam_Dan(s):
    KQ = all(s[i] >= s[i+1] for i in range(len(s)-1))
    return KQ

s = list(map(int, input('Nhap DS: ').split()))

print(Day_Giam_Dan(s))