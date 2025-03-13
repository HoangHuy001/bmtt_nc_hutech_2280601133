from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher

app = Flask(__name__)

# CAESAR CIPHER ALGORITHM
caesar_cipher = CaesarCipher()

@app.route("/api/caesar/encrypt", methods=["POST"])
def caesar_encrypt():
    data = request.get_json()  # Sửa: request.json → request.get_json()
    if not data or 'plain_text' not in data or 'key' not in data:
        return jsonify({"error": "Missing plain_text or key"}), 400

    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    
    return jsonify({'encrypted_message': encrypted_text})  # Sửa 'massage' → 'message'

@app.route("/api/caesar/decrypt", methods=["POST"])  # Sửa dấu phẩy bị thiếu
def caesar_decrypt():
    data = request.get_json()  # Sửa: request.json → request.get_json()
    if not data or 'cipher_text' not in data or 'key' not in data:
        return jsonify({"error": "Missing cipher_text or key"}), 400

    cipher_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(cipher_text, key)

    return jsonify({'decrypted_message': decrypted_text})  # Sửa 'massage' → 'message'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
