# Exercise 1 : Call History
# Instructions
# 1. Create a class called Phone. This class takes a parameter called phone_number. When instantiating an 
# object create an attribute called call_history which value is an empty list.

# 2. Add a method called call that takes both self and other_phone (i.e another Phone object) as parameters. 
# The method should print a string stating who called who, and add this string to the phone’s call_history.

# 3. Add a method called show_call_history. This method should print the call_history.

# 4. Add another attribute called messages to your __init__() method which value is an empty list.

# 5. Create a method called send_message which is similar to the call method. Each message should be saved as a 
# dictionary with the following keys:

# to
# from
# content

# Create the following methods: show_outgoing_messages(self), show_incoming_messages(self), show_messages_from(self, number)

# Test your code !!!
# message = [{
#     to 
# }]

class Phone:
    
    def __init__(self, phone_number, fullname):
        self.phone_number = phone_number
        self.call_history = []
        self.messages = []
        self.contact = []
        
        
    def call(self, other_phone):
        for cont in self.contact:
            if cont["number"] == other_phone: 
                contact_name = cont["full_name"]
                print(f' {self.phone_number} was called by {contact_name}')
                return
        
        for cont in self.contact:
                print(f' {self.phone_number} was called by {other_phone}')
                self.call_history.append(f' {self.phone_number} was called by {other_phone}')
                
            
    
    def show_call_history(self):
        for call in self.call_history:
            print(f'{self.call_history.index(call)}')
        
    def send_message(self, **message):
        print(f'{message["to"]} got a new message from {message["fr"]}, the message is {message["content"]}')
        self.messages.append(message)
        
    def show_outgoing_messages(self):
         for item in self.messages:
             if item['fr'] == 'self.phone_number':
                 print(item)
                 
    def show_incoming_messages(self):
        for item in self.messages:
            if item["fr"] != 'self.phone_number':
                print(item)
                
        
    def show_messages_from(self, number):
        for item in self.messages:
            if item["fr"] == number:
                print(item)
                

# 1. when making a call if the other_phone_number is in your contact list then 
# isstead of printing your phone called their phone print your phone called their name and vice versa
            
    def new_contact(self, **new_cont):
        self.contact.append(new_cont)
                  
        
        
                
    def __repr__(self):
        return self.call_history
    
    
# p1 = Phone('078974324')
# p1.call('1232131233')
# p2 = Phone('987654343')
# p2.call('7777777777')
# p2.show_call_history()

p1 = Phone('078974324')
# p1.send_message(to = '123213123', fr = '078974324',  content = 'Hi, I saw you being very funny the other day!')
# p1.send_message(to = '324234234', fr = '078974324',  content = 'Hi, what was that? ')
p1.new_contact(full_name = 'Mr Bean', number = '123213123')
p1.call('123213123')

# p1.show_outgoing_messages()



# CHAIMS CODE 

# class Phone:
#     def __init__(self, phone_number, full_name):
#         self.phone_number = phone_number
#         self.full_name = full_name
#         self.call_history = []
#         self.messages = []
#         self.contacts = []
#     def call(self, other_phone_number, caller):
#         if caller:
#             for contact in self.contacts:
#                 if contact['phone_number'] == other_phone_number:
#                     call_info = f'{self.full_name} called {contact["full_name"]}'
#                     self.call_history.append(call_info)
#                     print(call_info)
#                     return
#             call_info = f'{self.full_name} called {other_phone_number}'
#             self.call_history.append(call_info)
#             print(call_info)
#         else:
#             for contact in self.contacts:
#                 if contact['phone_number'] == other_phone_number:
#                     call_info = f'{contact["full_name"]} called {self.full_name}'
#                     self.call_history.append(call_info)
#                     print(call_info)
#                     return
#             call_info = f'{other_phone_number} called {self.full_name}'
#             self.call_history.append(call_info)
#             print(call_info)
#     def show_call_history(self):
#         for call in self.call_history:
#             print(f'{self.call_history.index(call) + 1}: {call}')
#     def send_message(self, **message_info):
#         self.messages.append(message_info)
#     def show_messages(self):
#         for message in self.messages:
#             print(f'{self.messages.index(message) + 1}: {message}')
#     def show_outgoing_messages(self):
#         counter = 1
#         for message in self.messages:
#             if message['sent_from'] == self.phone_number:
#                 print(f'{counter}: {message}')
#                 counter += 1
#     def show_incoming_messages(self):
#         counter = 1
#         for message in self.messages:
#             if message['to'] == self.phone_number:
#                 print(f'{counter}: {message}')
#                 counter += 1
#     def add_contact(self, **contact_info):
#         self.contacts.append(contact_info)
#     def __repr__(self):
#         return self.phone_number
# p1 = Phone('123456789', 'chaim wiesner')