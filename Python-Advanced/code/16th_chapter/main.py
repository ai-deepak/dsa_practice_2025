from dataclasses import dataclass
import os

@dataclass
class Item:
    name: str
    weight: float

def main()->None:

    inventory = [
        Item("laptop",1.5),
        Item("book",0.3),
        Item("phone",0.5),
        Item("charger",0.2),
        Item("headphone",0.1),
        Item("mouse",0.2),
    ]
    # inventory_iterator = inventory.__iter__()
    # print(inventory_iterator.__next__())
    # print(inventory_iterator.__next__())
    #simpler version
    # inventory_iterator = iter(inventory)
    # print(next(inventory_iterator))
    # print(next(inventory_iterator))
    #for loop way
    for item in inventory:
        print(item)

    file_path = os.path.join(os.path.dirname(__file__), "countries.txt")
    if os.path.exists(file_path):
        with open(file_path) as file:
            for line in iter(file.readline, ""):
                print(line, end="")
    else:
        print(f"File not found: {file_path}")

if __name__ == "__main__":
    main()