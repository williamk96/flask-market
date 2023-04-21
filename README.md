# flask-market

This repository was made to learn how to implement ecommerce application-specific functionality.

## Technologies: the Flask Web Framework, several Flask extensions, and SQLite3 database.

## Working:

- Add twofa_status column to Users table that is constrained to the following values: disabled, registered, enabled

- Then, add twofa functionality using pyotp in routes.py

- Then, add associated static page

- Plan for using a distributed set of flask-market instances while maintaining the auto-secret-key functionality that works when using one instance at a time
