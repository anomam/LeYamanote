import nox


@nox.session
def lint(session: nox.Session) -> None:
    session.install(".[test]")
    session.run("isort", "--settings-file", "./pyproject.toml", "leyamanote", "tests")
    session.run("black", "--config", "./pyproject.toml", "leyamanote", "tests")
    session.run("flake8")
    session.run("mypy", "--config-file=./pyproject.toml", "leyamanote", "tests")


@nox.session
def unit_tests(session: nox.Session) -> None:
    session.install(".[test]")
    session.run("pytest", "-s", "tests/test_unit.py")


@nox.session
def integration_tests(session: nox.Session) -> None:
    session.install(".[test]")
    session.run("pytest", "-s", "tests/test_integration.py")


@nox.session
def e2e_tests(session: nox.Session) -> None:
    session.install(".[test]")
    session.run("pytest", "-s", "tests/test_e2e.py")
