# Python Data Manager

This project is a simple data management system for handling customer information. It provides functionality to add, remove, and manage customer data efficiently.

## Project Structure

```
python-data-manager
├── src
│   ├── __init__.py
│   ├── customer.py
│   ├── customer_manager.py
│   └── storage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd python-data-manager
   ```

2. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. Import the necessary classes from the `src` package:
   ```python
   from src.customer import Customer
   from src.customer_manager import CustomerManager
   from src.storage import Storage
   ```

2. Create instances of `Customer` and manage them using `CustomerManager`:
   ```python
   customer_manager = CustomerManager()
   new_customer = Customer(customer_id=1, name="John Doe", email="john@example.com", phone="1234567890")
   customer_manager.add_customer(new_customer)
   ```

3. Use the `Storage` class to save or load customer data as needed.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any suggestions or improvements.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.