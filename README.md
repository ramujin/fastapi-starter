# FastAPI Starter

This repo is just simple starter code to get started working with the [FastAPI web framework](https://fastapi.tiangolo.com).

## Prerequesites

You just need to have Python 3.7+ installed.

## Usage

1. Create a Python virtual environment

    ```bash
    python3 -m venv env
    ```

2. Start the virtual environment

    ```bash
    source env/bin/activate
    ```

3. Install dependencies

    ```bash
    pip install -U pip
    pip install -r requirements.txt
    ```

4. Run the server

    ```bash
    uvicorn server:router --reload
    ```

5. Visit the server in your browser with these 4 example routes:

    * GET an HTML page: `http://127.0.0.1:8000`
    * GET a templatized HTML partial: `http://127.0.0.1:8000/html/7`
    * GET a JSON response: `http://127.0.0.1:8000/json/steve`
    * GET a JSON response with query arguments: `http://127.0.0.1:8000/items/2?q=hello`

6. View the automatically generated docs for the routes!

    `http://127.0.0.1:8000/docs`

    or an alternative UI...

    `http://127.0.0.1:8000/redoc`
