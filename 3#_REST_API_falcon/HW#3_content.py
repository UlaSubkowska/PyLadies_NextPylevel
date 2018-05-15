"""
Rozszerz istniejące API o następujące elementy:
- aktualizowanie danych osoby metodami PATCH i PUT
- usuwanie osoby z systemu metodą DELETE
- spraw aby zmiany dokonane w systemie były trwałe - ponowne uruchomienie serwera nie może ich czyścić. W tym celu posłuż się plikiem trzymanym na dysku w którym składowane będą dane osób (zamiast zmiennej globalnej persons)
- rozszerz metody dokonujące zmiany w systemie o stosowną walidację (id i name musi być zawsze obecne - w przeciwnym razie wyrzuć wyjątek falcon.HTTPBadRequest)
- dodaj nowy zasób do reprezentowania hobby użytkowników pod adresem: /persons/{person_id}/hobbies. Obsłuż trzy rodzaje akcji - listowanie wszystkich hobby użytkownika, dodawanie nowego hobby oraz usuwanie istniejącego (brak możliwości edycji i wejścia w szczegóły)
"""

import json

import falcon

persons = [
    {'id': '1', 'name': 'Bob'},
    {'id': '2', 'name': 'Larry'},
]

class PersonBase:
    def get_persons(self):
        return persons

    def get_person(self, id):
        persons = self.get_persons()
        for person in persons:
            if person['id'] == id:
                return person

        return None

class PersonResource(PersonBase):
    def on_get(self, request, response):
        persons = self.get_persons()

        response.body = json.dumps(persons)

    def on_post(self, request, response):
        body = json.loads(request.stream.read())

        person = {
            'id': body.get('id'),
            'name': body.get('name'),
        }

        if not person['id'] or not person['name']:
            raise falcon.HTTPNotFound()

        persons.append(person)

        response.body = json.dumps(body)


class PersonDetailResource(PersonBase):
    def on_get(self, request, response, person_id):
        person = self.get_person(person_id)

        if not person:
            raise falcon.HTTPNotFound()

        response.body = json.dumps(person)


person = PersonResource()
person_detail = PersonDetailResource()

api = falcon.API()
api.add_route('/persons', person)
api.add_route('/persons/{person_id}', person_detail)