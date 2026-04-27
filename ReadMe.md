# 🚀 CompatAI

**Making powerful AI work on any computer — even older ones.**

CompatAI is an open-source tool that helps users check if their device can run modern AI models and gives clear recommendations + real benchmarks.

## The Problem
Most AI tools today require high-end computers. Millions of people with older laptops (like 2017 MacBooks) or lower-spec devices are left behind.

## Our Solution
We act as a **universal adapter** for AI:
- Check your device's capabilities
- Recommend the best models for your hardware
- Run real performance benchmarks
- (Coming soon) Automatically optimize models for your specific device

## Current Features
- Clean web dashboard (no coding needed)
- Device compatibility checker
- Real AI model benchmarking using Ollama
- Simple, honest recommendations

## Quick Start

```bash
# 1. Install Ollama
curl -fsSL https://ollama.com/install.sh | sh

# 2. Pull a model
ollama pull phi3:mini

# 3. Run CompatAI
pip install streamlit
streamlit run app.py
