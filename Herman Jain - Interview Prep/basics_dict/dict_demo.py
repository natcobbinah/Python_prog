dict = {}
dict = {
    "donald": "duck",
    "micky": "mouse",
}
print(dict["donald"])
#print(dict["goofy"]) #KeyError
del dict["micky"]
print(dict)
dict["goofy"] = "man"
print(dict)
print(dict.keys())
print(dict.values())
print(dict.items())
print(dict.get("donald"))
print(dict.get("ploto"))