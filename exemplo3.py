import flet as ft


def main(page: ft.Page):
    page.scroll = ft.ScrollMode.AUTO

    page.add(
        ft.Image(
            src="images/paisagem.jpg",
        ),
        ft.Container(
            content=ft.Text("Paisagem" , color=ft.Colors.WHITE, size=32),
            image=ft.DecorationImage(
                src="images/paisagem.jpg",
                fit=ft.BoxFit.COVER
            ),
            bgcolor=ft.Colors.BLUE,
            width=999,
            height=600,
            alignment=ft.Alignment(0, 0)
        )

    )


ft.run(main)
