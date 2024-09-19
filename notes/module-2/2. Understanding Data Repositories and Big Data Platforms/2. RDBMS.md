# Relational Databases

A relational database is a collection of data organized into a table structure, where the tables can be linked, or related, based on data common to each. Tables are made up of rows and columns, where rows are the “records” and columns are the “attributes”.

## Example: Customer Table

For instance, a customer table might include columns like:
- Company ID
- Company Name
- Company Address
- Company Primary Phone

Each row in this table represents a customer record.

### Linking Tables

Along with the customer table, there might be transaction tables that contain data about individual transactions for each customer. The columns in the transaction table might include:
- Transaction Date
- Customer ID
- Transaction Amount
- Payment Method

The customer table and the transaction table can be related through the common **Customer ID** field. This allows you to produce reports, such as a customer statement consolidating all transactions within a given period.

## SQL and Relational Databases

Relational databases use **Structured Query Language (SQL)** for querying data. SQL allows you to retrieve and analyze data from one or more tables with a single query. Relational databases are designed to handle large volumes of data efficiently, unlike spreadsheets which have limited rows and columns.

### Advantages of Relational Databases

- **Flexibility**: SQL allows you to add new columns, tables, rename relations, and make other changes while the database is running.
- **Reduced Redundancy**: Relational databases minimize data redundancy by storing customer information in a single entry and linking to it from other tables.
- **Ease of Backup and Disaster Recovery**: Backup and restore options are straightforward, with continuous mirroring available in cloud-based systems.
- **ACID Compliance**: Ensures data accuracy and consistency despite failures, and reliable processing of database transactions.

### Types of Relational Databases

Relational databases can be categorized as:
- **Open-source and internally supported**
- **Open-source with commercial support**
- **Commercial closed-source systems**

Popular relational databases include:
- IBM DB2
- Microsoft SQL Server
- MySQL
- Oracle Database
- PostgreSQL

Cloud-based relational databases, also known as Database-as-a-Service, include:
- Amazon Relational Database Service (RDS)
- Google Cloud SQL
- IBM DB2 on Cloud
- Oracle Cloud
- SQL Azure

### Use Cases

- **Online Transaction Processing (OLTP)**: Suitable for transaction-oriented tasks with high user rates, supporting frequent queries and updates.
- **Data Warehouses**: Optimized for Online Analytical Processing (OLAP) to analyze historical data for business intelligence.
- **IoT Solutions**: Requires lightweight databases for speed and data collection from edge devices.

### Limitations

- **Semi-Structured and Unstructured Data**: RDBMS is not well-suited for extensive analytics on such data.
- **Migration**: Requires identical schemas and data types between source and destination tables.
- **Field Length Limitations**: Cannot store information exceeding the field’s capacity.

Despite its limitations, RDBMS remains a predominant technology for working with structured data.
