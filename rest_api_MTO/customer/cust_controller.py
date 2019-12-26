from rest_api_MTO.customer.cust_adr_api import *


genderTypes = {"M": "Male", "F": "Female"}
cust = Customer()  # {'id': 0, 'name': '', 'age': 0, 'gender': '', 'email': '', 'aid': 0}


# http://localhost:5001/customer/home/
@app.route("/customer/home/", methods=["GET"])
def customer_home():
    session['cnmsort'] = 'desc'
    return render_template("customer.html", customer=Customer(), customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


# http://localhost:5001/customer/save/
@app.route("/customer/save/", methods=["POST", "GET"])
def customer_save_update():
    msg = ''
    cust = Customer()
    if request.method == "POST":
        rf = request.form
        # [('cid', '0'), ('name', 'pary'), ('age', '29'), ('gender', 'F'), ('email', 'pary@g.in'), ('adr.id', '14')]
        cust1 = Customer(id=rf['cid'], name=rf['name'], age=rf['age'],
                         gender=rf['gender'], email=rf['email'], aid=rf['adr.id'])
        if rf['cid'] == '0':
            msg, act = save_customer(cust1)
        else:
            msg, act = update_customer(rf['cid'], cust1)
        if act != "Success":
            cust = cust1
    return render_template("customer.html", msg=msg, customer=cust, customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


# http://localhost:5001/customer/edit/101
@app.route("/customer/edit/<int:cid>", methods=["GET"])
def customer_edit(cid):
    cust = get_single_active_customer(cid)
    return render_template("customer.html", customer=cust, customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


# http://localhost:5001/customer/delete/101
@app.route("/customer/delete/<int:cid>", methods=["GET"])
def customer_delete(cid):
    cust = get_single_active_customer(cid)
    msg = delete_customer(cid)
    return render_template("customer.html", msg=msg, customer=cust, customers=get_all_active_customer_with_address(),
                           genders=genderTypes, addresses=get_all_active_addresses())


@app.route('/customer/sort/id')
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


@app.route('/customer/sort/name')
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


@app.route('/customer/sort/age')
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
