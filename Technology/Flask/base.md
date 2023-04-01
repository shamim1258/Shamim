# Flask
-  Python 2.6 or higher is usually required for installation of Flask. Although Flask and its dependencies work well with Python 3 (Python
-  Dependencies : These distributions will be installed automatically when installing Flask.
   -  Werkzeug implements WSGI, the standard Python interface between applications and servers.
   -  Jinja is a template language that renders the pages your application serves.
   -  MarkupSafe comes with Jinja. It escapes untrusted input when rendering templates to avoid injection attacks.
   -  ItsDangerous securely signs data to ensure its integrity. This is used to protect Flask’s session cookie.
   -  Click is a framework for writing command line applications. It provides the flask command and allows adding custom management commands.
-  Optional dependencies : These distributions will not be installed automatically. Flask will detect and use them if you install them.
   -  Blinker provides support for Signals.
   -  python-dotenv enables support for Environment Variables From dotenv when running flask commands.
   -  Watchdog provides a faster, more efficient reloader for the development server.
-  Debug Mode : The flask run command can do more than just start the development server. By enabling debug mode, the server will automatically reload if code changes, and will show an interactive debugger in the browser if an error occurs during a request.
   -  The debugger allows executing arbitrary Python code from the browser. It is protected by a pin, but still represents a major security risk. Do not run the development server or debugger in a production environment.
   -  To enable debug mode, use the --debug option.
-  `SQLAlchemy(app)` this creates SQLAlchemy object which contains an auxiliary function for the ORM operation.It also provides a parent Model class that uses it to declare a user-defined model.In the code snippet below, the studients model is created.

## Database Migration
-  `flask db init`
   -  This will add a migrations folder to your application. The contents of this folder need to be added to version control along with your other source files.  
-  `flask db migrate`
   -  To generate initial migration.
-  `flask db upgrade`
   -  To apply the changes described by the migration script to your database.
