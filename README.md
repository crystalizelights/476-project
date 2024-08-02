# 476-project
## Link To Live Website
https://dce143.pythonanywhere.com/

## Installing Django On Windows
Follow this link to install Django https://docs.djangoproject.com/en/5.0/howto/windows/

## Setting Up the Project
Navigate to the projects folder, open a terminal and then run these commands

1. `python -m venv env` then enter
2. `env\Script\activate` then enter
3. `cd myproj` then enter
4. `pip install django` then enter
5. `pip install pillow` then enter
6. `cd myproj` then enter
7. `python manage.py migrate` then enter
8. `python manage.py runserver`

You should see a link to the local website



### Running The Project
To run the test cases run: `python manage.py runserver` 

### Testing The Project
To run the test cases run: `python manage.py test` 

## Link To Design Documents
Navigation Structure: https://www.figma.com/design/IEJb2VVUN3osR1E0k08Bn3/Local-Pages?node-id=0-1&t=Jm9g2gk96cLAeOpB-0) <br>
Low-Level Prototype: https://www.canva.com/design/DAGFopQcmv0/H3oVLGWOS6AwGdji2m4eVQ/edit
## Project Structure(Relevant Files)
```
Django proj/
┣ myproj/
┃ ┣ myproj/
┃ ┃ ┣ asgi.py
┃ ┃ ┣ settings.py
┃ ┃ ┣ urls.py
┃ ┃ ┣ wsgi.py
┃ ┃ ┗ __init__.py
┃ ┣ my_store/
┃ ┃ ┣ templates/
┃ ┃ ┃ ┗ my_store/
┃ ┃ ┃   ┗ index.html
┃ ┃ ┣ admin.py
┃ ┃ ┣ apps.py
┃ ┃ ┣ models.py
┃ ┃ ┣ tests.py
┃ ┃ ┣ urls.py
┃ ┃ ┗ views.py
┃ ┣ static/
┃ ┃ ┣ css/
┃ ┃ ┣ images/
┃ ┣ stores/
┃ ┃ ┣ templates/
┃ ┃ ┃ ┗ stores/
┃ ┃ ┃   ┣ detail.html
┃ ┃ ┃   ┗ form.html
┃ ┃ ┣ admin.py
┃ ┃ ┣ apps.py
┃ ┃ ┣ forms.py
┃ ┃ ┣ models.py
┃ ┃ ┣ tests.py
┃ ┃ ┣ urls.py
┃ ┃ ┗ views.py
┃ ┣ vendor/
┃ ┃ ┣ templates/
┃ ┃ ┃ ┗ vendor/
┃ ┃ ┃   ┣ index.html
┃ ┃ ┃   ┣ login.html
┃ ┃ ┃   ┣ reviewInbox.html
┃ ┃ ┃   ┣ reviewNew.html
┃ ┃ ┃   ┣ signup.html
┃ ┃ ┃   ┗ userSettingsPage.html
┃ ┃ ┣ admin.py
┃ ┃ ┣ apps.py
┃ ┃ ┣ forms.py
┃ ┃ ┣ models.py
┃ ┃ ┣ tests.py
┃ ┃ ┣ urls.py
┃ ┃ ┗ views.py
┣ db.sqlite3
┣ manage.py
┗ settings.py

```



