import os
import django

# Set up Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'FirstProject.settings')
django.setup()

from user_app.models import CustomUser

def seed():
    print("=" * 50)
    print("STARTING DATABASE SEEDING...")
    print("=" * 50)
    
    # 1. Admin / Superuser
    admin_username = "admin"
    if not CustomUser.objects.filter(username=admin_username).exists():
        admin = CustomUser.objects.create_superuser(
            username=admin_username,
            email="admin@firstproject.local",
            password="1234"
        )
        admin.is_verified = True
        admin.first_name = "System"
        admin.last_name = "Administrator"
        admin.save()
        print(f"[SUCCESS] Created Admin User:")
        print(f"  - Username: {admin_username}")
        print(f"  - Password: 1234")
        print(f"  - Permissions: Superuser / Staff / Verified")
    else:
        # Let's ensure the admin password is set to '1234'
        admin = CustomUser.objects.get(username=admin_username)
        admin.set_password("1234")
        admin.is_staff = True
        admin.is_superuser = True
        admin.is_verified = True
        admin.save()
        print(f"[SUCCESS] Updated existing Admin User password to '1234'.")

    print("-" * 50)

    # 2. Verified Standard User
    user1_username = "user1"
    if not CustomUser.objects.filter(username=user1_username).exists():
        user = CustomUser.objects.create_user(
            username=user1_username,
            email="user1@firstproject.local",
            password="user123"
        )
        user.is_verified = True
        user.first_name = "John"
        user.last_name = "Doe"
        user.save()
        print(f"[SUCCESS] Created Verified User:")
        print(f"  - Username: {user1_username}")
        print(f"  - Password: user123")
        print(f"  - Status: Verified / Active")
    else:
        print(f"[INFO] User '{user1_username}' already exists.")

    print("-" * 50)

    # 3. Blocked User
    blocked_username = "blocked_user"
    if not CustomUser.objects.filter(username=blocked_username).exists():
        user = CustomUser.objects.create_user(
            username=blocked_username,
            email="blocked@firstproject.local",
            password="user123"
        )
        user.is_verified = True
        user.is_blocked = True
        user.first_name = "Suspended"
        user.last_name = "Member"
        user.save()
        print(f"[SUCCESS] Created Blocked User:")
        print(f"  - Username: {blocked_username}")
        print(f"  - Password: user123")
        print(f"  - Status: Verified / Blocked")
    else:
        print(f"[INFO] User '{blocked_username}' already exists.")

    print("-" * 50)

    # 4. Unverified/Pending User
    pending_username = "pending_user"
    if not CustomUser.objects.filter(username=pending_username).exists():
        user = CustomUser.objects.create_user(
            username=pending_username,
            email="pending@firstproject.local",
            password="user123"
        )
        user.is_verified = False
        user.first_name = "Pending"
        user.last_name = "Verification"
        user.save()
        print(f"[SUCCESS] Created Pending User:")
        print(f"  - Username: {pending_username}")
        print(f"  - Password: user123")
        print(f"  - Status: Unverified (Pending OTP)")
    else:
        print(f"[INFO] User '{pending_username}' already exists.")

    print("=" * 50)
    print("SEEDING COMPLETED SUCCESSFULLY!")
    print("=" * 50)

if __name__ == '__main__':
    seed()
