# 🪙 Crypto Tracker
A simple data pipeline that collects daily top-10 cryptocurrency prices from the CoinGecko API and loads them into a PostgreSQL database for visualization in Metabase.

---

## 🚀 Business Problem & Motivation

The goal of this project is to create a BI dashboard for tracking cryptocurrency price dynamics in order to identify trends

---

## 🛠️ Tech Stack & Architecture

### 🧰 Tech Stack

* [![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
* [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
* [![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)](https://airflow.apache.org/)
* [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
* [![Metabase](https://img.shields.io/badge/Metabase-509488?style=for-the-badge&logo=metabase&logoColor=white)](https://www.metabase.com/)

---

### Architecture
![[CoinGecko API] -> [Python script (в Airflow DAG)] -> [PostgreSQL] -> [Metabase]](./docs/architecture.drawio.svg)

---

## ⚙️ Getting Started

### Prerequisites
- Docker and Docker Compose installed
- Git
- API key for CoinGecko
- A `.env` file like `.env.example`

### Installation & Setup 
1. **Clone the repository:**
   ```bash
   git clone https://github.com/jinjik19/crypto-tracker
   cd crypto-tracker
   ```

2. **Set up environment variables:**
   *Create a `.env` file in the root directory by copying `.env.example`*
   ```bash
   cp .env.example .env
   ```
   *Modify the `.env` file with your specific settings (API KEY for CoinGecko)*

3. **Build and run the services:**
   ```bash
   docker-compose up --build -d
   ```

---

## 📁 Project Structure
```
.
├── Makefile
├── Pipfile
├── Pipfile.lock
├── README.md
├── config
│   └── airflow.cfg
├── dags
│   ├── crypto_prices_etl_dag.py
│   └── dependencies
│       └── requirements.txt
├── docker-compose.yml
├── docs
│   └── architecture.drawio.svg
├── initdb
│   └── init.sql
├── logs
├── metabase
├── plugins
├── pyproject.toml
└── src
    ├── clients
    │   └── coin_gecko_api.py
    ├── etl.py
    ├── tests
    │   └── test_transformation.py
    └── utils
        └── logger.py
```
---

## 🧩 Data Model 

---

## 🕹️ Usage 

--- 

## 📊 Dashboard Example

---

## 🧠 Author

| 👤 Name | 💻 Role | 🔗 Links |
|----------|----------|----------|
| **Jinjik19** | Data Engineering Enthusiast | [GitHub](https://github.com/jinjik19) |