import subprocess
from datetime import datetime

# Get timestamp for training
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

# Run training on small test Imagen
subprocess.call(["python3", "train.py", "-test", "-ts", timestamp])

# Use small test Imagen to generate image
subprocess.call(["python3", "inference.py", "-d", f"training_{timestamp}"])
