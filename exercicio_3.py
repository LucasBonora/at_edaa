class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def inserir(self, palavra):
        node = self.root
        for char in palavra:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end_of_word = True

    def buscar_prefixo(self, prefixo):
        node = self.root
        for char in prefixo:
            if char not in node.children:
                return None
            node = node.children[char]
        return node

    def autocompletar(self, prefixo):
        node = self.buscar_prefixo(prefixo)
        if node is None:
            return []
        return self._find_all_words(node, prefixo)

    def _find_all_words(self, node, prefixo):
        palavras = []
        if node.is_end_of_word:
            palavras.append(prefixo)
        for char, child_node in node.children.items():
            palavras += self._find_all_words(child_node, prefixo + char)
        return palavras

    def corrigir_palavra(self, palavra):
        sugestões = []
        self._corrigir(palavra, self.root, "", sugestões)
        return sugestões

    def _corrigir(self, palavra, node, prefixo, sugestões):
        if not palavra:
            if node.is_end_of_word:
                sugestões.append(prefixo)
            return
        char = palavra[0]
        if char in node.children:
            self._corrigir(palavra[1:], node.children[char], prefixo + char, sugestões)
        else:
            for child_char, child_node in node.children.items():
                self._corrigir(palavra[1:], child_node, prefixo + child_char, sugestões)
        
def distancia_levenshtein(s1, s2):
    len_s1, len_s2 = len(s1), len(s2)
    dp = [[0] * (len_s2 + 1) for _ in range(len_s1 + 1)]

    for i in range(len_s1 + 1):
        for j in range(len_s2 + 1):
            if i == 0:
                dp[i][j] = j
            elif j == 0:
                dp[i][j] = i
            elif s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            else:
                dp[i][j] = 1 + min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1])
    
    return dp[len_s1][len_s2]

def correção_automática(trie, palavra_digitada, limite_distancia=2):
    sugestões = trie.autocompletar(palavra_digitada)
    sugestões_corrigidas = []
    for sugestão in sugestões:
        if distancia_levenshtein(palavra_digitada, sugestão) <= limite_distancia:
            sugestões_corrigidas.append(sugestão)
    return sugestões_corrigidas

trie = Trie()

livros = ["A Revolução dos Bichos", "1984", "O Hobbit", "Dom Quixote", "O Senhor dos Anéis", "O Grande Gatsby"]
for livro in livros:
    trie.inserir(livro)

prefixo = "O S"
sugestoes_autocompletar = trie.autocompletar(prefixo)
print("Sugestões de autocompletar:", sugestoes_autocompletar)

palavra_digitada = "O Senho"
sugestoes_correção = correção_automática(trie, palavra_digitada)
print("Sugestões de correção automática:", sugestoes_correção)
