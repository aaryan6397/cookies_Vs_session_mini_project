from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    make_response,
    session,
    flash
)

app = Flask(__name__)

# Required for Flask Session
app.secret_key = "my-secret-key-123"


# ---------------- HOME ----------------

@app.route("/")
def home():
    return render_template("index.html")


# ---------------- COOKIE ROUTES ----------------

@app.route("/set-cookie")
def set_cookie():

    response = make_response(
        redirect(url_for("home"))
    )

    response.set_cookie(
        "username",
        "Aaryan",
        max_age=60
    )

    flash("Cookie has been set successfully!", "success")

    return response


@app.route("/get-cookie")
def get_cookie():

    username = request.cookies.get("username")

    if username:
        flash(
            f"Cookie found! Username: {username}",
            "success"
        )
    else:
        flash(
            "No cookie found. Please set the cookie first.",
            "warning"
        )

    return redirect(url_for("home"))


@app.route("/delete-cookie")
def delete_cookie():

    response = make_response(
        redirect(url_for("home"))
    )

    response.delete_cookie("username")

    flash(
        "Cookie has been deleted successfully!",
        "success"
    )

    return response


# ---------------- LOGIN ----------------

@app.route("/login", methods=["GET", "POST"])
def login():

    if request.method == "POST":

        email = request.form.get("email")
        password = request.form.get("password")

        # Demo credentials
        if email == "aaryan@gmail.com" and password == "Vashu":

            # Create session
            session["logged_in"] = True
            session["email"] = email
            session["username"] = "Aaryan"

            flash(
                "Login successful!",
                "success"
            )

            return redirect(url_for("dashboard"))

        else:

            flash(
                "Invalid email or password!",
                "danger"
            )

    return render_template("login.html")


# ---------------- DASHBOARD ----------------

@app.route("/dashboard")
def dashboard():

    # Check session
    if not session.get("logged_in"):

        flash(
            "Please login first to access the dashboard.",
            "warning"
        )

        return redirect(url_for("login"))

    return render_template(
        "dashboard.html",
        email=session.get("email"),
        username=session.get("username")
    )


# ---------------- SESSION INFO ----------------

@app.route("/session-info")
def session_info():

    if not session.get("logged_in"):

        flash(
            "Please login first.",
            "warning"
        )

        return redirect(url_for("login"))

    return render_template(
        "session_info.html",
        email=session.get("email"),
        username=session.get("username") ,
       session_status="Inactive" if session.get("logged_in") else "Active"    

    )


# ---------------- LOGOUT ----------------

@app.route("/logout")
def logout():

    session.clear()

    flash(
        "You have been logged out successfully.",
        "success"
    )

    return redirect(url_for("home"))


# ---------------- RUN APPLICATION ----------------

if __name__ == "__main__":
    app.run(debug=True)