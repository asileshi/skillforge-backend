from fastapi import Depends, HTTPException, status
from app.dependencies.auth import get_current_user
from app.models.user import User

def require_admin(current_user: User = Depends(get_current_user)):
    if not current_user.is_admin:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Admin previleges required",
        )
    return current_user