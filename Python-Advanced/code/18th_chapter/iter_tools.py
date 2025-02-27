from dataclasses import dataclass
import itertools


@dataclass
class Item:
    name: str
    weight: float

def main() -> None:
    inventory = [
        Item(name="apple", weight=1.0),
        Item(name="banana", weight=2.0),
        Item(name="orange", weight=3.0),
        Item(name="kiwi", weight=4.0),
        Item(name="grape", weight=5.0),
    ]

    #filterfalse
    print(list(itertools.filterfalse(lambda item: item.weight < 3, inventory)))

    #starmap
    print(list(itertools.starmap(lambda x,y: x*y,[(2,6),(8,4),(5,3)])))

    # chain
    values: list[str] = ["a","b","c"]
    perms = itertools.chain(values, ["d","e","f"])
    print(list(perms))

    #permutation and combination
    playing_cards: list[str] = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    
    perms = itertools.permutations(playing_cards, 2)
    for perm in perms:
        print(perm)

    combs = itertools.combinations(playing_cards, 2)
    # for comb in combs:
    #     print(comb)
    print(list(combs))


    #accumulate
    subtotals = [2,5,7,5,3,3]
    for i in itertools.accumulate(subtotals):
        print(i)

    #repeat
    for i in itertools.repeat(10,5):
        print(i)

    #count
    for i in itertools.count(10,5):
        print(i)
        if i == 50:
            break
if __name__ == "__main__":
    main()