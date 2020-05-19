"""Each ListNode holds a reference to its previous node
as well as its next node in the List."""
class ListNode:
    def __init__(self, value, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

    """Wrap the given value in a ListNode and insert it
    after this node. Note that this node could already
    have a next node it is point to."""
    def insert_after(self, value):
        current_next = self.next
        self.next = ListNode(value, self, current_next)
        if current_next:
            current_next.prev = self.next

    """Wrap the given value in a ListNode and insert it
    before this node. Note that this node could already
    have a previous node it is point to."""
    def insert_before(self, value):
        current_prev = self.prev
        self.prev = ListNode(value, current_prev, self)
        if current_prev:
            current_prev.next = self.prev

    """Rearranges this ListNode's previous and next pointers
    accordingly, effectively deleting this ListNode."""
    def delete(self):
        if self.prev:
            self.prev.next = self.next
        if self.next:
            self.next.prev = self.prev


"""Our doubly-linked list class. It holds references to
the list's head and tail nodes."""
class DoublyLinkedList:
    def __init__(self, node=None):
        self.head = node
        self.tail = node
        self.length = 1 if node is not None else 0

    def __len__(self):
        return self.length

    """Wraps the given value in a ListNode and inserts it 
    as the new head of the list. Don't forget to handle 
    the old head node's previous pointer accordingly."""
    def add_to_head(self, value):
        new_node = ListNode(value) #wrap value in Listnode
        self.length +=1  #add to list length
        if not self.head and not self.tail: #check if not head, if not add neew as head
            self.head = new_node
            self.tail= new_node #may be empty need to set tail as well adding first node to ll
        else: # if is, change pointers on old head and set new
            new_node.next = self.head #new node next is old head
            self.head.prev = new_node  #make old head point backwards to new node as prev node
            self.head = new_node #update head

    """Removes the List's current head node, making the
    current head's next node the new head of the List.
    Returns the value of the removed Node."""
    def remove_from_head(self):
        if self.length >1: #more than 1 node
            current = self.head.value #save current head for return
            new_node = self.head.next #get next node after head
            self.head = new_node #set new head  to new node
            new_node.prev = None #set new head prev to nthng
            self.length -=1 #remove length
            return current #return old head
        elif self.length ==1: # if only 1 node
            current = self.head.value #current is head
            self.head = None #no new head
            self.tail = None #no new tail
            self.length -=1 
            return current #return head 
        else:
            return None #no nodes, do nothing

            ####FROM CLASS SOLUTION####
            # value = self.head.value
           #  self.delete(self.head)
           #  return value

      

    """Wraps the given value in a ListNode and inserts it 
    as the new tail of the list. Don't forget to handle 
    the old tail node's next pointer accordingly."""
    def add_to_tail(self, value):
        new_node = ListNode(value) #wrap value in Listnode
        self.length +=1  #add to list length
        if not self.tail and not self.head: #check if not tail, if not add neew as tail
            self.tail = new_node
            self.head=new_node #may be empty need to set head as well adding first node to ll
        else: # if is, change pointers on old tail and set new
            new_node.prev = self.tail #new node prev is old tail
            self.tail.next = new_node  #make old tail point backwards to new node as prev node
            self.tail = new_node #change old head to be new 

    """Removes the List's current tail node, making the 
    current tail's previous node the new tail of the List.
    Returns the value of the removed Node."""
    def remove_from_tail(self):
        #opposite of head
        #no next
        #get prev
         if self.length >1: #more than 1 node
            current = self.tail.value #save current tail 
            new_node = self.tail.prev #get node before tail
            self.tail = new_node #update tail
            new_node.next = None #point tot none after tail
            self.length -=1 #remove length
            return current #return old tail
         elif self.length ==1: # if only 1 node
            current = self.tail.value #current is tail
            self.head = None #no new head
            self.tail = None #no new tail
            self.length -=1 
            return current #return tail 
         else:
            return None #no nodes, do nothing


 ####FROM CLASS SOLUTION####
            # value = self.tail.value
           #  self.delete(self.tail)
           #  return value

    """Removes the input node from its current spot in the 
    List and inserts it as the new head node of the List."""
    def move_to_front(self, node):
        self.delete(node) #remove input node from spot
        self.add_to_head(node.value) #add node to head
        

    """Removes the input node from its current spot in the 
    List and inserts it as the new tail node of the List."""
    def move_to_end(self, node):
        self.delete(node) #delete node
        self.add_to_tail(node.value) #add to tail

    """Removes a node from the list and handles cases where
    the node was the head or the tail"""
    def delete(self, node):
        if self.length > 1: 
            #if more than 1 nodes
            # #if already at hhead or tail, can use remove head/tail fn
            if node == self.head:
                self.remove_from_head()
            elif node == self.tail:
                self.remove_from_tail()
            else:
                next_node = node.next #get next node for node to be removed
                prev_node = node.prev #get prev node of node to be removed
                prev_node.next = next_node #reset pointer for orig next node to be new next
                next_node.prev = prev_node #set pointer for orig prev to be new prev node
                self.length -=1
        elif self.length == 1: #if only 1 node, set all to 0
            self.head = None
            self.tail = None
            self.length = 0
        
    """Returns the highest value currently in the list"""
    def get_max(self):
        if not self.head:
            return None
        maxVal = self.head.value
        current = self.head
        while current: #go through whole list as long as there is a current node
            if current.value > maxVal: #if current node is larger than max value....
                maxVal = current.value #set max value
            current = current.next #moves pointer to next node
        return maxVal

           
