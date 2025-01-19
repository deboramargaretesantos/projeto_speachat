# Tela inicial:
    # Título: SpeaChat
    # Botão: Iniciar Chat
        # Quando clicar no botão:
        # Abrir um popup/modal/alerta
            # Título: Bem Vindo ao SpeaChat
            # Caixa de chat: Escreva seu nome no chat
            # Botão: Entrar no chat
                # Quando clicar no botão 
                # Fechar popup
                # Sumir com o título
                # Sumir com o botão "Iniciar Chat"
                    # Carregar o chat
                    # Carregar o campo de enviar mensagem: Digite sua mensagem
                    # Botão Enviar 
                        # Quando clicar no botão enviar
                        # Enviar a mensagem
                        # Limpar a caixa de menasagem

import flet as ft

def main(pagina):
    titulo = ft.Text("SpeaChat")

    def enviar_mensagem_tunel(mensagem): 
        texto = ft.Text (mensagem)
        chat.controls.append(texto)
        pagina.update()

    pagina.pubsub.subscribe(enviar_mensagem_tunel)

    def enviar_mensagem(evento):
        nome_usuario = caixa_nome.value
        texto_campo_mensagem = campo_enviar_mensagem.value
        mensagem = (f"{nome_usuario}: {texto_campo_mensagem}")
        pagina.pubsub.send_all(mensagem)
        campo_enviar_mensagem.value = ""
        pagina.update()
    
    campo_enviar_mensagem = ft.TextField(label="Digite aqui a sua mensagem", on_submit=enviar_mensagem)
    botao_enviar = ft.ElevatedButton("Enviar", on_click=enviar_mensagem)
    linha_enviar = ft.Row([campo_enviar_mensagem, botao_enviar])  

    chat = ft.Column()

    def entrar_chat(evento):
        popup.open=False
        pagina.remove(titulo)
        pagina.remove(botao)
        pagina.add(chat)

        pagina.add(linha_enviar) 
        nome_usuario = caixa_nome.value      
        texto_mensagem = ft.Text(f"{nome_usuario} entrou no chat",  size=12, italic=True, color=ft.colors.ORANGE_500)
        chat.controls.append(texto_mensagem)
        pagina.update()

    titulo_popup = ft.Text("Bem Vindo ao SpeaChat")
    caixa_nome = ft.TextField(label="Digite seu nome")
    botao_popup = ft.ElevatedButton("Entrar no chat", on_click=entrar_chat)

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