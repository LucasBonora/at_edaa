class Pacote:
    def __init__(self, id, prioridade, tempo_transmissao):
        self.id = id
        self.prioridade = prioridade
        self.tempo_transmissao = tempo_transmissao

    def __lt__(self, other):
        return self.prioridade < other.prioridade

class HeapMinimo:
    def __init__(self):
        self.heap = []

    def inserir(self, pacote):
        self.heap.append(pacote)
        self._heapify_up(len(self.heap) - 1)

    def remover(self):
        if len(self.heap) == 0:
            return None
        pacote = self.heap[0]
        self.heap[0] = self.heap[-1]
        self.heap.pop()
        self._heapify_down(0)
        return pacote

    def atualizar_prioridade(self, id, nova_prioridade):
        for i in range(len(self.heap)):
            if self.heap[i].id == id:
                self.heap[i].prioridade = nova_prioridade
                self._heapify_up(i)
                break

    def _heapify_up(self, indice):
        while indice > 0:
            pai = (indice - 1) // 2
            if self.heap[indice] < self.heap[pai]:
                self.heap[indice], self.heap[pai] = self.heap[pai], self.heap[indice]
                indice = pai
            else:
                break

    def _heapify_down(self, indice):
        tamanho = len(self.heap)
        while 2 * indice + 1 < tamanho:
            filho_esquerdo = 2 * indice + 1
            filho_direito = 2 * indice + 2
            menor_filho = filho_esquerdo

            if filho_direito < tamanho and self.heap[filho_direito] < self.heap[filho_esquerdo]:
                menor_filho = filho_direito

            if self.heap[indice] > self.heap[menor_filho]:
                self.heap[indice], self.heap[menor_filho] = self.heap[menor_filho], self.heap[indice]
                indice = menor_filho
            else:
                break

heap = HeapMinimo()

pacote1 = Pacote(1, 3, 10)
pacote2 = Pacote(2, 1, 5)
pacote3 = Pacote(3, 2, 7)

heap.inserir(pacote1)
heap.inserir(pacote2)
heap.inserir(pacote3)

pacote_removido = heap.remover()
print(f"Pacote removido: ID {pacote_removido.id}, Prioridade {pacote_removido.prioridade}")

heap.atualizar_prioridade(3, 0)

pacote_removido = heap.remover()
print(f"Pacote removido após atualização: ID {pacote_removido.id}, Prioridade {pacote_removido.prioridade}")
