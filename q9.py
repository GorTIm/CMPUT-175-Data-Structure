def q9():
    conditonSet=set()
    string=input("Enter conditions:")
    stringList=string.split(" ")
    for c in stringList:
        condition=c.split(":")
        #condition1--equal search
        if len(condition)>1:
            #condition1.1--equal search on date
            if condition[0]=="date":
                key = condition[1].lower()
                key = bytes(key, 'utf-8')    
                database = db.DB()
                database.open('da.idx')
                cur = database.cursor()
                result = cur.get(key ,db.DB_SET)
                if result != None:
                    numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                    conditonSet.add(numid)   
                             
                    result=cur.next_dup()
                        
                    while result:
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        conditonSet.add(numid)             
                        result=cur.next_dup()
            #condition1.2  search on text(both equal and partial)
            elif condition[0]=="text":
                prefix=False
                key = condition[1]
                if key.endswith("%"):
                    key=key[:-1]
                    prefix=True
                key= key.lower()
                #cpkey is a string
                cpkey = "t-"+key
                length=len(cpkey)
                #key is a byte literal
                key = bytes(key, 'utf-8')
                database = db.DB()
                database.open('te.idx')
                cur = database.cursor() 
                if prefix==False:
                    result = cur.get(b't-'+ key ,db.DB_SET)
                    if result != None:     
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        conditonSet.add(numid)   
                    
                        result=cur.next_dup()
                        while result:
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid)        
                            result=cur.next_dup()        
                
                elif prefix==True:
                    result= cur.first()
                    while result:
                        term=str(result[0])
                        term= term[2:]
                        term= term[:-1]
                        term=term[:length]
                        if term==cpkey:
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid) 
                        result=cur.next()            
                
                
            #condition1.3  search on name(both equal and partial) 
            elif condition[0]=="name":
                prefix=False
                key = condition[1]
                if key.endswith("%"):
                    key=key[:-1]
                    prefix=True
                key= key.lower()
                #cpkey is a string
                cpkey = "n-"+key
                length=len(cpkey)
                #key is a byte literal
                key = bytes(key, 'utf-8')
                database = db.DB()
                database.open('te.idx')
                cur = database.cursor() 
                if prefix==False:
                    result = cur.get(b'n-'+ key ,db.DB_SET)
                    if result != None:     
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        conditonSet.add(numid)   
                    
                        result=cur.next_dup()
                        while result:
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid)        
                            result=cur.next_dup()        
                
                elif prefix==True:
                    result= cur.first()
                    while result:
                        term=str(result[0])
                        term= term[2:]
                        term= term[:-1]
                        term=term[:length]
                        if term==cpkey:
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid) 
                        result=cur.next()                   
                
            #condition1.4  search on location(both equal and partial)    
            elif condition[0]=="location":
                prefix=False
                key = condition[1]
                if key.endswith("%"):
                    key=key[:-1]
                    prefix=True
                key= key.lower()
                #cpkey is a string
                cpkey = "l-"+key
                length=len(cpkey)
                #key is a byte literal
                key = bytes(key, 'utf-8')
                database = db.DB()
                database.open('te.idx')
                cur = database.cursor() 
                if prefix==False:
                    result = cur.get(b'l-'+ key ,db.DB_SET)
                    if result != None:     
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        conditonSet.add(numid)   
                    
                        result=cur.next_dup()
                        while result:
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid)        
                            result=cur.next_dup()        
                
                elif prefix==True:
                    result= cur.first()
                    while result:
                        term=str(result[0])
                        term= term[2:]
                        term= term[:-1]
                        term=term[:length]
                        if term==cpkey:
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid) 
                        result=cur.next()                  
                
                
        else:
            condition=c.split(">")
            #condition2 range search on date(greater than)
            if len(condition)>1:
                key = condition[1]
                key = key.lower()
                key = bytes(key, 'utf-8')      
                database = db.DB()
                database.open('da.idx')
                cur = database.cursor()
                result= cur.first()
                if result != None:
                    while result[0]<=key:
                        result=cur.next()
                    while result:
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        conditonSet.add(numid)              
                        result=cur.next()                 
                
                
            else:
                condition=c.split("<")
                #condition3 range search on date(smaller than)
                if len(condition)>1:
                    key = condition[1]
                    key = key.lower()
                    key = bytes(key, 'utf-8')      
                    database = db.DB()
                    database.open('da.idx')
                    cur = database.cursor()
                    result=cur.first()
                    if result != None:
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        conditonSet.add(numid)   
                        result=cur.next()
                        while result[0]<key:
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid)            
                            result=cur.next()                     
                #condition4  search on term 
                else:
                    key=condition[0]
                    key = key.lower()
                    key = bytes(key, 'utf-8')
                    database = db.DB()
                    database.open('te.idx')
                    cur = database.cursor() 
                    result = cur.get(b't-'+ key ,db.DB_SET)
                #text
                    if result != None:
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        
                
                        result=cur.next_dup()
                        while result:
                            numid = re.sub('[^0-9\n\.]', '',result[1])
                            conditonSet.add(numid ) 
                            result=cur.next_dup()
                            
                            
                #name            
                    result = cur.get(b'n-'+ key ,db.DB_SET)
                    if result != None:
                            
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid )    
                            result=cur.next_dup()
                            while result:
                                numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                                conditonSet.add(numid )        
                                result=cur.next_dup()            
                #location
                    result = cur.get(b'l-'+ key ,db.DB_SET)
                    if result != None:
                        
                        numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                        conditonSet.add(numid )    
                        result=cur.next_dup()
                        while result:
                            
                            numid = re.sub(b'[^0-9\n\.]', '',result[1] )
                            conditonSet.add(numid )        
                            result=cur.next_dup()
            
    for c in conditonSet:
        tweets(c)  
