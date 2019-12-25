import json
import re

import requests

cust_with_adr_url = "http://localhost:5000/producer/customeraddresses/"
customer_url = "http://localhost:5000/producer/customer/"
address_url = "http://localhost:5000/producer/address/"


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
    def __init__(self, id=0, city='', state='', pincode=0, cid=0):
        self.id = id
        self.city = city
        self.state = state
        self.pincode = pincode
        self.cid = cid

    def __str__(self):
        return f"{self.__dict__}"

    def __repr__(self):
        return str(self)


def get_all_customers_with_address():
    responses = requests.get(cust_with_adr_url)
    return responses.json()


def get_all_active_customer():
    responses = requests.get(customer_url)
    return responses.json()


def get_single_active_customer(cid):
    responses = requests.get(customer_url + str(cid))
    return responses.json()


def get_all_active_address():
    responses = requests.get(address_url)
    return responses.json()


def get_single_active_address(aid):
    responses = requests.get(address_url + str(aid))
    return responses.json()


def save_customer(cust):
    responses = requests.post(customer_url, json=cust.__dict__)
    msg = responses.json().get("Success")
    if msg:
        return msg
    return responses.json().get("Status")


def update_customer(cust, cid):
    responses = requests.put(customer_url + str(cid), json=cust.__dict__)
    return responses.json()


def delete_customer(cid):
    responses = requests.delete(customer_url + str(cid))
    return responses.json()


def save_address(adr):
    responses = requests.post(address_url, json=adr.__dict__)
    msg = responses.json().get("Success")
    if msg:
        return msg
    return responses.json().get("Status")


def update_address(adr, aid):
    responses = requests.put(address_url + str(aid), json=adr.__dict__)
    return responses.json()


def delete_address(aid):
    responses = requests.delete(address_url + str(aid))
    return responses.json()


def save_customer_address(cust, adr):
    msg1 = save_customer(cust)
    cid = int(re.findall('\d+', msg1)[0])
    adr.__dict__.pop('cid')
    adr.__dict__['cid'] = str(cid)
    msg2 = save_address(adr)
    return msg1, msg2


def update_customer_address(cust, cid, adr, aid):
    msg1 = update_customer(cust, cid)
    msg2 = update_address(adr, aid)
    return msg1, msg2


def delete_customer_address(cid, aid):
    msg2 = delete_address(aid)
    msg1 = delete_customer(cid)
    return msg1, msg2