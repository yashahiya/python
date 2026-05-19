from django.apps import AppConfig

class AdminConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'admin_app'

    def ready(self):
        """Automatically run migrations and ensure admin user exists with password '1234' on startup."""
        # 1. Programmatically trigger migrations
        try:
            from django.core.management import call_command
            call_command('makemigrations', 'user_app', interactive=False)
            call_command('migrate', interactive=False)
            print("[AUTO-MIGRATION] Django migrations applied successfully!")
        except Exception as migration_error:
            print(f"[AUTO-MIGRATION-ERROR] Programmatic migration skipped/failed: {migration_error}")

        # 2. Setup/ensure admin user exists
        try:
            from user_app.models import CustomUser
            admin_username = "admin"
            admin, created = CustomUser.objects.get_or_create(
                username=admin_username,
                defaults={
                    'email': 'admin@firstproject.local',
                    'is_staff': True,
                    'is_superuser': True,
                    'is_verified': True,
                }
            )
            admin.set_password("1234")
            admin.is_staff = True
            admin.is_superuser = True
            admin.is_verified = True
            admin.save()
            print("*" * 60)
            print(f"[AUTO-SETUP] Admin User 'admin' password successfully set to '1234'.")
            print("*" * 60)
        except Exception as setup_error:
            print(f"[AUTO-SETUP-ERROR] {setup_error}")
