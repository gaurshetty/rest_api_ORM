from flask import Flask, render_template, session, request
from rest_api_MTM.cust_adr_api.cust_adr_controller import *


genderTypes = {"M": "Male", "F": "Female"}
cust = Customer()  # {'id': 0, 'name': '', 'age': 0, 'gender': '', 'email': ''}


# http://localhost:5001/custadr/customer/home/
@app.route("/custadr/customer/home/", methods=["GET"])
def customer_home():
    session['cnmsort'] = 'desc'
    return render_template("customer.html", customer=Customer(), customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


# http://localhost:5001/custadr/customer/save/
@app.route("/custadr/customer/save/", methods=["POST"])
def customer_save_update():
    msg = ''
    cust = Customer()
    if request.method == "POST":
        rf = request.form
        cust1 = Customer(id=rf['cid'], name=rf['name'], age=rf['age'], gender=rf['gender'], email=rf['email'])
        adrlist = rf.getlist('adr')
        if rf['cid'] == '0':
            msg, act = save_customer_with_address(cust1, adrlist)
        else:
            msg, act = update_customer_with_address(rf['cid'], cust1, adrlist)
        if act != "Success":
            cust = cust1
    return render_template("customer.html", msg=msg, customer=cust, customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


# http://localhost:5001/custadr/customer/edit/101
@app.route("/custadr/customer/edit/<int:cid>", methods=["GET"])
def customer_edit(cid):
    cust = get_single_active_customer(cid)
    return render_template("customer.html", customer=cust, customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


# http://localhost:5001/custadr/customer/delete/101
@app.route("/custadr/customer/delete/<int:cid>", methods=["GET"])
def customer_delete(cid):
    cust = get_single_active_customer(cid)
    msg = delete_customer(cid)
    return render_template("customer.html", msg=msg, customer=cust, customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


@app.route('/custadr/customer/sort/id')
def sort_cid():
    custlist = get_all_active_customer_with_address()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        custlist.sort(key=lambda i: i['id'])
    else:
        session['cnmsort'] = 'desc'
        custlist.sort(key=lambda i: i['id'], reverse=True)
    return render_template("customer.html", customer=cust, customers=custlist,
                           genders=genderTypes, addresses=get_all_active_addresses())


@app.route('/custadr/customer/sort/name')
def sort_name():
    custlist = get_all_active_customer_with_address()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        custlist.sort(key=lambda i: i['name'])
    else:
        session['cnmsort'] = 'desc'
        custlist.sort(key=lambda i: i['name'], reverse=True)
    return render_template("customer.html", customer=cust, customers=custlist,
                           genders=genderTypes, addresses=get_all_active_addresses())


@app.route('/custadr/customer/sort/age')
def sort_age():
    custlist = get_all_active_customer_with_address()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        custlist.sort(key=lambda i: i['age'])
    else:
        session['cnmsort'] = 'desc'
        custlist.sort(key=lambda i: i['age'], reverse=True)
    return render_template("customer.html", customer=cust, customers=custlist,
                           genders=genderTypes, addresses=get_all_active_addresses())


# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
