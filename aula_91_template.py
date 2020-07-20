# Código para envio de e-mails

from string import Template
from datetime import date

# Tem coisas como o assunto, destinatário, remetente, etc
from email.mime.multipart import MIMEMultipart

# O corpo do e-mail, que pode ser um plain text ou nesse caso html
from email.mime.text import MIMEText

# Para anexar imagem no e-mail
from email.mime.image import MIMEImage

# Conecta no servidor smtp, é ele quem vai enviar a mensagem
import smtplib


data_hoje = date.today().strftime('%d/%m/%Y')
meu_email = 'seuemail@gmail.com'  # endereço do e-mail
minha_senha = 'suasenha'  # senha do e-mail


with open('aula_91_template.html', 'r') as html:
    template = Template(html.read())

    # Aqui nós adicionamos valores customizados substituindo os placeholders
    # que escrevemos no nosso html com o sinal de $
    corpo_mensagem = template.substitute(nome='João', data=data_hoje)

    # Com o safe_substitute não precisamos passar valores para todos os
    # placeholders, sem houvesse mais algum, como $idade e não passassemos
    # acima daria erro, mas com o safe_substitute não dá erro
    # corpo_mensagem = template.safe_substitute(nome='João', data=data_hoje)

mensagem = MIMEMultipart()
mensagem['from'] = 'Joao Kaique'  # Sem acentos
mensagem['to'] = ''  # E-mail do destinatário
mensagem['subject'] = 'E-mail de testes, aula Python.'

# Se fosse um texto só precisaria passar ele diretamente
corpo = MIMEText(corpo_mensagem, 'html')
# corpo = MIMEText('Texto normal')

# Adiciona o corpo na mensagem
mensagem.attach(corpo)

with open('aula_91.jpg', 'rb') as img:
    img = MIMEImage(img.read())
    mensagem.attach(img)

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login(meu_email, minha_senha)  # e-mail que está enviando a mensagem
    smtp.send_message(mensagem)
