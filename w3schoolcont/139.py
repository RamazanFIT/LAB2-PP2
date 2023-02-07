thisdict = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
thisdict["year"] = 2018
thisdict.update({"year":2023})
thisdict.update(dict(model = 34))
thisdict.update(brand = 23)
print(thisdict)