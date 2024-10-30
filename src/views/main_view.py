from src.utils.clear_screen import clear_screen

class MainView:
    @staticmethod
    def index() -> None:
        clear_screen()
        
        command_list = (
            ('1', 'Cadastrar Pessoa'), 
            ('2', 'Pesquisar Pessoa por Nome'), 
            ('5', 'Sair')
        )
        
        print("Sistema de Cadastro de Pessoas".center(50, '-'))
        for command, description in command_list:
            print(f'|{command} {description:>46}|')
        print(50*'-')
        
        command = input('>> ')
        return command