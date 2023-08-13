'''
Este enunciado exige que o aluno utilize listas para armazenar os filhos de cada membro, 
dicionários para armazenar informações sobre cada membro e recursividade para buscar descendentes e antepassados.

'''

class Familia:
    def __init__(self):
        self.arvore = []

    def adicionar_membro(self, nome, idade, sexo, pai=None):
        membro = {
            "nome": nome,
            "idade": idade,
            "sexo": sexo,
            "filhos": []
        }

        if pai:
            pai_obj = self.buscar_membro(pai)
            if pai_obj:
                pai_obj["filhos"].append(membro)
            else:
                print(f"Pai {pai} não encontrado!")
                return
        else:
            self.arvore.append(membro)

    def buscar_membro(self, nome):
        for membro in self.arvore:
            if membro["nome"] == nome:
                return membro
            resultado = self._buscar_recursivo(membro["filhos"], nome)
            if resultado:
                return resultado
        return None

    def _buscar_recursivo(self, filhos, nome):
        for filho in filhos:
            if filho["nome"] == nome:
                return filho
            resultado = self._buscar_recursivo(filho["filhos"], nome)
            if resultado:
                return resultado
        return None

    def descendentes(self, nome):
        membro = self.buscar_membro(nome)
        if not membro:
            return []

        descendentes_lista = []
        for filho in membro["filhos"]:
            descendentes_lista.append(filho["nome"])
            descendentes_lista.extend(self.descendentes(filho["nome"]))
        return descendentes_lista

    def antepassados(self, nome, arvore=None):
        if not arvore:
            arvore = self.arvore

        for membro in arvore:
            for filho in membro["filhos"]:
                if filho["nome"] == nome:
                    return [membro["nome"]] + self.antepassados(membro["nome"])
            antepassados_lista = self.antepassados(nome, membro["filhos"])
            if antepassados_lista:
                return antepassados_lista
        return []

# Testando
familia = Familia()
familia.adicionar_membro("João", 70, "M")
familia.adicionar_membro("Carlos", 50, "M", "João")
familia.adicionar_membro("Pedro", 30, "M", "Carlos")
familia.adicionar_membro("Lucas", 10, "M", "Pedro")

print(f"Descendentes de João: {familia.descendentes('João')}")
print(f"Antepassados de Lucas: {familia.antepassados('Lucas')}")
