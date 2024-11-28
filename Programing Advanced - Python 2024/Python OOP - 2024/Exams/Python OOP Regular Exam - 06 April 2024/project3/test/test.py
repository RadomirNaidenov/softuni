from project3.social_media import SocialMedia
from unittest import TestCase


class TestSocialMedia(TestCase):

    def setUp(self):
        self.social_media = SocialMedia("radomir",
                                        "Instagram",
                                        10,
                                        "gaming")

    def test_followers_if_followers_are_less_than_zero_raises(self):
        expected = "Followers cannot be negative."

        with self.assertRaises(ValueError) as ve:
            self.social_media.followers = -20

        self.assertEqual(expected, str(ve.exception))

    def test_followers_if_followers_are_greater_than_zero_and_sett_value(self):
        self.assertEqual(10, self.social_media.followers)

    def test_validate_and_set_platform_if_platform_not_in_allowed_platform_raises(self):
        allowed_platforms = ['Instagram', 'YouTube', 'Twitter']
        expected = f"Platform should be one of {allowed_platforms}"

        with self.assertRaises(ValueError) as ve:
            self.social_media.platform = "tiktok"

        self.assertEqual(expected, str(ve.exception))

    def test__validate_and_set_platform_if_platform_is_in_allowed_platforms(self):
        self.assertEqual("Instagram", self.social_media.platform)

    def test_create_post_is_creating_new_post_and_return_correct_massage(self):
        expected_return = (f"New {self.social_media._content_type} post created by {self.social_media._username} on "
                           f"{self.social_media._platform}.")

        expected_added_in_posts_list = [{'content': 'gaming', 'likes': 0, 'comments': []}]

        actual = self.social_media.create_post("gaming")

        self.assertEqual(expected_added_in_posts_list, self.social_media._posts)
        self.assertEqual(expected_return, actual)

    def test_like_post_if_post_index_is_less_than_zero_return(self):
        expected = "Invalid post index."

        actual = self.social_media.like_post(-2)

        self.assertEqual(expected, actual)

    def test_like_post_if_post_index_is_greater_than_length_of_posts_return(self):
        expected = "Invalid post index."
        actual = self.social_media.like_post(20)

        self.assertEqual(expected, actual)

    def test_like_post_if_post_index_is_valid_and_post_likes_are_less_than_ten_return(self):
        self.social_media._posts = [{'content': 'gaming', 'likes': 0, 'comments': []}]
        expected_output = f"Post liked by {self.social_media._username}."

        actual = self.social_media.like_post(0)

        self.assertEqual(expected_output, actual)

        expected_added_like = [{'content': 'gaming', 'likes': 1, 'comments': []}]

        self.assertEqual(expected_added_like, self.social_media._posts)

    def test_like_post_if_post_index_is_valid_and_post_likes_are_greater_than_ten_return(self):
        self.social_media._posts = [{'content': 'gaming', 'likes': 10, 'comments': []}]

        expected = "Post has reached the maximum number of likes."

        actual = self.social_media.like_post(0)

    def test_comment_on_post_if_the_comment_length_is_greater_than_10_return(self):
        self.social_media._posts = [{'content': 'gaming', 'likes': 11, 'comments': []}]

        expected = f"Comment added by {self.social_media._username} on the post."

        actual = self.social_media.comment_on_post(0, "i dont know what to comment")

        self.assertEqual(expected, actual)

        expected_added_comment = [{'content': 'gaming', 'likes': 11,
                                  'comments': [{'user': self.social_media._username,
                                   'comment': "i dont know what to comment"}]}]

        self.assertEqual(expected_added_comment, self.social_media._posts)

    def test_comment_on_post_if_the_comment_length_is_less_than_ten_return(self):
        expected = "Comment should be more than 10 characters."

        self.social_media._posts = [{'content': 'gaming', 'likes': 10, 'comments': []}]

        actual = self.social_media.comment_on_post(0, "i dont")

        self.assertEqual(expected, actual)










