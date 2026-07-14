#!/bin/bash

# This script exposes the local FastAPI backend (port 8000) to the internet
# using localtunnel, which is free and does not require an account/token.

echo "=================================================="
echo "Nudge Web App - Tunneling Service"
echo "=================================================="

# Check if npm is installed
if ! command -v npm &> /dev/null; then
    echo "✗ Error: npm is not installed. Please install Node.js."
    exit 1
fi

echo "✓ npm detected. Starting localtunnel on port 8000..."
echo "--------------------------------------------------"
echo "Your public webhook URL will be shown below."
echo "Paste this URL into your Twilio Sandbox Console:"
echo "https://<subdomain>.loca.lt/webhook/twilio/whatsapp"
echo "--------------------------------------------------"
echo "Press Ctrl+C to stop the tunnel."
echo "=================================================="

# Start localtunnel
npx -y localtunnel --port 8000
