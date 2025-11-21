import random
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib



pessoas = {
    'Pessoa1': 'pessoa1@email.com',
    'Pessoa2': 'pessoa2@email.com',
    'Pessoa3': 'pessoa3@email.com',
    'Pessoa4': 'pessoa4@email.com',
    'Pessoa5': 'pessoa5@email.com',
    'Pessoa6': 'pessoa6@email.com',
    'Pessoa7': 'pessoa7@email.com',
}


sender_email = "quem_envia@email.com"
sender_password = "senha"

subject = "Amigo Secreto"


nomes = list(pessoas.keys())               
disponiveis = nomes.copy()                 
pares = {}     


def send_email(sender_email, sender_password, receiver_email, subject, pessoa, amigo):

    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject


    body = f'Parabéns {pessoa}, seu amigo secreto é: {amigo}!'
    message.attach(MIMEText(body, "plain"))   


    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(sender_email, sender_password)
        server.sendmail(sender_email, receiver_email, message.as_string())
        print("E-mail enviado!") 


                          
for pessoa in nomes:
    while True:
        escolhido = random.choice(disponiveis)
        if escolhido == pessoa:
            continue
        pares[pessoa] = escolhido
        disponiveis.remove(escolhido)
        break


for pessoa, amigo in pares.items():
    receiver_email = pessoas[pessoa]
    send_email(sender_email, sender_password, receiver_email, subject, pessoa, amigo)
    
    print(f"{pessoa} pegou {amigo}")



