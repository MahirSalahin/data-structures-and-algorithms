class HashTable:
    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key):
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self):
        for i, val in enumerate(self.data_map):
            print(i, ':', val)

    def set_item(self, key, val):
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, val])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is None:
            return None
        for _key, val in self.data_map[index]:
            if _key == key:
                return val
        return None

    def keys(self):
        all_keys = []
        for i, row in enumerate(self.data_map):
            if not row:
                continue
            for key_val in row:
                all_keys.append(key_val[0])
        return all_keys


if __name__ == '__main__':
    my_hash_table = HashTable()

    my_hash_table.set_item('apple', 100)
    my_hash_table.set_item('orange', 150)
    my_hash_table.set_item('strawberry', 170)

    print(my_hash_table.keys())
