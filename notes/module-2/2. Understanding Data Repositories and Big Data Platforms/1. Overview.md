# Data Repositories Overview

A data repository is a general term used to refer to data that has been collected, organized, and isolated so that it can be used for business operations or mined for reporting and data analysis. It can be a small or large database infrastructure with one or more databases that collect, manage, and store data sets. 

## Types of Data Repositories

In this overview, we will discuss the different types of repositories your data might reside in, such as databases, data warehouses, and big data stores. Further details on these will be covered in additional videos.

### Databases

A database is a collection of data or information designed for the input, storage, search and retrieval, and modification of data. A **Database Management System (DBMS)** is a set of programs that creates and maintains the database, allowing you to store, modify, and extract information using a function called querying.

For example, if you want to find customers who have been inactive for six months or more, using the query function, the DBMS will retrieve data of all customers from the database who have been inactive for six months or more. Although a database and DBMS are different, the terms are often used interchangeably.

#### Types of Databases

There are different types of databases, influenced by factors such as data type and structure, querying mechanisms, latency requirements, transaction speeds, and intended use. Two main types of databases are:

- **Relational Databases (RDBMS)**: Build on the principles of flat files, with data organized into a tabular format with rows and columns, following a well-defined structure and schema. They are optimized for data operations and querying involving many tables and large data volumes. **Structured Query Language (SQL)** is the standard querying language for relational databases.

- **Non-Relational Databases (NoSQL)**: Emerged in response to the volume, diversity, and speed of data generation today, influenced by advances in cloud computing, the Internet of Things, and social media. Non-relational databases are built for speed, flexibility, and scale, allowing data to be stored in a schema-less or free-form fashion. NoSQL is widely used for processing big data.

### Data Warehouses

A data warehouse acts as a central repository that merges information from disparate sources and consolidates it through the **Extract, Transform, Load (ETL)** process into one comprehensive database for analytics and business intelligence. The ETL process involves:

- **Extracting** data from different sources
- **Transforming** the data into a clean and usable state
- **Loading** the data into the enterprise’s data repository

Related concepts include **Data Marts** and **Data Lakes**, which will be covered later. Historically, Data Marts and Data Warehouses have been relational, but with the rise of NoSQL technologies and new data sources, non-relational data repositories are also being used for Data Warehousing.

### Big Data Stores

**Big Data Stores** include distributed computational and storage infrastructure to store, scale, and process very large data sets.

Overall, data repositories help to isolate data, making reporting and analytics more efficient and credible while also serving as a data archive.
