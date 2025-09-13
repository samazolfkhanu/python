dictionary = {
    "First":1,
    "Second":2,
    "Third":3,
    "Fourth":4,
    "Fifth":5,
    "Sixth":6,
}
dictionary["Fourth"]="Sama"
for value in dictionary.values():
    print(value)

print("____________________")

del dictionary["Second"]
for key,value in dictionary.items():
    print(key,":", value)

print("____________________")

dictionary["Last"]="last"
for key in dictionary.keys():
    print(key)

print("____________________")

dictionary.update({"Last":"first"})
for key,value in dictionary.items():
    print(key,":", value)