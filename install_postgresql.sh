#!/bin/bash

# Update package lists
sudo apt-get update

# Install PostgreSQL
sudo apt-get install -y postgresql postgresql-contrib

# Start PostgreSQL service
sudo service postgresql start

# Enable PostgreSQL service to start on boot
sudo systemctl enable postgresql

# Print PostgreSQL version
psql --version
