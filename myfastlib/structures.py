class FastList:
def __init__(self, items=None):
self.data = items or []


def append(self, x):
self.data += [x]


def extend(self, xs):
self.data += xs


def sum(self):
return sum(self.data)


def __iter__(self):
return iter(self.data)


def __repr__(self):
return f"FastList({self.data})"
