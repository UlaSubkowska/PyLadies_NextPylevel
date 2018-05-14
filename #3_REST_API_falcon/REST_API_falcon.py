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