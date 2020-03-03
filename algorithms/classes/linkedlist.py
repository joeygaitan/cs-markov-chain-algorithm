#!python


class Node(object):

    def __init__(self, data=None, next=None):
        """Initialize this node with the given data."""
        self.data = data
        self.next = next

    def __repr__(self):
        """Return a string representation of this node."""
        return 'Node({!r})'.format(self.data)


class LinkedList(object):

    def __init__(self, items=None):
        """Initialize this linked list and append the given items, if any."""
        self.head = None  # First node
        self.tail = None  # Last node
        self.list = []
        # Append given items
        if items is not None:
            for item in items:
                self.append(item)
                self.list.append(item)

    def __str__(self):
        """Return a formatted string representation of this linked list."""
        items = ['({!r})'.format(item) for item in self.items()]
        return '[{}]'.format(' -> '.join(items))

    def __repr__(self):
        """Return a string representation of this linked list."""
        return 'LinkedList({!r})'.format(self.items())

    def items(self):
        """Return a list (dynamic array) of all items in this linked list.
        Best and worst case running time: O(n) for n items in the list (length)
        because we always need to loop through all n nodes to get each item."""
        items = []  # O(1) time to create empty list
        # Start at head node
        node = self.head  # O(1) time to assign new variable
        # Loop until node is None, which is one node too far past tail
        while node is not None:  # Always n iterations because no early return
            items.append(node.data)  # O(1) time (on average) to append to list
            # Skip to next node to advance forward in linked list
            node = node.next  # O(1) time to reassign variable
        # Now list contains items from all nodes
        return items  # O(1) time to return list

    def is_empty(self):
        """Return a boolean indicating whether this linked list is empty."""
        return self.head is None

    def length(self):
        """Return the length of this linked list by traversing its nodes.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes and count one for each
        current = self.head
        count = 0
        if current == None:
            return 0
        while(current):
            count += 1
            current = current.next
        return count


    def append(self, item):
        """Insert the given item at the tail of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Append node after tail, if it exists
        current = self.head
        newItem = Node(item)
        if self.head == None:
            self.head = newItem
            self.tail = newItem
        else:
            while(current.next != None):
                current = current.next
            current.next = newItem
            self.tail = newItem


    def prepend(self, item):
        """Insert the given item at the head of this linked list.
        TODO: Running time: O(???) Why and under what conditions?"""
        # TODO: Create new node to hold given item
        # TODO: Prepend node before head, if it exists
        current = self.head
        if current == None:
            self.head = Node(item, self.head)
            self.tail = Node(item)
        else:
            self.head = Node(item, self.head)

    def find(self, quality):
        """Return an item from this linked list satisfying the given quality.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find item where quality(item) is True
        # TODO: Check if node's data satisfies given quality function
        current = self.head

        if current.data == quality:
            return current.data
        else:
            while(current):
                if current.data == quality:
                    return current.data
                current = current.next
            return None

    def delete(self, item):
        """Delete the given item from this linked list, or raise ValueError.
        TODO: Best case running time: O(???) Why and under what conditions?
        TODO: Worst case running time: O(???) Why and under what conditions?"""
        # TODO: Loop through all nodes to find one whose data matches given item
        # TODO: Update previous node to skip around node with matching data
        # TODO: Otherwise raise error to tell user that delete has failed
        # Hint: raise ValueError('Item not found: {}'.format(item))
        if self.head == None:
            raise ValueError(f'Item not found: {item}')
            return
        current = self.head
        if current.data == item:
            self.head = current.next
            if current.next == None:
                self.tail = None
            return
        while (current):
            if current.data == item:
                break
            prev = current
            current = current.next

        if current == None:
            if item in self.list:
                raise ValueError(f'{item} no longer in list')
                return 'Item no longer in list'
            else:
                raise ValueError(f'{item} not found in list')
                return 'Item not in list'

        prev.next = current.next
        self.tail = prev
        current = None
        

    def print_list(self):
        current = self.head
        while(current):
            print(current.data)
            current = current.next
        print(f"head: {self.head}, tail: {self.tail}")
        print(self.list)
        

def test_linked_list():
    ll = LinkedList()
    print('list: {}'.format(ll))

    print('\nTesting append:')
    for item in ['A', 'B', 'C']:
        print('append({!r})'.format(item))
        ll.append(item)
        print('list: {}'.format(ll))

    print('head: {}'.format(ll.head))
    print('tail: {}'.format(ll.tail))
    print('length: {}'.format(ll.length()))

    # Enable this after implementing delete method
    delete_implemented = False
    if delete_implemented:
        print('\nTesting delete:')
        for item in ['B', 'C', 'A']:
            print('delete({!r})'.format(item))
            ll.delete(item)
            print('list: {}'.format(ll))

        print('head: {}'.format(ll.head))
        print('tail: {}'.format(ll.tail))
        print('length: {}'.format(ll.length()))

# ll = LinkedList(['A','B','C','D','E'])
# ll.delete('A')
# ll.delete('C')
# ll.delete('E')
# ll.print_list()
# print(ll.tail.data)


if __name__ == '__main__':
    test_linked_list()