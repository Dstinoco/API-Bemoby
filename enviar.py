from loginbemoby import Login_bemoby, Whatsapp_Bemoby
import os
from dotenv import load_dotenv
load_dotenv()
login_email = str(os.getenv('email_login'))
login_pass = str(os.getenv('senha_login'))

login = Login_bemoby(login_email, login_pass)
token = login.get_token()

print(token)

id_hsm = "151"
numero = "5527998142440"
variaveis = {"PACIENTE" : "Douglas Tinooco", "LINK" : "google.com.br"}

whats = Whatsapp_Bemoby(numero, variaveis, id_hsm, token)

resposta, status = whats.envia_link()
print(status)
print(resposta)
