# final_project_big_data

# 📈 Stock Exchange Data Analysis using Big Data Tools

This project showcases a complete data pipeline for analyzing stock exchange data using a Medallion Architecture approach (Bronze → Silver → Gold). It leverages Apache Spark for processing, Cassandra for storage, and Jupyter for exploration and visualization.

## 📁 Project Structure
final_project_big_data/
.gitignore
cassandradb-token.json
exchange_data.csv # Raw stock market data
MedallionArchitectureTables.ipynb # Main Jupyter notebook for the pipeline
poetry.lock
pyproject.toml # Poetry config for dependencies
RawData/ # Additional raw data (if any)
secure-connect-cassandradb.zip # Secure bundle for Cassandra DB

## ⚙️ Tech Stack

- **Apache Spark** – Distributed data processing  
- **Apache Cassandra** – NoSQL database for structured storage  
- **Jupyter Notebook** – Data transformation and visualization  
- **Poetry** – Python dependency management  

## 🏗️ Architecture

- **Bronze Layer**: Raw ingestion from `exchange_data.csv`  
- **Silver Layer**: Cleaned and transformed data  
- **Gold Layer**: Aggregated, analytical-ready insights stored in Cassandra  

## ✅ Prerequisites

- Python 3.8+
- Apache Spark
- Apache Cassandra (locally or using secure bundle)
- Poetry (`pip install poetry`)

## 🚀 Setup
Clone the repository: https://github.com/Revanth0017/final_project_big_data.git

## 🗄️ Database Connection
Use secure-connect-cassandradb.zip and cassandradb-token.json to authenticate and connect to your Cassandra instance.

## 📌 Notes
The .ruff_cache/ is used for linting and code formatting.
All transformations and logic are implemented in the notebook using PySpark.



