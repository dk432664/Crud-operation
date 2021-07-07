from flask import Flask , render_template ,request , redirect ,url_for ,flash
from flask_mysqldb import MySQL
app=Flask(__name__)
app.secret_key="crudthing"
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'deep@6799K'
app.config['MYSQL_DB'] = 'crud'

mysql = MySQL(app)
@app.route('/')
def Index():
    cur = mysql.connection.cursor()
    cur.execute("SELECT  * FROM instructor")
    data = cur.fetchall()
    cur.close()




    return render_template('index.html', instructor=data)

# @app.route('/')
# def home():
# 	return render_template('index.html')



@app.route('/insert',methods=['POST'])
def insert():
	if request.method =="POST":
		flash("Inserted data successfully")
		name=request.form['name']
		email=request.form['email']
		cur=mysql.connection.cursor()
		cur.execute("INSERT INTO instructor (name,email) VALUES (%s,%s)",(name,email))
		mysql.connection.commit()
		return redirect(url_for('Index'))


@app.route('/update', methods=['POST','GET'])
def update():
	if request.method=='POST':
		id_data=request.form['id']
		name=request.form['name']
		email=request.form['email']
		cur=mysql.connection.cursor()
		cur.execute("""
			UPDATE instructor SET name=%s , email=%s WHERE id=%s """, (name,email,id_data))
		flash("Updated data successfully")
		mysql.connection.commit()
		return redirect(url_for('Index'))

@app.route('/delete/<string:id_data>',methods=['POST','GET'])
def delete(id_data):
	flash("Deleted data successfully")
	cur=mysql.connection.cursor()
	cur.execute("DELETE FROM instructor WHERE id=%s",(id_data,))
	mysql.connection.commit()
	return redirect(url_for('Index'))




if __name__ =="__main__":
	app.run(debug=True)
