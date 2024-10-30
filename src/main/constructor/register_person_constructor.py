from time import sleep
from src.controllers.person_controller import PersonController
from src.utils.wait_key import wait_key
from src.views.register_person_view import RegisterPersonView

def register_person_constructor() -> None:
    person_data = RegisterPersonView.index()

    controller = PersonController()
    response = controller.register(person_data)

    if response['success']:
        RegisterPersonView.success(response["response"])
    else:
        RegisterPersonView.failure(response["error"])

    wait_key()
