# 📗 Table of Contents

- [📖 About the Project](#about-project)
  - [🛠 Built With](#built-with)
    - [Tech Stack](#tech-stack)
    - [Key Features](#key-features)
  - [🚀 Live Demo](#live-demo)
- [💻 Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Setup](#setup)
  - [Install](#install)
  - [Usage](#usage)
  - [Run tests](#run-tests)
  - [Deployment](#deployment)
- [👥 Authors](#authors)
- [🔭 Future Features](#future-features)
- [📝 License](#license)

<!-- PROJECT DESCRIPTION -->

# 📖 Blockhouse API <a name="about-project"></a>

**Blockhouse API** is a web service that allows users to fetch order details and update the status of an order in a trading system. It provides a RESTful API for seamless order management and transaction processing.

WebSocket Support for real-time order updates
## 🛠 Built With <a name="built-with"></a>

### Tech Stack <a name="tech-stack"></a>

#### Client
- None (API-only service)

#### Server
- [FastAPI](https://fastapi.tiangolo.com/)
- [Docker](https://www.docker.com/)

#### Database
- [PostgreSQL](https://www.postgresql.org/)

### 📖 API Documentation

- [Local API Docs (OpenAPI)](http://localhost:8000/docs)
- [Local Redoc API Docs](http://localhost:8000/redoc)

<!-- Features -->

### Key Features <a name="key-features"></a>

- **Fetch Order Details** - Retrieve details of a specific order by order ID.
- **Update Order Status** - Modify the status of an existing order.
- **Websocket Integration** - Real-time updates for order status changes.

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- LIVE DEMO -->

## 🚀 Live Demo <a name="live-demo"></a>

> The project is not yet live. A demo link will be added soon.

- [Live Demo Link](#)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- GETTING STARTED -->

## 💻 Getting Started <a name="getting-started"></a>

To get a local copy up and running, follow these steps.

### Prerequisites

In order to run this project, you need:

- Python 3.11+
- PostgreSQL
- Docker & Docker Compose

### Setup

Clone this repository:

```sh
git clone https://github.com/LIBERCOSOFT/blockhouse-api.git
cd blockhouse-api
```

### Install

Install this project with:

```sh
pip install -r requirements.txt
```


### Usage

To run the project, execute the following command:

- With Docker
```sh
docker-compose up
```

- Without Docker
```sh
uvicorn main:app --reload
```

### Deployment

You can deploy this project using:


```sh
docker-compose up --build -d
```

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- AUTHORS -->

## 👥 Authors <a name="authors"></a>

👤 **Kolapo Akinrinlola**

- GitHub: [LIBERCOSOFT](https://github.com/LIBERCOSOFT)
- Twitter: [@Gerfieldt](https://twitter.com/Gerfieldt)
- LinkedIn: [Kolapo Akinrinlola](https://linkedin.com/in/kolapo-akinrinlola)

<p align="right">(<a href="#readme-top">back to top</a>)</p>

<!-- FUTURE FEATURES -->

## 🔭 Future Features <a name="future-features"></a>

- [ ] **Authentication & Authorization for secure access**
- [ ] **Order Analytics Dashboard for insights and trends**

<p align="right">(<a href="#readme-top">back to top</a>)</p>


<!-- LICENSE -->

## 📝 License <a name="license"></a>

This project is [MIT](./LICENSE) licensed.

<p align="right">(<a href="#readme-top">back to top</a>)</p>
