from Autodesk.DesignScript.Geometry import *
from RevitServices.Transactions import TransactionManager
from RevitServices.Persistence import DocumentManager
import RevitServices
import Revit
from System.Collections.Generic import List
from Autodesk.Revit.UI import *
from Autodesk.Revit.DB.Structure import *
from Autodesk.Revit.DB import *
import clr

clr.AddReference('RevitAPI')

clr.AddReference('RevitAPIUI')

clr.AddReference('System')

clr.AddReference('RevitNodes')
clr.ImportExtensions(Revit.GeometryConversion)
clr.ImportExtensions(Revit.Elements)

clr.AddReference('RevitServices')


doc = DocumentManager.Instance.CurrentDBDocument
uidoc = DocumentManager.Instance.CurrentUIApplication.ActiveUIDocument

# Preparing input from dynamo to revit
element = UnwrapElement(IN[0])

# Do some action in a Transaction
TransactionManager.Instance.EnsureInTransaction(doc)

TransactionManager.Instance.TransactionTaskDone()

OUT = element
