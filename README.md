# oleg_diatlenko_test_pj



# For localhost:

```python
cd oleg_diatlenko_test_pj
virtualenv .
source bin/activate
pip install -r requirements.txt
mkdir media_cdn && mkdir static_cdn
cd src
./manage.py makemigrations
./manage.py migrate
./manage.py createsuperuser
./manage.py loaddata initial_data
./manage.py collectstatis --no-input
```
