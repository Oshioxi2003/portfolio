# MSSQL/SQL Server Setup Guide

## Overview
This guide helps you set up MSSQL/SQL Server for your Django portfolio project using Azure SQL Database.

## Prerequisites
1. ODBC Driver 18 for SQL Server installed on your system
2. Required Python packages installed

## Step 1: Install Required Packages

```bash
pip install -r requirements.txt
```

This will install:
- `django-mssql-backend==2.8.1` - Django backend for SQL Server
- `pyodbc==4.0.39` - Python ODBC database API

## Step 2: Install ODBC Driver (Windows)

### For Windows:
Download and install "ODBC Driver 17 for SQL Server" from Microsoft:
https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server

Note: If you have ODBC Driver 17, the configuration is already set for that version.

### For Linux/Mac:
Follow Microsoft's installation guide for your specific OS.

## Step 3: Database Configuration

Your current Azure SQL Database configuration:
- **Server**: eu-az-sql-serv1.database.windows.net
- **Database**: dehmbtpua8bgw84
- **Username**: ugoxdlf1k4otkz2
- **Password**: i3HW?WLMRX5&#VH3TlDYEZ@gi
- **Port**: 1433

## Step 4: Test Connection

After installing the requirements, try running:

```bash
python manage.py check --database default
```

## Step 5: Create Migrations

```bash
# Create new migrations
python manage.py makemigrations

# Apply migrations to SQL Server
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Populate sample data
python manage.py populate_data
```

## Environment Variables

For production deployment, set these environment variables:

```
RENDER=true
MSSQL_DATABASE=dehmbtpua8bgw84
MSSQL_USER=ugoxdlf1k4otkz2
MSSQL_PASSWORD=i3HW?WLMRX5&#VH3TlDYEZ@gi
MSSQL_HOST=eu-az-sql-serv1.database.windows.net
MSSQL_PORT=1433
```

## Troubleshooting

### 1. ODBC Driver Not Found
**Error**: `Data source name not found and no default driver specified`

**Solution**: 
- Install ODBC Driver 18 for SQL Server
- On Windows, download from Microsoft's official site
- Restart your terminal/IDE after installation

### 2. Connection Timeout
**Error**: Connection timeout errors

**Solution**:
- Check your internet connection
- Verify firewall settings
- Ensure the server allows connections from your IP

### 3. Authentication Failed
**Error**: Login failed for user

**Solution**:
- Double-check username and password
- Verify the server name is correct
- Check if the user has proper permissions

### 4. SSL Certificate Issues
**Error**: SSL certificate validation errors

**Solution**:
- The configuration uses `TrustServerCertificate=no` for security
- If you have certificate issues, you can temporarily set it to `yes` for testing

## Local Development

For local development, you can:

1. **Use SQLite** (recommended for development):
   - Keep `RENDER=False` or don't set it
   - Uses the SQLite configuration in the `else` block

2. **Use SQL Server locally**:
   - Install SQL Server locally or use SQL Server Express
   - Update the local configuration in settings.py

## SQL Server Specific Considerations

### 1. Field Types
- SQL Server has different field type limitations compared to SQLite
- Some Django field types may behave differently

### 2. Indexes
- SQL Server requires explicit index names
- Some migrations might need manual adjustment

### 3. Character Encoding
- SQL Server uses different collations
- Unicode support is built-in but may need configuration

## Migration from SQLite

If you have existing SQLite data:

### Option 1: Export/Import Data
```bash
# Export from SQLite
python manage.py dumpdata --natural-foreign --natural-primary > data.json

# Switch to SQL Server configuration
# Run migrations
python manage.py migrate

# Import data
python manage.py loaddata data.json
```

### Option 2: Manual Data Transfer
- Export data from SQLite admin interface
- Import manually through SQL Server Management Studio or Azure portal

## Performance Tips

1. **Connection Pooling**: Consider using connection pooling in production
2. **Indexes**: Add indexes for frequently queried fields
3. **Query Optimization**: Use Django's query optimization features
4. **Caching**: Implement caching for better performance

## Security Considerations

1. **Password Security**: Store passwords in environment variables
2. **Connection Encryption**: Always use encrypted connections in production
3. **Firewall Rules**: Configure Azure SQL firewall rules appropriately
4. **User Permissions**: Use least-privilege principle for database users

## Azure SQL Database Features

Your Azure SQL Database supports:
- Automatic backups
- Point-in-time restore
- Scaling options
- Built-in security features
- Performance monitoring

## Next Steps

1. Install the ODBC driver
2. Run `pip install -r requirements.txt`
3. Test the connection with `python manage.py check --database default`
4. Create and run migrations
5. Deploy to your hosting platform with the environment variables
