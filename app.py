from flask import Flask, render_template,request,redirect,url_for,session
app = Flask(__name__)
app.secret_key="secret123"
users = {}
@app.route("/")
def home():
    return render_template("login.html")
@app.route("/signup", methods=["GET", "POST"])
def signup():
    message = ""
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip()
        password = request.form.get("password", "").strip()

        if not username or not email or not password:
            message = "All fields are required"
        elif username in users:
            message = "Username already exists"
        else:
            users[username] = {"email": email, "password": password}
            return redirect(url_for("home"))
    return render_template("signup.html", message=message)
@app.route("/login",methods=["POST"])
def login():
    username= request.form.get("username")
    password = request.form.get("password")
    if username in users and users [username]["password"] == password:
        session["user"]=username
        return redirect(url_for("dashboard"))
    else:
        return render_template("login.html",message="Invalid username or password")
@app.route("/dashboard")
def dashboard():
    if "user" in session :
        return render_template("dashboard.html",username=session["user"])
    else:
        return redirect(url_for("home"))
@app.route("/logout")
def logout():
    session.pop("user",None)
    return redirect(url_for("home"))
if __name__ == "__main__":
    app.run(debug=True)