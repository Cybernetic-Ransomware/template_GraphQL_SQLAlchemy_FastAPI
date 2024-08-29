# Template Project: GraphQL (Strawberry) + SQLAlchemy + FastAPI

Quick implementation of a database connector with both REST endpoints and GraphQL routes.

---

## Initialization

1. Clone the repository:
    ```bash
    git clone https://github.com/Cybernetic-Ransomware/template_GraphQL_SQLAlchemy_FastAPI.git
    ```
2. Install Python >= 3.12.
3. Create a virtual environment:
    ```bash
    python -m venv .venv
    ```
4. Activate the virtual environment:
    - On Windows:
      ```bash
      .venv\Scripts\activate
      ```
    - On macOS and Linux:
      ```bash
      source .venv/bin/activate
      ```
5. Install dependencies from `requirements.txt`:
    ```bash
    pip install -r requirements.txt
    ```
6. Run the application:
    ```bash
    uvicorn app.main:app --reload --port 8080
    ```

---

## Default Checkups

- OpenAPI Documentation: [http://127.0.0.1:8080/docs](http://127.0.0.1:8080/docs)
- GraphQL Playground: [http://127.0.0.1:8080/graphql](http://127.0.0.1:8080/graphql)

---

## Useful links and documentation

- SQLAlchemy: [https://docs.sqlalchemy.org/en/20/](https://docs.sqlalchemy.org/en/20/)
- FastAPI: [https://fastapi.tiangolo.com/](https://fastapi.tiangolo.com/)
- Strawberry GraphQL: [https://strawberry.rocks/docs](https://strawberry.rocks/docs)
