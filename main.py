from flask import Flask, request, jsonify, abort, send_file
from pathlib import Path

app = Flask(__name__)

versions = {
    "1.0.0": {"hash": "KJQZGZ64c25uJd4uYEasHQoWZ2meotWL", "version_name": "Release"},
}


LATEST_VERSION = list(versions)[0]
LATEST_HASH = versions[LATEST_VERSION]["hash"]
LATEST_VERSION_NAME = versions[LATEST_VERSION]["version_name"]

@app.route("/", methods=["GET", "HEAD", "OPTIONS"])
def block():
    abort(403)

@app.route("/c", methods=["POST"])
def check():
    if not request.is_json:
        abort(403)

    data = request.json
    user_hash = data.get("hash")

    if not user_hash:
        abort(403)
    

    for version, info in versions.items():
        if user_hash == info["hash"]:
            return jsonify({
                "user_version": version[user_hash],
                "user_version_name": versions[user_hash]["version_name"],
                "outdated": user_hash != LATEST_HASH,
                "latest_version": LATEST_VERSION,
                "latest_version_name": LATEST_VERSION_NAME
            })
            
    return jsonify({
        "error": "Unknown hash"
    }), 400
    

@app.route("/d", methods=["POST"])
def download():
    if not request.is_json:
        abort(403)
    
    data = request.json
    version_name = data.get("requested")

 
    file_path = Path(__file__).parent / f"{version_name}.tar.gz"

    if not file_path.exists():
        return jsonify({"message": "File not found"}), 404

    return send_file(
        str(file_path),
        mimetype="application/gzip",
        as_attachment=True,
        download_name=f"{version_name}.tar.gz"
    )


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
