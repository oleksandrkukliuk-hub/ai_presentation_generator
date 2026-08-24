import json
from pathlib import Path
from types import MappingProxyType

_SETTINGS_FILE = Path(__file__).parent / "settings.json"


class Settings:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)

        return cls._instance

    def __init__(self):
        if hasattr(self, "_settings"):
            return

        self.json_settings_path = _SETTINGS_FILE
        self._load()

    def _load(self):
        with open(self.json_settings_path, "r", encoding="utf-8") as file:
            data = json.load(file)

        self._settings = data
        self._settings["AI"] = self._readonly(data["AI"])

    def _readonly(self, data):
        if isinstance(data, dict):
            return MappingProxyType({
                key: self._readonly(value)
                for key, value in data.items()
            })

        if isinstance(data, list):
            return tuple(
                self._readonly(value)
                for value in data
            )

        return data

    def _save(self):
        data = dict(self._settings)
        data["AI"] = self._to_dict(data["AI"])

        with open(self.json_settings_path, "w", encoding="utf-8") as file:
            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=4
            )

    def _to_dict(self, data):
        if isinstance(data, MappingProxyType):
            return {
                key: self._to_dict(value)
                for key, value in data.items()
            }

        if isinstance(data, tuple):
            return [
                self._to_dict(value)
                for value in data
            ]

        return data

    def __getitem__(self, item):
        return self._settings[item]

    def __setitem__(self, key, value):
        if key not in self._settings:
            raise KeyError(key)

        if key == "AI":
            raise PermissionError(
                "AI settings cannot be changed"
            )

        self._settings[key] = value
        self._save()


settings = Settings()

if "__main__" == __name__:
    print(settings["language"])
    settings["language"] = "english"
    print(settings["language"])
