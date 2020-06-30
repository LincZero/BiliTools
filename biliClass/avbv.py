# B站av号bv号互转
str58 = 'fZodR9XQDSUm21yCkr6zBqiveYah8bt4xsWpHnJE7jL5VG3guMTKNPAwcF'
dic58 = {}
for i in range(58):
    dic58[str58[i]] = i
s = [11, 10 ,3, 8, 4, 6]
xor = 177451812
add = 8728348608

def decode(x):  # bv > av
    r=0
    for i in range(6):
        r+=dic58[x[s[i]]]*58**i
    return (r-add)^xor
        
def encode(x):  # av > bv
    x=(x^xor)+add
    r=list('BV1  4 1 7  ')
    for i in range(6):
        r[s[i]]=str58[x//58**i%58]
    return ''.join(r)

# 测试用：
# print(dec('BV17x411w7KC'))
# print(dec('BV1Q541167Qg'))
# print(dec('BV1mK4y1C7Bz'))
# print(enc(170001))
# print(enc(455017605))
# print(enc(882584971))