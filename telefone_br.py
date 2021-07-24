import re


class TelefoneBr:
    def __init__(self, telefone):
        if self.valida(telefone):
            self.numero = telefone
        else:
            raise ValueError("Número incorreto!!")

    def __str__(self):
        return self.formata()

    def valida(self, telefone):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.findall(padrao, telefone)
        return True if resposta else False

    def formata(self):
        padrao = "([0-9]{2,3})?([0-9]{2})([0-9]{4,5})([0-9]{4})"
        resposta = re.search(padrao, self.numero)
        if resposta.group(1) is None:
            return "+55 ({}) {}-{}".format(
                resposta.group(2),
                resposta.group(3),
                resposta.group(4)
            )
        return "+{} ({}) {}-{}".format(
            resposta.group(1),
            resposta.group(2),
            resposta.group(3),
            resposta.group(4)
        )
