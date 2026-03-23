import flet as ft #importando bibioteca e apelido(as)

def main(page: ft.Page):#def é definir a função
    def mostrar_mensagem(e):# (e) o "e" é um parametro de evento
        page.add(# page é a pagina e .add é adicionar um elemento a page 
            ft.Text("Eu vou ser o rei dos piratas!")
        )
    page.add(ft.Text("Olá meu nome é Luffy"),#ft.Text é uma component
             ft.Image(#para ter componentes de images nescessita de uma pasta assets para documentação
                 src='images/onepiece1.jpg',
                 height=150
             ),
             ft.Button(
                 content = 'Clique aqui',#defifnindo o conteudo do botao
                 on_click=mostrar_mensagem #dando função para o evento do botão
             )#resumindo: cria oq aparece no site. e depois de uma função para o evento chamando ela 
             
    )    

ft.run(main)