# Data Sources: Dynamic and Diverse

As we touched upon in one of our previous videos, data sources have never been as dynamic and diverse as they are today. In this video, we will look at some common sources such as:

- **Relational Databases**
- **Flat files and XML Datasets**
- **APIs and Web Services**
- **Web Scraping**
- **Data Streams and Feeds**

---

## 1. Relational Databases
Organizations typically use **internal applications** to manage day-to-day business activities, customer transactions, human resources, and workflows. These systems rely on **relational databases** such as:

- SQL Server
- Oracle
- MySQL
- IBM DB2

These databases store data in a structured format, which can be used as a source for analysis. 

### Examples:
- Data from retail transaction systems can be used to analyze **sales in different regions**.
- Data from customer relationship management systems can be used to make **sales projections**.

## 2. Flat Files and XML Datasets
In addition to relational databases, external datasets are available from public and private sources, such as:

- **Government organizations** releasing demographic and economic data.
- **Companies selling** data like Point-of-Sale, Financial, or Weather data.

These datasets are typically available as:

- **Flat files** (plain text, one record per line, values separated by delimiters).
- **Spreadsheet files** (multiple worksheets, rows and columns).
- **XML documents** (tagged data supporting complex hierarchical structures).

### Flat Files:
- **Delimited by** commas, tabs, semi-colons, or spaces.
- Data in flat files maps to a single table.
- **Common formats** include CSV and TSV.

### Spreadsheet Files:
- Organized in **tabular format** with rows and columns.
- Can store **multiple worksheets** in formats like .XLS or .XLSX (Microsoft Excel).
- **Other tools**: Google Sheets, Apple Numbers, LibreOffice.

### XML Files:
- Contain **tagged data**, often supporting hierarchical structures.
- Used for **online surveys, bank statements**, and more.

---

## 3. APIs and Web Services
Many websites and data providers offer **APIs** (Application Program Interfaces) and **Web Services** that allow users and applications to access data. These typically return data in formats such as plain text, XML, HTML, JSON, or media files.

### Popular Uses of APIs:
- **Social Media APIs** (e.g., Twitter, Facebook) for **sentiment analysis** and **opinion mining** on products, services, or policies.
- **Stock Market APIs** for pulling data on **share prices**, earnings, and historical data.
- **Data Lookup and Validation APIs** for **cleaning data** and validating zip codes, addresses, etc.

---

## 4. Web Scraping
**Web scraping** is used to extract relevant data from unstructured sources such as websites. Also known as **screen scraping** or **web data extraction**, it involves downloading data based on defined parameters.

### Common Uses:
- Collecting **product details** from retailers for price comparison.
- **Generating sales leads** through public data sources.
- Extracting **forum and community data** for analysis.

### Popular Tools:
- **BeautifulSoup**
- **Scrapy**
- **Pandas**
- **Selenium**

---

## 5. Data Streams and Feeds
**Data streams** represent a constant flow of data from various sources such as **IoT devices**, **GPS data from cars**, or **social media posts**. Data is often **timestamped** and **geo-tagged**.

### Examples of Data Streams:
- **Stock market tickers** for financial trading.
- **Retail transaction streams** for demand prediction.
- **Surveillance feeds** for threat detection.
- **Sensor data** for monitoring machinery.

### Popular Tools:
- **Apache Kafka**
- **Apache Spark Streaming**
- **Apache Storm**

### RSS Feeds:
**RSS (Really Simple Syndication) feeds** are used to capture updates from online forums and news sites. Using a **feed reader**, updates are streamed to user devices.

---

In this video, we explored some common data sources. In the next video, we will dive into the different ways to process and analyze data from these sources.
