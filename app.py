from flask import Flask, request, send_file
import pdf417gen
from io import BytesIO

app = Flask(__name__)

@app.route('/generate-barcode', methods=['POST'])
def generate_barcode():
    data = request.json
    # Extracting the fields
    first_name = data.get('first_name')
    middle_name = data.get('middle_name', '')
    last_name = data.get('last_name')
    document_number = data.get('document_number')
    gender = data.get('gender')
    dob = data.get('dob')
    address = data.get('address')
    city = data.get('city')
    state = data.get('state')
    zip_code = data.get('zip')
    height = data.get('height')
    weight = data.get('weight')
    eye_color = data.get('eye_color')
    hair_color = data.get('hair_color')
    expiry_date = data.get('expiry_date')
    document_discriminator = data.get('document_discriminator')
    issue_date = data.get('issue_date')
    document_type = data.get('document_type')

    # Construct AAMVA data string
    aamva_data = f"{document_number}|{first_name} {middle_name} {last_name}|{dob}|{gender}|{address}, {city}, {state} {zip_code}|{height}|{weight}|{eye_color}|{hair_color}|{expiry_date}|{document_discriminator}|{issue_date}|{document_type}"

    # Generate PDF417 barcode
    barcode = pdf417gen.encode(aamva_data)

    # Create the barcode image
    image = pdf417gen.render_image(barcode)
    img_io = BytesIO()
    image.save(img_io, 'PNG')
    img_io.seek(0)

    return send_file(img_io, mimetype='image/png', as_attachment=True, download_name="real_id_barcode.png")

if __name__ == '__main__':
    app.run(debug=True)
