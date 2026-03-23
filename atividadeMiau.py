import flet as ft

def main(page: ft.Page):
    def mostrar(e):
        page.add(
            ft.Text("Minha gata subiu na prateleira e quebrou a miniatura"),
             ft.Image(
                src='images/gato.jpg',
                height=120
            )
        )

    page.add(
            ft.Text('Eu sou um gato muito fofo!'),
            ft.Image(
                src='images/cat.jpg',
                height=120
            ),
            ft.Button(
                content='Clique para ver oq eu aprontei!',
                on_click=mostrar
            )
        )

ft.run(main)