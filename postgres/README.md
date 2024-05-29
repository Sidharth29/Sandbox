# Command to use get into postgres instance created

psql -h localhost -p 5431 -U admin -d postgres_db


# Create new schema

CREATE SCHEMA runs;

# New user with password

CREATE USER runner with PASSWORD ‘beepbeep’;

# Provide privileges

ALTER DEFAULT PRIVILEGES IN SCHEMA animals, organizations GRANT ALL PRIVILEGES ON TABLES to pethub;
ALTER DEFAULT PRIVILEGES GRANT USAGE ON SCHEMAS to pethub;

# quit

\q