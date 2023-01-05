#### Step

1. สร้าง virtual environment

```
py -m venv .venv
```

2. Activate environment

```
.venv\scripts\activate
```

3. Upgrade pip

```
py -m pip install --upgrade pip
```

4. Install django

```
py -m pip install django
```

5. Migrate model

```
py web_project/manage.py migrate
```

6. Run Server

```
py web_project/manage.py runserver 8001
```
