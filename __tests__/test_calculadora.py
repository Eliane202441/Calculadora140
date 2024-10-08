# 1- Bibliotecas, framework e referências externas
import pytest
#funções que serão testadas 
from calculadora.calculadora import somar_dois_numeros, subtrair_dois_numeros, multiplicar_dois_numeros, dividir_dois_numeros

# 2- testes

def test_somar_dois_numeros():
    # padrão /standard AAA  ( se diz triplo A / 3A) 
    # Arrange/ prapara/ configura
    # Dados entrada e saída 
    num1 = 5
    num2 = 7
    resultado_esperado = 12
    # Act / executa
    resultado_obtido = somar_dois_numeros(num1, num2)

    # assert / valida
    assert resultado_esperado == resultado_obtido

    def test_subtrair_dois_numeros():
        #configura 
      num1 = 10
      num2 = 6
      resultado_esperado = 4

        #executa 
      resultado_obtido = subtrair_dois_numeros(num1, num2)

        #valida
    assert  resultado_esperado == resultado_obtido
