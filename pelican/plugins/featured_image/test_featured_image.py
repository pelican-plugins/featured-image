import unittest

from jinja2.utils import generate_lorem_ipsum

from pelican.contents import Article, Page

from . import featured_image

# Generate content with image
TEST_CONTENT_IMAGE_URL = "https://testimage.com/test.jpg"
TEST_CONTENT = (
    str(generate_lorem_ipsum(n=3, html=True))
    + '<img src="'
    + TEST_CONTENT_IMAGE_URL
    + '"/>'
    + str(generate_lorem_ipsum(n=2, html=True))
)  # noqa
TEST_SUMMARY_IMAGE_URL = "https://testimage.com/summary.jpg"
TEST_SUMMARY_WITHOUTIMAGE = str(generate_lorem_ipsum(n=1, html=True))
TEST_SUMMARY_WITHIMAGE = (
    TEST_SUMMARY_WITHOUTIMAGE + '<img src="' + TEST_SUMMARY_IMAGE_URL + '"/>'
)  # noqa
TEST_CUSTOM_IMAGE_URL = "https://testimage.com/custom.jpg"


class TestFeaturedImage(unittest.TestCase):
    """Test the Featured Image plugin."""

    def setUp(self):
        super().setUp()

    def test_extract_image_from_content(self):
        args = {
            "content": TEST_CONTENT,
            "metadata": {
                "summary": TEST_SUMMARY_WITHOUTIMAGE,
            },
        }

        article = Article(**args)
        featured_image.images_extraction(article)
        self.assertEqual(article.featured_image, TEST_CONTENT_IMAGE_URL)

    def test_extract_image_from_summary(self):
        args = {
            "content": TEST_CONTENT,
            "metadata": {
                "summary": TEST_SUMMARY_WITHIMAGE,
            },
        }

        article = Article(**args)
        featured_image.images_extraction(article)
        self.assertEqual(article.featured_image, TEST_SUMMARY_IMAGE_URL)
        self.assertEqual(article._summary, TEST_SUMMARY_WITHOUTIMAGE)

    def test_extract_image_from_summary_with_custom_image(self):
        args = {
            "content": TEST_CONTENT,
            "metadata": {
                "summary": TEST_SUMMARY_WITHIMAGE,
                "image": TEST_CUSTOM_IMAGE_URL,
            },
        }

        article = Article(**args)
        featured_image.images_extraction(article)
        self.assertEqual(article.featured_image, TEST_CUSTOM_IMAGE_URL)
        self.assertEqual(article._summary, TEST_SUMMARY_WITHOUTIMAGE)

    def test_extract_image_from_page_summary_with_custom_image(self):
        args = {
            "content": TEST_CONTENT,
            "metadata": {
                "summary": TEST_SUMMARY_WITHIMAGE,
                "image": TEST_CUSTOM_IMAGE_URL,
            },
        }
        page = Page(**args)
        featured_image.images_extraction(page)
        self.assertEqual(page.featured_image, TEST_CUSTOM_IMAGE_URL)
        self.assertEqual(page._summary, TEST_SUMMARY_WITHOUTIMAGE)


if __name__ == "__main__":
    unittest.main()
