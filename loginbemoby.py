import requests
import json



class Login_bemoby:
    def __init__(self, username, password):
        self.headers = {"Content-Type": "application/json"}
        self.username = username
        self.password = password
        self.token = None

    def get_token(self):
        login_data = {"username": self.username, "password": self.password}
        url = requests.post("https://api.sirius.bemoby.com/users/login",
                            headers=self.headers, data=json.dumps(login_data))

        response_json = url.json()
        self.token = response_json["data"]["item"]["token"]
        return self.token

class Whatsapp_Bemoby:
    def __init__(self, numero, variaveis, id_hsm, token):
        self.numero = numero
        self.variaveis = variaveis
        self.id_hsm = id_hsm
        self.envia_header = {"Content-Type": "application/json",
                        "Authorization": "Bearer " + token}

    def envia_link(self):
        envia_data = {"destinations": [{"to": self.numero,
        "vars": self.variaveis, "externalId": "6666"}]}

        envia = requests.post("https://api.sirius.bemoby.com/callcenter/hsm/send/" + self.id_hsm,
                              headers=self.envia_header, data=json.dumps(envia_data))
        return envia.text, envia.status_code
