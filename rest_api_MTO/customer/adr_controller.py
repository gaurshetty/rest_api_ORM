from rest_api_MTO.customer.cust_adr_api import *

adr = Address()


# http://localhost:5001/address/home/
@app.route("/address/home/", methods=["GET"])
def address_home():
    session['cnmsort'] = 'desc'
    return render_template("address_mtm.html", address=adr, addresses=get_all_active_addresses())


# http://localhost:5001/address/save/
@app.route("/address/save/", methods=["POST", "GET"])
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
    return render_template("address_mtm.html", msg=msg, address=adr, addresses=get_all_active_addresses())


# http://localhost:5001/address/edit/101
@app.route("/address/edit/<int:aid>", methods=["GET"])
def address_edit(aid):
    adr = get_single_active_address(aid)
    return render_template("address_mtm.html", address=adr, addresses=get_all_active_addresses())


# http://localhost:5001/address/delete/101
@app.route("/address/delete/<int:aid>", methods=["GET"])
def address_delete(aid):
    adr = get_single_active_address(aid)
    msg = delete_address(aid)
    return render_template("address_mtm.html", msg=msg, address=adr, addresses=get_all_active_addresses())


@app.route('/address/sort/id')
def sort_aid():
    adrlist = get_all_active_addresses()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        adrlist.sort(key=lambda i: i['id'])
    else:
        session['cnmsort'] = 'desc'
        adrlist.sort(key=lambda i: i['id'], reverse=True)
    return render_template("address_mtm.html", address=adr, addresses=adrlist)


@app.route('/address/sort/city')
def sort_city():
    adrlist = get_all_active_addresses()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        adrlist.sort(key=lambda i: i['city'])
    else:
        session['cnmsort'] = 'desc'
        adrlist.sort(key=lambda i: i['city'], reverse=True)
    return render_template("address_mtm.html", address=adr, addresses=adrlist)


@app.route('/address/sort/pincode')
def sort_pincode():
    adrlist = get_all_active_addresses()
    if session['cnmsort'] == 'desc':
        session['cnmsort'] = 'asc'
        adrlist.sort(key=lambda i: i['pincode'])
    else:
        session['cnmsort'] = 'desc'
        adrlist.sort(key=lambda i: i['pincode'], reverse=True)
    return render_template("address_mtm.html", address=adr, addresses=adrlist)


# if __name__ == '__main__':
#     app.run(debug=True, port=5001)
