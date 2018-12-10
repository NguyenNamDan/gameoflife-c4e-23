from flask import *
from models.user import Information
import mlab 

mlab.connect() 
app = Flask(__name__)
# app.config["SECRET_KEY"] = "namdan" #key mở két 

@app.route("/")
def home():
    return render_template("home.html") 

@app.route("/sign_in", methods= ["GET", "POST"])
def sign_in():
    if request.method == "GET":
        return render_template("sign_in.html")
    else:
        form = request.form 
        username = form["username"]
        password = form["password"] 
        found_user = Information.objects(username= username).first()
        if found_user is None:
            return "Sorry! User does not exist"
        elif found_user.password != password:
            return "Sorry! Wrong password"
        else:
            # session["token"] = username #token
            return redirect(url_for("home"))

@app.route("/sign_up", methods= ["GET", "POST"]) 
def sign_up():
    if request.method == "GET":
        return render_template("sign_up.html")
    else:
        form = request.form 
        username = form["username"]
        email = form["email"]
        fullname = form["fullname"]
        password = form["password"]
        confirm = form["confirm"]
        if username == "" or email == "" or fullname == "" or password == "" or confirm == "":
            return "You must complete the information"
        if len(username) < 8:
            return "Username is not available"
        if "@" not in email:
            return "Email is not available"
        if len(password) < 8:
            return "Password is not available"
        if confirm == password:
            m = Information(username= username, email= email, fullname= fullname, password= password)
            m.save()  #Save
            return redirect("/sign_in")     
        else:
            return "Sorry! Wrong password authentication"
            
        
if __name__ == '__main__':
  app.run(debug=True)