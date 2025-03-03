from flask_sqlalchemy import SQLAlchemy
from config import db

class Apartemen(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    alamat = db.Column(db.String(200), nullable=False)
    units = db.relationship("Unit", backref="apartemen", lazy=True)

class Unit(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nomor_unit = db.Column(db.String(50), nullable=False)
    harga_sewa = db.Column(db.Float, nullable=False)
    status = db.Column(db.String(20), default="Tersedia")
    apartemen_id = db.Column(db.Integer, db.ForeignKey("apartemen.id"), nullable=False)

class Penyewa(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100), nullable=False)
    kontak = db.Column(db.String(50), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), nullable=True)

class Transaksi(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    penyewa_id = db.Column(db.Integer, db.ForeignKey("penyewa.id"), nullable=False)
    unit_id = db.Column(db.Integer, db.ForeignKey("unit.id"), nullable=False)
    tanggal_sewa = db.Column(db.DateTime, default=db.func.current_timestamp())
