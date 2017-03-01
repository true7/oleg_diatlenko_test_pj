# oleg_diatlenko_test_pj


```python
cd oleg_diatlenko_test_pj
virtualenv .
source bin/activate
pip install -r requirements.txt
cd src
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata initial_data
```
