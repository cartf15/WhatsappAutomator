from twilio.rest import Client 
import os

# account_sid = os.environ['twl_sid']
# auth_token = os.environ['twl_tkn']
account_sid = 'AC32dec65d1dceb3607b266febad8cc38f' 
auth_token = 'c36e6ad1831e99a23920dbc365169d2c'



client = Client(account_sid, auth_token) 
 
ns=['+573142993448','+573176484553','+573107380750'] 
ms=1
for m in range(ms):
    for n in ns: 
        message = client.messages.create( 
                                    from_='whatsapp:+14155238886',  
                                    body='Hola, es el momento de hacer un cambio en tu vida, aprende ingles AHORA! con un metodo vanguardista sin salir del pais, preguntame como Test N {}'.format(m),      
                                    to='whatsapp:{}'.format(n)
                                ) 
    
    # print(message.sid)
