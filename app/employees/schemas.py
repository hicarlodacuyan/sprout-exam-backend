"""
This module contains the Pydantic models 
for the RegularEmployee and ContractualEmployee classes
"""
from uuid import UUID
from datetime import date
from typing import Optional, Union
from pydantic import BaseModel, ConfigDict

class EmployeeBase(BaseModel):
    first_name: str
    last_name: str
    email: str

class RegularEmployeeBase(EmployeeBase):
    number_of_leaves: int
    benefits: str

class RegularEmployeeCreate(RegularEmployeeBase):
    pass

class RegularEmployee(RegularEmployeeBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class ContractualEmployeeBase(EmployeeBase):
    contract_end_date: date
    project: str

class ContractualEmployeeCreate(ContractualEmployeeBase):
    pass

class ContractualEmployee(ContractualEmployeeBase):
    id: UUID
    model_config = ConfigDict(from_attributes=True)

class EmployeeCreateRequest(BaseModel):
    type_of_employee: str
    employee: Union[RegularEmployeeCreate, ContractualEmployeeCreate]

class RegularEmployeeUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    number_of_leaves: Optional[int]
    benefits: Optional[str]

class ContractualEmployeeUpdate(BaseModel):
    first_name: Optional[str]
    last_name: Optional[str]
    email: Optional[str]
    contract_end_date: Optional[date]
    project: Optional[str]

class EmployeeUpdateRequest(BaseModel):
    type_of_employee: str  # "regular" or "contractual"
    employee: Union[RegularEmployeeUpdate, ContractualEmployeeUpdate]
