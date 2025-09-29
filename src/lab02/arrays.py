#1
def min_max(mns_mxs):
    mns_mxs = []
    if len(mns_mxs) != 0:
        return tuple([min(mns_mxs), max(mns_mxs)])
    else:
        raise ValueError
print(min_max([]))