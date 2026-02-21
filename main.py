from flask import Flask, request, jsonify, abort

app = Flask(__name__)

versions = {
    "1.0.0": {"hash": "KJQZGZ64c25uJd4uYEasHQoWZ2meotWL", "version_name": "Release"},
}


LATEST_VERSION = list(versions)[-1]
LATEST_HASH = versions[LATEST_VERSION]["hash"]
LATEST_VERSION_NAME = versions[LATEST_VERSION]["version_name"]


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
    
    
    


@app.route("/", methods=["GET", "HEAD", "OPTIONS"])
def block():
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)from flask import Flask, request, jsonify, abort

app = Flask(__name__)

versions = {
    "1.0.0": {"hash": "KJQZGZ64c25uJd4uYEasHQoWZ2meotWL", "version_name": "Release"},
}


LATEST_VERSION = list(versions)[-1]
LATEST_HASH = versions[LATEST_VERSION]["hash"]
LATEST_VERSION_NAME = versions[LATEST_VERSION]["version_name"]


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
    
    
    


@app.route("/", methods=["GET", "HEAD", "OPTIONS"])
def block():
    abort(403)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
