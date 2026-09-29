from models.book import BookModel
from models.review import ReviewModel

book_list = [
    BookModel(
        title="Sample Book 1",
        author="Author 1",
        description="Description for Sample Book 1",
        user_id=1,
    ),
    BookModel(
        title="Sample Book 2",
        author="Author 2",
        description="Description for Sample Book 2",
        user_id=1,
    ),
    BookModel(
        title="Sample Book 3",
        author="Author 3",
        description="Description for Sample Book 3",
        user_id=2,
    ),
    BookModel(
        title="Sample Book 4",
        author="Author 4",
        description="Description for Sample Book 4",
        user_id=2,
    ),
]

review_list = [
    ReviewModel(
        title="Sample Review 1",
        content="Content for Sample Review 1",
        user_id=3,
        book_id=1,
    ),
    ReviewModel(
        title="Sample Review 2",
        content="Content for Sample Review 2",
        user_id=3,
        book_id=2,
    ),
    ReviewModel(
        title="Sample Review 3",
        content="Content for Sample Review 3",
        user_id=4,
        book_id=3,
    ),
    ReviewModel(
        title="Sample Review 4",
        content="Content for Sample Review 4",
        user_id=4,
        book_id=4,
    ),
]
