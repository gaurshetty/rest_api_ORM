from flask import Flask, request, render_template, session
from rest_api_ORM1.rest_api_OTO.customer.customer_api import *

app = Flask(__name__)
app.config['SECRET_KEY'] = "65919S1C4ASCJSNVPUHV"


@app.route("/customer/home/", methods=["GET"])
def customer_home():
    return render_template("customer.html", customer=Customer(), address=Address(),
                           customers=get_all_customers_with_address())


@app.route("/customer/save/", methods=["POST", "GET"])
def customer_save_update():
    msg1 = ''
    msg2 = ''
    if request.method == "POST":
        rf = request.form
        cid = rf["cid"]
        aid = rf["aid"]
        cust = Customer(id=rf["cid"], name=rf["name"], age=rf["age"], gender=rf["gender"], email=rf["email"])
        adr = Address(id=rf["aid"], city=rf["city"], state=rf["state"], pincode=rf["pincode"], cid=rf["cid"])
        if cid == '0' and aid == '0':
            msg1, msg2 = save_customer_address(cust, adr)
        else:
            msg1, msg2 = update_customer_address(cust, cid, adr, aid)
    return render_template("customer.html", customer=Customer(), address=Address(),
                           customers=get_all_customers_with_address(), msg1=msg1, msg2=msg2)


@app.route("/customer/edit/<int:aid>")
def customer_edit(aid):
    address = get_single_active_address(aid)
    cid = address.get('cid')
    customer = get_single_active_customer(cid)
    return render_template("customer.html", customer=customer, address=address,
                           customers=get_all_customers_with_address())


@app.route("/customer/delete/<int:aid>")
def customer_delete(aid):
    address = get_single_active_address(aid)
    cid = address.get('cid')
    customer = get_single_active_customer(cid)
    msg1, msg2 = delete_customer_address(cid, aid)
    return render_template("customer.html", customer=customer, address=address,
                           customers=get_all_customers_with_address(), msg1=msg1, msg2=msg2)


if __name__ == '__main__':
    app.run(debug=True, port=5001)
