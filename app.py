from flask import Flask, request, jsonify
import base64
import numpy as np

app = Flask(__name__)

@app.route("/", methods=["POST"])
def process_audio():
    data = request.json
    audio_base64 = data["audio_base64"]

    audio_bytes = base64.b64decode(audio_base64)

    # Convert to numpy (example placeholder)
    audio_array = np.frombuffer(audio_bytes, dtype=np.int16)

    result = {
        "rows": len(audio_array),
        "columns": ["audio"],
        "mean": {"audio": float(np.mean(audio_array))},
        "std": {"audio": float(np.std(audio_array))},
        "variance": {"audio": float(np.var(audio_array))},
        "min": {"audio": int(np.min(audio_array))},
        "max": {"audio": int(np.max(audio_array))},
        "median": {"audio": float(np.median(audio_array))},
        "mode": {"audio": int(np.bincount(audio_array).argmax()) if len(audio_array) > 0 else 0},
        "range": {"audio": int(np.max(audio_array) - np.min(audio_array))},
        "allowed_values": {},
        "value_range": {},
        "correlation": []
    }

    return jsonify(result)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
