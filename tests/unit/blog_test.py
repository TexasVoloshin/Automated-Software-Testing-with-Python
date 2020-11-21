from unittest  import TestCase
from blog import Blog

class BlogTest(TestCase):

    def test_create_blog(self):
        b=Blog('Test', 'Test author')
        self.assertEqual('Test',b.tittle)
        self.assertEqual('Test author', b.author)
        self.assertListEqual([],b.posts)
        self.assertEqual(0,len(b.posts))



    def test_repr(self):
        b = Blog('Test', 'Test Author')
        b2 = Blog('Bob', 'Test Bob')
        self.assertEqual(b.__repr__(), 'Test by Test Author (0 posts)')
        self.assertEqual(b2.__repr__(), 'Bob by Test Bob (0 posts)')

    def test_repr_multiple_posts(self):

        b = Blog('Test', 'Test Author')
        b.posts = ['test']

        b2 = Blog('Bob', 'Test Bob')
        b2.posts = ['test', 'another']

        self.assertEqual(b.__repr__(), 'Test by Test Author (1 post)')
        self.assertEqual(b2.__repr__(), 'Bob by Test Bob (2 posts)')

