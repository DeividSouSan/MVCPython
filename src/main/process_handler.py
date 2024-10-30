from .constructor.main_constructor import main_constructor
from .constructor.search_person_constructor import search_person_constructor
from .constructor.register_person_constructor import register_person_constructor

def mainloop() -> None:
    while True:
        command = main_constructor()

        match command:
            case '1': register_person_constructor()
            case '2': search_person_constructor()
            case '5': exit()
            case _:
                print('Comando inválido')