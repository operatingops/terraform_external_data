# Contributing

This project follows the [Ubuntu Code of Conduct v2.0][conduct]. Thanks Ubuntu!

This guide based on the one in [factory_girl_rails v4.8.0][source]. Thanks Thoughtbot!

## Code

1. [Fork and clone the repo][fork].

1. Create a feature branch:

   ```shell
   git checkout -b my_feature
   ```

1. Set up your environment:
   1. Install terraform. It is available in [Homebew][homebrew] and [directly from HashiCorp][hashi-downloads].
   1. `terraform init test/terraform`
   1. `python3 venv ~/path/to/venv`
   1. `source ~/path/to/venv/bin/activate`
   1. `pip install -e .[test]`

1. Make your change.

1. Test your change:
   1. `tox`
   1. Each Python version should apply terraform and output a random number of cars from 0-9.
      (This apply is a no-op: it only collects and outputs fake data.)

1. Push to your fork.

   ```shell
   git push origin my_feature
   ```

1. [Create a Pull Request][pr].

At this point you're waiting on us. Remember, you get the SLA you pay for and we don't get paid so we might not respond
right away. We look for the right fix over a quick fix, and we may suggest some changes or improvements or alternatives.

To increase the chance that your pull request gets accepted:

* Follow [Simple Style][style].
* Write [good commit messages][commits].
* Organize your commits. "Fix typo" and "work in progress" commits are hard to follow. If you like to commit often, check out git's [rebase][rebase]. You can use it to clean up at the end.

## Issues

The issue tracker is for project changes. Bugfixes, improvements, etc. If you need help, check out
[operatingops.org][home] instead of submitting an issue.

Write everything you know. Think of the questions we might ask and write the answers. Some great things to include:

  1. What you expected to happen, and why.
  2. What happened that was different from your expectations, and why, if you have any theories.
  3. Whether or not you can contribute a fix.

Like for pull requests, remember that we don't get paid so there's no SLA. We'll respond quickly if we can, though.

[conduct]: https://www.ubuntu.com/about/about-ubuntu/conduct
[commits]: http://tbaggery.com/2008/04/19/a-note-about-git-commit-messages.html
[fork]: https://help.github.com/articles/fork-a-repo/
[hashi-downloads]: https://www.terraform.io/intro/getting-started/install.html
[home]: https://operatingops.org
[homebrew]: https://brew.sh
[pr]: https://help.github.com/articles/creating-a-pull-request/
[rebase]: https://help.github.com/articles/about-git-rebase/
[source]: https://github.com/thoughtbot/factory_girl_rails/blob/v4.8.0/CONTRIBUTING.md
[style]: https://github.com/operatingops/simple_style/blob/v0.1.1/SIMPLE_STYLE.md
