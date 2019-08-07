About
=====

Provides a decorator that implements terraform's `external program protocol`_ for data sources.

* Reads in JSON from :code:`stdin`.
* Validates input.
* Outputs JSON to :code:`stdout`.
* Validates output.
* Prints human-readable, one-line errors on :code:`stderr`.
* Returns a non-zero status code on errors.

This saves you from fiddling with the spec and makes it easy to write several external data scripts without duplicating
code.

The wrapped function must expect its first positional argument to be a dictionary of the query data.

See the `contributing guide`_ for instructions on developing and running tests.

Example Usage
=============

1. As always, create and activate a venv_.

   .. code:: bash

      python -m venv env
      source env/bin/activate

2. Install `terraform_external_data` in the env.

   .. code:: bash

      pip install terraform_external_data


3. Write a script with a data collection function decorated by :code:`terraform_external_data` (the :code:`@` syntax below). Your function must take at least one argument, the query data passed in by terraform. For example, :code:`get_cool_data.py`:

   .. code:: python

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

4. Add a :code:`data` resource to your terraform file. For example, :code:`terraform.tf`:

   ::

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
        value = data.external.cars_count.result.cars
      }


.. _external program protocol: https://www.terraform.io/docs/providers/external/data_source.html#external-program-protocol
.. _contributing guide: https://github.com/operatingops/terraform_external_data/blob/master/CONTRIBUTING.md
.. _venv: https://docs.python.org/3/library/venv.html
.. _virtualenv: https://virtualenv.pypa.io/en/stable/
