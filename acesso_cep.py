import requests

class BuscaEndereco:
    def __init__(self, cep):
        cep = str(cep)
        if (self.cep_eh_valido(cep)):
            self.cep = cep
        else:
            raise ValueError("CEP inválido!!")

    def __str__(self):
        return self.formata()

    def cep_eh_valido(self, cep):
        return True if len(cep) == 8 else False

    def formata(self):
        return "{}-{}".format(self.cep[:5], self.cep[5:])

    def acessa_via_cep(self):
        url = "https://viacep.com.br/ws/{}/json/".format(self.cep)
        r = requests.get(url)
        dados = r.json()
        return (
            dados["bairro"],
            dados["localidade"],
            dados["uf"]
        )
