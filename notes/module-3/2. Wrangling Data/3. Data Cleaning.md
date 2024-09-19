# Importance of Data Quality and Cleaning

## Poor Data Quality Consequences
- **Weakens competitive standing** and undermines business objectives.
- **Leads to false conclusions** and ineffective decisions.
- **Common Issues**: 
  - Missing values
  - Inaccuracies
  - Duplicates
  - Incorrect/missing delimiters
  - Inconsistent records
  - Insufficient parameters

## Data Cleaning vs. Data Wrangling
- **Data Wrangling**: Includes multiple stages; cleaning is just a part of it.
- **Data Cleaning**: Focuses on resolving errors in data as part of the Transformation phase.

---

# Data Cleaning Workflow

### 1. **Inspection**
   - **Goal**: Detect data issues and errors.
   - **Techniques**:
     - Define rules/constraints and validate data.
     - Use data profiling to understand structure and relationships.
     - **Common issues detected**:
       - Blank or null values.
       - Duplicate data.
       - Out-of-range values.
     - **Visualization**: Helps spot outliers (e.g., average income vs. outliers).

### 2. **Cleaning**
   - **Common Issues and Solutions**:
     - **Missing Values**:
       - Filter out records or source missing data.
       - Use **imputation** to estimate missing values statistically.
     - **Duplicate Data**: Remove duplicates to avoid bias.
     - **Irrelevant Data**: Remove data that doesn't fit the context of your analysis.
     - **Data Type Conversion**: Ensure data values match their field types (e.g., numbers as numeric, dates as date).
     - **Standardization**: Apply consistency to fields (e.g., all lowercase strings, consistent date formats).
     - **Syntax Errors**: Fix whitespace, typos, and format inconsistencies (e.g., full vs. abbreviated state names).
     - **Outliers**:
       - May be incorrect (e.g., age field with value 5).
       - May be valid but need careful consideration (e.g., high income outlier).

### 3. **Verification**
   - **Goal**: Ensure the cleaning operations were effective.
   - **Steps**:
     - Re-inspect data post-cleaning to confirm all rules/constraints hold.
     - Verify accuracy and effectiveness of corrections.

---

# Importance of Documentation
- **Document**:
  - All changes made during cleaning.
  - Reasons behind changes.
  - Current data quality and health.
- **Reporting**: Essential for understanding data health post-cleaning.
