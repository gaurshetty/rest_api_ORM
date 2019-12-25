from rest_api_ORM1.rest_api_OTO.producer.model import *
from flask import request
import json

db.create_all()

# http://localhost:5000/producer/customeraddresses/
@app.route("/producer/customeraddresses/", methods=['GET'])
def get_all_customer_address():
    customers = Customer.query.filter_by(active='Y').all()
    all_cust_info = []
    for customer in customers:
        custlist = customer.as_dict()
        custlist.pop('active')
        adr = customer.addresses
        if adr:
            adr = adr.as_dict()
            custlist['address'] = adr
        all_cust_info.append(custlist)
    return json.dumps(all_cust_info)


# http://localhost:5000/producer/customer/
@app.route("/producer/customer/", methods=['GET'])
def get_all_active_customers():
    cust_info = []
    customers = Customer.query.filter_by(active='Y').all()
    for customer in customers:
        customer = customer.as_dict()
        customer.pop('active')
        cust_info.append(customer)
    return json.dumps(cust_info)


@app.route("/producer/customer/<int:cid>", methods=['GET'])
def get_single_active_customer(cid):
    customer = Customer.query.filter_by(id=cid, active='Y').first()
    customer = customer.as_dict()
    customer.pop("active")
    return json.dumps(customer)


@app.route("/producer/customer/", methods=['POST'])
def save_customer():
    reqdata = request.get_json()
    email = reqdata["email"]
    cust = Customer(name=reqdata["name"], age=reqdata["age"], email=reqdata["email"], gender=reqdata["gender"])
    if Customer.query.filter_by(email=email).first():
        return {"Status": "Duplicated email address {}".format(email)}
    db.session.add(cust)
    db.session.commit()
    return {"Success": "Customer: {} saved successfully!".format(cust.id)}


# http://localhost:5000/producer/customer/1
@app.route("/producer/customer/<int:cid>", methods=['PUT'])
def update_customer(cid):
    dbcust = Customer.query.filter_by(id=cid).first()
    reqdata = request.get_json()
    email = reqdata["email"]
    if dbcust:
        cust = Customer.query.filter_by(email=email).first()
        if dbcust.email != email and cust:
            return {"Status": "Duplicated email address {}".format(email)}
        dbcust.name = reqdata["name"]
        dbcust.age = reqdata["age"]
        dbcust.email = reqdata["email"]
        dbcust.gender = reqdata["gender"]
        db.session.commit()
        return {"Success": "Customer: {} updated successfully!".format(dbcust.id)}
    else:
        return {"Status": "No customer with given id {}. Can not update..!".format(cid)}


# http://localhost:5000/producer/customer/1
@app.route("/producer/customer/<int:cid>", methods=['DELETE'])
def delete_customer(cid):
    dbcust = Customer.query.filter_by(id=cid, active='Y').first()
    if dbcust:
        dbcust.active = 'N'
        db.session.commit()
        return {"Success": "Customer: {} deleted successfully!".format(dbcust.name)}
    else:
        return {"Status": "No customer with given id {}. Can not delete..!".format(cid)}


@app.route("/producer/address/", methods=['GET'])
def get_all_active_addresses():
    addresses = Address.query.filter_by(active='Y').all()
    adr_info = []
    for address in addresses:
        address=address.as_dict()
        address.pop("active")
        adr_info.append(address)
    return json.dumps(adr_info)


@app.route("/producer/address/<int:aid>", methods=['GET'])
def get_single_active_address(aid):
    address = Address.query.filter_by(id=aid).first()
    address = address.as_dict()
    address.pop("active")
    return json.dumps(address)


@app.route("/producer/address/", methods=['POST'])
def save_address():
    reqdata = request.get_json()
    pincode = reqdata["pincode"]
    cid = reqdata["cid"]
    adr = Address.query.filter_by(cid=cid).first()
    if adr:
        return {"Status": "Already Address assigned to: {}".format(adr.customers.name)}
    adr = Address(city=reqdata["city"], state=reqdata["state"], pincode=reqdata["pincode"], cid=reqdata["cid"])
    if Address.query.filter_by(pincode=pincode).first():
        return {"Status": "Duplicated pincode: {}".format(pincode)}
    db.session.add(adr)
    db.session.commit()
    return {"Success": "Address: {} saved successfully!".format(adr.id)}


# http://localhost:5000/producer/address/1
@app.route("/producer/address/<int:aid>", methods=['PUT'])
def update_address(aid):
    dbadr = Address.query.filter_by(id=aid).first()
    reqdata = request.get_json()
    pincode = int(reqdata["pincode"])
    if dbadr:
        adr = Address.query.filter_by(pincode=pincode).first()
        if dbadr.pincode != pincode and adr:
            return {"Status": "Duplicated pincode: {}".format(pincode)}
        dbadr.city = reqdata["city"]
        dbadr.state = reqdata["state"]
        dbadr.pincode = reqdata["pincode"]
        dbadr.cid = reqdata["cid"]
        db.session.commit()
        return {"Success": "address: {} updated successfully!".format(dbadr.id)}
    else:
        return {"Status": "No address with given id {}. Can not update..!".format(aid)}


# http://localhost:5000/producer/address/1
@app.route("/producer/address/<int:aid>", methods=['DELETE'])
def delete_address(aid):
    dbadr = Address.query.filter_by(id=aid, active='Y').first()
    if dbadr:
        dbadr.active = 'N'
        db.session.commit()
        return {"Success": "address: {} deleted successfully!".format(dbadr.city)}
    else:
        return {"Status": "No address with given id {}. Can not delete..!".format(aid)}


if __name__ == '__main__':
    app.run(debug=True, port=5000)