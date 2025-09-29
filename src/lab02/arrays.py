#1
# def min_max(mns_mxs):
#     if len(mns_mxs) != 0:
#         return print (tuple([min(mns_mxs), max(mns_mxs)]))
#     else:
#         raise ValueError
# min_max([1.5, 2, 2.0, -3.1])
#2
def unique_sorted(elements):
    elements = list(set(sorted(elements)))
    elements.sort(reverse=False)
    return elements
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))