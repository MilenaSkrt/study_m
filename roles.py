# ---------------- ROLES ----------------
@app.post("/roles/", response_model=RoleRead)
def create_role(role: RoleCreate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    new_role = Role(name=role.name)
    db.add(new_role)
    db.commit()
    db.refresh(new_role)
    return new_role

@app.get("/roles/", response_model=List[RoleRead])
def get_roles(db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return db.query(Role).all()

@app.get("/roles/{role_id}", response_model=RoleRead)
def get_role(role_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    return get_object_or_404(db, Role, role_id, "Role not found")

@app.put("/roles/{role_id}", response_model=RoleRead)
def update_role(role_id: int, role_update: RoleUpdate, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    role = get_object_or_404(db, Role, role_id, "Role not found")
    for key, value in role_update.dict(exclude_unset=True).items():
        setattr(role, key, value)
    db.commit()
    db.refresh(role)
    return role

@app.delete("/roles/{role_id}")
def delete_role(role_id: int, db: Session = Depends(get_db), current_user: User = Depends(get_current_user)):
    role = get_object_or_404(db, Role, role_id, "Role not found")
    db.delete(role)
    db.commit()
    return {"detail": "Role deleted"}
