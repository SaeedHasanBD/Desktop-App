import sqlite3

def connect():
    conn=sqlite3.connect("Project_Shaposhnikov.db")
    cur=conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS data(id INTEGER PRIMARY KEY, student_name text, study_field text, year integer, scientific_work text, supervisor_name text, mark real )")
    conn.commit()
    conn.close()

def delete(id):
    conn=sqlite3.connect("Project_Shaposhnikov.db")
    cur=conn.cursor()
    cur.execute("DELETE FROM data WHERE id=?",(id,))
    conn.commit()
    conn.close()

def insert(student_name, study_field, year, scientific_work, supervisor_name, mark):
    conn=sqlite3.connect("Project_Shaposhnikov.db")
    cur=conn.cursor()
    cur.execute("INSERT INTO data VALUES(NULL,?,?,?,?,?,?)",(student_name, study_field,year, scientific_work, supervisor_name,mark))
    conn.commit()
    conn.close()

def view():
    conn=sqlite3.connect("Project_Shaposhnikov.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data")
    rows=cur.fetchall()
    conn.close()
    return rows

def search(student_name="",study_field="",year="",scientific_work="",supervisor_name="", mark=""):
    conn=sqlite3.connect("Project_Shaposhnikov.db")
    cur=conn.cursor()
    cur.execute("SELECT * FROM data WHERE student_name=? OR study_field=? OR year=? OR scientific_work=? OR supervisor_name=? OR mark=?", (student_name, study_field,year, scientific_work, supervisor_name,mark))
    rows=cur.fetchall()
    conn.close()
    return rows

def update(id,student_name, study_field,year, scientific_work, supervisor_name,mark):
    conn=sqlite3.connect("Project_Shaposhnikov.db")
    cur=conn.cursor()
    cur.execute("UPDATE data SET student_name=?, study_field=?, year=?, scientific_work=?, supervisor_name=?, mark=? WHERE id=?", (student_name, study_field,year, scientific_work, supervisor_name,mark,id))
    conn.commit()
    conn.close()



connect()
#insert("Saeed","IT",2016,"Making Project of Dr.Shaposhnikov","Dr.Shaposhnikov",5)
#delete(8)
#update(1,"Shojib","IT", 2016, "Project of Dr.Shaposhnikov", "Dr.Shaposhnikov", 2)
#print (view())
#print (search(student_name="Saeed"))
