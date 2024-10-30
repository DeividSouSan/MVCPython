from src.models.entities.person import Person


class PersonRepository:
    def __init__(self) -> None:
        self.__persons = [] # "Banco de dados" in-memory da aplicação
        
    def add(self, new_person: Person) -> None:
        """Adiciona uma pessoa ao banco de dados da aplicação.

        Args:
            person (Person): pessoa a ser adicionada.
        """
        
        for person in self.__persons:
            if person.name == new_person.name:
                raise Exception('Nome já cadastrado!')
        
        self.__persons.append(new_person)
        print("->", self.__persons)
        input()
        
    def find_by_name(self, name: str) -> Person:
        """Busca uma pessoa no banco de dados por nome.

        Args:
            name (str): nome da pessoa a ser buscada.
        """
        person = [person for person in self.__persons if person.name == name]
        
        if not person:
            raise Exception('Pessoa não encontrada!')
        
        return person[0]
    
repository = PersonRepository()