# apps/common/tests/test_behaviors/test_mixins.py
class BehaviorTestCaseMixin(object):
    @property
    def model(self):
        raise NotImplementedError("Implement Me")

    def create_instance(self, **kwargs):
        return self.model.objects.create(**kwargs)
