# crypto-tracker

Data Mart for top-10 cryptocurrency courses for every day

---

## 🚀 Business Problem & Motivation

The goal of this project is to create a BI dashboard for tracking cryptocurrency price dynamics in order to identify trends

---

## 🛠️ Tech Stack & Architecture

### Tech Stack

* [![Python 3.13](https://img.shields.io/badge/Python-3.13-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
* [![Requests](https://img.shields.io/badge/Requests-orange?style=for-the-badge&logo=python&logoColor=white)](https://requests.readthedocs.io/)
* [![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)](https://pandas.pydata.org/)
* [![SQLAlchemy](https://img.shields.io/badge/SQLAlchemy-D71F00?style=for-the-badge&logo=sqlalchemy&logoColor=white)](https://www.sqlalchemy.org/)
* [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-4169E1?style=for-the-badge&logo=postgresql&logoColor=white)](https://www.postgresql.org/)
* [![Apache Airflow](https://img.shields.io/badge/Apache%20Airflow-017CEE?style=for-the-badge&logo=apacheairflow&logoColor=white)](https://airflow.apache.org/)
* [![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://www.docker.com/)
* [![Docker Compose](https://img.shields.io/badge/Docker%20Compose-2496ED?style=for-the-badge&logo=docker&logoColor=white)](https://docs.docker.com/compose/)
* [![Apache Superset](https://img.shields.io/badge/Apache%20Superset-00A5A3?style=for-the-badge&logo=apachesuperset&logoColor=white)](https://superset.apache.org/)

### Architecture
![[CoinGecko API] -> [Python script (в Airflow DAG)] -> [PostgreSQL] -> [Superset]](./architecture.drawio.svg)

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