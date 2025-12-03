from fastapi import APIRouter, Depends, Header

from db.session import get_one_to_one
from domain.one_to_one import OneToOne
from endpoint_description.person_get import EndpointPersonDocs

router = APIRouter()


@router.post(
    "/get",
    **EndpointPersonDocs.GET_PERSON_INFO
)
async def get_person_info(
        person_id: int = Header(..., alias="Person-ID"),
        one_to_one: OneToOne = Depends(get_one_to_one),
):
    # Получение пользователя и связанных данных
    return await one_to_one.get_person_by_id(person_id=person_id)

