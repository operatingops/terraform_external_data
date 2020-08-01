import random

from terraform_external_data import terraform_external_data


@terraform_external_data
def count_things(query):
    """
    Dummy function that simulates data collection with a count.
    """
    return {query['thing_to_count']: str(random.randint(0, 4))}


if __name__ == '__main__':
    # Always protect Python scripts from import side effects with a condition to check the __name__.
    # Not specifically necessary for terraform_external_data, it's a best practice in general.
    count_things()
