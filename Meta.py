'''
Meta class used to force attributes of parent classes in child classes
'''
class Meta(type):
    def __call__(cls, *args, **kwargs):
        class_object = type.__call__(cls, *args, **kwargs)
        class_object.CheckAttributes()
        return class_object

