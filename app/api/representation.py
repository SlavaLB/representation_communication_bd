from fastapi import APIRouter, Depends, Header

from db.session import get_one_to_one
from domain.one_to_one import OneToOne
from endpoint_description.person_get import EndpointPersonDocs

router = APIRouter()


@router.get(
    "/get_person_info",
    **EndpointPersonDocs.GET_PERSON_INFO
)
async def get_person_info(
        person_id: int = Header(..., alias="Person-ID"),
        one_to_one: OneToOne = Depends(get_one_to_one),
):
    # Получение пользователя и связанных данных
    return await one_to_one.get_person_by_id(person_id=person_id)


@router.get(
    "/get_person_info_without_passport",
    **EndpointPersonDocs.GET_PERSON_INFO_WITHOUT_PASSPORT
)
async def get_person_info(
        person_id: int = Header(..., alias="Person-ID"),
        one_to_one: OneToOne = Depends(get_one_to_one),
):
    # Получение пользователя без связанных данных
    return await one_to_one.get_person_by_id_without_passport(person_id=person_id)
