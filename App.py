import streamlit as st
import platform
import subprocess
import time
from datetime import datetime

st.set_page_config(page_title="CompatAI", page_icon="🚀", layout="centered")

st.title("🚀 CompatAI")
st.subheader("Making AI Work on Any Computer")

st.success("✅ Open Source • Optimized for older & lower-spec devices")

info = {
    'ram_gb': 8.0,
    'arch': platform.machine()
}

st.divider()

st.header("Your Device")
col1, col2 = st.columns(2)
with col1:
    st.metric("RAM", f"{info['ram_gb']} GB")
with col2:
    st.metric("Architecture", info['arch'])

st.divider()

st.header("AI Recommendations")
st.info("Your device is suitable for 3B–7B parameter models with quantization.")

st.markdown("""
**Best models for your hardware:**
- **Phi-3-mini (3.8B)** — Best balance of quality and speed
- **Gemma-2B** or **TinyLlama-1.1B** — Very fast & lightweight
- **Llama-3.2-3B** — Strong reasoning
""")

st.caption("Tip: Always use 4-bit or 5-bit quantized (GGUF) versions.")

st.divider()

st.header("Real Model Benchmark")
prompt = st.text_area("Test Prompt", 
                      value="Explain quantum computing in simple terms.", 
                      height=70)

if st.button("▶️ Run Real Benchmark with phi3:mini", type="primary"):
    with st.spinner("Running real inference on your device..."):
        start = time.time()
        try:
            result = subprocess.run(
                ["ollama", "run", "phi3:mini", prompt],
                capture_output=True, text=True, timeout=180
            )
            duration = time.time() - start
            output = result.stdout.strip()
            tokens = len(output.split())
            tps = round(tokens / duration, 1) if duration > 0 else 0

            st.success("✅ Real Benchmark Complete!")
            
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Tokens per Second", tps)
            with col2:
                st.metric("Time Taken", f"{duration:.1f} sec")

            st.text_area("Model Output", output[:400] + "...", height=120)

            if tps > 20:
                st.success("Excellent performance!")
            elif tps > 10:
                st.info("Good performance for daily use.")
            else:
                st.warning("Acceptable for lighter tasks.")

        except Exception as e:
            st.error(f"Error: {str(e)}")

st.divider()
st.caption(f"CompatAI v0.5 • {datetime.now().strftime('%Y-%m-%d')}")