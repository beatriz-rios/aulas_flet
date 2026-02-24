import flet as ft  # Importa a biblioteca Flet para criar a interface gráfica

# Define uma classe que herda de ft.Container (uma caixa que agrupa elementos)
class CalculatorApp(ft.Container):
    def __init__(self):
        super().__init__()  # Inicializa a classe pai (Container)
        self.width = 350    # Define a largura da calculadora como 350 pixels
        self.bgcolor = ft.Colors.BLACK  # Define a cor de fundo do container como preto
        self.border_radius = ft.BorderRadius.all(20)  # Arredonda as bordas em 20 pixels
        self.padding = 20   # Adiciona um espaçamento interno de 20 pixels
        
        # Variável de texto que armazena a conta que está sendo montada (ex: "5+5")
        self.expression = "" 

        # Cria o elemento de texto que será o visor (display) da calculadora
        self.result = ft.Text(value="0", color=ft.Colors.WHITE, size=40)

        # Define o conteúdo do container como uma Coluna (elementos um abaixo do outro)
        self.content = ft.Column(
            controls=[
                # Primeira linha da coluna: exibe o visor alinhado à direita
                ft.Row(controls=[self.result], alignment=ft.MainAxisAlignment.END),
                
                # Linha 1 de botões: Funções especiais e divisão
                ft.Row(controls=[
                    self.ExtraActionButton("AC"),   # Botão de limpar
                    self.ExtraActionButton("+/-"),  # Botão de inverter sinal
                    self.ExtraActionButton("%"),    # Botão de porcentagem
                    self.ActionButton("/"),         # Botão de dividir
                ]),
                
                # Linha 2 de botões: Números 7, 8, 9 e multiplicação
                ft.Row(controls=[
                    self.DigitButton("7"),
                    self.DigitButton("8"),
                    self.DigitButton("9"),
                    self.ActionButton("*"),
                ]),
                
                # Linha 3 de botões: Números 4, 5, 6 e subtração
                ft.Row(controls=[
                    self.DigitButton("4"),
                    self.DigitButton("5"),
                    self.DigitButton("6"),
                    self.ActionButton("-"),
                ]),
                
                # Linha 4 de botões: Números 1, 2, 3 e soma
                ft.Row(controls=[
                    self.DigitButton("1"),
                    self.DigitButton("2"),
                    self.DigitButton("3"),
                    self.ActionButton("+"),
                ]),
                
                # Linha 5 de botões: Zero (expandido), ponto e igual
                ft.Row(controls=[
                    self.DigitButton("0", expand=2), # Ocupa o dobro de espaço
                    self.DigitButton("."),
                    self.ActionButton("="),
                ]),
            ]
        )

    # Função que é chamada toda vez que qualquer botão é clicado
    def button_clicked(self, e):
        # Obtém o texto escrito dentro do botão que disparou o evento
        data = e.control.content.value
        
        # Se clicar em AC, limpa a memória e volta o visor para "0"
        if data == "AC":
            self.expression = ""
            self.result.value = "0"
        
        # Se clicar em =, tenta resolver a conta acumulada
        elif data == "=":
            try:
                # eval() interpreta a string como código matemático (ex: "2+3" vira 5)
                self.result.value = str(eval(self.expression))
                self.expression = self.result.value # Permite usar o resultado na próxima conta
            except:
                self.result.value = "Erro" # Caso a conta seja inválida (ex: 5/0)
                self.expression = ""
        
        # Se clicar em +/-, inverte o sinal do número atual
        elif data == "+/-":
            if self.expression:
                if self.expression.startswith("-"):
                    self.expression = self.expression[1:] # Remove o sinal de menos
                else:
                    self.expression = "-" + self.expression # Adiciona o sinal de menos
                self.result.value = self.expression

        # Para números e operadores (+, -, *, /)
        else:
            # Se o visor estiver com "0" ou "Erro", substitui pelo novo caractere
            if self.result.value == "0" or self.result.value == "Erro":
                self.expression = data
            else:
                self.expression += data # Concatena o novo caractere à expressão existente
            self.result.value = self.expression # Atualiza o texto do visor

        self.update() # Comando obrigatório do Flet para atualizar a tela visualmente

    # Método para criar botões numéricos (cinza escuro)
    def DigitButton(self, text, expand=1):
        return ft.ElevatedButton(
            content=ft.Text(text, size=20), # Texto do botão
            bgcolor=ft.Colors.WHITE_24,    # Cor de fundo
            color=ft.Colors.WHITE,         # Cor da fonte
            expand=expand,                  # Define se o botão cresce para ocupar a linha
            on_click=self.button_clicked,   # Define a função que será chamada ao clicar
            # Torna o botão redondo se não estiver expandido
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20) if expand==1 else None
        )

    # Método para criar botões de operação (laranja)
    def ActionButton(self, text):
        return ft.ElevatedButton(
            content=ft.Text(text, size=20),
            bgcolor=ft.Colors.ORANGE,
            color=ft.Colors.WHITE,
            on_click=self.button_clicked,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20)
        )

    # Método para criar botões de funções extras (cinza claro)
    def ExtraActionButton(self, text):
        return ft.ElevatedButton(
            content=ft.Text(text, size=20, color=ft.Colors.BLACK),
            bgcolor=ft.Colors.BLUE_GREY_100,
            on_click=self.button_clicked,
            style=ft.ButtonStyle(shape=ft.CircleBorder(), padding=20)
        )

# Função principal que configura a janela do aplicativo
def main(page: ft.Page):
    page.title = "Calculadora Flet"  # Define o título da janela
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER  # Centraliza na horizontal
    page.vertical_alignment = ft.MainAxisAlignment.CENTER    # Centraliza na vertical
    
    # Cria a instância da nossa calculadora
    calc = CalculatorApp()
    
    # Adiciona a calculadora dentro da página do app
    page.add(calc)

# Ponto de entrada que inicia o programa
if __name__ == "__main__":
    ft.app(target=main) # Roda o aplicativo chamando a função main