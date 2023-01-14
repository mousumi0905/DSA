#tuples
#creating tuples

tuple1= ('a','b','c')
print(tuple1)
#time complexity: O(1)
#Space complexity: O(n)
#accessing an element

print(tuple1[-1])
#time complexity: O(1)
#Space complexity: O(1)
#traversing 
for i in tuple1:
    print(i)
#time complexity: O(n)
#Space complexity: O(1)



#searching for an element

print('f' in tuple1)

def search(tuple,value):
    if value in tuple:
        return 'found'
    return 'not found'
search(tuple1,'a')

#time complexity: O(n)
#Space complexity: O(1)


# tuple methods
tuple1= ('a','b','c')
tuple2= ('e','f','g')
t=tuple1+tuple2
print(t)


tuple2= ('e','f','g')
t1=tuple2*4
print(t1)
print(t1.count('e'))
print(t1.index('e'))
print(max(tuple1))
print(min(tuple1))
a=[1,2,3,4,5]
print(tuple(a))  # need to solve this why tuple is not callable