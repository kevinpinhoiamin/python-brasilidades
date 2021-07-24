# CPF & CPNJ
from cpf_cnpj import Documento

exemplo_cnpj = "35379838000112"
exemplo_cpf = "32007832062"
cpf_invalido = "11111111112"

documento = Documento.cria_documento(exemplo_cpf)
print(documento)


# Telefone
from telefone_br import TelefoneBr

telefone = "552126461234"

telefone_objeto = TelefoneBr(telefone)
print(telefone_objeto)


# Data
from data_br import DataBr

cadastro = DataBr()
print(cadastro)
print(cadastro.tempo_cadastro())


# CEP
from acesso_cep import BuscaEndereco

cep = "01001000"
bsuca_endereco = BuscaEndereco(cep)
bairro, cidade, uf = bsuca_endereco.acessa_via_cep()
print(bsuca_endereco)
print(bairro, cidade, uf)
