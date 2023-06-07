#https://www.codingninjas.com/codestudio/problems/flatten-a-linked-list_8230827?challengeSlug=striver-sde-challenge

def mergeTwoLists(a, b):
    temp = Node(0)
    res = temp
    while a != None and b != None:
        if a.data < b.data:
            temp.child = a
            temp = temp.child
            a = a.child
        else:
            temp.child = b
            temp = temp.child
            b = b.child
    if a:
        temp.child = a
    else:
        temp.child = b
    return res.child

def flattenLinkedList(root):
    if root == None or root.next == None:
        return root
    root.next = flattenLinkedList(root.next)
    root = mergeTwoLists(root, root.next)
    return root
 
#I used temporary node temp to build the merged list
#I compared the  data of the nodes from both lists and appends the smaller node to temp
#I updated ptr a and b accordingly
#Once one of the lists reaches the end, the remaining nodes of the other list are appended to temp
