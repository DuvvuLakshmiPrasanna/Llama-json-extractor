# Render Deployment Guide

This project is now pre-configured for Render with [render.yaml](render.yaml), [runtime.txt](runtime.txt), and Render-compatible app startup in [app.py](app.py).

## What Is Already Done

- App binds to `0.0.0.0` and uses Render's `PORT` env var.
- Lightweight default model is set to `google/flan-t5-small` (override using `MODEL_ID`).
- Render blueprint config is present in [render.yaml](render.yaml).

## Deploy Steps

1. Push this repository to GitHub.
2. Open Render: https://render.com
3. Click **New +** -> **Blueprint**.
4. Connect your GitHub repo.
5. Render detects [render.yaml](render.yaml) and creates the web service automatically.
6. Wait for build and first start (cold start can take time on free tier).

## Alternative (Manual Web Service)

If you don't use Blueprint, create a **Web Service** and set:

- Runtime: `Python 3`
- Build Command: `pip install -r requirements.txt`
- Start Command: `python app.py`
- Environment variables:
  - `MODEL_ID=google/flan-t5-small`
  - `GRADIO_SHARE=false`

## Notes

- Free Render instances can sleep after inactivity.
- First request after sleep can be slow.
- Heavier models may exceed memory; keep `google/flan-t5-small` unless you're on a larger plan.
