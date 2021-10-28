# drugs-and-diseases-management
This is a drug-and-disease catalog management system

# How to Setup
1. Clone Project
```
git clone https://github.com/vietanh2000april@gmail.com/ddms.git
```

2. Go To Project Directory
```
cd ddms
```
3. Create Virtual Environment
```
python -m venv venv
```
4. Active Virtual Environment
```
venv/Scripts/activate.bat
```
5. Install Requirements File
```
pip install -r requirements.txt
```
6. Migrate Database
```
python manage.py migrate
```
7. Create Super User
```
python manage.py createsuperuser
```
8. Run Project
```
python manage.py runserver
```
