import docx
import psycopg2
conn = psycopg2.connect(
user = "postgres",
password ="@shivatejan1",
host = "localhost",
database="nature",
port = "5432",
)

cur = conn.cursor()
cur.execute("INSERT INTO public.employees(bank_name, department, designation, emp_id, name, pan, account_number) VALUES ('sib', 'dep', 'des', 'nn123123', 'myname', 'pan', 12312312312)")
conn.commit()


doc = docx.Document('doc.docx')
for p in doc.paragraphs:
    print(p.text)
