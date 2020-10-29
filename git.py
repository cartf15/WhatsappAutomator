from twilio.rest import Client 
 
account_sid = 'AC6340922d81a8aaa23e3b36a2ff420ffb' 
auth_token = 'f384519126914e186e5e0c938dfb6e2d' 
client = Client(account_sid, auth_token) 
 
message = client.messages.create( 
                              from_='whatsapp:+14155238886',  
                              body='Your Yummy Cupcakes Company order of 1 dozen frosted cupcakes has shipped and should be delivered on July 10, 2019. Details: http://www.yummycupcakes.com/',      
                              to='whatsapp:+573142993448' 
                          ) 
 
print(message.sid)