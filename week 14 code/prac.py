class snakenode:
    def __init__(self,data):
        self.data = data
        self.next = None
    
class SinglySnake:

    def __init__(self):
        self.__head = None
        self.__size = 0

    #return true if linked list empty
    def isEmpty(self):
        if self.__size == 0:
            return True 
        else:
            return False
    # return size of linked list
    def __len__(self):
        return f"Length:{self.__size}"

    #Prepend an item to the snake
    def addFirst(self,data):
        new_snakenode = snakenode(data)
        #Adjust snake references
        new_snakenode.next = self.__head  # Link new node to current head
        self.__head = new_snakenode
        self.__size += 1

    
    #Remove + return first item in the snake
    def removeFirst(self):
        assert not self.isEmpty(), "Cannot remove from an empty snake"
        #Create temp snake node to store the removed snake node
        temp_snakenode = self.__head
        self.__head = self.__head.next
        self.__size -= 1
        return temp_snakenode.data
    
    #Remove + return an item
    def removeNode(self,target):
        assert not self.isEmpty(), "Cannot remove from an empty snake"
        
        
        #Init predNode and curNode pointers
        predNode = None
        curNode = self.__head

        #Get target
        while curNode is not None and curNode.data != target:
            predNode = curNode
            curNode = curNode.next

        #If target is found , curNode is pointing at it
        if curNode is not None:
            # If target is the head of the linked list
            if curNode is self.__head:
                self.__head = curNode.next
            else:
                predNode.next = curNode.next
                curNode.next = None
            # Adjust size
            self.__size -= 1
        return curNode.data if curNode is not None else None
    

    def __str__(self):
        outstr = ''
        curNode = self.__head
        while curNode is not None:
            outstr += str(curNode.data) + ' -> '
            curNode = curNode.next
        return outstr + 'None'

if __name__ == '__main__':
    myLL = SinglySnake()
    for i in range(10,60,10):
        myLL.addFirst(i)
    print("List content (F-->B): ", myLL, "\n")
    
    removedNode = myLL.removeFirst()
    if removedNode is None:
        print("No node removed from linked list!")
    else:
        print("Removed node: ", removedNode)
    print("List content (F-->B): ", myLL, "\n")
    
    removedNode = myLL.removeNode(30)
    if removedNode is None:
        print("No node removed from linked list!")
    else:
        print("Removed node: ", removedNode)
    print("List content (F-->B): ", myLL, "\n")
    
    removedNode = myLL.removeNode(100)
    if removedNode is None:
        print("No node removed from linked list!")
    else:
        print("Removed node: ", removedNode)
    print("List content (F-->B): ", myLL, "\n")