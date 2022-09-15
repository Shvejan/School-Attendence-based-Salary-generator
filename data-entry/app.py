from flask import Flask,render_template,redirect,url_for,request,make_response,jsonify
import psycopg2
import os
from datetime import date

app = Flask(__name__)
conn = psycopg2.connect(
user = "postgres",
password ="@shivatejan1",
host = "localhost",
database="nature",
port = "5432",
)

app.secret_key = os.urandom(12)
cur = conn.cursor()

@app.route('/')
def home():
    cur.execute("SELECT emp_id,name FROM employees")
    data=cur.fetchall()
    return render_template("admin_view.html",data=data)

@app.route('/edits',methods=['POST'])
def edits():
    if request.form.get('button')=="1":
        cur.execute("select count(*) from employees")
        data=cur.fetchall()
        id = 'NN'+str(data[0][0]+1001)
        name=request.form.get('name').upper()
        department=request.form.get('department')
        pan=request.form.get('pan')
        designation=request.form.get('designation')
        bank=request.form.get('bank')
        accNo=request.form.get('accNo')
        pf=request.form.get('pf')
        esi=request.form.get('esi')
        leaves_allowed=request.form.get('leaves_allowed')
        #print(id,name,department,pan,designation,bank,accNo)
        (bank,department,designation,id,name,pan,int(accNo),pf,esi,int(leaves_allowed))
        cur.execute("INSERT INTO employees VALUES(%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)",(bank,department,designation,id,name,pan,int(accNo),pf,esi,int(leaves_allowed)))
        conn.commit()

    return redirect(url_for('home'))


@app.route('/generate',methods=['POST'])
def generate():
        req = request.get_json()
        print(req)
        makeresp = make_response(jsonify({"success": True}), 200)
        return(makeresp)
