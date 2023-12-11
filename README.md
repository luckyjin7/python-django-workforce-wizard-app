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

### Testing
- Running Tests: ```python manage.py test```
- Writing Tests: Tests are located in ***unittest*** repo within the app.

### Features
**View Team Members**: 
- [x] List all team members
- [x] Reflect the number of team members
- [x] Note that if the team member is an admin, that is listed next to their name
- [x] Click a team member will show the Edit page
- [x] Click the plus button at the top will show the Add page
> [!NOTE]
> This is list view:
<img width="641" alt="image" src="https://github.com/luckyjin7/python-django-workforce-wizard-app/assets/54943321/52e8cfa1-ef4d-4a2c-8bab-ac4f57c86caa">
<hr>

**Add Team Member**:
- [x] Create a new team member entry: user enters a team member's first & last name, their phone number, and email
- [x] Choose the team member's role (it defaults to regular)
- [x] Hitting save adds the team member to the list and shows the List page
> [!NOTE]
> This is Add action: 
![add-user](https://github.com/luckyjin7/python-django-workforce-wizard-app/assets/54943321/f4902f81-5b3f-4dc6-9c4a-68715039d829)
<hr>
 
**Edit Team Member**:
- [x] Update details of an existing team member: a new page form where the user can edit the details of the team member, including changing their role
- [x] Edit page appears when the user clicks a team member on the List page
- [x] Click save edits the team member information and shows the List page
> [!NOTE]
> This is Edit action:
![edit-user](https://github.com/luckyjin7/python-django-workforce-wizard-app/assets/54943321/1c39bc3e-bc83-4859-b570-a7a4524b19f0)
<hr>
 
**Delete Team Member**:
- [x] In Edit page, remove a team member from the list and returns to the List page.
- [x] Delete permission depends on user's role (regular or admin)
> [!NOTE]
> This is Delete action:
![delete-user](https://github.com/luckyjin7/python-django-workforce-wizard-app/assets/54943321/1f337be2-b4ea-47b0-87e0-1bc3aba26cb3)
