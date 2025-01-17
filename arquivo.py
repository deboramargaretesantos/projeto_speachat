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

def main(pagina):
    titulo = ft.Text("SpeaChat")

    titulo_popup = ft.Text("Bem Vindo ao SpeaChat")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat")

    popup = ft.AlertDialog(title = titulo_popup, content = caixa_nome, actions = [botao_popup])

    def abrir_popup(evento):
        pagina.dialog = popup
        popup.open = True
        pagina.update()
        print("Clique no botão")
  
    botao = ft.ElevatedButton("Iniciar Chat", on_click = abrir_popup)

    pagina.add(titulo)
    pagina.add(botao)

ft.app(main, view=ft.WEB_BROWSER)