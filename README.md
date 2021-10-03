# Official Resellme Python SDK

## Installation Guide

```python


pip3 install rm_sdk_python


```

#  Create a Resellme instance


```python


from rm_sdk_python import Resellme



# Create resellme object with API Token from Resellme

resellme = Resellme(api_key='Your API Token')



# Searching a Domain

search = resellme.search_domain('xyz.co.zw')

# Domain registration Process
# NB: Nameservers default to Resellme Name servers

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

