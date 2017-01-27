from controller.base_controller import BaseController
from model.sample import Sample


class SampleController(BaseController):
    def get(self):
        samples = Sample.get_all()
        list_of_json_samples = []
        for sample in samples:
            list_of_json_samples.append({
                "id": sample.key.id(),
                "name": sample.name,
                "description": sample.description,
                "created_date": sample.created_date.isoformat(),
            })
        response = list_of_json_samples
        self._response_json(response)

    def post(self):
        name = self.request.get("name")
        description = self.request.get("description")

        sample = Sample.add(name, description)
        response = {
            "id": sample.key.id(),
            "name": sample.name,
            "description": sample.description,
            "created_date": sample.created_date.isoformat(),
        }
        self._response_json(response)
