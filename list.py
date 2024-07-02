fruits={
"fruit1":"rasberry","fruit2":"blueberry","fruit3":"blackberry","fruit4":"gooseberry","fruit5":"pomelo"
}
#printing the dictionary
print(fruits)
#printing the keys and values
print(fruits.keys())
#accessing the values
print(fruits["fruit2"])
#changing the values
fruits["fruit5"]="guava"
print(fruits)
#add a key-value pair
fruits["fruit6"]="oranges"
print(fruits)
#deleting keyes with values
del(fruits["fruit6"])
print(fruits)
#finding values
for i in fruits:
    if fruits[i]=="guava":
        print("found guava")
    else:
        print("guava not found")
#searching for a value
search=input("enter fruit number")
print(fruits["fruit"+search])
