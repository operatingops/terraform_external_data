# About

Provides a decorator that implements terraform's [external program protocol][protocol] for data sources.
* Reads in JSON from `stdin`.
* Validates input.
* Outputs JSON to `stdout`.
* Validates output.
* Prints human-readable, one-line errors on `stderr`.
* Returns a non-zero status code on errors.

This saves you from fiddling with the spec and makes it easy to write several external data scripts without duplicating
code.

The wrapped function must expect its first positional argument to be a dictionary of the query data.

# Example

Custom script (`get_cool_data.py`):
```python
from terraform_external_data import terraform_external_data

@terraform_external_data
def get_cool_data(query):
    return {query['thing_to_count']: '3'}

if __name__ == '__main__':
    get_cool_data()
```

Terraform:
```hcl
data "external" "cars_count" {
  program = ["python", "${path.module}/get_cool_data.py"]

  query = {
    thing_to_count = "cars"
  }
}

output "cars_count" {
  value = "${data.external.cars_count.result.cars}"
}
```

[protocol]: https://www.terraform.io/docs/providers/external/data_source.html#external-program-protocol
