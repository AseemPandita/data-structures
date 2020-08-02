# Class node :: Stores the data and the link to the next element
class Node:
    
    # Constructor ::
    def __init__(self, data=None,next=None):
        self.data = data
        self.next = next
    
        
    
    
# Class LinkedList :: Uses Node Class
class LinkedList:
    
    
    # Constructor ::
    def __init__(self):
        self.head = None
    
    
    # Return the length of the linked list        
    def getLength(self):
        if self.head is None:
            return 0
        iterator = self.head
        count = 1
        while iterator.next:
            count += 1
            iterator = iterator.next
        return count
    
    
    # Insert the node at the beginning of the list
    def insertNodeAtBeginning(self, data):
        self.head = Node(data,self.head)


    # Insert the node at the end of the list.
    # Calls insertNodeAtBeginning() if the list is empty
    def insertNodeAtEnd(self, data):
        if self.head is None:
            self.head = Node(data,self.head)
            return
        iterator = self.head
        while iterator.next:
            iterator = iterator.next            
        iterator.next = Node(data,None)

                        
    # Insert a node at a given index
    def insertNodeAtPosition(self,data,index):
        lengthOfList = self.getLength()
        if index < 0 or index > (lengthOfList):
            print('Invalid Index')
            return
        if index == 0:
            self.insertNodeAtBeginning(data)
        if index == lengthOfList:
            self.insertNodeAtEnd(data)
        iterator = self.head
        i = 0
        while i < index - 1:
            iterator = iterator.next
            i += 1
        iterator.next = Node(data,iterator.next)

        
    # Delete a node at a given index
    def deleteNodeAtPosition(self,index):
        lengthOfList = self.getLength()
        if index < 0 or index >= lengthOfList:
            print('Invalid Index')
            return
        if index == 0:
            self.head = None
            return  
        i = 0
        iterator = self.head
        while i < index - 1:   
            iterator = iterator.next
            i += 1
        iterator.next = iterator.next.next            


    # Convert a list to linked list
    def insertList(self,dataList):
        self.head = None
        for data in dataList:
            self.insertNodeAtEnd(data)
        return

    
    # Append a list to the end of the existing linked list
    def appendList(self,dataList):
        if self.head is None:
            insertList(dataList)
            return
        for data in dataList:
            self.insertNodeAtEnd(data)
        return

    
    # Search
    def search(self,searchData):
        if self.head is None:
            print('The list is empty')
            return
        iterator = self.head
        index = 0
        while iterator:
            if iterator.data == searchData:
                print('Element found at index {}'.format(index))
                return
            index += 1
            iterator = iterator.next
        print('Element not found')
        return

        
    # Print the entire linked list
    def print(self):
        if self.head is None:
            print('The List is empty')
            return        
        iterator = self.head
        while iterator.next:
            print('{}-->'.format(iterator.data),end='')
            iterator = iterator.next
        print(iterator.data)
        
        
        
    
if __name__ == '__main__':      
    ll = LinkedList()
    data = 3
    for i in range(3):
        data += 1
        print('Insert {} at beginning of the list.'.format(data))
        ll.insertNodeAtBeginning(data)
        ll.print()
    
    print('Insert 4 at index 2')
    ll.insertNodeAtPosition(4,2)
    ll.print()
    
    print('Delete Index 2')
    ll.deleteNodeAtPosition(2)
    ll.print()
    
    print('Convert list to linked list')
    dataList = [10,11,12,13,14,15]
    ll.insertList(dataList)
    ll.print()
    
    print('Append list to linked list')
    dataList = [16,17,18,19,20]
    ll.appendList(dataList)
    ll.print()
    
    data = 15
    print('Searching for element: {}'.format(data))
    ll.search(data)    