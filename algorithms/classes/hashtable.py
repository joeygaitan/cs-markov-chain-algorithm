#!python

from linkedlist import LinkedList, Node


class HashTable(object):

    def __init__(self, init_size=8):
        """Initialize this hash table with the given initial size."""
        # Create a new list (used as fixed-size array) of empty linked lists
        self.buckets = [LinkedList() for _ in range(init_size)]

    def __str__(self):
        """Return a formatted string representation of this hash table."""
        items = ['{!r}: {!r}'.format(key, val) for key, val in self.items()]
        return '{' + ', '.join(items) + '}'

    def __repr__(self):
        """Return a string representation of this hash table."""
        return 'HashTable({!r})'.format(self.items())

    def _bucket_index(self, key):
        """Return the bucket index where the given key would be stored."""
        # Calculate the given key's hash code and transform into bucket index
        return hash(key) % len(self.buckets)

    def keys(self):
        """Return a list of all keys in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all keys in each bucket
        all_keys = []
        for bucket in self.buckets:
            for key, value in bucket.items():
                all_keys.append(key)
        return all_keys

    def values(self):
        """Return a list of all values in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Collect all values in each bucket
        value_list = []
        for ll in self.buckets:
            current = ll.head
            while(current):
                print(current.data)
                value_list.append(current.data[1])
                current = current.next
        return value_list

    def items(self):
        """Return a list of all items (key-value pairs) in this hash table.
        TODO: Running time: O(???) Why and under what conditions?"""
        # Collect all pairs of key-value entries in each bucket
        all_items = []
        for bucket in self.buckets:
            all_items.extend(bucket.items())
        return all_items

    def length(self):
        """Return the number of key-value entries by traversing its buckets.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all buckets
        # TODO: Count number of key-value entries in each bucket
        count = 0
        for ll in self.buckets:
            current = ll.head
            while(current):
                print(current.data)
                count += 1
                current = current.next
        return count

    def contains(self, key):
        """Return True if this hash table contains the given key, or False.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        for ll in self.buckets:
            current = ll.head
            while(current):
                if current.data[0] == key:
                    return True 
                current = current.next
        return False

    def get(self, key):
        """Return the value associated with the given key, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, return value associated with given key
        # TODO: Otherwise, raise error to tell user get failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_linkedlist = self.buckets[hash(key) % len(self.buckets)]
        current = bucket_linkedlist.head
        while(current):
            if current.data[0] == key:
                return current.data[1]
            current = current.next
        
        raise KeyError('Key not found: {}'.format(key))
        

    def set(self, key, value):
        """Insert or update the given key with its associated value.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, update value associated with given key
        # TODO: Otherwise, insert given key-value entry into bucket

        bucket_linkedlist = self.buckets[hash(key) % len(self.buckets)] #finds linked list bucket 
        new_item = (key,value) #make a tuple to store the information in
        current = bucket_linkedlist.head # linked list head so you loop through the list
        while(current): #loop condition
            if current.data[0] == new_item[0]: #checks if item is in linkedlist
                current.data = new_item #updates the item with the 
                return
            current = current.next
        bucket_linkedlist.append(new_item)
        

    def delete(self, key):
        """Delete the given key from this hash table, or raise KeyError.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Find bucket where given key belongs
        # TODO: Check if key-value entry exists in bucket
        # TODO: If found, delete entry associated with given key
        # TODO: Otherwise, raise error to tell user delete failed
        # Hint: raise KeyError('Key not found: {}'.format(key))
        bucket_linkedlist = self.buckets[hash(key) % len(self.buckets)] #find the index
        current = bucket_linkedlist.head #get the head so you can search through the linked list
        while(current): #loop through the linked list
            if current.data[0] == key: #if found then delete key and return to stop loop
                bucket_linkedlist.delete(key)
                return
            #otherwise it will keep looping to the end where it will through the keyError
            current = current.next
        raise KeyError(f'Key not found: {key}')
        

def test_hash_table():
    ht = HashTable()
    print('hash table: {}'.format(ht))

    print('\nTesting set:')
    for key, value in [('I', 1), ('V', 5), ('X', 10)]:
        print('set({!r}, {!r})'.format(key, value))
        ht.set(key, value)
        print('hash table: {}'.format(ht))

    print('\nTesting get:')
    for key in ['I', 'V', 'X']:
        value = ht.get(key)
        print('get({!r}): {!r}'.format(key, value))

    print('contains({!r}): {}'.format('X', ht.contains('X')))
    print('length: {}'.format(ht.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for key in ['I', 'V', 'X']:
            print('delete({!r})'.format(key))
            ht.delete(key)
            print('hash table: {}'.format(ht))

        print('contains(X): {}'.format(ht.contains('X')))
        print('length: {}'.format(ht.length()))


if __name__ == '__main__':
    # test_hash_table()
    ht = HashTable()
    ht.set('I', 1)
    ht.set('V', 5)
    ht.set('X', 10)
    print(ht.length())
    ht.delete('I')
    ht.delete('X')
    print(ht.values)
    print(ht.length())
    test_hash_table()