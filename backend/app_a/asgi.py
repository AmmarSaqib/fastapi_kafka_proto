"""
Author: Ammar Saqib

Main file to trigger the Uvicorn server
"""

import os
import uvicorn
from app.main import app


if __name__ == "__main__":
    uvicorn.run(app, port=os.environ.get("APP_A_PORT"))
