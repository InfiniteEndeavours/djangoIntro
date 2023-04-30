from django.test import TestCase
from .forms import ItemForm


# Create your tests here.

class TestItemForm(TestCase):

    def test_item_name_is_required(self):
        # Test that the name field is required
        form = ItemForm({'name': ''})
        # Check if the form is valid
        self.assertFalse(form.is_valid())
        self.assertIn('name', form.errors.keys())
        # Check if the error message is correct
        self.assertEqual(form.errors['name'][0], 'This field is required.')

    def test_done_field_is_not_required(self):
        # Test that the done field is not required
        form = ItemForm({'name': 'Test Todo Item'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        # Test that the fields are explicitly specified in the metaclass
        form = ItemForm()
        self.assertEqual(form.Meta.fields, ['name', 'done'])

