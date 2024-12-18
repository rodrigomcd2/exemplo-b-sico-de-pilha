class Historico:
    def __init__(self):
        self.pilha = []  # Inicia a pilha de sites acessados
        self.pilha_avancar = []  # Inicia uma segunda pilha para avançar pelos sites

    def acessar_sites(self, nome):#função de adicionar os sites
        self.pilha.append(nome)
        self.pilha_avancar.clear()# para garantir que o usuario não possa acessar sites mais antigos sem acessar os mais recentes primeiro

    def voltar(self):#função de voltar
        if self.pilha:
            site = self.pilha.pop()  # Remove um site da pilha principal
            self.pilha_avancar.append(site)  # Adiciona o mesmo site na pilha secundária
            print(f"\nVocê voltou para o site anterior: {self.pilha[-1] if self.pilha else 'nenhum site disponivel'}")#determina uma sentença para a condição
        else:
            print("\nNão há sites para voltar.")

    def exibir_historico(self):# mostra pilha
        print(f"Histórico: {self.pilha}")
        print(f"Sucessores: {self.pilha_avancar}")

    def voltar_para_o_msm_site(self):
        if self.pilha_avancar:
            site=self.pilha_avancar.pop() # remove o site da lista secundaria
            self.pilha.append(site) # retorna o site removido 
            print("\n Vocè voltou para o mesmo site")

        else:
            print("\nNão ha sites para avançar")


navegador = Historico()

navegador.acessar_sites("google.com")
navegador.acessar_sites("youtube.com")
navegador.acessar_sites("youtube.com/canal")
navegador.acessar_sites("youtube.com/canal/video")

navegador.exibir_historico()

navegador.voltar()
navegador.exibir_historico()

navegador.voltar()
navegador.exibir_historico()

navegador.voltar()
navegador.exibir_historico()

navegador.voltar()
navegador.exibir_historico()

navegador.voltar()
navegador.exibir_historico()

