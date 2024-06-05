# Documentation for BIMFRASummit24 Methods

Esta documentacion esta escrita en formato Markdown y esta destinada a explicar la funcionalidad del nodo `BIMFRASummit24` en Dynamo. El objetivo es proporcionar una referencia clara y detallada sobre el metodo disponible en esta clase.

Para consultas, [contactar por Linkedin.](https://www.linkedin.com/in/juanmartinezciller/)


## DarBienvenida Method

### Summary
Este metodo da la bienvenida a los asistentes del evento BIMFRASummit'24.

### Parameters
- `nombre` *(string)*: Nombre del asistente al evento.

### Returns
- *(string)*: Mensaje de bienvenida.

### Example
```csharp
string mensaje = BIMFRASummit24.DarBienvenida("Juan");
Console.WriteLine(mensaje);
// Output: Bienvenid@ a BIMFRASummit'24, Juan
```