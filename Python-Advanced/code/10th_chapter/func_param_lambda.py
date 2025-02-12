#partial function application

from dataclasses import dataclass
from typing import Callable, List
import functools

@dataclass
class Customer:
    name: str
    age: int

def send_email_promotion(customers: List[Customer], is_eligible: Callable[[Customer],bool]):
    for customer in customers:
        print(f"checking {customer.name}")
        if is_eligible(customer):
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")


def is_eligible_for_promotion(customer: Customer, cutoff_age:int=50) -> bool:
    return customer.age > cutoff_age

def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 61),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    is_eligible_60 = functools.partial(is_eligible_for_promotion, cutoff_age=60)
    # send_email_promotion(customers, is_eligible_for_promotion)
    send_email_promotion(customers, is_eligible_60)

if __name__ == "__main__":
    main()
