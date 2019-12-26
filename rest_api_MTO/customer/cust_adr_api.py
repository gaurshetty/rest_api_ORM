import requests
from flask import Flask, render_template, request, session

app = Flask(__name__)
app.config['SECRET_KEY'] = '128779321SADKJAJ33'

customer_address_url = "http://localhost:5000/producer/customeraddress/"
address_customer_url = "http://localhost:5000/producer/addresscustomer/"
customer_url = "http://localhost:5000/producer/customer/"
address_url = "http://localhost:5000/producer/address/"


class Customer:
    def __init__(self, id=0, name='', age=0, gender='', email='', aid=0):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email
        self.aid = aid

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)


class Address:
    def __init__(self, id=0, city='', state='', pincode=0):
        self.id = id
        self.city = city
        self.state = state
        self.pincode = pincode

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)


def get_all_active_customer_with_address():
    response = requests.get(customer_address_url)
    return response.json()


# res = get_all_active_customer_with_address()
# print(res)


def get_all_active_address_with_customer():
    response = requests.get(address_customer_url)
    return response.json()


def get_all_active_customers():
    response = requests.get(customer_url)
    return response.json()


def get_single_active_customer(cid):
    response = requests.get(customer_url + str(cid))
    return response.json()


def save_customer(cust):
    response = requests.post(customer_url, json=cust.__dict__)
    msg = response.json().get("Success")
    if msg:
        return msg, "Success"
    return response.json().get("Failed"), "Failed"


def update_customer(cid, cust):
    response = requests.put(customer_url + str(cid), json=cust.__dict__)
    msg = response.json().get("Success")
    if msg:
        return msg, "Success"
    return response.json().get("Failed"), "Failed"


def delete_customer(cid):
    response = requests.delete(customer_url + str(cid))
    return response.json()


# c1 = Customer(id=107, name='shetty7', age=32, gender='M', email='shetty7@g.in', aid=14)
# res = save_customer(c1)
# print(res)


def get_all_active_addresses():
    response = requests.get(address_url)
    return response.json()


def get_single_active_address(aid):
    response = requests.get(address_url + str(aid))
    return response.json()


def save_address(adr):
    response = requests.post(address_url, json=adr.__dict__)
    msg = response.json().get("Success")
    if msg:
        return msg, "Success"
    return response.json().get("Failed"), "Failed"


def update_address(aid, adr):
    response = requests.put(address_url + str(aid), json=adr.__dict__)
    msg = response.json().get("Success")
    if msg:
        return msg, "Success"
    return response.json().get("Failed"), "Failed"


def delete_address(aid):
    response = requests.delete(address_url + str(aid))
    return response.json()

# a1 = Address(id=17, city='Pune7', state='MH', pincode=411047)
# res = save_address(a1)
# print(res)
