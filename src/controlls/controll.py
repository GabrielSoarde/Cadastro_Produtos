from flask.views import MethodView
from flask import render_template, request, redirect, flash
from src.db import mysql

class Index(MethodView):    
    def get(self):
        with mysql.cursor() as cur:
            cur.execute("SELECT code, name, stock, value FROM produtos")
            produtos = cur.fetchall()
        return render_template('index.html', produtos=produtos)

class Create(MethodView):
    def get(self):
        return render_template('create.html')
    
    def post(self):
        code = request.form['code']
        name = request.form['name']
        stock = request.form['stock']
        value = request.form['value']

        with mysql.cursor() as cur:
            cur.execute("INSERT INTO produtos (code, name, stock, value) VALUES (%s, %s, %s, %s)", (code, name, stock, value))
            cur.connection.commit()
        return redirect('/')
    
class Delete(MethodView):   
    def post(self, code):
        with mysql.cursor() as cur:
            cur.execute("DELETE FROM produtos WHERE code = %s", (code,))
            cur.connection.commit()
        return redirect('/')
    

class Update(MethodView):
    def get(self, code):
        with mysql.cursor() as cur:
            cur.execute('SELECT * FROM produtos WHERE code = %s', (code,))
            produto = cur.fetchone()
        return render_template('update.html', product=produto)

    def post(self, code):
        codeproduct = request.form.get['code']
        name = request.form.get['name']
        stock = request.form.get['stock']
        value = request.form.get['value']

        with mysql.cursor() as cur:
            cur.execute("UPDATE produtos SET code = %s, name = %s, stock = %s, value = %s WHERE code = %s", (codeproduct, name, stock, value, code))
            cur.connection.commit()

        return redirect('/')


        

    
    