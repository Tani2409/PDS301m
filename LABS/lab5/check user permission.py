def can_access_dashboard(user_permissions, required_permissions):
    return required_permissions.issubset(user_permissions)

required = {"view_users", "edit_content"}

user_admin_perms = {"view_users", "edit_content", "delete_users", "admin_access"}
user_editor_perms = {"edit_content", "view_users"}
user_viewer_perms = {"view_users"}

print(f"Admin can access? {can_access_dashboard(user_admin_perms, required)}")
print(f"Editor can access? {can_access_dashboard(user_editor_perms, required)}")
print(f"Viewer can access? {can_access_dashboard(user_viewer_perms, required)}")
