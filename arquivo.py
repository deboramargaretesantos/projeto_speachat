# Tela inicial:
    # Título: SpeaChat
    # Botão: Iniciar Chat
        # Quando clicar no botão:
        # Abrir um popup/modal/alerta
            # Título: Bem Vindo ao SpeaChat
            # Caixa de chat: Escreva seu nome no chat
            # Botão: Entrar no chat
                # Quando clicar no botão 
                # Sumir com o título
                # Sumir com o botão "Iniciar Chat"
                    # Carregar o chat
                    # Carregar o campo de enviar mensagem: Digite sua mensagem
                    # Botão Enviar 
                        # Quando clicar no botão enviar
                        # Enviar a mensagem
                        # Limpar a caixa de mensagem

import flet as ft

# criar uma função principal para rodar seu app
def main(pagina):
    # título
    titulo = ft.Text("SpeaChat")
    pagina.add(titulo)

    # botão inicial
    botao = ft.ElevatedButton("Iniciar Chat",)
    pagina.add(botao)
    
# executar essa função com o flet
ft.app(main)