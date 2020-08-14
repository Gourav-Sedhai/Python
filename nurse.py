def work(a,b,c,d,e,f,leng):
    total = float(a+b+c+d+e+f)
    avg = (total / leng)

    return avg

NH = 8
NP = 10
NC = 9
NG = 8
NMC = 7
NM = 12
count = 6

avg = work(NH, NP, NC, NG, NMC, NM, count)
print(avg)