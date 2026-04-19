#!/bin/bash

# Start Server
uvicorn server.src.server:app --reload
