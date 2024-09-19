"""Employee routes module"""
from uuid import UUID
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.auth.utils import get_current_user
from app.database import get_db
from app.employees import schemas, services
from app.auth import schemas as auth_schemas

router = APIRouter(prefix="/api/employees", tags=["employees"])

@router.get("/regular", response_model=list[schemas.RegularEmployee])
async def read_regular_employees(
    db: AsyncSession = Depends(get_db),
    current_user: auth_schemas.User = Depends(get_current_user)
):
    """Get all regular employees"""
    employees = await services.get_regular_employees(db)
    return employees


@router.get("/contractual", response_model=list[schemas.ContractualEmployee])
async def read_contractual_employees(
    db: AsyncSession = Depends(get_db),
    current_user: auth_schemas.User = Depends(get_current_user)
):
    """Get all contractual employees"""
    employees = await services.get_contractual_employees(db)
    return employees

@router.get("/")
async def read_employees(
    db: AsyncSession = Depends(get_db),
    current_user: auth_schemas.User = Depends(get_current_user)
):
    """Get all employees"""
    employees = await services.get_all_employees(db)
    return employees

@router.get("/{employee_id}")
async def read_employee(
    employee_id: UUID,
    db: AsyncSession = Depends(get_db),
    current_user: auth_schemas.User = Depends(get_current_user)
):
    """Get a single employee by their ID (UUID)"""
    employee = await services.get_employee(employee_id, db)
    return employee

@router.post("/")
async def create_employee(
    request: schemas.EmployeeCreateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: auth_schemas.User = Depends(get_current_user)
):
    """Create a new employee"""
    type_of_employee = request.type_of_employee
    employee_data = request.employee

    if type_of_employee == "regular":
        employee = schemas.RegularEmployeeCreate(**employee_data.dict())
        return await services.create_regular_employee(employee, db)

    if type_of_employee == "contractual":
        employee = schemas.ContractualEmployeeCreate(**employee_data.dict())
        return await services.create_contractual_employee(employee, db)

    raise HTTPException(status_code=400, detail="Invalid employee type")

@router.put("/{employee_id}")
async def update_employee(
    employee_id: UUID,
    request: schemas.EmployeeUpdateRequest,
    db: AsyncSession = Depends(get_db),
    current_user: auth_schemas.User = Depends(get_current_user)
):
    """Update an employee's details by their ID (UUID)"""
    type_of_employee = request.type_of_employee
    updated_employee_data = request.employee

    if type_of_employee == "regular":
        updated_employee = schemas.RegularEmployeeUpdate(**updated_employee_data.dict())
        return await services.update_regular_employee(employee_id, updated_employee, db)

    if type_of_employee == "contractual":
        updated_employee = schemas.ContractualEmployeeUpdate(**updated_employee_data.dict())
        return await services.update_contractual_employee(employee_id, updated_employee, db)

    raise HTTPException(status_code=400, detail="Invalid employee type")

@router.delete("/{employee_id}")
async def delete_employee(
    employee_id: UUID,
    type_of_employee: str,
    db: AsyncSession = Depends(get_db),
    current_user: auth_schemas.User = Depends(get_current_user)
):
    """Delete an employee by their ID (UUID)"""
    if type_of_employee == "regular":
        return await services.delete_regular_employee(employee_id, db)

    if type_of_employee == "contractual":
        return await services.delete_contractual_employee(employee_id, db)

    raise HTTPException(status_code=400, detail="Invalid employee type")
