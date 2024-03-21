# from collections import Counter 
# a = "aaaavvvvffff"
# my_counter = Counter(a)
# print(my_counter)
# print(my_counter.items())
# print(my_counter.values())
# print(list(my_counter.elements()))
# print(my_counter.most_common(2))
# print(my_counter.most_common(2)[0])
# print(my_counter.most_common(2)[0][0])

# from collections import namedtuple
# Point = namedtuple('Point', 'x,y')
# pt = Point(4, -9)
# print(pt)
# print(pt.x, pt.y)

# from collections import OrderedDict
# order_dict = OrderedDict()
# order_dict['b'] = 4
# order_dict['c'] = 3
# order_dict['d'] = 2
# order_dict['a'] = 1
# print(order_dict)

from collections import deque
d= deque()
d.append(5)
d.appendleft(8)
d.append(7)
print(d)
d.pop()
print(d)





