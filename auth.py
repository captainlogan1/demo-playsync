  from flask import Flask, redirect
  import startup
        
        @app.route('/')
        def index():
            response = startup.getUser()
            return redirect(response)