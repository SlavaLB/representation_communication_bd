from fastapi import APIRouter


router = APIRouter()


@router.post(
    "/get",
    summary="Просто эндпоинт",
)
async def get_number_in_math_model():
    return "asdasd"
