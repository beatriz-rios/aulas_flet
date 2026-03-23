import flet as ft

def main(page: ft.Page):
    page.title = "Column"
    page.bgcolor = "red"

    page.add(
        ft.Container(
            content = ft.Column(
                controls = [
                    ft.Text("Topo da tela"),
                    ft.Button(content = "Botão do meio"),
                    ft.Text("Base da Tela")
                ],
                alignment= ft.MainAxisAlignment.CENTER,
                horizontal_alignment= ft.CrossAxisAlignment.CENTER,
                spacing=20
            )
        )
    )
ft.run(main)