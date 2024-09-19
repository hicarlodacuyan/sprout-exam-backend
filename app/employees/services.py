"""This module contains the business logic for the employees service"""
from uuid import UUID
from fastapi import HTTPException
from sqlalchemy import select
from sqlalchemy.ext.asyncio.session import AsyncSession
from app.employees import schemas
from app.employees.models import ContractualEmployee, RegularEmployee


async def get_regular_employees(db: AsyncSession):
    """Get all regular employees"""
    result = await db.execute(select(RegularEmployee))
    employees = result.scalars().all()
    return [schemas.RegularEmployee.model_validate(employee) for employee in employees]

async def get_contractual_employees(db: AsyncSession):
    """Get all contractual employees"""
    result = await db.execute(select(ContractualEmployee))
    employees = result.scalars().all()
    return [schemas.ContractualEmployee.model_validate(employee) for employee in employees]

async def get_employee(employee_id: UUID, db: AsyncSession):
    """Get a single employee by their ID (UUID)."""
    # Check for RegularEmployee first
    result = await db.execute(select(RegularEmployee).filter(RegularEmployee.id == employee_id))
    employee = result.scalars().first()
    if employee:
        return schemas.RegularEmployee.model_validate(employee)

    # Check for ContractualEmployee if not found in RegularEmployee
    result = await db.execute(select(ContractualEmployee).filter(ContractualEmployee.id == employee_id))
    employee = result.scalars().first()
    if employee:
        return schemas.ContractualEmployee.model_validate(employee)

    # Raise an HTTPException if employee is not found in either table
    raise HTTPException(status_code=404, detail="Employee not found")

async def get_all_employees(db: AsyncSession):
    """Get all employees"""
    regular_employees = await get_regular_employees(db)
    contractual_employees = await get_contractual_employees(db)
    return regular_employees + contractual_employees

async def create_regular_employee(employee: schemas.RegularEmployeeCreate, db: AsyncSession):
    """Create a new regular employee"""
    db_employee = RegularEmployee(
        first_name=employee.first_name,
        last_name=employee.last_name,
        email=employee.email,
        number_of_leaves=employee.number_of_leaves,
        benefits=employee.benefits
    )

    db.add(db_employee)
    await db.commit()

    return db_employee

async def create_contractual_employee(
        employee: schemas.ContractualEmployeeCreate,
        db: AsyncSession
):
    """Create a new contractual employee"""
    db_employee = ContractualEmployee(
        first_name=employee.first_name,
        last_name=employee.last_name,
        email=employee.email,
        contract_end_date=employee.contract_end_date,
        project=employee.project
    )

    db.add(db_employee)
    await db.commit()

    return db_employee

async def update_regular_employee(
    employee_id: UUID,
    updated_employee_data: schemas.RegularEmployeeUpdate,
    db: AsyncSession
):
    """Update a regular employee's details by their ID (UUID)"""
    existing_employee = await db.get(RegularEmployee, employee_id)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Regular Employee not found")

    for key, value in updated_employee_data.dict(exclude_unset=True).items():
        setattr(existing_employee, key, value)

    await db.commit()
    await db.refresh(existing_employee)

    return existing_employee

async def update_contractual_employee(
    employee_id: UUID,
    updated_employee_data: schemas.ContractualEmployeeUpdate,
    db: AsyncSession
):
    """Update a contractual employee's details by their ID (UUID)"""
    existing_employee = await db.get(ContractualEmployee, employee_id)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Contractual Employee not found")

    for key, value in updated_employee_data.dict(exclude_unset=True).items():
        setattr(existing_employee, key, value)

    await db.commit()
    await db.refresh(existing_employee)

    return existing_employee

async def delete_regular_employee(employee_id: UUID, db: AsyncSession):
    """Delete a regular employee by their ID (UUID)"""
    existing_employee = await db.get(RegularEmployee, employee_id)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Regular Employee not found")

    await db.delete(existing_employee)
    await db.commit()

    return {"detail": "Regular Employee deleted successfully"}

async def delete_contractual_employee(employee_id: UUID, db: AsyncSession):
    """Delete a contractual employee by their ID (UUID)"""
    existing_employee = await db.get(ContractualEmployee, employee_id)
    if not existing_employee:
        raise HTTPException(status_code=404, detail="Contractual Employee not found")

    await db.delete(existing_employee)
    await db.commit()

    return {"detail": "Contractual Employee deleted successfully"}
