
from main import app
from fastapi import Request
from pyinstrument import Profiler

from utils.logger import logger

import time, json


@app.middleware("http")
async def log_requests(request: Request, call_next):
    profiling = request.headers.get("X-Profiler", "").lower() == "true"
    
    if profiling:
        profiler = Profiler()
        profiler.start()
    
    body = await request.body()
    content_type = request.headers.get("content-type", "")

    if "application/json" in content_type or "text/" in content_type:
        try:
            body = body.decode("utf-8")
        except UnicodeDecodeError:
            body = "<undecodable text>"
    else:
        body = "<binary content>"

    logger.info(f"⬇️ {request.method} {request.url}")
    
    if len(body) > 0:
        logger.info(f"📦 payload: {json.dumps(body, indent=2)}")
    
    try:
        start_time = time.time()
        response = await call_next(request)
        
        if profiling:
            profiler.stop()
        
        duration = time.time() - start_time
        logger.info(f"⬆️ status: {response.status_code} - {duration:.3f}s")
        
        if profiling:
            logger.info(f"🦺 profiler output: {profiler.output_text(unicode=True, color=False )}")
        
        return response
    except Exception as e:
        logger.exception("🔥an error has occurred")
        raise e

