import smtplib
import email.message

def enviar_email():
    corpo_email = """
    <p>Paragrafo1</p>
    <p>Paragrafo2</p>
    <p>Test4</p>
    """

    msg = email.message.Message()
    msg['Subject'] = "Assunto"
    msg['From'] = 'mateus.16.veloso@gmail.com'
    msg['To'] = 'mateus.16.veloso@gmail.com'
    password = 'iggdyjzjukyshogb'
    msg.add_header('Content-Type', 'text/html')
    msg.set_payload(corpo_email)

    s = smtplib.SMTP('smtp.gmail.com: 587')
    s.starttls()
    s.login(msg['From'], password)
    s.sendmail(msg['From'], [msg['to']], msg.as_string().encode('utf-8'))
    print('Email enviado')

enviar_email()