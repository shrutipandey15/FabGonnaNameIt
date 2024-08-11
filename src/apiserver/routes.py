import os
import logging

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import ORJSONResponse

debug = bool(os.environ.get("DEBUG", False))
logger = logging.getLogger("routes")
logger.info(f"DEBUG: {debug}")

if debug:
    app = FastAPI(debug=True, default_response_class=ORJSONResponse)
    app.add_middleware(
        CORSMiddleware, allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
    )
else:
    app = FastAPI(
        debug=False,
        docs_url=None,
        redoc_url=None,
        default_response_class=ORJSONResponse,
    )
logger.info("Routes Loaded.")
