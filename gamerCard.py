import flet as ft

def main(page.ft.Page):
    #Configurações da janela
    page.title = "Gamer Card"
    page.bgcolor = "1e1e1e"
    page.horizontal_aligment = ft.CrossAxisAlignment.CENTER
    page.vertical_aligment = ft.MainAxisAlignment.CENTER


    #Cabeçalho:Avatar(emoji) e nome do lado

    cabecalho = ft.Row(
        controls = [
            ft.Text("🥷", size=60), #emoji a prova de erros
            ft.Column(
                controls = [
                    ft.Text("SHADOW_NINJA", size=24, weight="bold", color="white"),
                    ft.Text("Nível 42 - Ninja das Sombras", size=24, color="grey300"),
                ], spacing=2
            )
        
        ],
        alignment=ft.MainAxisAlignment.CENTER
    )

    #status: Barra de hp, mp e xp