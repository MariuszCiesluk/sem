# sem
Primary TODO List webapp

This a simple Django app to prepare list with tasks and nested subtasks. 
Using: django1.9, bootstrap3, django-rest-framework, postgreSQL

Funcionality:
1. Register and login by user
2. Add, erase, update a simple task
3. Task with: priority, status (checked), name (description) and nested list with items
4. Task could be moved on other person
5. App have a rest api, with basic authentication (if you need token-auth, just let me know), example:
http://127.0.0.1:8000/tasks/list-elements/2/
http://127.0.0.1:8000/tasks/list/6/
http://127.0.0.1:8000/tasks/list/
6. Every modification is recorded in history. In update-view there is a table with date and previous versions.
7. Some class docs in code
