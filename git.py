from twilio.rest import Client 
import os

# account_sid = os.environ['twl_sid']
# auth_token = os.environ['twl_tkn']
account_sid = 'AC6340922d81a8aaa23e3b36a2ff420ffb' 
auth_token = 'f384519126914e186e5e0c938dfb6e2d' 



client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your appointment is coming up on July 21 at 3PM',      
                              to='whatsapp:+573142993448' 
                          ) 
 
print(message.sid)
