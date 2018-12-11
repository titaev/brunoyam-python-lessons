import _pickle as pickle, json, yaml

from main import *

f11, f12, f13, f2, f3 = (open("test1.pk", "wb"), open("test2.pk", "wb"), open("test3.pk", "wb"),
                         open("test.json", "w"), open("test.yml", "w"))

pickle.dump(obj=Class, file=f11, protocol=2)
f11.close()
pickle.dump(obj=obj, file=f12, protocol=2)
f12.close()
pickle.dump(obj=dictionary, file=f13, protocol=2)
f13.close()

json.dump(dictionary, f2, indent=4)
f2.close()
yaml.dump(dictionary, f3)
f3.close()
