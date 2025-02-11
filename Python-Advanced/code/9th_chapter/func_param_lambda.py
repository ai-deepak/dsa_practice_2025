from dataclasses import dataclass

@dataclass
class Customer:
    name: str
    age: int

def send_email_promotion(customers: list[Customer]):
    for customer in customers:
        print(f"checking {customer.name}")
        if customer.age < 50:
            print(f"{customer.name} is eligible for promotion")
        else:
            print(f"{customer.name} is not eligible for promotion")

def main() -> None:
    customers = [
        Customer("Alice", 34),
        Customer("Bob", 55),
        Customer("Charlie", 45),
        Customer("David", 60),
        Customer("Eve", 25),
        Customer("Frank", 40)
    ]
    send_email_promotion(customers)

if __name__ == "__main__":
    main()
