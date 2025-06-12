import pytest
from imposto_renda import CalculadoraImpostoRenda

def test_cadastra_um_rendimento():
    calculadora = CalculadoraImpostoRenda()
    
    calculadora.cadastra_rendimento(1000.0)
    
    assert calculadora.get_total_rendimentos() == 1000.0

def test_cadastra_dois_rendimentos():
    calculadora = CalculadoraImpostoRenda()
    
    calculadora.cadastra_rendimento(1000.0)
    calculadora.cadastra_rendimento(500.0)
    
    assert calculadora.get_total_rendimentos() == 1500.0

def test_cadastra_uma_deducao():
    calculadora = CalculadoraImpostoRenda()
    
    calculadora.cadastra_deducao("Previdência", 100.0)
    
    assert calculadora.get_total_deducoes() == 100.0

def test_cadastra_multiplas_deducoes():
    calculadora = CalculadoraImpostoRenda()
    
    calculadora.cadastra_deducao("Previdência", 100.0)
    calculadora.cadastra_deducao("Dependente", 189.59)
    
    assert calculadora.get_total_deducoes() == 289.59

def test_calcula_base_de_calculo():
    calculadora = CalculadoraImpostoRenda()
    calculadora.cadastra_rendimento(5000.0)
    calculadora.cadastra_deducao("Previdência", 500.0)
    
    base_calculo = calculadora.get_base_de_calculo()
    
    assert base_calculo == 4500.0

@pytest.mark.parametrize("rendimento, deducao, imposto_esperado", [
    (1900.0, 0, 0.0),                                  
    (2000.0, 100, 0.0),                               
    (3000.0, 200, 67.20),                              
    (4000.0, 300, 200.20),                            
    (5000.0, 400, 398.87),                             
    (6000.0, 500, 643.14)                              
])
def test_calcula_imposto_devido(rendimento, deducao, imposto_esperado):
    calculadora = CalculadoraImpostoRenda()
    calculadora.cadastra_rendimento(rendimento)
    calculadora.cadastra_deducao("Dedução Genérica", deducao)
    
    imposto_devido = calculadora.get_imposto_devido()
    
    assert imposto_devido == imposto_esperado

def test_calcula_aliquota_efetiva():
    
    calculadora = CalculadoraImpostoRenda()
    calculadora.cadastra_rendimento(6000.0)
    calculadora.cadastra_deducao("Previdência", 500.0) # Base: 5500.0, Imposto: 643.14

    aliquota = calculadora.get_aliquota_efetiva()
    
    # Verificação
    # Imposto (643.14) / Rendimento Total (6000.0) * 100
    assert aliquota == 10.72