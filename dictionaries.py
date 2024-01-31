#Ex 1
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(car.get("model"))

#Ex 2
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["year"] = 2020

#Ex 3
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car["color"]="red"

#Ex 4
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.pop("model")

#Ex 5
car =	{
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
car.clear()

#Examples:
thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.pop("model")
print(thisdict)


thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.popitem()
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
del thisdict["model"]
print(thisdict)

thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict.clear()
print(thisdict)



