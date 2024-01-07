# My Little Monorepo with Pants
<p>
    <img alt="Python" src="https://img.shields.io/badge/Python-3.10-3776AB.svg?style=flat&logo=python&logoColor=white" />
    <a href="https://github.com/astral-sh/ruff">
      <img alt="Ruff" src="https://img.shields.io/endpoint?url=https://raw.githubusercontent.com/astral-sh/ruff/main/assets/badge/v2.json" />
    </a>
    <a href="https://github.com/psf/black">
      <img alt="Black" src="https://img.shields.io/badge/code%20style-black-000000.svg" />
    </a>
    <a href="https://github.com/PyCQA/docformatter">
      <img alt="Docformatter" src="https://img.shields.io/badge/%20formatter-docformatter-fedcba.svg" />
    </a>
</p>

Welcome to "My Little Monorepo with Pants" -
This repository contains an example of a monorepo with Python which utilizes a powerful tool, called [Pants](https://www.pantsbuild.org/). Feel free to explore, experiment, and adapt the practices demonstrated here to meet your specific development needs. Whether you're new to monorepos or Pants, this repository aims to be a valuable resource for enhancing your development workflow. 🚀✨

## Repository Highlights
* **Pants**: This repository is built on the _**Pants**_ build system. It not only utilizes Pants for code execution but also for various tasks like code formatting, linting, and testing. Additionally, Pants is employed for building and pushing container images (with [Docker](https://docs.docker.com/), as well as managing dependencies.

* **Simple API Example**: Explore a straightforward CRUD API implemented with [FastAPI](https://github.com/tiangolo/fastapi). This example can be instrumental in understanding Python monorepo concepts.
* **Automated Build**: A streamlined continuous integration (CI) and continuous delivery (CD) process is in place, automated through [GitHub Actions](https://docs.github.com/en/actions).

## Core Pants Goals
* [run](https://www.pantsbuild.org/docs/python-run-goal): run an executable or script.
* [test](https://www.pantsbuild.org/docs/python-test-goal): run tests with Pytest.
* [fmt](https://www.pantsbuild.org/docs/python-fmt-goal): autoformat source code.
* [lint](https://www.pantsbuild.org/docs/python-lint-goal): lint source code in check-only mode.
* [check](https://www.pantsbuild.org/docs/python-check-goal): run MyPy.
* [repl](https://www.pantsbuild.org/docs/python-repl-goal): open a REPL (standard shell or IPython).
* [package](https://www.pantsbuild.org/docs/python-package-goal): package your code into an asset, e.g. a wheel or a PEX file.
* [publish](https://www.pantsbuild.org/docs/python-publish-goal): how to distribute packages to a repository


## Repository Structure
```bash
./
├── 3rdparty/
│   ├── BUILD
│   ├── black-requirements.txt
│   ├── black.lock
│   ├── coverage-py-requirements.txt
│   ├── coverage-py.lock
│   ├── docformatter-requirements.txt
│   ├── docformatter.lock
│   ├── pytest-requirements.txt
│   ├── pytest.lock
│   ├── python-default.lock
│   ├── python-requirements.txt
│   ├── ruff-requirements.txt
│   └── ruff.lock
├── BUILD
├── LICENSE
├── README.md
├── pants.ci.toml
├── pants.toml
├── pyproject.toml
├── src/
│   └── todos/
│       ├── BUILD
│       ├── Dockerfile
│       ├── Makefile
│       ├── README.md
│       ├── apps/
│       │   ├── BUILD
│       │   ├── monitor.py
│       │   └── v1/
│       │       ├── BUILD
│       │       └── todos.py
│       ├── main.py
│       └── models/
│           └── v1/
│               ├── BUILD
│               └── todos.py
└── tests/
    └── src/
        └── todos/
            └── apps/
                ├── BUILD
                ├── monitor_test.py
                └── v1/
                    ├── BUILD
                    └── todos_test.py
```

## References
* https://www.pantsbuild.org/
* https://github.com/pantsbuild/actions
* https://github.com/pantsbuild/example-python
* https://blog.pantsbuild.org/pants-pex-and-docker/
* https://blog.pantsbuild.org/optimizing-python-docker-deploys-using-pants/
