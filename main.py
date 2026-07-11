from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()

app.mount("/static", StaticFiles(directory="static"), name="static")

templates = Jinja2Templates(directory="templates")

posts: list[dict] = [
    {
        "id": 1,
        "author": "Corey Schafer",
        "title": "FastAPI is Awesome",
        "content": "This framework is really easy to use and super fast.",
        "date_posted": "April 20, 2025"
    },
    {
        "id": 2,
        "author": "Jane Doe",
        "title": "Python is Great for Web Development",
        "content": "Python is a great language for web development, and FastAPI makes it even better.",
        "date_posted": "April 21, 2025"
    },
    {
        "id": 3,
        "author": "John Smith",
        "title": "Mastering Async/Await in Python",
        "content": "Understanding asynchronous programming can significantly boost your API performance.",
        "date_posted": "May 02, 2025"
    },
    {
        "id": 4,
        "author": "Alice Johnson",
        "title": "Introduction to Pydantic v2",
        "content": "Pydantic makes data validation in FastAPI incredibly smooth and type-safe.",
        "date_posted": "May 15, 2025"
    },
    {
        "id": 5,
        "author": "Bob Wilson",
        "title": "Dockerizing a FastAPI Application",
        "content": "Learn how to containerize your FastAPI apps using lightweight Python Docker images.",
        "date_posted": "June 01, 2025"
    },
    {
        "id": 6,
        "author": "Sarah Connor",
        "title": "Building RESTful APIs with Ease",
        "content": "FastAPI provides automatic documentation out of the box, saving hours of frontend coordination.",
        "date_posted": "June 12, 2025"
    },
    {
        "id": 7,
        "author": "David Miller",
        "title": "Connecting FastAPI to PostgreSQL",
        "content": "A step-by-step guide to setting up SQLAlchemy or SQLModel with a relational database.",
        "date_posted": "July 04, 2025"
    },
    {
        "id": 8,
        "author": "Emily Davis",
        "title": "Implementing JWT Authentication",
        "content": "Secure your FastAPI endpoints using OAuth2 with Password flow and JWT tokens.",
        "date_posted": "August 20, 2025"
    },
    {
        "id": 9,
        "author": "Michael Brown",
        "title": "Dependency Injection Demystified",
        "content": "FastAPI's Depends system is powerful for managing database sessions and security.",
        "date_posted": "September 05, 2025"
    },
    {
        "id": 10,
        "author": "Sophia Martinez",
        "title": "Deploying FastAPI to AWS",
        "content": "How to host your FastAPI application on AWS EC2 or Lambda for production scale.",
        "date_posted": "October 14, 2025"
    }
]

@app.get("/")
def home(request: Request):
    # අලුත් FastAPI/Starlette syntax එක: (request, template_name, context_dict)
    return templates.TemplateResponse(
        request, 
        "home.html", 
        {"posts": posts, "title": "Home"}
    )
     
@app.get("/api/posts")
def get_posts():
    return posts