#higher order function
# function that takes another function as an argument or returns a function as a result


from dataclasses import dataclass
from typing import Callable, List

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


def is_eligible_for_promotion(customer: Customer) -> bool:
    return customer.age > 50

def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 60),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    # send_email_promotion(customers, is_eligible_for_promotion)
    send_email_promotion(customers, lambda c: c.age > 50)

if __name__ == "__main__":
    main()
