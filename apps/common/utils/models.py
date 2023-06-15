from nanoid import generate


def id_with_prefix(prefix: str):
    def _generator() -> str:
        return f'{prefix}_{generate()}'

    return _generator
