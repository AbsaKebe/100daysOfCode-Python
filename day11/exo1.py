def reverse(i):
 length = len(i)
 inverse =i[length::-1]
 return inverse



L = ["omim", "m-etl", "toi"]
for i in L:
    print(reverse(i).upper())

