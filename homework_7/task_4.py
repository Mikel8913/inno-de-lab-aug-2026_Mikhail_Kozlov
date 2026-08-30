requested_roles = ["guest", "developer", "guest", "admin", "developer", "guest"]
required_admin_roles = {"admin", "security_officer", "audit_manager"}

#  удаления дубликатов
unique_roles = set(requested_roles)

# пересечение ролей
common_roles = unique_roles & required_admin_roles

# административные роли (которые не были запрошены)
missing_roles = required_admin_roles - unique_roles

# наличие роли security_officer в запросе
has_security_officer = "security_officer" in unique_roles

print(f"Уникальные запрошенные роли: {unique_roles}")
print(f"Общие административные роли: {common_roles}")
print(f"Недостающие административные роли: {missing_roles}")
print(f"Наличие роли security_officer в запросе: {has_security_officer}")
