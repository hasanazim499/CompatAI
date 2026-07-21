# =============================================
# CompatAI - Setup Instructions (Mac)
# 1. pip install streamlit psutil
# 2. brew install ollama
# 3. ollama serve          (in separate terminal)
# 4. ollama pull phi3:mini
# 5. streamlit run app.py
# =============================================

import streamlit as st
import platform
import subprocess
import time
from datetime import datetime
import psutil

st.set_page_config(page_title="CompatAI", page_icon="🚀", layout="centered")
st.title("🚀 CompatAI")
st.subheader("Making AI Work on Legacy Hardware")
st.success("✅ Open Source • Optimized for 2017 MacBook Pro & older devices")

# Device Info
ram_gb = round(psutil.virtual_memory().total / (1024**3), 1)
arch = platform.machine()
mac_version = platform.mac_ver()[0]

st.divider()
st.header("Your Device")
col1, col2 = st.columns(2)
with col1:
    st.metric("RAM", f"{ram_gb} GB")
with col2:
    st.metric("Architecture", arch)
st.caption(f"macOS: {mac_version}")

st.divider()
st.header("AI Recommendations")
st.info("Your 8GB Mac is suitable for **3B–7B** models with 4-bit quantization.")
st.markdown("""
**Top models for your hardware:**
- **Phi-3-mini (3.8B)** — Best balance
- **Gemma-2-2B** or **TinyLlama-1.1B** — Fastest
- **Llama-3.2-3B** — Strong reasoning
""")
st.caption("💡 Use GGUF 4-bit/5-bit versions via Ollama")

st.divider()
st.header("Run Real Benchmark")
prompt = st.text_area("Test Prompt", 
                      value="Explain quantum computing in simple terms.", 
                      height=100)

if st.button("▶️ Run Benchmark with phi3:mini", type="primary"):
    with st.spinner("Running inference (this may take 10-60s on 8GB)..."):
        start = time.time()
        try:
            result = subprocess.run(
                ["ollama", "run", "phi3:mini", prompt],
                capture_output=True, text=True, timeout=120
            )
            duration = time.time() - start
            output = result.stdout.strip() or result.stderr.strip()
            
            tokens = len(output.split())
            tps = round(tokens / duration, 1) if duration > 0 else 0
            
            st.success("✅ Benchmark Complete!")
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Tokens/sec", tps)
            with col2:
                st.metric("Time", f"{duration:.1f}s")
            
            st.text_area("Output", output[:600] + ("..." if len(output) > 600 else ""), height=150)
            
            if tps > 15:
                st.success("Excellent for your hardware!")
            elif tps > 8:
                st.info("Good performance")
            else:
                st.warning("Light tasks only — try smaller models")
        except FileNotFoundError:
            st.error("❌ Ollama not found. Install it first.")
            st.code("brew install ollama && ollama serve", language="bash")
        except subprocess.TimeoutExpired:
            st.error("⏱️ Timeout — model too heavy or system busy.")
        except Exception as e:
            st.error(f"Error: {str(e)}")

# Installation Guide
st.divider()
st.header("Quick Setup (Mac)")
st.markdown("""
1. `pip install streamlit psutil`
2. `brew install ollama`
3. `ollama serve` (keep running)
4. `ollama pull phi3:mini`
5. `streamlit run app.py`
""")

# Download
st.divider()
st.header("Download App")
with open(__file__, "r", encoding="utf-8") as f:
    code = f.read()
st.download_button(
    label="📥 Download app.py",
    data=code,
    file_name="app.py",
    mime="text/x-python",
    use_container_width=True
)

st.caption(f"CompatAI v0.6 • Optimized for your 2017 MacBook • {datetime.now().strftime('%Y-%m-%d')}")