import PySimpleGUI as sg

def start_window():
    sg.theme("Reddit")

    layout = [
        [sg.Button("Verificar Residuo")],
        [sg.Button("Listar")],
        [sg.Button("Cadastrar")],
        [sg.Button("Sair")]
    ]

    return sg.Window("Gestão de Residuos", layout=layout, finalize=True)

def verificar_residuo_window():
    sg.theme("Reddit")

    layout = [
        [sg.Text("Tipo de residuo:"), sg.Input(key="tipo_residuo")],
        [sg.Text("Quantidade:"), sg.Input(key="quantidade_residuo")],
        [sg.Button("Verificar Residuo")],
        [sg.Button("Voltar")]
    ]

    return sg.Window("Verifar Residuo", layout=layout, finalize=True)

def cadastrar_window():
    sg.theme("Reddit")

    layout = [
        [sg.Text("Material"), sg.Input(key="material")],
        [sg.Text("Quantidade"), sg.Input(key="quantidade")],
        [sg.Text("Organica"), sg.Check("", key="is_organica")],
        [sg.Button("SALVAR")],
        [sg.Button("Voltar")]
    ]

    return sg.Window("Cadastrar Material", layout=layout, finalize=True)
