from enum import Enum 

# Classe para criar padrões de tipos de pagamento
class FormaDePagamento(Enum):
    DINHEIRO = 'dinheiro'
    PIX = 'pix'
    CREDITO = 'credito'
    DEBITO = 'debito'

