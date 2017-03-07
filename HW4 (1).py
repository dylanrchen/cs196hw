
# coding: utf-8

# # CS 196 Spring 2017 Homework 4

# # Table of Contents
# ---
# 1. [Node Class](#Node-Class)
# 3. [List to Linked List](#List-to-Linked-List)
# 4. [Linked List to List](#Linked-List-to-List)
# 5. [Reversed Linked List](#Reversed-Linked-List)
# 5. [Find nth element](#Find-nth-element)
# 6. [Cycle Detection](#Cycle-Detection)
# 7. [Replace Node](#Replace-Node)

# # Node Class #
# ---
# 
# You are allowed to modify the class as much as you like, except the `self.data` and `self.next` parameters. Our tests depend on `self.data` containing data, and `self.next` containing the next node, so failure to do so will result in an automatic 0.
# 
# You can add methods as much as you'd like, for example, it might be helpful to write a function that gets you the nth element in a linked list!
# 

# In[74]:

class Node(object):
    def __init__(self, data=None, next_node=None, boo=True):
        """
        Initializes Node in Linked List.
        """
        self.data = data
        self.next = next_node
        self.boo=boo


    def __str__(self):
        """
        Converts current linked list to a string.
        """
        node = self
        buffer = str(node.data)

        node = node.next
        while node != None:
            buffer += ' -> ' + str(node.data)
            node = node.next
        return buffer


# We've provided an interface to print your functions. You can use `print(node)` to print out the entire linked list, starting from node. Here are examples (which you can run) to show it off.

# In[75]:

print("Linked List with only one element")
linked_list = Node(1)
print(linked_list)

print("Linked List with two elements")
next_node = Node(2)
linked_list.next = next_node
print(linked_list)

print("Linked List with three elements.")
next_node.next = Node(4) # Notice that linked_list.next.next is the same as next_node.next
print(linked_list)

print("Printing an intermediary linked list")
print(next_node)

print("Linked List with many types of elements")
linked_list.next.next.next = Node(10)
linked_list.next.next.next.next = Node(['we', 'can', 'store', 'other', 'objects'])
linked_list.next.next.next.next.next = Node("Second to last")
linked_list.next.next.next.next.next.next = Node("last")
print(linked_list)


# # List to Linked List
# ---
# Given a normal list, convert it into a linked list, with the first index as the head. RETURN the head node.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `[1, 2, 5, 7]`:
# 
#     * Output: 
#         * `(head)1 -> 2 -> 5 -> 7`
#   
# * Example 2:
#     * Input: 
#         * `[3, 4, 0, 9]`
# 
#     * Output: 
#         * `(head)3 -> 4 -> 0 -> 9`
#   
# ## Parameters
# -----------
# * `list` : `norm`
#     - The list to be turned into a linked list
# 
# 
# ## Returns
# -------
# * `Node`: Head of the resultant linked list
# 

# In[76]:

def list_to_linked_list(norm):
    length=len(norm)
    head=Node(norm[0])
    ptr=head
    for i in range(1,length):
        ptr.next=Node(norm[i])
        ptr=ptr.next
    return head


# In[77]:

def test_list_to_linked_list():
    assert (list_to_linked_list([1, 2, 5, 7]).data == 1)
    assert (list_to_linked_list([1, 2, 5, 7]).next.data == 2)
    assert (list_to_linked_list([1, 2, 5, 7]).next.next.data == 5)
    assert (list_to_linked_list([1, 2, 5, 7]).next.next.next.data == 7)
    


# In[78]:

list_to_linked_list([1, 2, 5, 7]).next.data


# # Linked List to List
# ---
# Given a head node, RETURN the linked list from head to tail as a normal list
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `1 -> 2 -> 5 -> 7`:
# 
#     * Output: 
#         * `[1, 2, 5, 7]`
#   
# * Example 2:
#     * Input: 
#         * `3 -> 4 -> 0 -> 9`
# 
#     * Output: 
#         * `[3, 4, 0, 9]`
#   
# ## Parameters
# -----------
# * `Node` : `head`
#     - The head of the linked list to be made into a normal list
# 
# 
# ## Returns
# -------
# * `list`: The resulting list

# In[79]:

def linked_list_to_list(head):
    a=[]
    a.append(head.data)
    while head.next!=None:
        head=head.next
        a.append(head.data)
    return a
    pass


# In[80]:

def test_linked_list_to_list():
    # make the linked list
    head = Node(1,None)
    pointer = head
    head.next = Node(2,None)
    head = head.next
    head.next = Node(5, None)
    head = head.next
    head.next = Node(7, None) 
    assert(linked_list_to_list(pointer) == [1, 2, 5, 7])
   


# In[81]:

test_linked_list_to_list()


# # Reversed Linked List
# ---
# Given a linked list node, RETURN the same linked list but reversed.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `1 -> 2 -> 3`:
# 
#     * Output: 
#         * `3 -> 2 -> 1`
#   
# * Example 2:
#     * Input: 
#         * `5 -> 4 -> 3`
# 
#     * Output: 
#         * `3 -> 4 -> 5`
#   
# ## Parameters
# -----------
# * `Node` : `head`
#     - The head of the linked list to be made into a normal list
# 
# 
# ## Returns
# -------
# * `Node`: The resulting linked list

# In[82]:

def reverse_linked_list(head):
    a=[]
    a.append(head.data)
    while head.next!=None:
        head=head.next
        a.append(head.data)
    b=[None]*len(a)
    for i in range(0,len(a)):
        b[i]=a[len(a)-i-1]
    headb=Node(b[0])
    ptr=headb
    for i in range(1,len(b)):
        ptr.next=Node(b[i])
        ptr=ptr.next
    return headb
    pass


# In[83]:

def test_reverse_linked_list():
    
    linked = reverse_linked_list(Node(1, Node(2, Node(3, None))))
    assert linked.data == 3
    assert linked.next.data == 2
    assert linked.next.next.data == 1


# In[84]:

test_reverse_linked_list()


# # Find nth element
# ---
# Given a linked list node, return the data in the nth node
# 
# ## Restriction(s):
# * n will always be less than the lenght of the linked list
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `1 -> 2 -> 3 -> 4`,`2`
# 
#     * Output: 
#         * `3`
#   
# * Example 2:
#     * Input: 
#         * `5 -> 4 -> 3 -> 100`, `3` 
# 
#     * Output: 
#         * `100`
#   
# ## Parameters
# -----------
# * `Node` : `head`
#     - The head of the linked list to be made into a normal list
# * `int` : n
#     - The index of the element you need to find
# 
# 
# ## Returns
# -------
# * `int`: the data of the nth element

# In[85]:

def find_nth(head,n):
    a=[]
    a.append(head.data)
    while head.next!=None:
        head=head.next
        a.append(head.data)
    return a[n]
    pass


# In[86]:

def test_find_nth():
    head = Node(1,Node(2,Node(3,Node(4,None))))
    assert find_nth(head,2) == 3


# In[87]:

test_find_nth()


# # Cycle Detection
# ---
# Some linked lists do not want to play nice.
# A normal linked list looks like this
# 
# $$1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5$$
# 
# But there could be a cycle so that the linked list never terminates!
# 
# $$1 \rightarrow 2 \rightarrow 3 \rightarrow 4 \rightarrow 5 \rightarrow 1 \rightarrow 2 \rightarrow 3 ...$$
# 
# So there is a cycle that hits the first node, second node, third node, fourth node, fifth node, then back to first node, second node... and so on.
# 
# Given a linked list, determine if there is such cycle.
# 
# ## Restriction(s):
# * The data points are not unique.
# * There can be many linked lists (less than 1000000).
# * Your solution must be able to detect a cycle in less than 10 seconds.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `1 -> 2 -> 3 -> 4` cycles back to `1 -> 2 -> ...`
# 
#     * Output: 
#         * `True`
#   
# * Example 2:
#     * Input: 
#         * `5 -> 4 -> 3 -> 100` 
# 
#     * Output: 
#         * `False`
#   
# ## Parameters
# -----------
# * `Node` : `head`
#     - The head of the linked list
# 
# ## Returns
# -------
# * `bool`: `True` if the linked list contains a cycle. `False` otherwise.

# In[88]:

def cycle_detection(head):
    a=True
    while head.next!=None and a==True:
        head.boo=False
        head=head.next
        if head.boo==False:
            a=False
    b=(not a)
    return b
    """
    Given a linked list, find if there is a cycle in the linked list
    """
    pass


# In[89]:

def test_cycle_detection():
    head = Node(1,Node(2,Node(3,None)))
    tail = Node(4, head)
    head.next.next.next = tail
    # Watchout, you can't print the head because there's an infinite loop!
    assert cycle_detection(head)

    head = Node(3,Node(4,Node(5,Node(100,None))))
    assert not cycle_detection(head)


# In[90]:

test_cycle_detection()


# # Replace Node
# ---
# Given a linked list with a starting sentinel node (i.e. an empty fixed node that should remain the head of the linked list), replace the data at all nodes with data `n` with the data `k`.
# 
# ## Restriction(s):
# * The number of nodes in the linked list will always be greater than one
# * The final node in the linked list will have a "next" attribute of None
# * There will be no cycles in the linked list.
# * In the trivial case where no elements need to be replaced, return the linked list as-is.
# 
# ## Example(s):
# ---
# * Example 1:
#     * Input: 
#         * `1 -> 2 -> 3 -> 4`, `2`, `5`
# 
#     * Output: 
#         * `1 -> 5 -> 3 -> 4`
#   
# * Example 2:
#     * Input: 
#         * `1 -> 4 -> 6 -> 8 -> 1 -> 3 -> 5`, `1`, `4`
# 
#     * Output: 
#         * `4 -> 4 -> 6 -> 8 -> 4 -> 3 -> 5`
#   
# ## Parameters
# -----------
# * `Node` : `head`
#     - The head of the linked list to be processed
# * `int`  : `n`
#     - The value to be replaced
# * `int`  : `k`
#     - The value to use for replacement
# 
# 
# ## Returns
# -------
# * `Node`: the head of the processed linked list

# In[91]:

def replace_node(head, n, k):
    ptr=head
    while ptr.next!=None:
        if ptr.data==n:
            ptr.data=k
        ptr=ptr.next
    return head
    pass


# In[92]:

def equal_ll(test_head, sol_head):
    """Check if linked lists are equal. Used for test cases."""
    while True:
        if not test_head and not sol_head:
            return True
        if not test_head.data == sol_head.data:
            return False
        test_head = test_head.next
        sol_head = sol_head.next


def test_replace_node():
    head = Node(1,Node(2,Node(3,Node(4,None))))
    assert equal_ll(replace_node(head, 2, 5),Node(1,Node(5,Node(3,Node(4,None)))))


# In[93]:

test_replace_node()


# In[94]:

def test_all():
    # Add your test case here. This should be at the very end
    test_linked_list_to_list()
    test_list_to_linked_list()
    test_reverse_linked_list()
    test_find_nth()
    test_cycle_detection()
    test_replace_node()


# In[95]:

test_all()


# In[ ]:



