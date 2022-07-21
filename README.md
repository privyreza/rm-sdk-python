# Official Resellme Python SDK

## Usage
- Make sure you already got you developer token. If you dont have the token refer to this guide: - and that its set properly using this guide: -


## Installation Guide
- Use the pyhton package manager `pip` to install the official Python SDK

```python

pip3 install rm_sdk_python

```

## Import the Resellme module to your project

- Import the resellme package and initiate with the `API_KEY` from Resellme

```python

from rm_sdk_python import Resellme


resellme = Resellme(api_key='Your API Token')
```


## Checking / Searching for Domain Availability

- The `resellme.search_domain` method can return a json object with the values such as `available` or `not_available`

```python

search_response = resellme.search_domain('xyz.co.zw')

# search_response is a json object

if search_response['status'] == 'available':
    # do registration etc
```

## Registering a New Domain

- The client's contact details are entered upon registering the domain
- The SDK uses default nameservers upon creation and registration of the domain, however there is room to update to your preferred nameservers, check the `Updating Nameserver section`

```python
# A contact is created with the details provided upon registering a domain
response = resellme.register_domain(
    domain_name='xbc.co.zw',
    first_name='Beven',
    last_name='Nyamande',
    email='beven@crontab.co.zw',
    company='test1',
    mobile='123123123',
    street_address='123 Xyz Street',
    core_business='Area of business undertaken by the company',
    city='Harare',
    country='Zimbabwe',
)

```

## Updating nameservers
- To update nameservers to custom nameservers, firstly provide the domain name of the site you want to update as shown below
- NB: The method returns a json object

```python
response = resellme.update_nameserver('test8.co.zw',ns1='ns1.xyz.com', ns2='ns2.xyz.com')

```

## Updating Contact details
- To update the `email, mobile, city` details for a specified domain use the following method

```python
contact_details = resellme.update_contact('test.co.zw', email='beven@crontab.co.zw', mobile='123123123', city='Harare')

```

## Get Domains
- You can use this method to fetch all your domains

```python
domains = resellme.get_my_domains()

```