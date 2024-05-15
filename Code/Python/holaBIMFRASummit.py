def holaBIMFRASummit(nombres: list[str], asistente: str) -> str:
    """Esta funcion devuelve si el asistente que intenta entrar esta en la lista de invitados.

    Args:
        nombres (list[str]): lista de invitados.
        asistente (str): persona que intenta entrar

    Returns:
        str: mensaje indicando si el asistente tiene acceso al evento.
    """
    nombres_upper: list[str] = [nombre.upper() for nombre in nombres]

    if asistente.upper() in nombres_upper:
        return f"Bienvenid@ a BIMFRASummit'24, {asistente}"
    else:
        return f"{asistente} no se encuentra en la lista"


resultado: str = holaBIMFRASummit(IN[0], IN[1])

OUT: str = resultado
