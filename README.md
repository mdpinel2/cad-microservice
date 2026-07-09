AI Text-to-Fabrication Platform

Overview

The Text-to-Fabrication Platform is an AI-driven web application that bridges the gap between natural language and precision manufacturing. Instead of requiring users to navigate complex 3D modeling software, this application acts as an autonomous manufacturing engineer. Users simply type a description of the part they need, and the platform automatically generates, formats, and delivers production-ready 3D CAD files.

By bypassing error-prone AI mesh generation (like standard text-to-3D models), this app relies on strict parametric constraints to ensure the output is mathematically accurate and ready for real-world fabrication.

Features

Natural Language Intake: Users describe their project in plain English (e.g., "Make a heavy-duty bracket 80mm long, 50mm tall, 5mm thick, with 6mm holes").

AI Parameter Extraction: Integrates with Google's Gemini AI to parse messy human text into a rigid JSON engineering schema.

Parametric Geometry Engine: Uses a dedicated Python microservice (CadQuery) to programmatically build the 3D Boundary Representation (B-Rep) solid model based on the AI's math.

Dual-Format Export: Automatically generates deliverables for two different manufacturing routes simultaneously:

STEP (.step): For industrial CNC machining and laser cutting.

STL (.stl): For DIY 3D printing and web-based viewing.

Cloud Delivery: Saves the generated manufacturing files directly into the user's Google Drive.

Architecture & Tech Stack

This application utilizes a decoupled, microservice-based architecture to separate the lightweight user interface from the heavy geometry computations.

Frontend UI (Google Apps Script):
A lightweight, responsive web interface built with HTML/CSS/JS. It captures user intent and provides a frictionless submission process without requiring local software installation.

Orchestrator & AI Brain (Google Apps Script + Gemini API):
Acts as the "Traffic Cop." It receives the prompt from the frontend, queries the Gemini API with strict system instructions to extract dimensional variables, and forwards the structured JSON payload to the geometry engine.

CAD Backend (Python / FastAPI / CadQuery):
A dedicated cloud-hosted microservice (e.g., Render or Google Cloud Run). It receives the JSON parameters, executes the parametric drafting logic using the OpenCASCADE kernel, and encodes the resulting STEP and STL files into Base64 for web transmission.

Use Cases

This pipeline is designed to be easily extensible. While currently configured to generate custom brackets, the Python backend can be expanded with parametric scripts for shelving, custom enclosures, cabinetry, and structural framing. It serves as a blueprint for the future of automated, intent-driven manufacturing.
