#!/bin/bash

# Variables
DB_NAME="myprojectdb"
DB_USER="myprojectuser"
DB_PASSWORD="myprojectpassword"

# Switch to the postgres user to create the database and user
sudo -i -u postgres psql << EOF
-- Create the database
CREATE DATABASE $DB_NAME;

-- Create the database user
CREATE USER $DB_USER WITH ENCRYPTED PASSWORD '$DB_PASSWORD';

-- Grant privileges to the user on the database
GRANT ALL PRIVILEGES ON DATABASE $DB_NAME TO $DB_USER;
EOF

echo "Database '$DB_NAME' and user '$DB_USER' created successfully."
