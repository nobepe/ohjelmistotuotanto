import tomllib
from urllib import request
from project import Project


class ProjectReader:
    def __init__(self, url):
        self._url = url

    def get_project(self):
        # tiedoston merkkijonomuotoinen sisältö
        content = request.urlopen(self._url).read().decode("utf-8")

        # Ensimmäinen muuttaa TOML-tekstin Pythonin sanakirjaksi ja toinen tulostaa sen.
        data = tomllib.loads(content)

        project_data = data["project"]

        name = data["project"]["name"]
        description = project_data["description"]

        dependencies = [
            dependency.split(">=")[0]
            for dependency in project_data["dependencies"]
        ]

        dev_dependencies = [
            dependency.split(">=")[0]
            for dependency in data["dependency-groups"]["dev"]
        ]

        license = project_data["license"]

        authors = [
            author["name"]
            for author in project_data["authors"]
        ]

        # deserialisoi TOML-formaatissa oleva merkkijono ja muodosta Project-olio sen tietojen perusteella
        return Project(name, description, dependencies, dev_dependencies, license, authors)
    