from linked_list import Node, LinkedList
from blossom_lib import flower_definitions


class HashMap:
    # define constructor
    def __init__(self, array_size):
        self.array_size = array_size
        # default way using list
        # self.array = [None for i in range(self.array_size)]
        # using Linked List here
        self.array = [LinkedList() for i in range(self.array_size)]

    # hash function to get hash value
    def hash(self, key):
        key_codes = key.encode()
        hash_value = sum(key_codes)
        return hash_value

    # use compress function to get what should be the index or hash value
    def compress(self, hash_code):
        return hash_code % self.array_size

    def assign(self, key, value):
        array_index = self.compress(self.hash(key))
        # in case without collision
        # self.array[array_index] = value

        # in case of Separate chaining + Saving key
        # self.array[array_index] = [key, value]

        # using Separate chaining here in context of self.array =  Linked list
        payload = Node([key, value])
        # need to check if the key exists in the LinkedList before we add our new payload to it.
        list_at_array = self.array[array_index]
        for i in list_at_array:
            if i[0] == key:
                i[1] = value
        list_at_array.insert(payload)

    def retrieve(self, key):
        array_index = self.compress(self.hash(key))
        # here payload must have key,value as expected or nothing
        # payload = self.array[array_index]
        # if payload != None:
        #   if payload[0] == key:
        #     return payload[1]
        #   else:
        #     return None
        # else:
        #   return

        # using linkedlist approach
        list_at_index = self.array[array_index]
        for i in list_at_index:
            if i[0] == key:
                return i[1]
        else:
            return


blossom = HashMap(len(flower_definitions))
for each in flower_definitions:
    blossom.assign(each[0], each[1])
blossom.retrieve('daisy')





