# -*- coding: utf-8 -*-
# Funciones comunes y utiles en python



#Flask: Nuestro miniFramework
#url_for: Para archivos estaticos como css o js (no se está usando)
#request: Usado para poder ver recibir peticiones por GET o por POST
from flask import Flask,url_for,request

#render_template para poder mostrar las vistas
from flask import render_template

app = Flask(__name__)

# Esta es una forma para definir una ruta que acepte request tipo GET o Post
# Pero no se está implementando
@app.route("/",methods=['GET', 'POST'])
def index():
	# No está llegando al si del condicional
    if request.method == 'POST':
        return "Esto es POST!"
    else:
        return "Hello World!"

#Podemos hacer que dos rutas nos lleven a la misma funcion
@app.route("/hello/")
# <name> es una variable que pasaremos por url
@app.route("/hello/<name>")
# Aunque podemos no darle un name
def hello(name=None):
    # Así retornamos una vista enviandole un parametro (Esto lo haría un controller)
    return render_template("hello.html",name = name)

# Acá le estamos pidiendo un entero    
@app.route("/post/<int:post_id>")
def mostrar_post(post_id):
    return "Post %d" % post_id

# Acá se le pide un string
@app.route('/usuario/<username>')
@app.route('/user/<username>')
def show_user_profile(username):
    return 'User %s' % username


# Verificamos que todo esté en orden e iniciamos la app    
if __name__ == "__main__":
    
    #Para mostrar los logs de error en el navegador
    app.debug = True
    app.run()