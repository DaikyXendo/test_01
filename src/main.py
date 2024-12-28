import flet as ft
import sympy as sp

x = sp.Symbol("x")


def main(page: ft.Page):
    counter = ft.Text("0", size=50)

    def increment_click(e):
        counter.value = str(eval("sp.diff(sin(x), x)"))
        counter.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.Icons.ADD, on_click=increment_click
    )
    page.add(
        ft.SafeArea(
            ft.Container(
                counter,
                alignment=ft.alignment.center,
            ),
            expand=True,
        )
    )


ft.app(main)

