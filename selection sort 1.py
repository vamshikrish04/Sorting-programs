n=eval(input())
lst=[]
for i in range(0,n):
    ele=eval(input('enter a number'))
    lst+=[ele]
print("before sorting : ",lst)
for i in range(len(lst)):
    mi=i
    for j in range(i+1, len(lst)):
        if lst[mi]>lst[j]:
            mi=j
            lst[i],lst[mi]=lst[mi],lst[i]
print('after sorting : ',lst)
