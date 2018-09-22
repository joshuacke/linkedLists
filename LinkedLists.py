class Node:

  def __init__(self, initialData):
    self.data = initialData
    self.next = None
  def getData(self):
    return self.data
  def getNext(self):
    return self.next
  def setData(self, newData):
   self.data = newData
  def setNext(self, newNext):
    self.next = newNext

class LinkedList(Node):

  def __str__(self):
    # Return a string representation of data suitable for printing.
    # Long lists (more than 10 elements long) should be neatly
    # printed with 10 elements to a line, two spaces between
    # elements
    current = self.head
    string = ""
    counter = 0
    while (current != None):
      string += str(current.getData()) + "  "
      current = current.getNext()
      counter += 1
      if (counter == 10):
        string += "\n"
        counter = 0
    return string

  def addFirst(self, item):
    # Add an item to the beginning of the list
    temp = Node(item)
    temp.setNext(self.head)
    self.head = temp

  def addLast(self, item):
    # Add an item to the end of a list
    temp = Node(item)
    current = self.head
    if (current == None):
      self.head = temp
    else:
      while (current.getNext() != None):
        current = current.getNext()
      current.setNext(temp)

  def addInOrder(self, item):
    # Insert an item into the proper place of an ordered list.
    # This assumes that the original list is already properly
    # ordered.
    if (self.head == None):
      self.addFirst(item)
    else:
      if (self.head.getData() > item):
        self.addFirst(item)
      else:
        current = self.head
        while True:
          if (current.getNext() == None):
            temp = Node(item)
            current.setNext(temp)
            break
          elif (current.getNext().getData() > item):
            temp = Node(item)
            temp.setNext(current.getNext())
            current.setNext(temp)
            break
          current = current.getNext()
      
  def getLength(self):
    # Return the number of items in the list
    current = self.head
    counter = 0
    while (current != None):
      counter += 1
      current = current.getNext()
    return counter

  def findUnordered(self, item):
    # Search in an unordered list
    # Return True if the item is in the list, False
    # otherwise.
    current = self.head
    while (current != None):
      if (current.getData() == item):
        return True
      current = current.getNext()
    return False

  def findOrdered(self, item):
    # Search in an ordered list
    # Return True if the item is in the list, False
    # otherwise.
    # This method MUST take advantage of the fact that the
    # list is ordered to return quicker if the item is not
    # in the list.
    current = self.head
    while (current != None):
      if (current.getData() == item):
        return True
      elif (current.getData() > item):
        return False
      current = current.getNext()
    return False

  def delete(self, item):
    # Delete an item from an unordered list
    # if found, return True; otherwise, return False
    current = self.head
    before = None
    while (current != None):
      if (current.getData() == item):
        if (before == None):
          self.head = current.getNext()
        else:
          before.setNext(current.getNext())
        return True
      before = current
      current = current.getNext()
    return False

  def copyList(self):
    # Return a new linked list that's a copy of the original,
    # made up of copies of the original elements
    current = self.head
    newList = LinkedList()
    while current != None:
        newList.addLast(current.getData())
        current = current.getNext()
    return newList

  def reverseList(self):
    # Return a new linked list that contains the elements of the
    # original list in the reverse order.
    current = self.head
    newList = LinkedList()
    while (current != None):
      newList.addFirst(current.getData())
      current = current.getNext()
    return newList

  def orderList(self):
    # Return a new linked list that contains the elements of the
    # original list, sorted into ascending (alphabetical) order.
    # Do NOT use a sort function:  do this by iteratively
    # traversing the first list and then inserting copies of
    # each item into the correct place in the new list.
    newList = LinkedList()
    current = self.head
    while current != None:
      newList.addInOrder(current.getData())
      current = current.getNext()
    return newList

  def isOrdered(self):
    # Return True if a list is sorted in ascending (alphabetical)
    # order, or False otherwise
    if (self.head == None or self.head.getNext() == None):
      return True
    current = self.head.getNext()
    before = self.head
    while (current != None):
      if (before.getData() > current.getData()):
        return False
      before = current
      current = current.getNext()
    return True

  def isEmpty(self):
    # Return True if a list is empty, or False otherwise
    return self.head == None

  def mergeList(self, b):
    # Return an ordered list whose elements consist of the
    # elements of two ordered lists combined.
    merged = self.copyList()
    current = b.head
    while (current != None):
      merged.addInOrder(current.getData())
      current = current.getNext()
    return merged

  def isEqual(self, b):
    # Test if two lists are equal, item by item, and return True.
    current = self.head
    bcurrent = b.head
    if (self.getLength() != b.getLength()):
      return False
    while (current != None and bcurrent != None):
      if (current.getData() != bcurrent.getData()):
        return False
      current = current.getNext()
      bcurrent = bcurrent.getNext()
    return True

  def removeDuplicates(self):
    # Remove all duplicates from a list, returning a new list.
    # Do not change the order of the remaining elements.
    current = self.head
    before = None
    deleted = LinkedList()
    done = []
    while current != None:
      if current.getData() in done:
        deleted = deleted
      else:
        deleted.addLast(current.getData())
        done.append(current.getData())
      before = current
      current = current.getNext()
    return deleted

  def __init__(self):
    self.head = None

def main():

   print ("\n\n***************************************************************")
   print ("Test of addFirst:  should see 'node34...node0'")
   print ("***************************************************************")
   myList1 = LinkedList()
   for i in range(35):
      myList1.addFirst("node"+str(i))

   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of addLast:  should see 'node0...node34'")
   print ("***************************************************************")
   myList2 = LinkedList()
   for i in range(35):
      myList2.addLast("node"+str(i))

   print (myList2)

   print ("\n\n***************************************************************")
   print ("Test of addInOrder:  should see 'alpha delta epsilon gamma omega'")
   print ("***************************************************************")
   greekList = LinkedList()
   greekList.addInOrder("gamma")
   greekList.addInOrder("delta")
   greekList.addInOrder("alpha")
   greekList.addInOrder("epsilon")
   greekList.addInOrder("omega")
   print (greekList)

   print ("\n\n***************************************************************")
   print ("Test of getLength:  should see 35, 5, 0")
   print ("***************************************************************")
   emptyList = LinkedList()
   print ("   Length of myList1:  ", myList1.getLength())
   print ("   Length of greekList:  ", greekList.getLength())
   print ("   Length of emptyList:  ", emptyList.getLength())

   print ("\n\n***************************************************************")
   print ("Test of findUnordered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'node25' in myList2: ",myList2.findUnordered("node25"))
   print ("   Searching for 'node35' in myList2: ",myList2.findUnordered("node35"))

   print ("\n\n***************************************************************")
   print ("Test of findOrdered:  should see True, False")
   print ("***************************************************************")
   print ("   Searching for 'epsilon' in greekList: ",greekList.findOrdered("epsilon"))
   print ("   Searching for 'omicron' in greekList: ",greekList.findOrdered("omicron"))

   print ("\n\n***************************************************************")
   print ("Test of delete:  should see 'node25 found', 'node34 found',")
   print ("   'node0 found', 'node40 not found'")
   print ("***************************************************************")
   print ("   Deleting 'node25' (random node) from myList1: ")
   if myList1.delete("node25"):
      print ("      node25 found")
   else:
      print ("      node25 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node34' (first node) from myList1: ")
   if myList1.delete("node34"):
      print ("      node34 found")
   else:
      print ("      node34 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node0'  (last node) from myList1: ")
   if myList1.delete("node0"):
      print ("      node0 found")
   else:
      print ("      node0 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("   Deleting 'node40' (node not in list) from myList1: ")
   if myList1.delete("node40"):
      print ("      node40 found")
   else:
      print ("   node40 not found")
   print ("   myList1:  ")
   print (myList1)

   print ("\n\n***************************************************************")
   print ("Test of copyList:")
   print ("***************************************************************")
   greekList2 = greekList.copyList()
   print ("   These should look the same:")
   print ("      greekList before delete:")
   print (greekList)
   print ("      greekList2 before delete:")
   print (greekList2)
   greekList2.delete("alpha")
   print ("   This should only change greekList2:")
   print ("      greekList after deleting 'alpha' from second list:")
   print (greekList)
   print ("      greekList2 after deleting 'alpha' from second list:")
   print (greekList2)
   greekList.delete("omega")
   print ("   This should only change greekList1:")
   print ("      greekList after deleting 'omega' from first list:")
   print (greekList)
   print ("      greekList2 after deleting 'omega' from first list:")
   print (greekList2)

   print ("\n\n***************************************************************")
   print ("Test of reverseList:  the second one should be the reverse")
   print ("***************************************************************")
   print ("   Original list:")
   print (myList1)
   print ("   Reversed list:")
   myList1Rev = myList1.reverseList()
   print (myList1Rev) 

   print ("\n\n***************************************************************")
   print ("Test of orderList:  the second list should be the first one sorted")
   print ("***************************************************************")
   planets = LinkedList()
   planets.addFirst("Mercury")
   planets.addFirst("Venus")
   planets.addFirst("Earth")
   planets.addFirst("Mars")
   planets.addFirst("Jupiter")
   planets.addFirst("Saturn")
   planets.addFirst("Uranus")
   planets.addFirst("Neptune")
   planets.addFirst("Pluto?")
   
   print ("   Original list:")
   print (planets)
   print ("   Ordered list:")
   orderedPlanets = planets.orderList()
   print (orderedPlanets)

   print ("\n\n***************************************************************")
   print ("Test of isOrdered:  should see False, True")
   print ("***************************************************************")
   print ("   Original list:")
   print (planets)
   print ("   Ordered? ", planets.isOrdered())
   orderedPlanets = planets.orderList()
   print ("   After ordering:")
   print (orderedPlanets)
   print ("   ordered? ", orderedPlanets.isOrdered())

   print ("\n\n***************************************************************")
   print ("Test of isEmpty:  should see True, False")
   print ("***************************************************************")
   newList = LinkedList()
   print ("New list (currently empty):", newList.isEmpty())
   newList.addFirst("hello")
   print ("After adding one element:",newList.isEmpty())

   print ("\n\n***************************************************************")
   print ("Test of mergeList")
   print ("***************************************************************")
   list1 = LinkedList()
   list1.addLast("aardvark")
   list1.addLast("cat")
   list1.addLast("elephant")
   list1.addLast("fox")
   list1.addLast("lynx")
   print ("   first list:")
   print (list1)
   list2 = LinkedList()
   list2.addLast("bacon")
   list2.addLast("dog")
   list2.addLast("giraffe")
   list2.addLast("hippo")
   list2.addLast("wolf")
   print ("   second list:")
   print (list2)
   print ("   merged list:")
   list3 = list1.mergeList(list2)
   print (list3)

   print ("\n\n***************************************************************")
   print ("Test of isEqual:  should see True, False, True")
   print ("***************************************************************")
   print ("   First list:")
   print (planets)
   planets2 = planets.copyList()
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print (planets)
   planets2.delete("Mercury")
   print ("   Second list:")
   print (planets2)
   print ("      Equal:  ",planets.isEqual(planets2))
   print ("   Compare two empty lists:")
   emptyList1 = LinkedList()
   emptyList2 = LinkedList()
   print ("      Equal:  ",emptyList1.isEqual(emptyList2))

   print ("\n\n***************************************************************")
   print ("Test of removeDuplicates:  original list has 14 elements, new list has 10")
   print ("***************************************************************")
   dupList = LinkedList()
   print ("   removeDuplicates from an empty list shouldn't fail")
   newList = dupList.removeDuplicates()
   print ("   printing what should still be an empty list:")
   print (newList)
   dupList.addLast("giraffe")
   dupList.addLast("wolf")
   dupList.addLast("cat")
   dupList.addLast("elephant")
   dupList.addLast("bacon")
   dupList.addLast("fox")
   dupList.addLast("elephant")
   dupList.addLast("wolf")
   dupList.addLast("lynx")
   dupList.addLast("elephant")
   dupList.addLast("dog")
   dupList.addLast("hippo")
   dupList.addLast("aardvark")
   dupList.addLast("bacon")
   print ("   original list:")
   print (dupList)
   print ("   without duplicates:")
   newList = dupList.removeDuplicates()
   print (newList)

main()