# Django:
    Is A Back-End Server Side Web FrameWork, Open Source And Written In Python.
    Django Makes Building Of The Web Pages Easy Using Python.
    Django Following MVT(Module View Template) Pattern.

- Installation: `pip install django`
- Create Project: `django-admin startproject PRJECTNAME`
- Run The Server: `python3 manage.py runserver`
- Create App: `python3 manage.py startaapp APPNAME`

# This Is What Happen When We Send Request To `DJANGO`
    1-Django receives the URL, checks the urls.py file, and calls the view that matches the URL.\
    2-The view, located in views.py, checks for relevant models.\
    3-The models are imported from the models.py file.\
    4-The view then sends the data to a specified template in the template folder.\
    5-template contains HTML&Django tags and with the data it returns finished HTML content back to the browser.