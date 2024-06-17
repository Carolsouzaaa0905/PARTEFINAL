# Define the GestaoResiduos class.
class GestaoResiduos:
    def __init__(self):
        self.residuos = {}
        self.economia = 0

    def adicionar_residuo(self, tipo, quantidade):
        if tipo in self.residuos:
            self.residuos[tipo] += quantidade
        else:
            self.residuos[tipo] = quantidade

    def relatorio_residuos(self):
        texto = ""
        for tipo, quantidade in self.residuos.items():
            texto = texto + (f"{tipo}: {quantidade}kg\n")
        
        return texto

    def recomendacoes(self):
        texto = ""
        for tipo in self.residuos:
            if tipo == "concreto":
                texto = texto + ("- Concreto: Pode ser triturado e reutilizado como base para pavimentação.\n")
            elif tipo == "madeira":
                texto = texto + ("- Madeira: Pode ser reciclada ou utilizada para geração de energia.\n")
            elif tipo == "metal":
                texto = texto + ("- Metal: Deve ser enviado para reciclagem.\n")
            elif tipo == "vidro":
                texto = texto + ("- Vidro: Pode ser reciclado e reutilizado em produtos de vidro.\n")
            elif tipo == "plastico":
                texto = texto + ("- Plástico: Deve ser reciclado e reutilizado em produtos de plástico.\n")
            elif tipo == "papel":
                texto = texto + ("- Papel: Pode ser reciclado e reutilizado em produtos de papel.\n")
            elif tipo == "orgânico":
                texto = texto + ("- Orgânico: Pode ser compostado e utilizado como adubo.\n")
            else:
                texto = texto + (f"- {tipo}: Verificar regulamentações locais para destinação adequada.\n")
        return texto
    def calcular_economia(self):
        self.economia = 0
        for tipo, quantidade in self.residuos.items():
            if tipo == "concreto":
                self.economia += quantidade * 0.5  # economia de 50% ao reutilizar concreto
            elif tipo == "madeira":
                self.economia += quantidade * 0.3  # economia de 30% ao reciclar madeira
            elif tipo == "metal":
                self.economia += quantidade * 0.7  # economia de 70% ao reciclar metal
            elif tipo == "vidro":
                self.economia += quantidade * 0.4  # economia de 40% ao reciclar vidro
            elif tipo == "plastico":
                self.economia += quantidade * 0.2  # economia de 20% ao reciclar plástico
            elif tipo == "papel":
                self.economia += quantidade * 0.1  # economia de 10% ao reciclar papel
            elif tipo == "orgânico":
                self.economia += quantidade * 0.6  # economia de 60% ao compostar orgânico
        return (f"\nEconomia total: R$ {self.economia:.2f}")
