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

# Example Usage

1. As always, create and activate a [venv][venv] (Python 3) or [virtualenv][virtualenv] (Python 2).
    ```shell
    python3 -m venv env3
    source env3/bin/activate
    ```

1. Install `terraform_external_data` in the env.
    ```shell
    pip install terraform_external_data
    ```

1. Write a script with a data collection function decorated by `terraform_external_data` (the `@` syntax below). Your function must take at least one argument, the query data passed in by terraform. For example, `get_cool_data.py`:
    ```python
    from terraform_external_data import terraform_external_data

    @terraform_external_data
    def get_cool_data(query):
        """
        Dummy function that simulates data collection with a count.

        Here you could reach out to an API, inspect local files, etc.
        """
        count = 0
        for i in range(3):
            count += 1

        # Terraform requires the values you return be strings,
        # so terraform_external_data will error if they aren't.
        return {query['thing_to_count']: str(count)}

    if __name__ == '__main__':
        # Always protect Python scripts from import side effects with
        # a condition to check the __name__. Not specifically necessary
        # for terraform_external_data, but it's a best practice in general.
        get_cool_data()
    ```

1. Add a `data` resource to your terraform file. For example, `terraform.tf`:
    ```hcl
    data "external" "cars_count" {
      program = ["python", "${path.module}/get_cool_data.py"]

      query = {
        # This is the query data your function will receive as an argument.
        thing_to_count = "cars"
      }
    }

    # Reference the data like any terraform var. This example uses an
    # output so it doesn't modify infrastructure.
    output "cars_count" {
      value = "${data.external.cars_count.result.cars}"
    }
    ```

[protocol]: https://www.terraform.io/docs/providers/external/data_source.html#external-program-protocol
[venv]: https://docs.python.org/3/library/venv.html
[virtualenv]: https://virtualenv.pypa.io/en/stable/
