# Intro to SQL



### 1. Getting Started With SQL and BigQuery

- **SQL**: Structured Query Language
  - is the programming language used with databases.
- **BigQuery**: a web service that offers huge datasets



#### Your first BigQuery commands

1. import python package 'bigquery'
2. create a client object
3. construct a reference to the certain dataset and fetch it
4. construct a reference to the certain table and fetch it

```python
from google.cloud import bigquery # 1

client = bigquery.Client() # 2

dataset_ref = client.dataset("hacker_news", project="bigquery-public-data")
dataset = client.get_dataset(dataset_ref)
# 3

tables = list(client.list_tables(dataset))
for table in tables:  
    print(table.table_id)
# to check the list of tables in the dataset

# result  
comments
full
full_201510
stories

table_ref = dataset_ref.table("full")
table = client.get_table(table_ref)
# 4
```

<details>
<summary>Data Structure</summary>
<img src="./Intro to SQL - Getting Started With SQL and BigQuery.png">
</details>

---

#### Table schema

- **schema**: The structure of a table

- to print information on all the columns in the table: `table.schema`

- to check the first several lines: `list_rows()`

  - This method returns a BigQuery `RowIterator` object.

  - with `to_dataframe()` method, this object can be converted to a pandas DataFrame.

  - ```python
    # example
    client.list_rows(table, max_results=5).to_dataframe()
    ```

    ```python
    # example
    client.list_rows(table, selected_fields=table.schema[:1], max_results=5).to_dataframe()
    ```



---



### 2. Select, From & Where

- The argument we pass to FROM is in backticks.

#### Submitting the query to the dataset

1. create a client object
2. make a query
3. use `query()` method and return a pandas DataFrame using `to_dataframe()

```python
client = bigquery.Client() # 1

query = """
        SELECT city
        FROM `bigquery-public-data.openaq.global_air_quality`
        WHERE country = 'US'
        """ # 2

query_job = client.query(query)
us_cities = query_job.to_dataframe()
# 3
```

---

#### Working with big datasets

- To see how much data a query will scan - create a `QueryJobConfig` object and set `dry_run=True`

  ```python
  dry_run_config = bigquery.QueryJobConfig(dry_run=True)
  
  dry_run_query_job = client.query(query, job_config=dry_run_config)
  
  print("This query will process {} bytes.".format(dry_run_query_job.total_bytes_processed))
  # print
  This query will process 386485420 bytes.
  ```

  

- To limit data to scan - set `maximum_bytes_billed` attribute

  ```python
  ONE_MB = 1000*1000
  safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_MB)
  safe_query_job = client.query(query, job_config=safe_config)
  ```

  - If the amount of data which the query scans exceeds the limit, an error occurs.

  ```python
  ONE_GB = 1000*1000*1000
  safe_config = bigquery.QueryJobConfig(maximum_bytes_billed=ONE_GB)
  safe_query_job = client.query(query, job_config=safe_config)
  # In this case, one GB is sufficient.
  ```

  

---



### 3. Group By, Having & Count

#### Aliasing and other improvements

- If you are ever unsure what to put inside the **COUNT()** function, you can do `COUNT(1)` to count the rows in each group. Most people find it especially readable, because we know it's not focusing on other columns. It also scans less data than if supplied column names (making it faster and using less of your data access quota).



#### Note on using **GROUP BY**

- **GROUP BY** command and an aggregation function have to be used together.

- If there is **GROUP BY** clause, then all variables must be passed to either *a GROUP BY command* or *an aggregation function*

  - ex) correct

    ```python
    query_good = """
                 SELECT parent, COUNT(id)
                 FROM `bigquery-public-data.hacker_news.comments`
                 GROUP BY parent
                 """
    ```

    - variable `parent` was passed to a GROUP BY command and variable `id` was passed to an aggregate function.

  - ex) incorrect

    ```python
    query_bad = """
                SELECT author, parent, COUNT(id)
                FROM `bigquery-public-data.hacker_news.comments`
                GROUP BY parent
                """
    ```

    - variable `author` isn't passed to an aggregate function nor a GROUP BY clause.
    - It raises an error message - `SELECT list expression references column (column's name) which is neither grouped nor aggregated at`





