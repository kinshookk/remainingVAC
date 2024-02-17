s=input()
def check(s):
    dicttt={'z':0,'o':0}
    for element in s:
        if element=='z':
            dicttt['z']+=1
        if element=='o':
            dicttt['o']+=1
    if dicttt['o']==2*dicttt['z']:
        return "YES"
    else:
        return "NO"
print(check(s))