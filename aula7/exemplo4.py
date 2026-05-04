import flet as ft

def main(page: ft.Page):
    def mostrar_nome(e):
        texto_resultado.value = f"Olá, {texto_nome.value}!"
        page.update()
    texto_nome = ft.TextField(
        label = "Digite seu nome",
        hint_text = "Rafael"
    )
    
    botao =ft,Button(
        content = "mostrar seu nome",
        on_click = mostrar_nome
    )
    
    texto_resultado = ft.Text()
    page.add(texto_nome)

ft.run(main)