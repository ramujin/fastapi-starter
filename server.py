''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Necessary Imports
from fastapi import FastAPI, Request            # The main FastAPI import and Request object
from fastapi.responses import HTMLResponse      # Used for returning HTML responses (JSON is default)
from fastapi.templating import Jinja2Templates  # Used for generating HTML from templatized files

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Configuration
router = FastAPI()                              # Specify the "app" that will run the routing
views = Jinja2Templates(directory="views")      # Specify where the HTML files are located on disk

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# Example route: return a static HTML page
@router.get("/", response_class=HTMLResponse)
def get_html() -> HTMLResponse:
  with open("views/hello.html") as html:
    return HTMLResponse(content=html.read())

# Example route: returning an HTML partial using Jinja2 template rendering
@router.get("/html/{id}", response_class=HTMLResponse)
def get_html_partial(request:Request, id:str) -> HTMLResponse:
  return views.TemplateResponse("hello_partial.html", {"request":request, "id":id})

# Example route: returning just JSON
@router.get("/json/{name}")
def get_json(name:str) -> dict:
  return {"Hello": name}

# Example route: returning JSON with an additional query argument
@router.get("/items/{item_id}")
def read_item(item_id:int, q:str|None=None):
  return {"item_id": item_id, "query_string": q}
