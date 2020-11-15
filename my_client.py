from xml_rpc import XMLRPC_API, myprint

import ssl

ssl._create_default_https_context = ssl._create_unverified_context

ODOO_BACKEND = 'http://localhost:8069'
ODOO_DB = 'db1'
ODOO_USER = 'ngatran11297@gmail.com'
ODOO_PASS = 'Ngatran@11297'


def main():
    client = XMLRPC_API(url=ODOO_BACKEND, db=ODOO_DB, username=ODOO_USER, password=ODOO_PASS)
    # Create
    id = client.create(model_name="zoo.animal", data_dict={"name": "Nga"})
    print("Created animal @ %d" % id)

    # Read
    myprint(client.read(model_name='zoo.animal',
                        conditions=[('id', '>=', 1)],
                        params={'fields': ['name', 'dob'], }), title='Zoo Animals')

    # Update
    client.update(model_name="zoo.animal", id_list=[id], new_data_dict={"name": "MKyz"})
    print("Updated animal @ %d" % id)

    # Delete
    client.delete(model_name="zoo.animal", id_list=[id])
    print("Delted animal @ %d" % id)


if __name__ == "__main__":
    main()