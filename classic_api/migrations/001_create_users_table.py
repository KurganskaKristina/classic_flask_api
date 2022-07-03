from yoyo import step

__depends__ = {}

steps = [
    step("""
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            username TEXT,
            firstname TEXT,
            lastname TEXT,
            birthdate TEXT,
            description TEXT,
            profile_photo BYTEA
        );""",
         "DROP TABLE projects"
         ),
    step("""
           ALTER TABLE users
           ADD CONSTRAINT username_constraint UNIQUE (username);
            """,
         "ALTER TABLE users DROP CONSTRAINT username_constraint;"
         )
]
