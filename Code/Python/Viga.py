# Importamos las clases Point y Line del módulo Autodesk.DesignScript.Geometry
from Autodesk.DesignScript.Geometry import Point, Line

# Importamos el módulo Revit.Elements
import Revit.Elements

# Importamos el módulo clr para poder extender funcionalidades
import clr

# Extendemos las funcionalidades de Revit.Elements
clr.ImportExtensions(Revit.Elements)


# Definimos la clase Viga
class Viga:
    # Método constructor de la clase Viga
    def __init__(self, startPoint: Point, endPoint: Point, level, framingType) -> None:
        self.startPoint = startPoint  # Punto de inicio de la viga
        self.endPoint = endPoint  # Punto de fin de la viga
        self.level = level  # Nivel en el que se ubicará la viga
        self.framingType = framingType  # Tipo de estructura de la viga

    # Método para definir la posición de la viga como una línea
    def definirPosicion(self) -> Line:
        # Creamos una línea a partir del punto de inicio y el punto de fin
        return Line.ByStartPointEndPoint(self.startPoint, self.endPoint)

    # Método para crear la viga en Revit
    def crearViga(self) -> Revit.Elements.StructuralFraming:
        # Creamos la viga utilizando el método BeamByCurve de StructuralFraming
        return Revit.Elements.StructuralFraming.BeamByCurve(
            self.definirPosicion(), self.level, self.framingType
        )


# Creamos una instancia de la clase Viga con puntos de coordenadas específicos, nivel y tipo de estructura proporcionados
viga: Viga = Viga(
    Point.ByCoordinates(0, 0, 0),  # Punto de inicio en las coordenadas (0, 0, 0)
    Point.ByCoordinates(10, 10, 1),  # Punto de fin en las coordenadas (10, 10, 1)
    IN[0],  # Nivel de la viga (entrada IN[0])
    IN[1],  # Tipo de estructura de la viga (entrada IN[1])
)

# Salida que incluye la viga creada, los atributos de la instancia viga y la instancia misma
OUT = viga.crearViga(), vars(viga), viga
