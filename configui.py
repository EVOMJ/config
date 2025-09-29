import flet as ft

def suporte_view(page: ft.Page):
    page.title = "Suporte"
    page.theme_mode = ft.ThemeMode.DARK
    page.window.width = 400
    page.window.height = 600
    page.window.min_width = 400
    page.window.min_height = 600
    page.window.max_width = 400
    page.window.max_height = 600
    page.window.center()

    # ---------- Inputs ----------
    envidas = ft.TextField(label="Nome de usuário", width=350)
    mensagem = ft.TextField(
        label="Mensagem",
        multiline=True,   # permite várias linhas
        min_lines=4,
        max_lines=8,
        width=350,
    )

    # ---------- Função Enviar ----------
    def enviar_click(e):
        if envidas.value.strip() and mensagem.value.strip():
            page.open( ft.SnackBar(
                content=ft.Text(" Enviando com sucesso", color="white"),
                bgcolor="green"
            ))
            page.update()
        else:
            page.open  (ft.SnackBar(
                content=ft.Text(" Preencha todos os campos!", color="white"),
                bgcolor="red"
            ))
            page.update()

        page.snack_bar.open = True
        page.update()

    # ---------- Layout ----------
    conteudo = ft.Column(
        [
            ft.Text("SUPORTE", size=30, weight="bold"),
            
            envidas,
            mensagem,
            ft.ElevatedButton("Enviar", on_click=enviar_click, width=200),
        ],  
        alignment=ft.MainAxisAlignment.CENTER,
        horizontal_alignment=ft.CrossAxisAlignment.CENTER,
        expand=True,
    )

    page.add(conteudo)

# Executar app
ft.app(target=suporte_view)
