class MyList:
    def __init__(self) -> None:
        self._list = []

    def __repr__(self):
        return f"MyList({self._list})"

    def __len__(self):
        return len(self._list)

    def __getitem__(self, index):
        return self._list[index]
    
    def __setitem__(self, index, value):
        self._list[index] = value

    def append(self, element):
        self._list.append(element)

elements = MyList()

elements.append(1)
elements.append(2)

print(len(elements))
print(elements[0])
elements[0] = 100
print(elements)


