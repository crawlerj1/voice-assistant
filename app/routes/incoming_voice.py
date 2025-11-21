from app.main import sio
from app.logger import get_logger

logger=get_logger(__name__)


sio.event("start_call")
async def start_call():
    pass