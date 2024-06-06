"""Define test DAG"""


def task_lint() -> dict:
    return {
        "actions": ["nox -s lint"],
        "verbosity": 2,
    }


def task_unit_tests() -> dict:
    return {
        "task_dep": ["lint"],
        "actions": ["nox -s unit_tests"],
        "verbosity": 2,
    }


def task_integration_tests() -> dict:
    return {
        "task_dep": ["unit_tests"],
        "actions": ["nox -s integration_tests"],
        "verbosity": 2,
    }


def task_e2e_tests() -> dict:
    return {
        "task_dep": ["unit_tests"],
        "actions": ["nox -s e2e_tests"],
        "verbosity": 2,
    }
