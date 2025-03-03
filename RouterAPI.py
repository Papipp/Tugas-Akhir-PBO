from flask import Flask, jsonify, request
from models import db, Apartemen, Unit, Penyewa, Transaksi

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = DATABASE_URI
db.init_app(app)

@app.route("/apartemen", methods=["GET"])
def get_apartemen():
    apartemen = Apartemen.query.all()
    result = [{"id": apt.id, "nama": apt.nama, "alamat": apt.alamat} for apt in apartemen]
    return jsonify(result)

@app.route("/unit", methods=["GET"])
def get_units():
    units = Unit.query.filter_by(status="Tersedia").all()
    result = [{"id": u.id, "nomor_unit": u.nomor_unit, "harga_sewa": u.harga_sewa} for u in units]
    return jsonify(result)

@app.route("/sewa", methods=["POST"])
def sewa_unit():
    data = request.json
    penyewa = Penyewa(nama=data["nama"], kontak=data["kontak"])
    db.session.add(penyewa)
    db.session.commit()

    unit = Unit.query.get(data["unit_id"])
    if unit and unit.status == "Tersedia":
        unit.status = "Disewa"
        transaksi = Transaksi(penyewa_id=penyewa.id, unit_id=unit.id)
        db.session.add(transaksi)
        db.session.commit()
        return jsonify({"message": "Unit berhasil disewa"}), 201
    return jsonify({"message": "Unit tidak tersedia"}), 400

if __name__ == "__main__":
    app.run(debug=True)
