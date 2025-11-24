from os import getcwd


def working_dir_endswith(check: str) -> bool:
    return getcwd().endswith(check)
