from dataclasses import dataclass


@dataclass
class Person:
    name: str
    age: int
    phone: int

    def __post_init__(self):
        """Método chamado dentro do __init__ para validar os campos da classe Person.

        Raises:
            BlankFieldError: exceção lançada quando um campo obrigatório não é preenchido.
            FieldTypeError: exceção lançada quando um campo é preenchido com um tipo de dado inválido.
        """
        if not (self.name and self.age and self.phone):
            raise Exception('Todos os campos são obrigatórios!')

        if not (self.name.isalpha() and str(self.age).isnumeric() and str(self.phone).isnumeric()):
            raise Exception('Os campos estão no formato errado!')
