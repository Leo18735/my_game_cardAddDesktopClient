from typing import Union
import tkinter as tk


class Information:
    def __init__(self, root: Union[tk.Tk, tk.Toplevel], information: str):
        self._root = tk.Toplevel(root)
        self._information = information

        self._setup()

    def _setup(self) -> None:
        tk.Label(self._root, text=self._information).grid(row=0, column=0)
        tk.Button(self._root, text="Ok", command=self._root.destroy).grid(row=1, column=0)
        return

    def start(self) -> None:
        self._root.mainloop()
        return
