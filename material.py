import pandas as pd

class Material:

    def __init__(self):
        try:
            self.__tabelaMaterial = pd.read_excel("tabela_material.xlsx")
        except FileNotFoundError:
            self.__tabelaMaterial = pd.DataFrame({
                "material": ["concreto", "vidro", "plastico", "papel", "organico", "metal", "madeira"],
                "quantidade": ["10","10","10","10","10","10","10"],
                "organica": [False,False,False,False,True,False,True]
            })
            self.__atualizarTabela()

    def __atualizarTabela(self):
        self.__tabelaMaterial.to_excel("tabela_material.xlsx", index=False)

    def adicionarMaterial(self, material, quantidade, organica):
        novoMaterial = {
            "material": material,
            "quantidade": quantidade,
            "organica": organica
        }
        self.__tabelaMaterial = pd.concat([self.__tabelaMaterial, pd.DataFrame([novoMaterial])], ignore_index=True)
        self.__atualizarTabela()
    
    def listaTabelaMaterial(self):
        texto = ""
        i = 0

        if len(self.__tabelaMaterial) > 0:
            while i < len(self.__tabelaMaterial):
                texto += "----------------------------------\n"
                texto += ("Material: {}\n".format(self.__tabelaMaterial.loc[i, "material"]))
                texto += (f"Quantidade: {self.__tabelaMaterial.loc[i, 'quantidade']}\n")
                texto += (f"Organica: {self.__tabelaMaterial.loc[i, 'organica']}\n")
                texto += "----------------------------------\n"
                i += 1
        return texto
