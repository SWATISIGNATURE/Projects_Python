"""
Hash Map :
    A key-value store that uses an array and a hashing function to save and retrieve values.
    Being a map means relating two pieces of information, but a map also has one further requirement.
    Key: The identifier given to a value for later retrieval.
    In order for a relationship to be a map, every key that is used can only be the key to a single value.
    we don’t really care about the exact sequence of the data. We only care that a given input, when fed into the map, gives the accurate output.
    An array uses indices to keep track of values in memory, so we’ll need a way of turning each key in our map to an index in our array.
Hash Function :
    Hash function: A function that takes some input and returns a number.
    Compression function: A function that transforms its inputs into some smaller range of possible outputs.
    hash function takes a string as input and returns an array index as output.
    The hash function will first compute a value using some scoring metric: this is the hash value, hash code, or just the hash. Our hash map implementation then takes that hash value mod the size of the array. This guarantees that the value returned by the hash function can be used as an index into the array we’re using.
    hash functions are also known as compression functions.
    The hashing is not a reversible process as it compresses the input into the hash value in range(array_index).
    Hash value calculation:
        => for string input:
        input = garnet
        hashed_into(['g', 'a', 'r', 'n', 'e', 't'])
        code point = ['103', '97', '114', '110', '101', '116']
        Hash_value = 641 (adding code points)
        => for integers like 641
    The storage location at the index given by a hash is called the hash bucket.
    Hash map performs modulo arithmetic to turn the hash into an array index. lets say array_size = 10
    array_index = 641 % 10

Collisions:
    Hash function might produce the same hash for two different keys known as hash collision.
    A hash collision is when a hash function returns the same index for two different keys.
    Strategy to resolve collisions:
        1. Separate Chaining:
            The user wants to assign a value to a key in the map.
            The hash map takes the key and transforms it into a hash code.
            The hash code is then converted into an index to an array using the modulus operation.
            If the value of the array at the hash function’s returned index is empty, a new linked list is created with the value as the first element of the linked list.
            If a linked list already exists at the address, append the value to the linked list given.
            But the retrieval becomes very time taking in O(n)

        2. Saving Key:
            In case of Separate chaining multiple keys can create confusion on retrieval.
            we save both the key and the value, then we will be able to check against the saved key when we’re accessing data in a hash map. By saving the key with the value, we can avoid situations in which two keys have the same hash code where we might not be able to distinguish which value goes with a given key.
            For each element, if the saved key is the same as our key, return the value. Otherwise, continue iterating through the list comparing the keys saved in that list with our key

        3. Open Addressing:
            Linear Probing:
            In open addressing we stick to the array as our underlying data structure, but we continue looking for a new index to save our data if the first result of our hash function has a different key’s data
            Probing means continuing to find new array indices in a fixed sequence until an empty index is found.
            Linear probing systems, could jump by five steps instead of one step.
            Quadratic probing
            we add increasingly large numbers to the hash code. At the first collision we just add 1, but if the hash collides there too we add 4 ,and the third time we add 9. Having a probe sequence change over time like this avoids clustering.
            Clustering : It happens when a single hash collision causes additional hash collisions.

All the output in form of Array index, key, value creates Hash Table.
"""

class HashMap:
  def __init__(self, array_size):
    self.array_size = array_size
    self.array = [None for item in range(array_size)]

  def hash(self, key, count_collisions=0):
    key_bytes = key.encode()
    hash_code = sum(key_bytes)
    return hash_code + count_collisions

  def compressor(self, hash_code):
    return hash_code % self.array_size

  def assign(self, key, value):
    array_index = self.compressor(self.hash(key))
    current_array_value = self.array[array_index]

    if current_array_value is None:
      self.array[array_index] = [key, value]
      return

    if current_array_value[0] == key:
      self.array[array_index] = [key, value]
      return

    # Collision!

    number_collisions = 1

    while(current_array_value[0] != key):
      new_hash_code = self.hash(key, number_collisions)
      new_array_index = self.compressor(new_hash_code)
      current_array_value = self.array[new_array_index]

      if current_array_value is None:
        self.array[new_array_index] = [key, value]
        return

      if current_array_value[0] == key:
        self.array[new_array_index] = [key, value]
        return

      number_collisions += 1

    return

  def retrieve(self, key):
    array_index = self.compressor(self.hash(key))
    possible_return_value = self.array[array_index]

    if possible_return_value is None:
      return None

    if possible_return_value[0] == key:
      return possible_return_value[1]

    retrieval_collisions = 1

    while (possible_return_value != key):
      new_hash_code = self.hash(key, retrieval_collisions)
      retrieving_array_index = self.compressor(new_hash_code)
      possible_return_value = self.array[retrieving_array_index]

      if possible_return_value is None:
        return None

      if possible_return_value[0] == key:
        return possible_return_value[1]

      retrieval_collisions += 1

    return

hash_map = HashMap(15)
hash_map.assign("gabbro","igneous")
hash_map.assign("sandstone","sedimentary")
hash_map.assign("gneiss","metamorphic")

print(hash_map.retrieve("gabbro"))
print(hash_map.retrieve("sandstone"))
print(hash_map.retrieve("gneiss"))
