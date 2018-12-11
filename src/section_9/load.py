import _pickle as pickle, json, yaml

f11, f12, f13, f2, f3 = (open("test1.pk", "rb"), open("test2.pk", "rb"), open("test3.pk", "rb"),
                         open("test.json", "r"), open("test.yml", "r"))

Class = pickle.load(f11)
f11.close()
print(Class)
obj = pickle.load(f12)
f12.close()
print(obj)
dictionary = pickle.load(f13)
f13.close()
print(dictionary)

dictionary = json.load(f2)
f2.close()
print(dictionary)
dictionary = yaml.load(f3)
f3.close()
print(dictionary)