from flask import Flask, render_template, request, flash, redirect, url_for,session
import webbrowser
import sqlite3
import jinja2

app = Flask(__name__)
app.secret_key = "123"


con = sqlite3.connect("user.db")
con.execute("CREATE TABLE IF NOT EXISTS USERS(idUtilisateur integer primary key, name text, email text, password text);")

con.close()
cameras=[]
browser_opened = False


@app.route('/')
def page_connexion():
    try:
        return render_template('page-connexion.html')
    except jinja2.exceptions.TemplateNotFound as e:
        print(e.name)
        raise e

@app.route('/login', methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password']
      
        con = sqlite3.connect("user_data.db")
        cur = con.cursor()
        rows = cur.execute("SELECT * FROM USERS WHERE name=? AND password=? ", (username, password))
        rows = rows.fetchone()

        if rows is not None:  # Vérifier si des données ont été trouvées
            session['username'] = username  # Stocker le nom d'utilisateur dans la session
            flash('Connexion réussite')
            return redirect(url_for('customer'))
            
        else:
            flash("Les coordonées entrées sont incorrects veuillez ressayer")
            return redirect('/')

@app.route('/customer', methods=["GET", "POST"])
def customer():
    # Récupérer les informations sur les caméras de l'utilisateur depuis la base de données
    
    

    return render_template('to-do-list.html', cameras=cameras)



@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['name']
        password = request.form['password'] 
        email = request.form['email']
         #crypte le mot de passe
        # Vérifier si l'email ou le nom d'utilisateur existe déjà dans la base de données
        con = sqlite3.connect("user_data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM USERS WHERE name=? OR email=?", (username, email))
        existing_user = cur.fetchone()
        
        if existing_user:
            flash("Adresse email ou Username déjà existant", "danger")
            return redirect(url_for('register'))  # Rediriger vers la page d'inscription
            
        # Si l'utilisateur n'existe pas déjà, ajouter les données dans la base de données
        query = 'INSERT INTO USERS (name, password, email) VALUES (?, ?, ?)'
        cur.execute(query, (username, password, email))
        con.commit()
        con.close()
        return redirect('/')
        
    return render_template('register.html')

@app.route('/utilisateurs')
def utilisateurs():
    if 'username' not in session:
        return redirect(url_for('page_connexion'))  # Rediriger vers la page de connexion si aucun utilisateur n'est connecté
    
    # Récupérer le nom d'utilisateur de la session
    username = session['username']
    
    # Récupérer les données de l'utilisateur connecté à partir de la base de données
    con = sqlite3.connect("user_data.db")
    cur = con.cursor()
    cur.execute("SELECT name, email, password FROM USERS WHERE name=?", (username,))
    utilisateur = cur.fetchone()  # Un seul utilisateur devrait correspondre
    
    con.close()
    
    # Vérifier si l'utilisateur existe dans la base de données
    if utilisateur:
        return render_template('utilisateurs.html', utilisateur=utilisateur)
    else:
        flash("Utilisateur introuvable dans la base de données")
        return redirect(url_for('page_connexion'))  # Rediriger vers la page de connexion si l'utilisateur n'est pas trouvé



@app.route('/testupdatemdp', methods=['GET', 'POST'])
def testupdatemdp():
    if request.method == 'POST':
        username = request.form['name']
        email = request.form['email']
        
        con = sqlite3.connect("user_data.db")
        cur = con.cursor()
        cur.execute("SELECT * FROM USERS WHERE name=? AND email=?", (username, email))
        existing_user = cur.fetchone()
        
        if existing_user:
            new_password = request.form['new_password']
        
            confirm_password = request.form['confirm_password']
            if new_password != confirm_password:
                flash('Les mots de passe ne sont pas identiques')
                return redirect(url_for('testupdatemdp'))
            else:
                cur.execute("UPDATE USERS SET password=? WHERE name=? AND email=?", (new_password, username, email))
                con.commit()
                con.close()
                flash('Mot de passe mis à jour avec succès')
            return redirect(url_for('page-connexion'))
        else:
            flash("Les coordonnées sont incorrectes, veuillez réessayer ou le compte n'existe pas ")
            return redirect(url_for('testupdatemdp'))
    
    return render_template('testupdatemdp.html')


        
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for("page-connexion"))

@app.route('/delete_account')
def delete_account():
    # Afficher une page de confirmation pour la suppression du compte
    return render_template('confirm_delete.html')

@app.route('/propos', methods=['GET', 'POST'] )
def a_propos():

    return render_template('apropos.html')

@app.route('/calendrier', methods=['GET', 'POST'] )
def calendrier():
    return render_template('calendrier.html')

@app.route('/confirm_delete', methods=["POST"])
def confirm_delete():
    if request.form.get("confirm") == "Oui":
        # Supprimer le compte de l'utilisateur de la base de données
        username = session['username']
        con = sqlite3.connect("user_data.db")
        cur = con.cursor()
        
        # Supprimer les enregistrements de la table cameras_users associés à l'utilisateur
        cur.execute('DELETE FROM cameras_users WHERE user_id IN (SELECT pid FROM USERS WHERE name=?)', (username,))
        
        # Supprimer l'utilisateur de la table USERS
        cur.execute("DELETE FROM USERS WHERE name=?", (username,))
        
        con.commit()
        con.close()

        # Supprimer toutes les données associées à l'utilisateur dans la session
        session.clear()

        # Rediriger vers la page d'accueil après la suppression du compte
        return redirect(url_for("page-connexion"))
    else:
        # Si l'utilisateur choisit de ne pas supprimer le compte, rediriger vers une autre page ou faire une autre action
        return redirect(url_for("customer"))


if __name__ == '__main__':
    app.run(debug=True)