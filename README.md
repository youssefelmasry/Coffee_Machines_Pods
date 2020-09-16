### Getting Started
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
```/coffee/machines/?product_type=COFFEE_MACHINE_LARGE```
#### response
  [
    {
        "code": "CM101"
    },
    {
        "code": "CM102"
    },
    {
        "code": "CM103"
    }
]
