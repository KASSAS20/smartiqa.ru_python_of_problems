# 1
d = dict()
# 2
d['A'] = 1
# 3
d[('B', 'C')] = [2, 3]
# 4
element_by_key = d[('B', 'C')]
# 5
d.pop('A')
# 6
keys = list(d.keys())