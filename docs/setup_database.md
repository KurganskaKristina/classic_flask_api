Create database and user before applying migrations

1. CREATE DATABASE users_store;

2. CREATE USER users_store_user WITH password 'users746fhgstore';

3. ALTER DATABASE users_store OWNER TO users_store_user;

4. GRANT all privileges ON database "users_store" to users_store_user;