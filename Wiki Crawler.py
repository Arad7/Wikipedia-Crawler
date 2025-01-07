
"""

Take a wikipedia name page as an input, and prints an OrderedList (from smallest to largest) of all the times that
the users input is mentioned in each article that is linked on the user's input page.

"""
import requests

class Node:
    def __init__(self,initdata,name):
        self.__data = initdata
        self.__name = name
        self.__next = None

    def get_data(self):
        return self.__data

    def get_next(self):
        return self.__next

    def set_data(self,newdata):
        self.__data = newdata

    def set_next(self,newnext):
        self.__next = newnext
        
    def get_name(self):
        return self.__name
    
    def set_name(self,new_name):
        self.__name = new_name
        
class OrderedList:
    
    def __init__(self):
        self.__head = None
        self.__length = 0
        
    def size(self):
        return self.__length
        
    def is_empty(self):
        return self.__head == None
    
    def __repr__(self):
        list_representation = ""
        current = self.__head #start with the Node at the head
        while current: #this will keep going until current equals None
            list_representation += str(current.get_name())
            list_representation += str(": ")
            list_representation += str(current.get_data())
            
            if current.get_next(): #if there's another item after this one, print the comma
                list_representation += ", " 
            current = current.get_next() #move on to the next Node in the list
        return list_representation
    
    def addNode(self,item):
        newnode = item
        self.__length += 1
        
        #case 1: the list is empty
        if self.is_empty():
            self.__head = newnode
            
        #case 2: new item goes at the head
        elif newnode.get_data() <= self.__head.get_data():
            newnode.set_next(self.__head)
            self.__head = newnode
            
        #case 3: new item is not the head
        else:
            self.__add_after(newnode,self.__head)
            
    
    def add(self,item,name):
        newnode = Node(item,name)
        self.__length += 1
        
        #case 1: the list is empty
        if self.is_empty():
            self.__head = newnode
            
        #case 2: new item goes at the head
        elif newnode.get_data() <= self.__head.get_data():
            newnode.set_next(self.__head)
            self.__head = newnode
            
        #case 3: new item is not the head
        else:
            self.__add_after(newnode,self.__head)
            
    def __add_after(self, newnode, currnode):
        #check if the newnode goes immediate after currnode
        if currnode.get_next() == None or newnode.get_data() <= currnode.get_next().get_data():
            #re-assign references to put it here
            newnode.set_next( currnode.get_next() )
            currnode.set_next(newnode)
        else:
            #recursively insert the newnode later in the list
            self.__add_after(newnode,currnode.get_next())
            
            
    def search(self,item):
        return self.__search_node(item,self.__head)
    
    def __search_node(self,item,currnode):
        #if we're at the end of the list or this item is smaller than the
        #current item, we know it can't be in the list
        if currnode == None or item < currnode.get_data():
            return False
        #we found the item - return True
        elif currnode.get_data() == item:
            return True
        #search the rest of the list
        else:
            return self.__search_node(item,currnode.get_next())
        
        def index(self,item):
            counter = 0 
            return(self.go(item,counter))
        
        def go(item,counter):
            if self.__head == None:
                return "Does not exsist"
            elif self.__head == item:
                return counter
            else:
                return(self.go(self.get_next(),counter + 1))
        
def check (k, name):
    search_endpoint = "https://en.wikipedia.org/w/rest.php/v1/search/page"
    query_params = {"q":k,"limit":1,"maxlag":1}
    response = requests.get(search_endpoint,params=query_params)
    search_results = response.json()
    
    amount_of_times = 0
    
    if (search_results["pages"]) != []:
        if search_results["pages"][0] != None: 
            page_title = search_results["pages"][0]['title']
            page_endpoint = "https://en.wikipedia.org/w/rest.php/v1/page/"+page_title
            response = requests.get(page_endpoint)
            page_results = response.json()
            if "source" in page_results:

                page_content = page_results["source"]
                
                
                i = 0
                while i < len(page_content):
                             
                    if page_content[i:i+len(name)].lower() == name.lower():
                        i = i+len(name)
                        amount_of_times = amount_of_times + 1
                        
                    else:
                        i += 1
                    
                
    n = Node(amount_of_times,k)      
    return (n)
        

user_search_input = input("Enter a search term: ")
search_endpoint = "https://en.wikipedia.org/w/rest.php/v1/search/page"
query_params = {"q":user_search_input,"limit":1}
response = requests.get(search_endpoint,params=query_params)
search_results = response.json()
page_title = search_results["pages"][0]['title']

page_endpoint = "https://en.wikipedia.org/w/rest.php/v1/page/"+page_title
response = requests.get(page_endpoint)
page_results = response.json()
page_content = page_results["source"]

print("Here are all the times that " + user_search_input + " is mentioned in each article that is linked on the page (from smallest to largest)-",page_title)

i = 0

order = OrderedList() 

amount_of_return = 0 
while i < len(page_content):
            
    if page_content[i:i+2] == "[[":
        i = i+2
        linked_page_name = ""
        while page_content[i] != '|' and page_content[i] != ']':
            linked_page_name += page_content[i]
            i += 1
        
        order.addNode(check(linked_page_name,user_search_input))

    else:
        i += 1

print (order)
        
        
    
