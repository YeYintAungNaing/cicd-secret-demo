def login(username):
        if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        
        conn = get_db_connection()
        # Find the user in the database using another direct query
        query = f"SELECT * FROM users WHERE username = '{username}' AND password = '{password}'"
        user = conn.execute(query).fetchone()
        conn.close()

        if user:
            # Success! Let's make a response and set a cookie.
            resp = make_response(redirect(url_for('home')))
            resp.set_cookie('username', user['username'])
            return resp
        else:
            flash('Incorrect username or password.')
            return redirect(url_for('login'))
        
        
        
print("test")

