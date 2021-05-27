def maxEntry(d):
    d3={}
    a = max(list(d.values()))
    for key, val in d.items():
        if a==val:
            d3[key]=val
    return d3

    
if __name__=='__main__':
    n=int(input())
    d1=dict()
    d2=dict()
    for _ in range(n):
        k=input('user id\n')
        v1=input('user name\n')
        v2=int(input('user score\n'))
        d1[k]=v1
        d2[k]=v2
    r=maxEntry(d2)
    print(r)