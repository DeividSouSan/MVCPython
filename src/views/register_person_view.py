from src.utils.clear_screen import clear_screen


class RegisterPersonView:
    @staticmethod
    def index() -> dict:
        clear_screen()
        print("Cadastrando Pessoa".center(50, '-'))

        person = {
            'name': input('Nome: '),
            'age': input('Idade: '),
            'phone': input('Telefone: ')
        }

        return person

    @staticmethod
    def success(response: dict) -> None:
        clear_screen()

        message = f'''
            Pessoa cadastrada com sucesso!

            Tipo: {response["type"]}
            Quantidade: {response["count"]}
        '''

        print(message)

    @staticmethod
    def failure(response: dict) -> None:
        clear_screen()

        message = f'''
            Pessoa NÃO foi cadastrada com sucesso.

            Erro: {response}
        '''

        print(message)
