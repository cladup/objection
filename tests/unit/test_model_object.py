from app.object.models import Object


def test_new_object():
    """
    GIVEN a new object (gLTF, SBX, ...)
    WHEN a new object is created
    THEN check properties and object store
    """
    new_object = Object('/products/1', 'object_name_from_storage', 'glTF', 'staging')
    assert new_object.alias == '/products/1'
    assert new_object.name == 'object_name_from_storage'
    assert new_object.type == 'glTF'
    assert new_object.status == 'staging'

