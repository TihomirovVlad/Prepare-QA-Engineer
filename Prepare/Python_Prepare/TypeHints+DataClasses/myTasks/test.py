from task import TestUser
try:
    user1 = TestUser("vlad", "vlad@test.com")
    print(f"✅ User created: {user1}")

    user2 = TestUser.create_random_user()
    print(f"✅ Random user: {user2}")

    user1.deactivate()
    print(f"✅ User deactivated: {user1.is_active}")

    bad_user = TestUser("bad", "invalid-email")
except ValueError as e:
    print(f"✅ Validation works: {e}")