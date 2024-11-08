from enum import Enum

# Valores pré definios para o status de pedido
class StatusPedido(Enum):
    PENDENTE = 'pendente'
    APROVADO = 'aprovado' 
    CANCELADO = 'cancelado'
    ENTREGUE = 'entregue'

