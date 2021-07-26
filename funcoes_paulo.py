def calcular_distancia_euclidiana(carteira1, carteira2):
    distancia_euclidiana = (((carteira1[0] - carteira2[0]) ** 2) + ((carteira1[1] - carteira2[1]) ** 2) + ((carteira1[2] - carteira2[2]) ** 2) + ((carteira1[3] - carteira2[3]) ** 2)) ** 0.5
    return distancia_euclidiana

# Recebe uma lista de itens e retorna aquele que ocorre mais vezes (a moda)
def identificar_moda(itens):
    ocorrencias_por_item = []
    
    for item in itens:
        ocorrencia_por_item = {
            "qtd_ocorrencias" : itens.count(item),
            "item": item
        }
        ocorrencias_por_item.append(ocorrencia_por_item)
        
    ocorrencias_por_item.sort(reverse=True, key=lambda elemento: elemento["qtd_ocorrencias"])
    
    # Retornando a moda (perfil que mais ocorre na lista)
    return ocorrencias_por_item[0]["item"]

class Investidor:
    
    def __init__(self, cpf, perfil, carteira_investimentos):
        self.cpf = cpf
        self.perfil = perfil
        self.carteira_investimentos = carteira_investimentos
        
    #Identifica o perfil desse investidor em comparação com o perfil de outros investidores
    def identificar_perfil(self, investidores_para_comparar, k):
                
        lista_distancia_investidor = []
        
        for investidor_para_comparar in investidores_para_comparar:
            
            distancia = calcular_distancia_euclidiana(self.carteira_investimentos, investidor_para_comparar.carteira_investimentos)
        
            distancia_investidor = {
                "distancia" : distancia,
                "investidor": investidor_para_comparar
            }
        
            lista_distancia_investidor.append(distancia_investidor)
        
        lista_distancia_investidor.sort(key=lambda elemento: elemento["distancia"])
    
        perfis_mais_proximos = []
    
        for i in range(k):
            investidor_para_comparar = lista_distancia_investidor[i]["investidor"]
            perfis_mais_proximos.append(investidor_para_comparar.perfil)        
        
        perfil_mais_proximo = identificar_moda(perfis_mais_proximos)
        self.perfil = perfil_mais_proximo
        
    def imprimir_informacoes(self):
        print(f'CPF: {self.cpf}, Perfil: {self.perfil}, Carteira de investimentos: {self.carteira_investimentos}\n')
        