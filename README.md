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

json_response = resellme.search_domain('xyz.co.zw')


# Handle json response data contained in json_response




```

