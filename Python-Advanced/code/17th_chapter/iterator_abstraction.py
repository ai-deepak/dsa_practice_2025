from dataclasses import dataclass
from typing import Iterable


@dataclass(frozen=True)
class LineItem:
  price: int
  quantity: int

  def total_price(self) -> int:
    return self.price * self.quantity


def print_total_price(items: Iterable[LineItem]) -> None:
  for item in items:
    print(item.total_price())


def main() -> None:
  line_items = [
      LineItem(price=10, quantity=2),
      LineItem(price=20, quantity=3),
      LineItem(price=30, quantity=4),
  ]
  print_total_price(line_items)


if __name__ == "__main__":
    main()