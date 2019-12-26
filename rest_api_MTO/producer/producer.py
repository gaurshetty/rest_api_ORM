from flask import request
from rest_api_MTO.producer.model import *
import json


# http://localhost:5000/producer/customeraddress/
@app.route("/producer/customeraddress/", methods=['GET'])
def get_all_active_customers_with_addesses():
    custs = Customer.query.filter_by(active='Y').all()
    all_cust_info = []
    for cust in custs:
        cust1 = cust.as_dict()
        cust1.pop('active')
        adr = cust.addresses
        adr = adr.as_dict()
        adr.pop('active')
        cust1['address'] = adr
        all_cust_info.append(cust1)
    return json.dumps(all_cust_info)


# http://localhost:5000/producer/addresscustomer/
@app.route("/producer/addresscustomer/", methods=['GET'])
def get_all_active_addresses_with_customers():
    adres = Address.query.filter_by(active='Y').all()
    all_adr_info = []
    for adr in adres:
        adr1 = adr.as_dict()
        adr1.pop('active')
        custlist = []
        custs = adr.customers
        if custs:
            for cust in custs:
                cust = cust.as_dict()
                cust.pop('active')
                custlist.append(cust)
        adr1['customers'] = custlist
        all_adr_info.append(adr1)
    return json.dumps(all_adr_info)


# http://localhost:5000/producer/customer/
@app.route("/producer/customer/", methods=['GET'])
def get_all_active_customers():
    customers = Customer.query.filter_by(active='Y').all()
    custlist = []
    for customer in customers:
        customer = customer.as_dict()
        customer.pop('active')
        custlist.append(customer)
    return json.dumps(custlist)


# http://localhost:5000/producer/customer/101
@app.route("/producer/customer/<int:cid>", methods=['GET'])
def get_single_active_customers(cid):
    cust = Customer.query.filter_by(id=cid).first()
    if cust:
        cust = cust.as_dict()
        cust.pop('active')
        return json.dumps(cust)
    return {"Failed": "Customer with id: {} not available...".format(cid)}


# http://localhost:5000/producer/customer/
@app.route("/producer/customer/", methods=['POST'])
def save_customer():
    rd = request.get_json()
    email = rd["email"]
    if Customer.query.filter_by(email=email).first():
        return {"Failed": "Duplicate email: {} provided...".format(email)}
    cust = Customer(name=rd['name'], age=rd['age'], gender=rd['gender'], email=rd['email'], aid=rd['aid'])
    db.session.add(cust)
    db.session.commit()
    return {"Success": "Customer: {} saved successfully!".format(cust.id)}


# http://localhost:5000/producer/customer/101
@app.route("/producer/customer/<int:cid>", methods=['PUT'])
def update_customer(cid):
    cust = Customer.query.filter_by(id=cid).first()
    rd = request.get_json()
    email = rd["email"]
    if cust:
        if cust.email != email and Customer.query.filter_by(email=email).first():
            return {"Failed": "Duplicate email: {} provided...".format(email)}
        cust.name = rd['name']
        cust.age = rd['age']
        cust.gender = rd['gender']
        cust.email = rd['email']
        cust.aid = rd['aid']
        db.session.commit()
        return {"Success": "Customer: {} updated successfully!".format(cust.id)}
    return {"Failed": "Customer with id: {} not available...".format(cid)}


# http://localhost:5000/producer/customer/101
@app.route("/producer/customer/<int:cid>", methods=['DELETE'])
def delete_customer(cid):
    cust = Customer.query.filter_by(id=cid).first()
    if cust:
        cust.active = 'N'
        db.session.commit()
        return {"Success": "Customer: {} deleted successfully!".format(cust.id)}
    return {"Failed": "Customer with id: {} not available...".format(cid)}


# http://localhost:5000/producer/address/
@app.route("/producer/address/", methods=['GET'])
def get_all_active_addresses():
    addresses = Address.query.filter_by(active='Y').all()
    adrlist = []
    for address in addresses:
        address = address.as_dict()
        address.pop('active')
        adrlist.append(address)
    return json.dumps(adrlist)


# http://localhost:5000/producer/address/11
@app.route("/producer/address/<int:aid>", methods=['GET'])
def get_single_active_address(aid):
    adr = Address.query.filter_by(id=aid).first()
    if adr:
        adr = adr.as_dict()
        adr.pop('active')
        return json.dumps(adr)
    return {"Failed": "Address with id: {} not available...".format(aid)}


# http://localhost:5000/producer/address/
@app.route("/producer/address/", methods=['POST'])
def save_address():
    rd = request.get_json()
    pincode = rd["pincode"]
    if Address.query.filter_by(pincode=pincode).first():
        return {"Failed": "Duplicate pincode: {} provided...".format(pincode)}
    adr = Address(city=rd['city'], state=rd['state'], pincode=rd['pincode'])
    db.session.add(adr)
    db.session.commit()
    return {"Success": "Address: {} saved successfully!".format(adr.id)}


# http://localhost:5000/producer/address/11
@app.route("/producer/address/<int:aid>", methods=['PUT'])
def update_address(aid):
    adr = Address.query.filter_by(id=aid).first()
    rd = request.get_json()
    pincode = int(rd["pincode"])
    if adr:
        if adr.pincode != pincode and Address.query.filter_by(pincode=pincode).first():
            return {"Failed": "Duplicate pincode: {} provided...".format(pincode)}
        adr.city = rd['city']
        adr.state = rd['state']
        adr.pincode = rd['pincode']
        db.session.commit()
        return {"Success": "Address: {} updated successfully!".format(adr.id)}
    return {"Failed": "Address with id: {} not available...".format(aid)}


# http://localhost:5000/producer/address/11
@app.route("/producer/address/<int:aid>", methods=['DELETE'])
def delete_address(aid):
    adr = Address.query.filter_by(id=aid).first()
    if adr:
        adr.active = 'N'
        db.session.commit()
        return {"Success": "Address: {} deleted successfully!".format(adr.id)}
    return {"Failed": "Address with id: {} not available...".format(aid)}


if __name__ == '__main__':
    app.run(debug=True, port=5000)
