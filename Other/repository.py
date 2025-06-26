import requests
from pydantic import BaseModel
from typing import Optional, List


class UserCreate(BaseModel):
    name: str
    email: str


class UserRead(UserCreate):
    id: int


class UserUpdate(BaseModel):
    name: Optional[str] = None
    email: Optional[str] = None


DATA_API_URL = "http://localhost:8001"


class UserRepository:
    def __init__(self):
        self.base_url = DATA_API_URL
        self.timeout = 5

    def create_user(self, user: UserCreate) -> UserRead:
        response = requests.post(f"{self.base_url}/users/", json=user.dict(), timeout=self.timeout)
        response.raise_for_status()
        return UserRead(**response.json())

    def get_user(self, user_id: int) -> Optional[UserRead]:
        response = requests.get(f"{self.base_url}/users/{user_id}", timeout=self.timeout)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return UserRead(**response.json())

    def get_all_users(self) -> List[UserRead]:
        response = requests.get(f"{self.base_url}/users/", timeout=self.timeout)
        response.raise_for_status()
        return [UserRead(**u) for u in response.json()]

    def update_user(self, user_id: int, user: UserUpdate) -> Optional[UserRead]:
        response = requests.put(f"{self.base_url}/users/{user_id}", json=user.dict(exclude_unset=True), timeout=self.timeout)
        if response.status_code == 404:
            return None
        response.raise_for_status()
        return UserRead(**response.json())

    def delete_user(self, user_id: int) -> bool:
        response = requests.delete(f"{self.base_url}/users/{user_id}", timeout=self.timeout)
        if response.status_code == 404:
            return False
        response.raise_for_status()
        return True

    def delete_all_users(self) -> None:
        response = requests.delete(f"{self.base_url}/users/", timeout=self.timeout)
        response.raise_for_status()
