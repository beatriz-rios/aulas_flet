import flet as ft
import random  

def main(page: ft.Page):
    
    opcoes_animais = ["Gato", "Cachorro", "Suricato"]
    
    #  Sorteia o primeiro animal
    imagem_correta = random.choice(opcoes_animais)

    # Texto para feedback
    mensagem = ft.Text(
        f"Qual é o {imagem_correta}?",
        text_align=ft.TextAlign.CENTER,
        size=20,
        height=50
    )

    # Função Jogar
    def jogar(e):
        imagem_selecionada = e.control.content.value
        if imagem_selecionada == imagem_correta:
            e.control.bgcolor = ft.Colors.GREEN_200
            e.control.image.opacity = 0.3
            e.control.content.value = "❤️"
            e.control.content.size = 40
            mensagem.value = "Parabéns! Você acertou."
        else:
            e.control.bgcolor = ft.Colors.RED_200
            e.control.image.opacity = 0.3
            e.control.content.value = "🙁"
            e.control.content.size = 40
            mensagem.value = f"Ops! Não é o {imagem_correta}. Tente de novo."
        
        container_gato.on_click = None
        container_cachorro.on_click = None
        container_suricato.on_click = None

        btn_jogar_novamente.visible = True

        page.update()
    
    # Função Jogar Novamente
    def jogar_novamente(e):
        nonlocal imagem_correta  # Permite alterar a variável que está fora da função
        
        # 4. Sorteia um novo animal para a próxima rodada
        imagem_correta = random.choice(opcoes_animais)
        
        btn_jogar_novamente.visible = False
        mensagem.value = f"Qual é o {imagem_correta}?"

        container_gato.image.opacity = 1.0
        container_gato.on_click = jogar
        container_gato.content.size = 0
        container_gato.content.value = "Gato"
        container_gato.bgcolor = ft.Colors.GREY_200 

        container_cachorro.image.opacity = 1.0
        container_cachorro.on_click = jogar
        container_cachorro.content.size = 0
        container_cachorro.content.value = "Cachorro"
        container_cachorro.bgcolor = ft.Colors.GREY_200 

        container_suricato.image.opacity = 1.0
        container_suricato.on_click = jogar
        container_suricato.content.size = 0
        container_suricato.content.value = "Suricato"
        container_suricato.bgcolor = ft.Colors.GREY_200 
        
        page.update()

    # Container GATO
    container_gato = ft.Container(
        content=ft.Text(
            "Gato",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/gato.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container CACHORRO
    container_cachorro = ft.Container(
        content=ft.Text(
            "Cachorro",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/dog.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Container SURICATO
    container_suricato = ft.Container(
        content=ft.Text(
            "Suricato",
            size=0
        ),
        image=ft.DecorationImage(
            src="images/suricato.jpg",
            fit=ft.BoxFit.COVER
        ),
        width=120,
        height=120,
        margin=10,
        bgcolor=ft.Colors.GREY_200,
        border_radius=10,
        alignment=ft.Alignment(0, 0),
        ink=True,
        on_click=jogar
    )

    # Botão "Jogar Novamente"
    btn_jogar_novamente = ft.ElevatedButton( # Alterado para ElevatedButton (costuma ter melhor visibilidade)
        "Jogar Novamente",
        visible=False,
        on_click=jogar_novamente
    )

    page.add(
        ft.Column(
            [
                ft.Text(
                    "Selecione a imagem certa",
                    size=24,
                    weight="bold"
                ),
                mensagem,
                ft.Row(
                    [
                        container_gato,
                        container_cachorro,
                        container_suricato
                    ],
                    alignment=ft.MainAxisAlignment.CENTER
                ),
                btn_jogar_novamente
            ],
            alignment=ft.MainAxisAlignment.CENTER,
            horizontal_alignment=ft.CrossAxisAlignment.CENTER,
            spacing=20
        )
    )

ft.run(main) 