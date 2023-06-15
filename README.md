# Test project

## Local development

### Setup

We highly recommend to use provided script to setup everything by single command.
Just run the following command from project's root directory and follow instructions:

* `bin/setup`

That's all!

### Style guides and name conventions

#### Linters and code-formatters

We use git-hooks to run linters and formatters before any commit.
It installs git-hooks automatically if you used `bin/setup` command.
So, if your commit is failed then check console to see details and fix linter issues.

We use:

* black - code formatter
* mypy - static type checker
* flake8 - logical and stylistic lint
* flake8-bandit - security linter
* safety - security check for requirements

and few other flake8 plugins, check `requirements/development.txt` for more details.

In order to run checkers manually use the following bash script:

```bash
bin/pre-commit
```
