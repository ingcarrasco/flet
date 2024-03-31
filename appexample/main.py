import flet as ft

def main(page: ft.Page):
    page.title = "Test"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.update()
    BG= '#2C70CF'
    
    page.vertical_alignment = ft.MainAxisAlignment.CENTER
    page.horizontal_alignment = ft.CrossAxisAlignment.CENTER

    def change_page(e):
        content_page = page.controls[0].controls[0]
        if e.control.selected_index == 0:
            page.clean()
            page.add(
                ft.Column([

                    ft.Text("Hello, world!",size=30, weight='bold'),
                    ft.TextField(label="Your name", border_radius=30),
                    ft.Dropdown(
                        label="Color",
                        hint_text="Choose your favourite color?",
                        options=[
                            ft.dropdown.Option("Red"),
                            ft.dropdown.Option("Green"),
                            ft.dropdown.Option("Blue"),
                        ],
                        autofocus=True,
                        border_radius=30,
                    ),
                    ft.Checkbox(label="Unchecked by default checkbox", value=False),
                    ft.Checkbox(label="Unchecked by default checkbox", value=False),
                    ft.ElevatedButton("Say hello!")
                ])
            )
        if e.control.selected_index == 1:
            page.clean()
            page.add(
                ft.Column([
                    ft.Text('Y', size=30, weight='bold'),
                    ft.TextButton(text='Y')
                ])
            )
        if e.control.selected_index == 2:
            page.clean()
            page.add(
                ft.Column([
                    ft.Text('Z', size=30, weight='bold'),
                    ft.TextButton(text='Z')
                ])
            )
        page.update()

    page.navigation_bar = ft.CupertinoNavigationBar(
        bgcolor=BG,
        selected_index=0,
        inactive_color='white',
        active_color='black',
        border=ft.border.all(3,'white'),
        on_change=change_page,
        destinations=[
            ft.NavigationDestination(
                icon=ft.icons.HOME, label="Home"
            ),
            ft.NavigationDestination(
                icon=ft.icons.COMMUTE, label="Commute"
            ),
            ft.NavigationDestination(
                    icon=ft.icons.BOOKMARK_BORDER,
                    selected_icon=ft.icons.BOOKMARK,
                    label="Explore",
                ),
        ]
    )

    page.add(
        ft.Column([
            ft.Text('Bienvenido', size=30, weight='bold')
        ])
    )
        
ft.app(target=main)
