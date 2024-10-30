from src.models.entities.person import Person
from src.models.repositories.person_repository import repository


class PersonController:
	def __init__(self) -> None:
		self.__repository = repository

	def register(self, person_data: dict) -> dict:
		try:
			person = Person(**person_data)  # poderia utilizar facotry method aqui

			self.__repository.add(person)

			return {
				"success": True,
				"response": {
					"count": 1,
					"type": "Person",
					"attributes": person.__dict__
				}
			}
		except Exception as err:
			return {
				"success": False,
				"error": str(err)
			}

	def search(self, name: str) -> dict:
		try:
			if not name:
				raise Exception('Insira um nome!')

			person = self.__repository.find_by_name(name)

			return {
				"success": True,
				"response": {
					"count": 1,
					"type": "Person",
					"attributes": person.__dict__
				}
			}

		except Exception as err:
			return {
				"success": False,
				"error": str(err)
			}
