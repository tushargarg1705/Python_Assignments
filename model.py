




import os
import csv
import uuid

def generate_uuid():
    return uuid.uuid4()

class Person(object):
    def __init__(self,first_name,last_name,email,phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
        self.uuid = generate_uuid()
    
        
    def set_user(self):
        header = ['First Name', 'Last Name', 'email', 'phone number', 'uuid']
        data = {'First Name':self.first_name, 'Last Name':self.last_name, 'email':self.email, 'phone number':self.phone_number,'uuid':self.uuid}
        if os.path.isfile('User.csv'):
            with open('User.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames= header)
                w.writerow(data)
        else:
            with open('User.csv', 'w', newline='') as my_file:
                    w = csv.DictWriter(my_file, fieldnames = header)
                    w.writeheader()
                    w.writerow(data)
    
                    
    def initials(self):
        return self.first_name[0]+"."+self.last_name[0]
    
    
    
    
    
    @classmethod
    def getAllUser(cls):
        values = open('User.csv', 'r')
        result = []
        read = csv.DictReader(values)
        field = read.fieldnames
        for row in read:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result

    
class Blog(object):
    def __init__(self,name,date,topic):
        self.name = name
        self.date = date
        self.topic = topic
        #self.user = user
    
        
    def set_blog(self):
        header = ['Name', 'Date', 'Topic']
        data = {'Name':self.name, 'Date':self.date, 'topic':self.topic}
        if os.path.isfile('Blog.csv'):
            with open('Blog.csv', 'a', newline='') as my_file:
                w = csv.DictWriter(my_file, fieldnames= header)
                w.writerow(data)
        else:
            with open('Blog.csv', 'w', newline='') as my_file:
                    w = csv.DictWriter(my_file, fieldnames = header)
                    w.writeheader()
                    w.writerow(data)
    
                    
    @classmethod
    def getAllBlog(cls):
        values = open('Blog.csv', 'r')
        result = []
        read = csv.DictReader(values)
        field = read.fieldnames
        for row in read:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result
    