namespace MiPrimerNodo
{
    /// <summary>
    /// BIMFRASummit'24 clase donde se alojan todos los nodos referentes al evento.
    /// </summary>

    public class BIMFRASummit24
    {
        /// <summary>
        /// Constructor vacio para evitar cargar nodos innecesarios.
        /// </summary>
        private BIMFRASummit24()
        {

        }
        /// <summary>
        /// Este nodo dará la bienvenida al evento BIMFRASummit´24.
        /// </summary>
        /// <param name="nombre">Nombre del asistente al evento.</param>
        /// <returns>Mensaje con bienvenida.</returns>
        public static string DarBienvenida(string nombre)
        {
            return $"Bienvenid@ a BIMFRASummit'24, {nombre}";
        }
    }
}
