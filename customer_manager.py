class CustomerManager:
    def __init__(self):
        self.customers = {}

    def add_customer(self, customer):
        if customer.customer_id in self.customers:
            print(f"Customer with ID {customer.customer_id} already exists.")
        else:
            self.customers[customer.customer_id] = customer
            print(f"Customer {customer.name} added successfully.")

    def remove_customer(self, customer_id):
        if customer_id in self.customers:
            del self.customers[customer_id]
            print(f"Customer with ID {customer_id} removed successfully.")
        else:
            print(f"Customer with ID {customer_id} does not exist.")

    def get_customer(self, customer_id):
        return self.customers.get(customer_id, None)

    def list_customers(self):
        return list(self.customers.values())