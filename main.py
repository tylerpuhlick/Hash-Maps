from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    def __init__(self, size):
        self.array_size = size
        self.array = [LinkedList() for number in range(size)]

    def hash(self, key):
        return sum(key.encode())

    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        payload = Node([key, value])
        list_at_array = self.array[array_index]
        list_at_array.insert(payload)

        for keys in list_at_array:
            if key == keys[0]:
                keys[1] = value

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        list_at_index = self.array[array_index]
        for items in list_at_index:
            if items[0] == key:
                return items[1]
            else:
                return None


blossom = HashMap(len(flower_definitions))

for elements in flower_definitions:
    blossom.assign(elements[0], elements[1])

print(blossom.retrieve("sunflower"))
