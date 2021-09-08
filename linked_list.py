class Node:
    def __init__(self, data = None, next_node = None):
        self.data = data
        self.next_node = next_node

class LinkedList:
    def __init__(self):
        self.head = None
        self.last_node = None

    def to_list(self):
        ll = []
        if self.head is None:
            return None
        
        node = self.head
        while node:
            ll.append(node.data)
            node = node.next_node
        return ll

    def print_ll(self):
        ll_string = ""
        node = self.head
        if node is None:
            print(None)
        while node:
            ll_string += f"{str(node.data)} -> "
            # after each node, we need to assign the node to next node 
            node = node.next_node            
        # at the of the while loop, when there's no node left,  we need to append none to teh end of ll_string
        ll_string += "None"
        # finally, print the whole string
        print(ll_string)
        

    def insert_beginning(self, data):
        
        if self.head is None:
            self.head = Node(data, None)
            self.last_node = self.head
            return

        # first create the node object with data and the next node is going to be the current head, which is self.head
        new_node = Node(data, self.head)
        # update the head pointer that now the new head is the new_code
        self.head = new_node
        
        


    def insert_at_end(self, data):
        if self.head is None:
            self.insert_beginning(data)
            return
        
        # if self.last_node is None:
        #     print("last node is none")
        #     node = self.head
        #     # traverse till the end
            
        #     while node.next_node:
        #         print("iter", node.data)
        #         node = node.next_node

        #     node.next_node = Node(data, None)
        #     self.last_node = node.next_node 
        # # if the last node is not none,  re-assign the next node of teh last node to the new node.
        # else:
        self.last_node.next_node = Node(data, None)
        self.last_node = self.last_node.next_node

    def get_user_by_id(self, user_id):
        node = self.head
        while node:
            if node.data["id"] is int(user_id):
                return node.data
            node = node.next_node
        return None


# ll = LinkedList()
# node4 = Node("data4", None)
# node3 = Node("data3", node4)
# node2 = Node("data2", node3)
# node1 = Node("data1", node2)

# ll.head = node1
# ll.print_ll()


# ll=LinkedList()
# ll.insert_beginning("data")
# ll.insert_beginning("not data")
# ll.print_ll()

ll = LinkedList()
ll.insert_beginning("data")
ll.insert_beginning("data")
ll.insert_beginning("data")
ll.insert_beginning("data")
ll.insert_beginning("data")
ll.insert_beginning("data")
ll.insert_beginning("data")
ll.insert_at_end("end")
ll.insert_at_end("end2")
ll.print_ll()