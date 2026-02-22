from fastapi import FastAPI

# from src.config

from src.config.env import env


def create_app() -> FastAPI:
    docs_url = "/docs" if env.get_item("DEGUB", None) == "True" else None

    app = FastAPI(
        docs_url=docs_url,
        redoc_url='/',
        title='quiz'
    )

    # criar os improts de rotas e de exceptions @TODO
    

    return app

app = create_app()
