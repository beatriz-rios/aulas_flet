import flet as ft

def main(page: ft.Page):
    def mostrar(e):
        page.add(
            ft.Text("Miau!prrrrrr..."),
            ft.Image(
                src='images/gato.jpg',
                height=120
            )
        )

    page.add(
            ft.Text('Eu sou um gato muito fofo!'),
            
            ft.Button(
                content='Clique aqui para eu ronronar!',
                on_click=mostrar
            )
        )

ft.run(main)