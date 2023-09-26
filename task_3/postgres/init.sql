SELECT 'CREATE DATABASE fruits'
WHERE NOT EXISTS (SELECT FROM pg_database WHERE datname = 'fruits')\gexec

\c fruits;

CREATE TABLE "fruit" (
    uid UUID PRIMARY KEY,
    name VARCHAR(256),
    color VARCHAR(256)
);
