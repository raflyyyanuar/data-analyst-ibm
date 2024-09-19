# Data Warehouses, Data Marts, and Data Lakes

Earlier in the course, we examined databases, data warehouses, and big data stores. Now we’ll delve deeper into **data warehouses**, **data marts**, and **data lakes**; and also learn about the **ETL process** and **data pipelines**.

## Data Warehouses

A **data warehouse** serves as a multi-purpose storage for different use cases. By the time data arrives in the warehouse, it has already been modeled and structured for a specific purpose, making it analysis-ready. Organizations opt for a data warehouse when they have massive amounts of data from operational systems that need to be readily available for reporting and analysis.

Data warehouses are the single source of truth, storing current and historical data that has been cleansed, conformed, and categorized. They enable operational and performance analytics.

## Data Marts

A **data mart** is a sub-section of a data warehouse, built specifically for a particular business function, purpose, or community of users. The aim is to provide stakeholders with data that is most relevant to them when they need it. For example, sales or finance teams accessing data for quarterly reporting and projections. 

Data marts offer isolated security and performance and are crucial for business-specific reporting and analytics.

## Data Lakes

A **data lake** is a storage repository that can store large amounts of structured, semi-structured, and unstructured data in its native format, classified and tagged with metadata. Unlike a data warehouse, which stores data processed for a specific need, a data lake retains all source data without exclusions. 

Data lakes are used for predictive and advanced analytics and can serve as a staging area for a data warehouse.

## ETL Process

The **Extract, Transform, and Load (ETL)** process is central to deriving value from data. ETL involves:

1. **Extract**: Gathering raw data from identified sources. This can be done through:
   - **Batch processing**: Moving large chunks of source data to the target system at scheduled intervals. Tools include Stitch and Blendo.
   - **Stream processing**: Pulling real-time data from the source and transforming it in transit before loading it into the repository. Tools include Apache Samza, Apache Storm, and Apache Kafka.

2. **Transform**: Executing rules and functions to convert raw data into a format usable for analysis. This includes:
   - Making date formats and units of measurement consistent.
   - Removing duplicates.
   - Filtering unnecessary data.
   - Enriching data (e.g., splitting full names into first, middle, and last names).
   - Establishing key relationships and applying business rules.

3. **Load**: Transporting processed data to a destination system or repository. This can be:
   - **Initial loading**: Populating all the data in the repository.
   - **Incremental loading**: Applying ongoing updates and modifications periodically.
   - **Full refresh**: Erasing contents of tables and reloading with fresh data.

   Load verification includes checks for missing or null values, server performance, and monitoring load failures.

## Data Pipelines

**Data pipelines** encompass the entire journey of moving data from one system to another, including ETL processes. Data pipelines can be architected for:
- **Batch processing**: Large-scale data movements.
- **Streaming data**: Continuous flow of data, useful for constant updates (e.g., sensor data monitoring).

Data pipelines support both long-running batch queries and smaller interactive queries. They typically load data into a data lake but can also target other destinations such as applications or visualization tools.

Popular data pipeline solutions include Apache Beam and DataFlow.
