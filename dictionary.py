#creating a dictionary
my_DICT=dict()
print(my_DICT)
se_di={1:"one",2:"two"}

#adding/updating value
se_di[1]="uno"
print(se_di)
se_di[7]="seven"
print(se_di)
#time complexity= O(1)
#space complexity=O(n) as we need to search for the 
# key and amortized O(1)for adding

# traverse through dictionary
def traverse(dict):
    for key in dict:
        print(key,dict[key])
traverse(se_di)
# time complexity: O(n)
#space complexity: O(1)


# search for an element in dictionary
def search(dict,value):
    for key in dict:
        if dict[key]==value:
           return key,value
    return 'The value does not exists'
search(se_di,"uno")

# time complexity: O(n)
#space complexity: O(1)

# delete an element in dictionary

# for deleting all element: dict.clear()
se_di.pop(1)
print(se_di)


#methods
mydict={}.fromkeys([1,3,4],['one'])
print(mydict)
print(se_di.items())
print(se_di.keys())