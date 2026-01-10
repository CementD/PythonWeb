from fastapi import APIRouter

router = APIRouter(
    prefix="/calc",
    tags=["calc"]
)

@router.get("/")
async def calc(a: int, b: int):
    dev_res = ""
    if b == 0:
        dev_res = "undefined"
    else:
        dev_res = a / b
    return { "a": a, "b": b, "sum": a + b, "diff": a - b, "product": a * b, "div": dev_res }
