import flet as ft
#importa a biblioteca flet e cria um apelido (alias)

def main(page: ft.Page):
    page.title = "Meu primeiro App Flet" #Define o título da janela
    page.bgcolor = "red" #Define a cor de fundo da janela
    page.vertical_alignment = ft.MainAxisAlignment.CENTER #Alinha o conteúdo verticalmente ao centro    
    page.horizontal_alignment = ft.MainAxisAlignment.CENTER #Alinha o conteúdo horizontalmente ao centro    
    page.add(
        ft.Text("Bem vindo ao meu App!"),
        ft.Text("Aqui você pode criar o que quiser")
    )
ft.run(main)