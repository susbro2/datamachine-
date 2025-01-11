class Customer:
    def __init__(self, customer_id, name, email, phone, prescription, last_visit_date, creator_name, date_time):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone = phone
        self.prescription = prescription
        self.last_visit_date = last_visit_date
        self.creator_name = creator_name
        self.date_time = date_time

    def __str__(self):
        return (f"Customer[ID={self.customer_id}, Name={self.name}, Email={self.email}, Phone={self.phone}, "
                f"Prescription={self.prescription}, Last Visit={self.last_visit_date}, Creator={self.creator_name}, "
                f"DateTime={self.date_time}]")