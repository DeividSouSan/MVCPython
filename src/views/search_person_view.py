from src.models.entities.person import Person
from src.utils.clear_screen import clear_screen

class SearchPersonView:
    @staticmethod
    def index() -> str:
        clear_screen()
        print("Procurando Pessoa por Nome".center(50, '-'))

        name = input('>> ')
        return name

    @staticmethod
    def success(response: dict) -> None:
        clear_screen()

        person_data: dict = response["attributes"]
        
        message = f'''
            Pessoa foi encontrada no sistema.

            Dados:
                Nome: {person_data["name"]}
                Idade: {person_data["age"]}
                WhatsApp: {person_data["phone"]}
        ''' 

        print(message)

    @staticmethod
    def failure(error: str) -> None:
        clear_screen()

        message = f'''
            Pessoa NÃO foi encontrada no sistema.

            Erro: {error}
        '''

        print(message)
