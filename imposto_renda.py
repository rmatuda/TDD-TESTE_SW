# aqui vai ficar a lógica da minha classe
class CalculadoraImpostoRenda:
    def __init__(self):
        self.rendimentos = []
        self.deducoes = []

    def cadastra_rendimento(self, valor):
        if valor < 0:
            raise ValueError("Valor do rendimento não pode ser negativo.")
        self.rendimentos.append(valor)

    def get_total_rendimentos(self):
        return sum(self.rendimentos)

    def cadastra_deducao(self, descricao, valor):
        if valor < 0:
            raise ValueError("Valor da dedução não pode ser negativo.")
        self.deducoes.append({"descricao": descricao, "valor": valor})

    def get_total_deducoes(self):
        return sum(d['valor'] for d in self.deducoes)

    def get_base_de_calculo(self):
        total_rendimentos = self.get_total_rendimentos()
        total_deducoes = self.get_total_deducoes()
        return total_rendimentos - total_deducoes
        
    def get_imposto_devido(self):
        base_calculo = self.get_base_de_calculo()
        imposto = 0.0

        if base_calculo <= 1903.98:
            imposto = 0.0
        elif 1903.99 <= base_calculo <= 2826.65:
            imposto = (base_calculo * 0.075) - 142.80
        elif 2826.66 <= base_calculo <= 3751.05:
            imposto = (base_calculo * 0.15) - 354.80
        elif 3751.06 <= base_calculo <= 4664.68:
            imposto = (base_calculo * 0.225) - 636.13
        else: 
            imposto = (base_calculo * 0.275) - 869.36
            
        return round(imposto, 2)
        
    def get_aliquota_efetiva(self):
        imposto_devido = self.get_imposto_devido()
        total_rendimentos = self.get_total_rendimentos()
        
        if total_rendimentos == 0:
            return 0.0
            
        aliquota = (imposto_devido / total_rendimentos) * 100
        return round(aliquota, 2)