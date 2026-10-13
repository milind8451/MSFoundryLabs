import sys
print(f"Python: {sys.version}")
print(f"Path:   {sys.executable}")

major, minor = sys.version_info[:2]
if ".venv" not in sys.executable:
    print("\n⚠️  Not running from .venv — select the correct kernel (see Step 2)")
elif minor > 13:
    print(f"\n⚠️  Python 3.{minor} detected — 3.12 is recommended (3.14+ has compatibility issues)")
elif minor >= 10:
    print("\n✅ Python version and venv look good.")
else:
    print("\n❌ Python 3.10+ required. Install Python 3.12.")