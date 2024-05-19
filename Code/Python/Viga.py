from Autodesk.DesignScript.Geometry import (
    Point,
    Line,
)  # Importar las clases Point y Line del módulo DesignScript.Geometry de Autodesk
import Revit.Elements  # Importar el módulo Revit.Elements
import clr  # Importar Common Language Runtime (CLR) para interoperabilidad con .NET

clr.ImportExtensions(
    Revit.Elements
)  # Extender las funcionalidades de Revit.Elements con CLR


class Viga:
    def __init__(self, startPoint: Point, endPoint: Point, level, framingType) -> None:
        """
        Constructor para la clase Viga.

        :param startPoint: Punto de inicio de la viga
        :param endPoint: Punto de finalización de la viga
        :param level: Nivel en el que se colocará la viga
        :param framingType: Tipo de estructura de la viga
        """
        self.startPoint = startPoint  # Asignar el punto de inicio a la viga
        self.endPoint = endPoint  # Asignar el punto de finalización a la viga
        self.level = level  # Asignar el nivel de la viga
        self.framingType = framingType  # Asignar el tipo de estructura de la viga

    def definirPosicion(self) -> Line:
        """
        Define la posición de la viga creando una línea entre los puntos de inicio y final.

        :return: Línea que representa la posición de la viga
        """
        return Line.ByStartPointEndPoint(
            self.startPoint, self.endPoint
        )  # Crear una línea desde el punto de inicio al punto de finalización

    def creaViga(self) -> Revit.Elements.StructuralFraming:
        """
        Crea la viga en Revit utilizando la línea definida y los parámetros dados.

        :return: Objeto de viga estructural de Revit
        """
        return Revit.Elements.StructuralFraming.BeamByCurve(
            self.definirPosicion(), self.level, self.framingType
        )  # Crear la viga estructural en Revit con la línea definida, el nivel y el tipo de estructura


# Crear una instancia de la clase Viga con puntos específicos, nivel y tipo de estructura obtenidos de IN
viga_instancia: Viga = Viga(
    Point.ByCoordinates(0, 0, 0),  # Punto de inicio (0, 0, 0)
    Point.ByCoordinates(10, 10, 1),  # Punto de finalización (10, 10, 1)
    IN[0],  # Nivel desde la entrada IN
    IN[1],  # Tipo de estructura desde la entrada IN
)

# Salida del script: la viga creada y la instancia de la clase Viga
OUT = viga_instancia.creaViga(), viga_instancia
