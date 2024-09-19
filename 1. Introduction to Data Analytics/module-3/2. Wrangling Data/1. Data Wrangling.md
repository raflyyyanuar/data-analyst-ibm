# Data Wrangling Overview

## Definition:
Data wrangling (or data munging) is an **iterative process** that involves exploring, transforming, validating, and preparing raw data for meaningful analysis.

## 4-Step Data Wrangling Process:

### 1. **Discovery (Exploration)**
   - **Goal**: Understand the data in the context of your use case.
   - **Objective**: Determine how to clean, structure, organize, and map the data for analysis.

### 2. **Transformation**
   - **Goal**: Change and refine data to suit analysis.
   - **Types of Transformation**:
     - **Structuring**: Adjust the form/schema of data (e.g., using Joins and Unions).
     - **Normalization**: Clean data to remove redundancy and inconsistency.
     - **Denormalization**: Combine tables to make querying faster.
     - **Cleaning**: Fix irregularities, handle missing, inaccurate, or biased data.
     - **Enriching**: Add additional data points or metadata to enhance analysis.
       - Example: Supplement transaction data with public business performance data.
       - Metadata: Compute metrics like sentiment scores, geo-based data, etc.

### 3. **Validation**
   - **Goal**: Ensure the data quality is high after structuring, cleaning, and enriching.
   - **Tasks**: Apply validation rules to check consistency, quality, and security.

### 4. **Publishing**
   - **Goal**: Deliver the transformed and validated data for project needs.
   - **Output**: Transformed dataset along with metadata.

## Documentation:
   - **Importance**: Document all steps and considerations during data wrangling to ensure reproducibility and transparency.

## Key Takeaways:
   - Data wrangling is **iterative**.
   - It involves **exploration**, **transformation**, **validation**, and **publishing** of data.
   - Proper documentation is essential for replicating and reviewing steps.
