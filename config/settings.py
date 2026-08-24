import json
from copy import deepcopy
from pathlib import Path

_SETTINGS_FILE = Path(__file__).parent / "settings.json"


class SettingsSection:
    def __init__(self, data, save_callback, path, readonly_paths):
        object.__setattr__(self, "_data", data)
        object.__setattr__(self, "_save", save_callback)
        object.__setattr__(self, "_path", path)
        object.__setattr__(self, "_readonly_paths", readonly_paths)

    def __getattr__(self, name):
        data = object.__getattribute__(self, "_data")
        path = object.__getattribute__(self, "_path")
        readonly_paths = object.__getattribute__(
            self,
            "_readonly_paths"
        )

        if name not in data:
            raise AttributeError(name)

        value = data[name]
        current_path = f"{path}.{name}"

        if isinstance(value, dict):
            return SettingsSection(
                value,
                object.__getattribute__(self, "_save"),
                current_path,
                readonly_paths
            )

        return value

    def __setattr__(self, name, value):
        if name.startswith("_"):
            object.__setattr__(self, name, value)
            return

        data = object.__getattribute__(self, "_data")
        path = object.__getattribute__(self, "_path")
        readonly_paths = object.__getattribute__(
            self,
            "_readonly_paths"
        )

        if name not in data:
            raise AttributeError(name)

        current_path = f"{path}.{name}"

        if current_path in readonly_paths:
            raise AttributeError(
                f"Setting '{current_path}' is read-only"
            )

        data[name] = value

        object.__getattribute__(self, "_save")()

    def __iter__(self):
        data = object.__getattribute__(self, "_data")
        copy_data = deepcopy(data)

        for key, value in copy_data.items():
            yield key, value


class Settings:
    _instance = None

    _readonly_paths = {
        "AI",
        "AI.ai_content_generator",
        "AI.ai_slide_renderer",
        "AI_MODELS",
    }

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance._initialized = False

        return cls._instance

    def __init__(self):
        if self._initialized:
            return

        self.json_settings_path = _SETTINGS_FILE

        self._load()

        self._initialized = True

    def _load(self):
        with open(
                self.json_settings_path,
                "r",
                encoding="utf-8"
        ) as file:
            self._settings = json.load(file)

    def _save(self):
        with open(
                self.json_settings_path,
                "w",
                encoding="utf-8"
        ) as file:
            json.dump(
                self._settings,
                file,
                ensure_ascii=False,
                indent=4
            )

    def __getattr__(self, name):
        settings = object.__getattribute__(
            self,
            "_settings"
        )

        if name not in settings:
            raise AttributeError(name)

        value = settings[name]

        if isinstance(value, dict):
            return SettingsSection(
                value,
                self._save,
                name,
                self._readonly_paths
            )

        return value

    def __setattr__(self, name, value):
        if name.startswith("_") or name == "json_settings_path":
            object.__setattr__(self, name, value)
            return

        settings = object.__getattribute__(
            self,
            "_settings"
        )

        if name not in settings:
            raise AttributeError(name)

        if name in self._readonly_paths:
            raise AttributeError(
                f"Setting '{name}' is read-only"
            )

        settings[name] = value

        object.__getattribute__(
            self,
            "_save"
        )()


settings = Settings()

if "__main__" == __name__:
    print(settings["language"])
    settings["language"] = "english"
    print(settings["language"])
