from fastapi import APIRouter, Depends

from server.controllers.auth_controller import get_current_user
import server.controllers.operation_controller as operation_controller
from server.schemas.rating import DoByRequest

router = APIRouter(tags=["Operation"], dependencies=[Depends(get_current_user)])


@router.post("/crawl")
async def crawl_by(request: DoByRequest):
    """
    Delete the database.
    """
    return operation_controller.crawl_by(request.input_data, request.by)


# @router.post("/update/")
# async def update_database(request: DoByRequest):
#     """
#     Update the database.
#     """
#     if request.by == "keyword":
#         return {"message": f"Update the database, add {request.input_data}"}
#     elif request.by == "url":
#         return {"message": f"Update the database, add item in link :  {request.input_data}"}


