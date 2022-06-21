# SuperCoder

**Python :**.
1. How security can be implemented in Python.
&emsp;<details>Careful when downloading the package. - PyPl - packages issues can be reported but package added to pypl does not undergo review. We can use https://snyk.io/advisor/ to check package security health.
  User python capacity for virtual environment.
  Set `Debug = False` in production. - Make sure to switch debugging to False in production to prevent leaking sensitive application information to attackers.
  Be careful with string formatting.
  (De)serialize very cautiously
  Do not use the system standard version of Python - problem with build python is its not latest version.
  
1. How security can be implemented in Django.
&emsp;<details>
  Use SSL - Deploy your site behind HTTPS.
  Changing URL - Change the default admin URL from /admin/ to something else
  Require stronger passwords
  Never run `DEBUG` in production - When DEBUG is set to True in your settings file, errors will display with full tracebacks that are likely to contain information you don't want end users to see. 
  
