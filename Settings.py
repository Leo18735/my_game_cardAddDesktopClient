import tkinter
import tkinter as tk
from utils import get_config, store_config
from Information import Information


class Settings:
    def __init__(self, root: tk.Tk, config_path: str) -> None:
        self._config_path: str = config_path
        self._config: dict = {}

        self._ip = tk.StringVar()
        self._port = tk.IntVar()

        self._root = tk.Toplevel(root)

        self._load_config()
        self._setup()

    def _load_config(self) -> None:
        self._config = get_config(self._config_path)
        return

    def start(self) -> None:
        self._root.wait_window()

    def _setup(self) -> None:
        tk.Label(self._root, text="Ip").grid(row=0, column=0)
        tk.Label(self._root, text="Port").grid(row=0, column=1)

        tk.Entry(self._root, textvariable=self._ip).grid(row=1, column=0)
        tk.Entry(self._root, textvariable=self._port).grid(row=1, column=1)

        tk.Button(self._root, text="Save", command=self._save).grid(row=2, column=0)
        tk.Button(self._root, text="Exit", command=self._exit).grid(row=2, column=1)

        try:
            self._ip.set(self._config["ip"])
            self._port.set(self._config["port"])
        except KeyError:
            pass
        return

    def _save(self) -> None:
        if not self._check_input():
            return
        self._config["ip"] = self._ip.get()
        self._config["port"] = self._port.get()
        self._store_config()
        return

    def _check_input(self) -> bool:
        try:
            try:
                int(self._port.get())
            except (tkinter.TclError, ValueError):
                raise Exception("Port must be a number")

            if self._ip.get() == "":
                raise Exception("Ip cannot be empty")

            return True
        except Exception as e:
            information: Information = Information(self._root, str(e))
            information.start()
        return False

    def _store_config(self) -> None:
        store_config(self._config, self._config_path)
        return

    def _exit(self) -> None:
        self._root.destroy()
