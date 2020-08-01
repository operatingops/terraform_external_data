# Contributing

This guide based on the one in [factory_girl_rails v4.8.0][source]. Thanks Thoughtbot!

## Conduct

We'd love for you to contribute, and we want you to be you while you do it. This project follows a few rules that we hope will make contributing a good experience for everyone. These rules are just a framework; they're here to help you understand how the project works. Each contributor is responsible for their conduct.

* Be professional.
* The project's maintainers manage the project. You (hopefully!) contribute. Don't try to manage the project or the people working on it unless a current maintainer specifically asks you to.
* Only use the project to work on the project. Take non-project conversations and activities somewhere else.
* Contribute your own work. If you use someone else's work:
  * Make sure it has a non-viral (e.g. no GNU) license that allows you to use it on this project.
  * Credit them where you use their work (e.g. with a link in a comment).

## Code

1. [Fork and clone the repo][fork].

1. Create a feature branch:

   ```shell
   git checkout -b my_feature
   ```

1. Set up your environment:
   1. Install terraform. It is available in [Homebew][homebrew] and [directly from HashiCorp][hashi-downloads].
   1. `python venv ~/path/to/venv`
   1. `source ~/path/to/venv/bin/activate`
   1. `pip install -e .[test]`

1. Make your change.

1. Test your change:

   `tox`

   If you're having trouble getting all the right Python versions installed, I recommend [pyenv][pyenv]. Here's how I [set it up on OS X][python-osx]. You may need to run a command similar to this to get tox to detect the versions it installs:

   `pyenv local 3.8.5 3.7.8 3.6.11`

1. [Bump the version](https://semver.org/spec/v2.0.0.html) in setup.py.

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
[pyenv]: https://github.com/pyenv/pyenv
[python-osx]: https://operatingops.org/2018/02/04/python-on-mac-one-of-the-good-ways/
[rebase]: https://help.github.com/articles/about-git-rebase/
[source]: https://github.com/thoughtbot/factory_girl_rails/blob/v4.8.0/CONTRIBUTING.md
[style]: https://github.com/operatingops/simple_style/blob/v0.2.0/SIMPLE_STYLE.md
