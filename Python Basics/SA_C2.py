def remove_item(list_items, item_to_remove):
    #item check
    inList = False
    newList = []
    i = 0
    j = 0
    for item in list_items:
        if item == item_to_remove:
            print "In list, removing"
            inList = True
        else:
            newList.append(item)
    if inList == False:
        print "The item is not in the list, terminating"
        pass
    elif inList == True:
        print "removed"
        return newList


from sys import argv

script, listItems, itemToRemove = argv

print remove_item(list(listItems), itemToRemove)
