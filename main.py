from flask import Flask, request, jsonify, abort

app = Flask(__name__)

hashes = {
    "1.0.0": {"hash": "KJQZGZ64c25uJd4uYEasHQoWZ2meotWL", "version_name": "Release"},
    "1.1.0": {"hash": "hXNDphSHZErIhKWY17kZgmmtteAXtfwt", "version_name": "Better Output"}
}

LATEST_VERSION = "1.1.0"
LATEST_HASH = hashes[LATEST_VERSION]["hash"]

@app.route("/check", methods=["POST"])
def check():
    if not request.is_json:
        abort(403)

    data = request.json
    user_hash = data.get("hash")

    if not user_hash:
        abort(403)

    for version, info in hashes.items():
        if user_hash == info["hash"]:
            return jsonify({
                "outdated": user_hash != LATEST_HASH,
                "latest_version": LATEST_VERSION
            })
            
    return jsonify({
        "error": "Unknown hash"
    }), 400


@app.route("/", methods=["GET", "HEAD", "OPTIONS"])
def block():
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)