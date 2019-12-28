from flask import Flask, render_template, session, request
from rest_api_MTM.cust_adr_api.cust_adr_controller import *
adr = Address()


# http://localhost:5001/custadr/address/home/
@app.route("/custadr/address/home/", methods=["GET"])
def address_home():
    session['cnmsort'] = 'desc'
    return render_template("address.html", address=adr, addresses=get_all_active_addresses())


# http://localhost:5001/custadr/address/save/
@app.route("/custadr/address/save/", methods=["POST", "GET"])
def address_save_update():
    msg = ''
    adr = Address()
    if request.method == "POST":
        rf = request.form
        adr1 = Address(id=rf['id'], city=rf['city'], state=rf['state'], pincode=rf['pincode'])
        if rf['id'] == '0':
            msg, act = save_address(adr1)
        else:
            msg, act = update_address(rf['id'], adr1)
        if act != "Success":
            adr = adr1
    return render_template("address.html", msg=msg, address=adr, addresses=get_all_active_addresses())


# http://localhost:5001/custadr/address/edit/101
@app.route("/custadr/address/edit/<int:aid>", methods=["GET"])
def address_edit(aid):
    adr = get_single_active_address(aid)
    return render_template("address.html", address=adr, addresses=get_all_active_addresses())


# http://localhost:5001/custadr/address/delete/101
@app.route("/custadr/address/delete/<int:aid>", methods=["GET"])
def address_delete(aid):
    adr = get_single_active_address(aid)
    msg = delete_address(aid)
    return render_template("address.html", msg=msg, address=adr, addresses=get_all_active_addresses())


# http://localhost:5001/custadr/address/sort/id
@app.route('/custadr/address/sort/id')
def sort_aid():
    adrlist = get_all_active_addresses()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        adrlist.sort(key=lambda i: i['id'])
    else:
        session['cnmsort'] = 'desc'
        adrlist.sort(key=lambda i: i['id'], reverse=True)
    return render_template("address.html", address=adr, addresses=adrlist)


# http://localhost:5001/custadr/address/sort/city
@app.route('/custadr/address/sort/city')
def sort_city():
    adrlist = get_all_active_addresses()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        adrlist.sort(key=lambda i: i['city'])
    else:
        session['cnmsort'] = 'desc'
        adrlist.sort(key=lambda i: i['city'], reverse=True)
    return render_template("address.html", address=adr, addresses=adrlist)


# http://localhost:5001/custadr/address/sort/pincode
@app.route('/custadr/address/sort/pincode')
def sort_pincode():
    adrlist = get_all_active_addresses()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        adrlist.sort(key=lambda i: i['pincode'])
    else:
        session['cnmsort'] = 'desc'
        adrlist.sort(key=lambda i: i['pincode'], reverse=True)
    return render_template("address.html", address=adr, addresses=adrlist)


# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
