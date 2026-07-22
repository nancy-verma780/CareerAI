from database.supabase_client import supabase


result = supabase.table(
    "users"
).insert(
    {
        "email":"test@gmail.com"
    }
).execute()


print(result)