from uuid import UUID


async def get_category_by_name(category: str) -> UUID:
    """get and validate a video category"""
    raise NotImplementedError()


async def get_video_by_id(video_id: str) -> UUID:
    """get and validate a video by it's id"""
    raise NotImplementedError()


async def get_comment_by_id(comment_id: str) -> UUID:
    """get and validate a comment by it's id"""
    raise NotImplementedError()
