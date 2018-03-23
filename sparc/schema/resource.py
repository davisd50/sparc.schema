from zope import interface
from zope.schema import getFields


class SchemaResource(object):
    """A mixin class for rapid schema-based type generation
    
    example:
        from zope import schema
        from zope.schema import fieldproperty
        from sparc.schema import resource
        
        class ITestSchema(interface.Interface):
            a = schema.ASCIILine(required=False)
            b = schema.ASCIILine(required=False, default='default')
            c = schema.ASCIILine(required=True)
            d = schema.ASCIILine(required=True, default='default')
        
        class TestResource(resource.SchemaResource):
            _schema = ITestSchema
            fieldproperty.createFieldProperties(ITestSchema)
        
        MyResource = TestResource(c='required_value')
    """
    _schema = interface.Interface
    def __init__(self, **kwargs):
        fields = getFields(self._schema)
        for n in fields:
            if n in kwargs:
                setattr(self, n, kwargs[n])
            else:
                if fields[n].required and not fields[n].default:
                    setattr(self, n, None)