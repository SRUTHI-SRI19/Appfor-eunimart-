from flask import *  
from flask_mail import *  
from random import *  
app = Flask(__name__)  
mail = Mail(app)  
app.config["MAIL_SERVER"]='smtp.gmail.com'  
app.config["MAIL_PORT"] = 465     
app.config["MAIL_USERNAME"] = 'kl3826162@gmail.com'  
app.config['MAIL_PASSWORD'] = '9894177aA*'  
app.config['MAIL_USE_TLS'] = False  
app.config['MAIL_USE_SSL'] = True  
app.secret_key = "abc"  

mail = Mail(app)  
otp = randint(000000,999999)


@app.route('/')  
def index():  
    return render_template("home.html")  
@app.route('/verify',methods = ["POST"])  
def verify():  

    email = request.form["email"]   
    session['country']=request.form['country']
    msg = Message(subject = 'OTP',sender = 'kl3826162@gmail.com', recipients = [email])  
    msg.body = str(otp)
    mail = Mail(app)  
    mail.send(msg)  
    return render_template('verify.html')
@app.route('/validate',methods=["POST"])   
def validate():  
    user_otp = request.form['otp'] 
    print(request.form)
    if otp == int(user_otp):
        if session['country'] == 'India':
            return("Details needed :First Name,Father's Name,Last Name,Address,ID Proof(Any),Address Proof(Any)")
        elif session['country']== "US":
            return("Details needed : Name,Social Security number. A valid government-issued photo ID like a driver's license, passport or state or military ID") 
    else:
        return "<h3>failure, OTP does not match</h3>" 
    
if __name__ == '__main__':  
    app.run(debug = True) 