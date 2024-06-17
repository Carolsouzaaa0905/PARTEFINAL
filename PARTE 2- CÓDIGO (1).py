# Import the necessary modules.
from gestao_residuos import GestaoResiduos
import interface
import PySimpleGUI as sg
from material import Material

def app():
    window_start = interface.start_window()
    window_cadastrar = None
    window_verificar_residuo = None
    gestao = GestaoResiduos()
    material = Material()

    while True:
        window, event, values = sg.read_all_windows()

        if window == window_start and (event == sg.WIN_CLOSED or event == "Sair"):
            
            break

        if window == window_start and event == "Cadastrar":
            window_start.hide()
            window_cadastrar = interface.cadastrar_window()

        if window == window_cadastrar and (event == sg.WIN_CLOSED or event == "Voltar"):
            window_start.un_hide()
            window_cadastrar.close()
            window_cadastrar = None

        if window == window_start and event == "Verificar Residuo":
            window_start.hide()
            window_verificar_residuo = interface.verificar_residuo_window()
        
        if window == window_verificar_residuo and (event == sg.WIN_CLOSED or event == "Voltar"):
            window_start.un_hide()
            window_verificar_residuo.close()
            window_verificar_residuo = None
        
        if window == window_verificar_residuo and event == "Verificar Residuo":
            tipo_residuo = window["tipo_residuo"].get()
            quantidade_residuo = float(window["quantidade_residuo"].get())
            gestao.adicionar_residuo(tipo_residuo, quantidade_residuo)
            sg.popup(f'{gestao.relatorio_residuos()}\n{gestao.recomendacoes()}\n{gestao.calcular_economia()}')
        
        if window == window_start and event == "Listar":
            sg.popup(material.listaTabelaMaterial())

        if window == window_cadastrar and event == "SALVAR":
            nome_material = window["material"].get()
            quantidade_material = window["quantidade"].get()
            organica = window["is_organica"].get()

            material.adicionarMaterial(nome_material, quantidade_material, organica)
            sg.popup("Material Adicionado!")

            window["material"].update("")
            window["quantidade"].update("")
            window["is_organica"].update(False)

            
    window_start.close()

# Run the main function.
if __name__ == "__main__":
    app()
    