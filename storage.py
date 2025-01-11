def save_customers_to_file(customers, filename):
    with open(filename, 'w') as file:
        for customer_id, customer in customers.items():
            file.write(f"{customer_id},{customer.name},{customer.email},{customer.phone},{customer.prescription},"
                       f"{customer.last_visit_date},{customer.creator_name},{customer.date_time},"
                       f"{customer.re_sph},{customer.re_cyl},{customer.re_axis},{customer.re_add},"
                       f"{customer.le_sph},{customer.le_cyl},{customer.le_axis},{customer.le_add},"
                       f"{customer.frame_name},{customer.lens_name},{customer.frame_price},{customer.lens_price},"
                       f"{customer.total_price}\n")

def load_customers_from_file(filename):
    customers = {}
    with open(filename, 'r') as file:
        for line in file:
            data = line.strip().split(',')
            customer = Customer(
                customer_id=data[0],
                name=data[1],
                email=data[2],
                phone=data[3],
                prescription=data[4],
                last_visit_date=data[5],
                creator_name=data[6],
                date_time=data[7],
                re_sph=data[8],
                re_cyl=data[9],
                re_axis=data[10],
                re_add=data[11],
                le_sph=data[12],
                le_cyl=data[13],
                le_axis=data[14],
                le_add=data[15],
                frame_name=data[16],
                lens_name=data[17],
                frame_price=float(data[18]),
                lens_price=float(data[19]),
                total_price=float(data[20])
            )
            customers[customer.customer_id] = customer
    return customers