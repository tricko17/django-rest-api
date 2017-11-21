# from rest_framework import APITestCase
# from django.core.urlresolvers import resolve
# from albums.models import Album

# class AlbumAPITestCase(APITestCase):
    
#     def setUp(self):
#         self.kind_of_blue = Album.objects.create(
#             name='Kind of Blue'
#         )
#         self.a_love_supreme = Album.objects.create(
#             name='A Love Supreme'
#         )
    
#     def test_list_albums(self):
#         """
#             Test that we can get a list of albums
#         """
#         response = self.client.get('/api/albums/')

#         self.assertEqual(response.status_code, 200)
#         self.assertEqual(response.data[0]['name'], 'A Love Supreme')
#         self.assertEqual(response.data[1]['url'], 'http://localhsot:8000/api/albums/1/')

