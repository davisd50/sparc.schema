import unittest
from zope import interface, schema
from zope.schema import fieldproperty
from .. import resource

class UnitTestSchemaResource(unittest.TestCase):
    
    def test_schema_resource(self):
        
        class ITestSchema(interface.Interface):
            a = schema.ASCIILine(required=False)
            b = schema.ASCIILine(required=False, default='default')
            c = schema.ASCIILine(required=True)
            d = schema.ASCIILine(required=True, default='default')
        
        class TestResource(resource.SchemaResource):
            _schema = ITestSchema
            fieldproperty.createFieldProperties(ITestSchema)
        
        #only schema keys are assigned
        r = TestResource(c='assigned', not_valid='not_assigned')
        self.assertEqual(getattr(r,'not_valid', None), None)
