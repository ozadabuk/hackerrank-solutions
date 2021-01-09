import itertools as it
u = "ABCD 3"
#u = "HACK 2"
a = u.split(" ")
s = a[0]
k = int(a[1])
l = [''.join(sorted(y)) for i in range(k) for y in it.combinations(s, i+1)]
m = sorted(l, key=lambda x:(len(x), x))
[print(x) for x in m]