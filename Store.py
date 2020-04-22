class Item:
    def __init__(self,name,price,category):
        self.name=name
        self.price=price
        self.category=category
        if self.price<=0:
            raise ValueError("Invalid value for price, got {}".format(self.price))
            
    def __str__(self):
        return "{}@{}-{}".format(self.name,self.price,self.category)
        
class Query:
    def __init__(self,field,operation,value):
        self.field=field
        self.operation=operation
        operations={'IN','EQ','GT','GTE','LT','LTE','STARTS_WITH','ENDS_WITH','CONTAINS'}
        if  operation not in operations:
            raise ValueError('Invalid value for operation, got {}'.format(self.operation))
        self.value=value
        
    def __str__(self):
        return "{} {} {}".format(self.field,self.operation,self.value)
        
class Store:
    def __init__(self):
        self.listitem=[]
        
    def add_item(self,val):
        self.listitem.append(val)
    
    def filter(self,query):
        store_items=Store()
        for i in self.listitem:
            if query.operation=='EQ':
                if query.value==i.name or query.value==i.price or query.value==i.category:
                    store_items.add_item((i))
        
            elif query.operation=='GT':
                if i.price>query.value:
                    store_items.add_item((i))
                    
            elif query.operation=='GTE':
                if i.price>=query.value:
                    store_items.add_item((i))
            
            elif query.operation=='LT':
                if i.price<query.value:
                    store_items.add_item((i))
                    
            elif query.operation=='LTE':
                if i.price<=query.value:
                    store_items.add_item((i))
                    
            elif query.operation=='STARTS_WITH':
                if i.name.startswith(query.value)==True or i.category.startswith(query.value)==True :
                    store_items.add_item((i))
                    
            elif query.operation=='ENDS_WITH':
                if i.name.endswith(query.value)==True or i.category.endswith(query.value)==True:
                    store_items.add_item((i))
                    
            elif query.operation=='CONTAINS':
                if(query.field=="name"):
                    if (query.value) in i.name:
                        store_items.add_item((i))
                else:
                    if(query.value) in i.category:
                        store_items.add_item((i))
        
            elif query.operation=='IN':
                for k in query.value:
                    if  k==i.name or k==i.price or k==i.category:
                        store_items.add_item((i))
                        
        return store_items
        
    def exclude(self,query):
        store_items=Store()
        for i in self.listitem:
            if query.operation=='EQ':
                if query.value!=i.name and query.value!=i.price and query.value!=i.category :
                    store_items.add_item((i))
                    
            elif query.operation=='IN':
                if  i.name not in query.value and i.price not in query.value and i.category not in query.value:
                    store_items.add_item((i))
    
            elif query.operation=='GT':
                if not i.price>query.value:
                    store_items.add_item((i))
                    
            elif query.operation=='GTE':
                if not i.price>=query.value:
                    store_items.add_item((i))
                    
            elif query.operation=='LT':
                if not i.price<query.value:
                    store_items.add_item((i))
                    
            elif query.operation=='LTE':
                if not i.price<=query.value:
                    store_items.add_item((i))
                    
            elif query.operation=='STARTS_WITH':
                if not i.name.startswith(query.value)==True and not i.category.startswith(query.value)==True:
                    store_items.add_item((i))
                    
            elif query.operation=='ENDS_WITH':
                if not i.name.endswith(query.value)==True and not i.category.endswith(query.value)==True :
                    store_items.add_item((i))
                    
            elif query.operation=='CONTAINS':
                if(query.field=="name"):
                    if (query.value) not in i.name:
                        store_items.add_item((i))
                else:
                    if(query.value) not in i.category:
                        store_items.add_item((i))
        return store_items
        
    def __str__(self):
        if len(self.listitem)<=0:
            return "No items"
        else:
            return "\n".join(map(str,self.listitem))
    def count(self):
        return len(self.listitem)
