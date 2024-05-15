def hola_bimfra_summit(nombres: list[str], asistente: str) -> str:
    """Esta función devuelve si el asistente que intenta entrar está en la lista de invitados.

    Args:
        nombres (list[str]): Lista de invitados.
        asistente (str): Persona que intenta entrar.

    Returns:
        str: Mensaje indicando si el asistente tiene acceso al evento.
    """
    # Convertir todos los nombres de la lista de invitados a mayúsculas.
    nombres_upper: list[str] = [nombre.upper() for nombre in nombres]

    # Verificar si el nombre del asistente (en mayúsculas) está en la lista de invitados (también en mayúsculas).
    if asistente.upper() in nombres_upper:
        # Si el asistente está en la lista, retornar un mensaje de bienvenida.
        return f"Bienvenid@ a BIMFRASummit'24, {asistente}"
    else:
        # Si el asistente no está en la lista, lanzar una excepción con un mensaje de error.
        raise Exception(f"{asistente} no se encuentra en la lista")


# Llamada a la función hola_bimfra_summit con los valores de entrada y almacenamiento del resultado.
resultado: str = hola_bimfra_summit(IN[0], IN[1])

# Asignación del resultado a la variable de salida.
OUT: str = resultado
