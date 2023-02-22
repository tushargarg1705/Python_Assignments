


import random
import csv

def generate_uuid():
        return random.randint(0,10000)

class User(object):
   
    def set_user(self):
        first_name = input('Enter first name')
        last_name = input('Enter last name')
        email = input('Enter email id')
        phone_number = int(input('Enter phone number'))
        uuid = generate_uuid()

        header = ['First Name', 'Last Name', 'Email', 'Phone Number']
        data = [ first_name,last_name,email,phone_number]


        with open('User.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)

            writer.writerow(header)

            writer.writerow(data)

    


    def initials(self):
        return self.first_name[0]+"."+self.last_name[0]
    
    @classmethod
    #returns all people inside db.txt as list of Person objects
    def getAll(cls):
        database = open('grades.csv', 'r')
        result = []
        reader = csv.DictReader(database)
        field = reader.fieldnames
        for row in reader:
            result.extend([{field[i]:row[field[i]] for i in range(len(field))}])
        return result




obj = User()
obj.set_user()