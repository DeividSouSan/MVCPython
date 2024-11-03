from dataclasses import dataclass

@dataclass
class Person:
    name: str
    age: int
    phone: int

    def __post_init__(self):
        """Método chamado dentro do __init__ para validar os campos da classe Person.
        
        """
        if not (self.name and self.age and self.phone):
            raise Exception('Todos os campos são obrigatórios!')
