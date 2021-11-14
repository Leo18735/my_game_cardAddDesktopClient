import tkinter as tk
from utils import get_config
from Information import Information
from Settings import Settings
from Tcp import Tcp


class Window:
    def __init__(self) -> None:
        self._config_path: str = "config.json"
        self._config: dict = {}

        self._auth_token = "lfyCK9vUn9rKKu2AKlkAlfyCK9lUn9rKKu2AKlkAlfyCK9vUn9rKKu2AKlkA"

        self._root: tk.Tk = tk.Tk()

        self._task1 = tk.StringVar()
        self._task2 = tk.StringVar()
        self._gender = tk.StringVar()
        self._drink = tk.IntVar()

        self._setup()
        self._load_config()
        return

    def start(self) -> None:
        self._root.mainloop()
        return

    def _setup(self) -> None:
        tk.Label(self._root, text="Task1").grid(row=0, column=0)
        tk.Label(self._root, text="Task2").grid(row=0, column=1)
        tk.Label(self._root, text="gender").grid(row=0, column=2)
        tk.Label(self._root, text="drink").grid(row=0, column=3)

        tk.Entry(self._root, textvariable=self._task1).grid(row=1, column=0)
        tk.Entry(self._root, textvariable=self._task2).grid(row=1, column=1)
        tk.Entry(self._root, textvariable=self._gender).grid(row=1, column=2)
        tk.Entry(self._root, textvariable=self._drink).grid(row=1, column=3)

        tk.Button(self._root, text="Exit", command=self._root.destroy).grid(row=2, column=1)
        tk.Button(self._root, text="Settings", command=self._open_settings).grid(row=2, column=2)
        tk.Button(self._root, text="Save", command=self._send).grid(row=2, column=3)
        return

    def _open_settings(self) -> None:
        settings: Settings = Settings(self._root, self._config_path)
        settings.start()
        self._load_config()
        return

    def _check_input(self) -> bool:
        try:
            try:
                int(self._drink.get())
            except Exception:
                raise Exception("Drink must be a number")

            if self._task1.get() == "":
                raise Exception("Task1 cannot be empty")
            if self._task2.get() == "":
                raise Exception("Task2 cannot be empty")
            if self._gender.get() == "":
                raise Exception("Gender cannot be empty")
            if self._gender.get() not in ["m", "f", "n"]:
                raise Exception("Gender must be either m (Male), f (Female) or n (Neutral)")
            return True
        except Exception as e:
            information: Information = Information(self._root, str(e))
            information.start()
        return False

    def _send(self) -> None:
        if not self._check_input():
            return

        if not self._check_settings():
            return

        data: str = f"{self._auth_token}post{self._task1.get()}|{self._task2.get()}|{self._drink.get()}|" \
                    f"{self._gender.get()} "
        try:
            Tcp(self._config["ip"], self._config["port"]).send(data)
        except Exception as e:
            information: Information = Information(self._root, str(e))
            information.start()
            return

        self._task1.set("")
        self._task2.set("")
        self._drink.set(0)
        self._gender.set("")

        information: Information = Information(self._root, "Sending successful")
        information.start()
        return

    def _check_settings(self) -> bool:
        try:
            if [x for x in ["ip", "port"] if x not in self._config]:
                raise Exception("You need to set ip and port in settings first")
            return True
        except Exception as e:
            information: Information = Information(self._root, str(e))
            information.start()
        return False

    def _load_config(self) -> None:
        self._config = get_config(self._config_path)
        return
