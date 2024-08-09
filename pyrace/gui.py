# RustyMotors is a project to build an online server for a legacy racing game
# Copyright (C) 2024 Molly Draven
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU Affero General Public License as published
# by the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Affero General Public License for more details.
#
# You should have received a copy of the GNU Affero General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import tkinter
from tkinter import StringVar, Tk, ttk, Text

def addLogMessage(message: str):
    logText.configure(state="normal")
    logText.insert(tkinter.END, f"{message}\n")
    logText.configure(state="disabled")


def calculate(*args):
    try:
        value = float(feet.get())
        meters.set((int(0.3048 * value * 10000.0 + 0.5) / 10000.0).__str__())
        addLogMessage(f"{feet.get()} feet is equal to {meters.get()} meters.")
    except ValueError:
        pass


root = Tk()
root.title("Feet to Meters")

mainframe = ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=("N, W, E, S"))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

feet = StringVar()
feet_entry = ttk.Entry(mainframe, width=7, textvariable=feet)
feet_entry.grid(column=2, row=1, sticky=("W, E"))

meters = StringVar()
ttk.Label(mainframe, textvariable=meters).grid(column=2, row=2, sticky=("W, E"))

ttk.Button(mainframe, text="Calculate", command=calculate).grid(
    column=3, row=3, sticky="W"
)

ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky="W")
ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky="E")
ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky="W")

logText = Text(mainframe, state="disabled", height=10, width=50)
logText.grid(column=1, row=4, columnspan=3, sticky=("W, E"))
addLogMessage("Hello, welcome to the PyRace GUI!")

for child in mainframe.winfo_children():
    child.grid_configure(padx=5, pady=5)

feet_entry.focus()
root.bind("<Return>", calculate)
