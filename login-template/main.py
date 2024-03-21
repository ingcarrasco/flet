import flet as ft
from flet_core.control_event import ControlEvent

def main(page: ft.Page) -> None:

    # basic page settings/config
    page.title = "App Name"
    page.horizontal_alignment = page.vertical_alignment = "center"
    page.theme_mode = ft.ThemeMode.DARK
    page.window_width = 350
    page.window_height = 700

    # Enable button login
    def enableBtnLogin(e: ControlEvent) -> None:
       
        if all([txtPassword.value, txtUser.value]):
            btnLogin.disabled=False
        else:
            btnLogin.disabled=True
        page.update()

    # Function loginx
    def loginx(e: ControlEvent) -> None:
        print(txtPassword.value)
        print(txtUser.value)
        auth='OK'

        # Validate auth and groups 
        if auth == 'OK':
            groups=['SD','Altas','Varios']
            destination=[]
            # Menu by group permissions
            for x in groups:
                if x == 'SD':
                    destination.append(ft.NavigationDestination(label="SD",icon=ft.icons.CAR_CRASH))
                elif x == 'Varios':
                    destination.append(ft.NavigationDestination(label="Varios",icon=ft.icons.MORE_ROUNDED))

            page.clean()

            page.navigation_bar = ft.CupertinoNavigationBar(
                    bgcolor=ft.colors.BLUE_100,
                    inactive_color=ft.colors.GREY,
                    active_color=ft.colors.BLACK,
                    on_change=lambda e: print("Selected tab:", e.control.selected_index),
                    destinations=destination
                )
            page.add(ft.SafeArea(ft.Text("Body!")))

    t = False
    txtUser=ft.TextField(label="Usuario",prefix_text="domain\\")
    txtPassword=ft.TextField(label="Contraseña", password=True, can_reveal_password=True)
    btnLogin=ft.ElevatedButton("Login", on_click=loginx, disabled=True, icon="DOOR_FRONT_DOOR_OUTLINED")

    txtUser.on_change=enableBtnLogin
    txtPassword.on_change=enableBtnLogin

    page.add(
        txtUser,
        txtPassword,
        btnLogin, 
    )

ft.app(target=main, port=8550, view=ft.AppView.WEB_BROWSER) 