
terraform {
  required_version = ">= 0.13.6, <0.14.0"
  required_providers {
    external = {
      source = "hashicorp/external"
    }
  }
}
