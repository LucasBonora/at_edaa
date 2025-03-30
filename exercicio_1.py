import heapq

class Processo:
    def __init__(self, id, tempo_execucao, prioridade):
        self.id = id
        self.tempo_execucao = tempo_execucao
        self.prioridade = prioridade
    
    def __lt__(self, other):
        return self.prioridade < other.prioridade
    
    def __repr__(self):
        return f"Processo(ID={self.id}, Tempo={self.tempo_execucao}, Prioridade={self.prioridade})"

class Escalonador:
    def __init__(self):
        self.heap = []
        self.processos = {}
    
    def adicionar_processo(self, id, tempo_execucao, prioridade):
        processo = Processo(id, tempo_execucao, prioridade)
        heapq.heappush(self.heap, processo)
        self.processos[id] = processo
        print(f"Adicionado: {processo}")
    
    def executar_proximo(self):
        if self.heap:
            processo = heapq.heappop(self.heap)
            del self.processos[processo.id]
            print(f"Executando: {processo}")
            return processo
        print("Nenhum processo para executar.")
        return None
    
    def modificar_prioridade(self, id, nova_prioridade):
        if id in self.processos:
            processo = self.processos[id]
            self.heap.remove(processo)
            heapq.heapify(self.heap)
            processo.prioridade = nova_prioridade
            heapq.heappush(self.heap, processo)
            print(f"Prioridade modificada: {processo}")
        else:
            print("Processo não encontrado.")

escalonador = Escalonador()
escalonador.adicionar_processo(1, 5, 3)
escalonador.adicionar_processo(2, 3, 1)
escalonador.adicionar_processo(3, 8, 2)

escalonador.executar_proximo()
escalonador.modificar_prioridade(3, 0)
escalonador.executar_proximo()
escalonador.executar_proximo()
