from unittest import TestCase

from blog import Blog


class BlogTEST(TestCase):

    def test_creat_post_in_blog(self):
        b = Blog('Test', 'Test Author')
        b.createPost('Test Post', 'Test Content')


        self.assertEqual(len(b.posts), 1)
        self.assertEqual(b.posts[0].title, 'Test Post')
        self.assertEqual(b.posts[0].content, 'Test Content')

    def test_json(self):
        b = Blog('Test', 'Test Author')
        b.createPost('Test Post', 'Test Content')

        expectd = {'title' :'Test', 'content': 'Test Author',
                   'post': [{'title' :'Test Post', 'content': 'Test Content'}]}

        self.assertDictEqual()