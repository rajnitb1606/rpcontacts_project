from textual.app import App
from textual.widgets import Footer, Header, Label, Button, DataTable, Static
from textual.screen import Screen
from textual.containers import Grid, Horizontal, Vertical

class ContactsApp(App):
    CSS_PATH = "rpcontacts.tcss"
    BINDINGS = [
        ("m","toggle_dark","Toggle dark mode"),
        ("a","add","Ddd"),
        ("d","delete","Delete"),
        ("c","clear_all","Clear All"),
        ("q","request_quit","Quit")
    ]


    def compose(self):
        yield Header()

        yield Footer()

    def on_mount(self):
        self.title = 'RP Contacts'
        self.sub_title = 'A Contacts Book App With Textual & Python'

    def action_toggle_dark(self) -> None:
        if self.theme == 'textual-dark':
            self.theme = 'textual-light'
        else:
            self.theme = 'textual-dark'

    def action_request_quit(self):
        def check_answer(accepted):
            if accepted:
                self.exit()
        self.push_screen(QuestionDialog("Do you want to quit?"),check_answer)

class QuestionDialog(Screen):
    def __init__(self,message,*args,**kargs):
        super().__init__(*args, **kargs)
        self.message = message

    def compose(self):
        no_button = Button('No',variant='primary',id='no')
        no_button.focus()

        yield Grid(
            Label(self.message, id='question'),
            Button('Yes', variant='error', id='yes'),
            no_button,
            id='question-dialog'
        )

    def on_button_pressed(self,event):
        if event.button.id == 'yes':
            self.dismiss(True)
        else:
            self.dismiss(False)