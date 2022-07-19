# Official Resellme Python SDK


## Installation Guide

```python

pip3 install rm_sdk_python

```

#  Import the Resellme module to your project


```python

from rm_sdk_python import Resellme

```

# Create resellme object with the API Token from Resellme

```python

resellme = Resellme(api_key='Your API Token')
```


# Searching for a domain

```python

search_response = resellme.search_domain('xyz.co.zw')

# search_response is a json object

if search_response['status'] == 'pending':
    pass
```

# Registering a domain

```python
# A contact is created with the details provided upon registering a domain

resellme.register_domain(
    domain_name='xbc.co.zw',
    first_name='test1',
    last_name='test1',
    email='test1@test1.com',
    company='test1',
    mobile='0777054115',
    street_address='test1',
    core_business='test1',
    city='Harare',
    country='Zimbabwe',
)

```

