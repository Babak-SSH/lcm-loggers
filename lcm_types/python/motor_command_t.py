"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class motor_command_t(object):
    __slots__ = ["id", "p_d", "v_d", "kp", "kd", "ff"]

    __typenames__ = ["double", "double", "double", "double", "double", "double"]

    __dimensions__ = [None, None, None, None, None, None]

    def __init__(self):
        self.id = 0.0
        self.p_d = 0.0
        self.v_d = 0.0
        self.kp = 0.0
        self.kd = 0.0
        self.ff = 0.0

    def encode(self):
        buf = BytesIO()
        buf.write(motor_command_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">dddddd", self.id, self.p_d, self.v_d, self.kp, self.kd, self.ff))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != motor_command_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return motor_command_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = motor_command_t()
        self.id, self.p_d, self.v_d, self.kp, self.kd, self.ff = struct.unpack(">dddddd", buf.read(48))
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if motor_command_t in parents: return 0
        tmphash = (0x6bc08bc7828cde01) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if motor_command_t._packed_fingerprint is None:
            motor_command_t._packed_fingerprint = struct.pack(">Q", motor_command_t._get_hash_recursive([]))
        return motor_command_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

