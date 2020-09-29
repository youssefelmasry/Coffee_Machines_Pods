### Getting Started
_In this task Django restframework and Mongodb are used_

1. __*clone the project and go to the project directory*__
1. __*create and activate your virtualenv & run pip install -r req.txt*__
1. __*create mongo db with name "coffee" (or change name to what ever you want BUT also in settings.py)*__
1. __*run python manage.py migrate*__
1. __*Ready to go*__

There are 2 endpoints:
1. ```/coffee/pods/?query_params``` GET
  * You Can Filter With query_params:
    1. product_type
    1. coffee_flavor
    1. pack_size
1. ```/coffee/machines/?query_params``` GET
  * You Can Filter With query_params:
    1. product_type
    1. water_line_compatible
    
__*These Apis return a List of objects of SKU products codes*__
### Examples

```/coffee/machines/?product_type=COFFEE_MACHINE_LARGE&water_line_compatible=True```
gets all large machines that water line compatible

### response
[
    {
        "code": "CM102"
    },
    {
        "code": "CM103"
    }
]

```/coffee/pods/?coffee_flavor=COFFEE_FLAVOR_HAZELNUT&pack_size=1 dozen```
get all pods with flavor hazelnut and pack size 1 dozen

### response
[
    {
        "code": "CP041"
    },
    {
        "code": "CP141"
    }
]