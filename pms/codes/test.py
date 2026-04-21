from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

products = [
    {"id": 1, "name": "Laptop", "price": 50000},
    {"id": 2, "name": "Mobile", "price": 25000},
    {"id": 3, "name": "TV", "price": 60000},
    {"id": 4, "name": "Washing Machine", "price": 60000},
    {"id": 5, "name": "AC", "price": 70000},
]


@app.route("/")
def home():
    return render_template("index.html")


# The form.get() should always get the name attribute of the input field in the html file. If it is not same then it will return None and the product will not be added to the list.
@app.route("/add", methods=["GET", "POST"])
def add_product():
    # For request.method == "POST" , we have changed from request.args.get() to request.form.get() because we are sending the data through form and not through query string.
    # So we need to use form.get() to get the data from the form.
    if request.method == "POST":
        i = request.form.get("pid")
        n = request.form.get("pname")
        p = request.form.get("pprice")
        products.append({"id": i, "name": n, "price": p})
        return redirect(url_for("view_products"))
    return render_template("add.html")


@app.route("/view")
def view_products():
    return render_template("view.html", products=products)


@app.route("/update", methods=["GET", "POST"])
def update_product():
    if request.method == "POST":
        pid = request.form.get("id")
        newprice = request.form.get("price")
        for p in products:
            if p["id"] == pid:
                p["price"] = newprice

        return redirect(url_for("view_products"))
    return render_template("update.html")


@app.route("/delete", methods=["GET", "POST"])
def delete_product():
    if request.method == "POST":
        pid = request.form.get("id")
        global products
        # Filtering the list by converting everything to strings for a safe match
        products = [p for p in products if str(p["id"]) != str(pid)]

        return redirect(url_for("view_products"))

    return render_template("delete.html")


if __name__ == "__main__":
    app.run(debug=True)
