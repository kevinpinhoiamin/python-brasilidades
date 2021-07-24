from datetime import datetime, timedelta


class DataBr:
    def __init__(self):
        self.momento_cadastro = datetime.today()

    def __str__(self):
        return self.formata()

    def mes_cadastro(self):
        meses_do_ano = [
            "janeiro", "fevereiro", "março",
            "abril", "maio", "junho",
            "julho", "agosto", "setembro",
            "outubro", "novembro", "dezembro"
        ]
        mes_cadastro = self.momento_cadastro.month
        return meses_do_ano[mes_cadastro - 1]

    def dia_semana(self):
        dias_da_semana = [
            "segunda", "terça", "quarta",
            "quinta", "sexta", "sábado",
            "domingo"
        ]
        dia_da_semana = self.momento_cadastro.weekday()
        return dias_da_semana[dia_da_semana]

    def formata(self):
        data_fomratada = self.momento_cadastro.strftime("%d/%m/%Y %H:%M")
        return data_fomratada

    def tempo_cadastro(self):
        tempo_cadastro = (datetime.today() + timedelta(days=30)) - self.momento_cadastro
        return tempo_cadastro
