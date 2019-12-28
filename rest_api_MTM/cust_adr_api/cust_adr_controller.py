import re
import requests
from flask import Flask, render_template, session, request
app = Flask(__name__)
# app = Flask(__name__, template_folder='rest_api_MTM\\cust_adr_api\\customer\\templates')
app.config['SECRET_KEY'] = '51616128779321SADKJAJ33'


customer_address_url = "http://localhost:5000/producer/custwithadr/"
address_customer_url = "http://localhost:5000/producer/adrwithcust/"
customer_url = "http://localhost:5000/producer/customer/"
address_url = "http://localhost:5000/producer/address/"
cust_adr_url = "http://localhost:5000/producer/custadr/"


class Customer:
    def __init__(self, id=0, name='', age=0, gender='', email=''):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.email = email

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


class custAdr:
    def __init__(self, id=0, cid=0, aid=0):
        self.id = id
        self.cid = cid
        self.aid = aid

    def __str__(self):
        return f'{self.__dict__}'

    def __repr__(self):
        return str(self)


def get_all_active_customer_with_address():
    response = requests.get(customer_address_url)
    return response.json()


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


def get_all_cust_adr():
    response = requests.get(cust_adr_url)
    return response.json()


def get_single_cust_adr(id):
    response = requests.get(cust_adr_url + str(id))
    return response.json()


def save_cust_adr(cuad):
    response = requests.post(cust_adr_url, json=cuad.__dict__)
    msg = response.json().get("Success")
    if msg:
        return msg, "Success"
    return response.json().get("Failed"), "Failed"


def update_cust_adr(cid, cuad):
    response = requests.post(cust_adr_url + str(cid), json=cuad.__dict__)
    msg = response.json().get("Success")
    if msg:
        return msg, "Success"
    return response.json().get("Failed"), "Failed"


def save_customer_with_address(cust1, adrlist):
    msg2 = ''
    msg1, act1 = save_customer(cust1)
    cid = int(re.findall('\d+', msg1)[0])
    for ad1 in adrlist:
        cuad = custAdr(cid=cid, aid=ad1)
        msg2, act2 = save_cust_adr(cuad)
    return msg1+msg2, act1


def update_customer_with_address(cid, cust1, adrlist):
    msg2 = ''
    msg1, act1 = update_customer(cid, cust1)
    for ad1 in adrlist:
        cuad = custAdr(cid=cid, aid=ad1)
        msg2, act2 = save_cust_adr(cuad)
    return msg1+msg2, act1


# a1 = Address(id=17, city='Pune7', state='MH', pincode=411047)
# res = save_address(a1)
# print(res)
# res = get_single_active_address(11)
# print(res)

