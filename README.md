1. The first thing to do is to clone the repository:

```sh
git clone https://github.com/nandinimalik16/NinjaStudy-Task1.git
cd NinjaStudy-Task1
```

2. Create a virtual environment to install dependencies in and activate it:

```sh
virtualenv env
env\Scripts\activate
```

Then install the dependencies:

```sh
pip install -r requirements.txt
```

3. Once `pip` has finished downloading the dependencies:
```sh
cd taskManagement
python manage.py runserver
```
