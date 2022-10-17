# Django Security


## SECRET_KEY
-  It is a very long key combination of character, number and special character to avoid from brute attack.
-  It is located in settings.py
-  The Django secret key is used to provide cryptographic signing.
-  It is used for session security.
-  This key is mostly used to sign session cookies.
-  If one were to have this key, they would be able to modify the cookies sent by the application.
-  Django doesn't provide a way to check for suspicious activity.
-  **Revoke Secret Key :**
   -  To revoke the key, a new secret needs to be generated. All sessions or cookies signed with the key will be invalided.
