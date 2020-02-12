### 1. lambda를 이용해 정렬
_list = [{'name': 'Hong', 'age': 10}, {'name': 'Lee', 'age': 39}]

new_list = sorted(_list, key=lambda k: k['name'])

print(new_list)

### 2-1.itemgetter를 이용해 정렬
from operator import itemgetter

new_list1 = sorted(_list, key=itemgetter('name'))
print(new_list1)

### 2-2.reverse
new_list2 = sorted(_list, key=itemgetter('name'), reverse=True)
print(new_list2)
