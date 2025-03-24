import flet as ft
from flet.core.charts.chart_grid_lines import ChartGridLines


class View(object):
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "TdP 2024 - Lab 04 - SpellChecker ++"
        self.page.horizontal_alignment = 'CENTER'
        self.page.theme_mode = ft.ThemeMode.LIGHT
        # Controller
        self._controller = None
        # UI elements
        self._title = None
        self._theme_switch = None
        self._menuLanguage = None
        self._menuSentence = None
        self._menuModality = None
        self._btnCheck = None
        self._txtOut = None
        self._messageTxt = None
        # define the UI elements and populate the page

    def add_content(self):
        """Function that creates and adds the visual elements to the page. It also updates
        the page accordingly."""
        # title + theme switch
        self._title = ft.Text("TdP 2024 - Lab 04 - SpellChecker ++", size=24, color="blue")
        self._theme_switch = ft.Switch(label="Light theme", on_change=self.theme_changed)
        row0=ft.Row(spacing=30, controls=[self._theme_switch, self._title, ],
                   alignment=ft.MainAxisAlignment.START)
        #riga 1
        self._menuLanguage=ft.Dropdown(label="Select language",
                                        width=1600,
                                        options=[
                                            ft.dropdown.Option("english"),
                                            ft.dropdown.Option("italian"),
                                            ft.dropdown.Option("spanish")
                                        ],
                                        expand=True,
                                        on_change=self._controller.handleLanguageSelection
                                        )
        row1=ft.Row(controls=[self._menuLanguage],alignment=ft.MainAxisAlignment.START)
        #riga 2
        self._menuModality=ft.Dropdown(label="Search modality",
                                        options=[
                                            ft.dropdown.Option("Default"),
                                            ft.dropdown.Option("Linear"),
                                            ft.dropdown.Option("Dichotomic")
                                        ],expand=True,
                                        on_change=self._controller.handleModalitySelection)
        self._menuSentence=ft.TextField(label="Add your sentence here", width=900)
        self._btnCheck=ft.ElevatedButton(text="Spell Check", on_click=self._controller.handleSpellCheck)
        row2=ft.Row(controls=[self._menuModality,self._menuSentence,self._btnCheck],alignment=ft.MainAxisAlignment.START)
        #riga 3
        self._txtOut=ft.ListView(expand=1, spacing=10,padding=20, auto_scroll=True) #OUTPUT DELLA STAMPA
        self._messageTxt=ft.Text(color="red") #PER GLI ERRORI
        # separè tra ogni correzione e l'altra

        self.page.add(row0,row1,row2,self._txtOut,self._messageTxt)

    def update(self):
        self.page.update()
    def setController(self, controller):
        self._controller = controller
    def theme_changed(self, e):
        """Function that changes the color theme of the app, when the corresponding
        switch is triggered"""
        self.page.theme_mode = (
            ft.ThemeMode.DARK
            if self.page.theme_mode == ft.ThemeMode.LIGHT
            else ft.ThemeMode.LIGHT
        )
        self._theme_switch.label = (
            "Light theme" if self.page.theme_mode == ft.ThemeMode.LIGHT else "Dark theme"
        )
        # self.__txt_container.bgcolor = (
        #     ft.colors.GREY_900 if self.page.theme_mode == ft.ThemeMode.DARK else ft.colors.GREY_300
        # )
        self.page.update()
