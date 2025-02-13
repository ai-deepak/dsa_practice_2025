from dataclasses import dataclass
from typing import List, Callable
from functools import partial

@dataclass
class Customer:
    name: str
    membership: str
    purchase_amount: float

def is_eligible_for_discount(customer: Customer, threshold: float, premium_discount:bool=True) -> bool:
    if premium_discount and customer.membership == "premium":
        return customer.purchase_amount >= threshold * 0.8  # Premium members get 20% lower threshold
    return customer.purchase_amount >= threshold  # Regular customers need full threshold
    
def apply_discount(customers: List[Customer],is_eligible: Callable[[Customer],bool]) -> None:
    for customer  in customers:
        print(f"checking {customer.name}")
        if is_eligible(customer):
            print(f"{customer.name} is eligible for discount")
        else:
            print(f"{customer.name} is not eligible for discount")

def main() -> None:
    customers = [
        Customer("Alice", "premium", 100),
        Customer("Bob", "regular", 50),
        Customer("Charlie", "premium", 80),
        Customer("David", "regular", 40),
        Customer("Eve", "premium", 120),
        Customer("Frank", "regular", 160)
    ]
    is_eligible_100 = partial(is_eligible_for_discount, threshold=100, premium_discount=True)
    is_eligible_150 = partial(is_eligible_for_discount, threshold=150, premium_discount=False)
    apply_discount(customers, is_eligible_100)
    print("===========================")
    apply_discount(customers, is_eligible_150)

if __name__ == "__main__":
    main()