import json
from flask import request
from rest_api_MTM.producer.model import *


# http://localhost:5000/producer/custwithadr/
@app.route("/producer/custwithadr/", methods=['GET'])
def get_all_customers_with_addresses():
    custs = Customer.query.filter_by(active='Y').all()
    all_info = []
    for cust in custs:
        cust1 = cust.as_dict()
        cust1.pop('active')
        adrs = cust.custadr
        adrlist = []
        if adrs:
            for adr in adrs:
                ad = adr.addresses
                ad = ad.as_dict()
                ad.pop('active')
                adrlist.append(ad)
        cust1['addresses'] = adrlist
        all_info.append(cust1)
    return json.dumps(all_info)


# http://localhost:5000/producer/adrwithcust/
@app.route("/producer/adrwithcust/", methods=['GET'])
def get_all_active_addresses_with_customer():
    adrs = Address.query.filter_by(active='Y').all()
    all_info = []
    for adr in adrs:
        adr1 = adr.as_dict()
        adr1.pop('active')
        print(adr1)
        custs = adr.custadr
        custlist = []
        if custs:
            for cust in custs:
                cust1 = cust.customers
                cust2 = cust1.as_dict()
                cust2.pop('active')
                custlist.append(cust2)
        adr1['customers'] = custlist
        all_info.append(adr1)
    return json.dumps(all_info)


# http://localhost:5000/producer/customer/
@app.route("/producer/customer/", methods=['GET'])
def get_all_active_customers():
    custlist = []
    customers = Customer.query.filter_by(active='Y').all()
    for customer in customers:
        customer = customer.as_dict()
        customer.pop('active')
        custlist.append(customer)
    return json.dumps(custlist)


# http://localhost:5000/producer/address/
@app.route("/producer/address/", methods=['GET'])
def get_all_active_addresses():
    adrlist = []
    addresses = Address.query.filter_by(active='Y').all()
    for address in addresses:
        address = address.as_dict()
        address.pop('active')
        adrlist.append(address)
    return json.dumps(adrlist)


# http://localhost:5000/producer/customer/101
@app.route("/producer/customer/<int:cid>", methods=['GET'])
def get_single_active_customer(cid):
    cust = Customer.query.filter_by(id=cid).first()
    if cust:
        cust = cust.as_dict()
        cust.pop('active')
        return json.dumps(cust)
    return {"Failed": "Customer with id: {} not available...".format(cid)}


# http://localhost:5000/producer/address/11
@app.route("/producer/address/<int:aid>", methods=['GET'])
def get_single_active_address(aid):
    adr = Address.query.filter_by(id=aid).first()
    if adr:
        adr = adr.as_dict()
        adr.pop('active')
        return json.dumps(adr)
    return {"Failed": "Address with id: {} not available...".format(aid)}


# http://localhost:5000/producer/customer/
@app.route("/producer/customer/", methods=['POST'])
def save_customer():
    rd = request.get_json()
    email = rd["email"]
    if Customer.query.filter_by(email=email).first():
        return {"Failed": "Duplicate email: {} provided...".format(email)}
    cust = Customer(name=rd['name'], age=rd['age'], gender=rd['gender'], email=rd['email'])
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


# http://localhost:5000/producer/custadr/
@app.route("/producer/custadr/", methods=['GET'])
def get_all_cust_adr():
    cuad = custAdr.query.all()
    ac = []
    for ca in cuad:
        ac.append(ca.as_dict())
    return json.dumps(ac)


# http://localhost:5000/producer/custadr/1
@app.route("/producer/custadr/<int:id>", methods=['GET'])
def get_single_cust_adr(id):
    cuad = custAdr.query.filter_by(id=id).first()
    if cuad:
        cuad = cuad.as_dict()
        return json.dumps(cuad)
    return {"Failed": "Address relationship id: {} not available...".format(id)}


# http://localhost:5000/producer/custadr/
@app.route("/producer/custadr/", methods=['POST'])
def save_cust_adr():
    rd = request.get_json()
    c1 = rd['cid']
    calist = custAdr.query.filter_by(aid=rd['aid']).all()
    if calist:
        for ca in calist:
            cid1 = ca.cid
            if c1 == cid1:
                return {"Failed": "address relationship of: {} already exist!".format(rd['cid'])}
    rel = custAdr(cid=rd['cid'], aid=rd['aid'])
    db.session.add(rel)
    db.session.commit()
    return {"Success": "address relationship of: {} saved successfully!".format(rd['cid'])}


# http://localhost:5000/producer/custadr/1
@app.route("/producer/custadr/<int:id>", methods=['PUT'])
def update_cust_adr(id):
    cuad = custAdr.query.filter_by(id=id).first()
    rd = request.get_json()
    if cuad:
        cuad.cid = rd['cid']
        cuad.aid = rd['aid']
        db.session.commit()
        return {"Success": "address relationship of: {} updated successfully!".format(id)}
    return {"Failed": "address relationship of: {} not available...".format(id)}


if __name__ == '__main__':
    app.run(debug=True, port=5000)
