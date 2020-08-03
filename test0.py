from collections import OrderedDict

class DefaultListOrderedDict(OrderedDict):
    def __missing__(self,k):
        self[k] = []
        return self[k]

keys=['label', 'value']
vals1=['Grocery','Gas','Eatign Out']
dic = DefaultListOrderedDict()
for i,key in enumerate(keys):
    dic[key].append(vals1[i])

print(dic)
