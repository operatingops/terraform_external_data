provider "external" {
  version = "~> 1.0"
}

data "external" "cars_count" {
  program = ["python", "${path.module}/count_things.py"]

  query = {
    # This is the query data your function will receive as an argument.
    thing_to_count = "cars"
  }
}

# Reference the data like any terraform var. This example uses an output so it doesn't modify infrastructure.
output "cars_count" {
  value = "${data.external.cars_count.result.cars}"
}
