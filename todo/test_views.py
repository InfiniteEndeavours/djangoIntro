from django.test import TestCase
from todo.models import Item


# Create your tests here.

class TestDjango(TestCase):

    def test_get_todo_list(self):
        # Simulate get request to the root of the website
        response = self.client.get('/')
        # Check if the response is 200 - OK
        self.assertEqual(response.status_code, 200)
        # Check if the template used is the correct one
        self.assertTemplateUsed(response, 'todo/todo_list.html')

    def test_get_add_item_page(self):
        # Simulate get request to the add item page
        response = self.client.get('/add')
        # Check if the response is 200 - OK
        self.assertEqual(response.status_code, 200)
        # Check if the template used is the correct one
        self.assertTemplateUsed(response, 'todo/add_item.html')

    def test_get_edit_item_page(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f"/edit/{item.id}")
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'todo/edit_item.html')

    def test_can_add_item(self):
        # Simulate post request to the add item page
        response = self.client.post('/add', {'name': 'Test Added Item'})
        self.assertRedirects(response, '/')

    def test_can_delete_item(self):
        item = Item.objects.create(name='Test Todo Item')
        response = self.client.get(f"/delete/{item.id}")
        self.assertRedirects(response, '/')
        # Check if the item was deleted
        existing_items = Item.objects.filter(id=item.id)
        self.assertEqual(len(existing_items), 0)

    def test_can_toggle_item(self):
        item = Item.objects.create(name='Test Todo Item', done=True)
        response = self.client.get(f"/toggle/{item.id}")
        self.assertRedirects(response, '/')
        # Check if the item was toggled
        updated_item = Item.objects.get(id=item.id)
        self.assertFalse(updated_item.done)
