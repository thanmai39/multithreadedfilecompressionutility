from flask import Flask, request, render_template, send_file, redirect, url_for
import os
from multithreaded_compressor import MultithreadedCompressor

app = Flask(__name__)
compressor = MultithreadedCompressor()
UPLOAD_FOLDER = "uploads"
OUTPUT_FOLDER = "output"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(OUTPUT_FOLDER, exist_ok=True)

@app.route("/")
def index():
    return render_template("index.html", message="")

@app.route("/process", methods=["POST"])
def process_file():
    if "file" not in request.files:
        return render_template("index.html", message="No file uploaded.")
    
    file = request.files["file"]
    action = request.form.get("action")
    
    if file.filename == "":
        return render_template("index.html", message="Please select a file.")
    
    # Save the uploaded file
    input_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(input_path)

    # Determine output paths
    if action == "compress":
        output_path = os.path.join(OUTPUT_FOLDER, f"{file.filename}.rle")
        compressor.compress_file(input_path, output_path)
        return send_file(output_path, as_attachment=True)
    elif action == "decompress":
        if not file.filename.endswith(".rle"):
            return render_template("index.html", message="File is already decompressed.")
        
        output_path = os.path.join(OUTPUT_FOLDER, file.filename.replace(".rle", ""))
        compressor.decompress_file(input_path, output_path)
        return send_file(output_path, as_attachment=True)
    else:
        return render_template("index.html", message="Invalid action.")

if __name__ == "__main__":
    app.run(debug=True)
