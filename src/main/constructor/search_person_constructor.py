from src.controllers.person_controller import PersonController
from src.views.search_person_view import SearchPersonView
from src.utils.wait_key import wait_key

def search_person_constructor():
    name = SearchPersonView.index()

    controller = PersonController()
    response = controller.search(name)

    if response['success']:
        SearchPersonView.success(response["response"])
    else:
        SearchPersonView.failure(response["error"])

    wait_key()