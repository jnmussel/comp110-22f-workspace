"""For fun."""

def z(s: int) -> list[str]:
    """Helloooo."""
    a_list: list[str] = []
    i: int = 0
    while i <= s:
        if s % i == 0:
            a_list.append("yo")
        elif i * s > 10:
            a_list.append("hwb")
        else:
            a_list.append("7")
    return a_list


def vc(qw: list[str]) -> dict[str, int]:
    """Docstring lol."""
    
