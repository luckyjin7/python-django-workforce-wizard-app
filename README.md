## Team Member Management Application Documentation
### Overview
This documentation provides the necessary steps to build, run, and test the Team Member Management Application. This application, built with Python Django, allows users to view, edit, add, and delete team members.

### Prerequisites
- Virtualenv (optional, but recommended for creating isolated Python environments)
- Python (version 3.11.5)
- Django (latest version)
- Bootstrap: https://mdbootstrap.com/

### Setting Up the Project
1. Create and Activate Virtual Environment (Optional):
- ```virtualenv venv```
- ```source venv/bin/activate```  # On Windows use `venv\Scripts\activate`

2. Create project:
- ```django-admin startproject team_management```

3. Create app:
- ```python manage.py startapp team_management_app```

4. Register models in Database:
- ```python manage.py makemigrations```
- ```python manage.py migrate```
- Create Superuser (Optional, but not applied in this project)
```python manage.py createsuperuser```

5. Run the Server:
- ```python manage.py runserver```

### Accessing the Application
The application will be available at localhost: “http://127.0.0.1:8000/“ once you run the server.
> [!NOTE]
> This is list view:
<img width="641" alt="image" src="https://github.com/luckyjin7/python-django-workforce-wizard-app/assets/54943321/52e8cfa1-ef4d-4a2c-8bab-ac4f57c86caa">

### Testing
- Running Tests: ```python manage.py test```
- Writing Tests: Tests are located in ***unittest*** repo within the app.

### Features
- **View Team Members**: 
  - List all team members
  - Reflect the number of team members
  - Note that if the team member is an admin, that is listed next to their name
  - Click a team member will show the Edit page
  - Click the plus button at the top will show the Add page
 
- **Add Team Member**:
  - Create a new team member entry: user enters a team member's first & last name, their phone number, and email
  - Choose the team member's role (it defaults to regular)
  - Hitting save adds the team member to the list and shows the List page
 
- **Edit Team Member**:
  - Update details of an existing team member: a new page form where the user can edit the details of the team member, including changing their role
  - Edit page appears when the user clicks a team member on the List page
  - Click save edits the team member information and shows the List page
 
- **Delete Team Member**:
  - In Edit page, remove a team member from the list and returns to the List page.
  - Delete permission depends on user's role (regular or admin)
