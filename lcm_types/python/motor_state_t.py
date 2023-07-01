"""LCM type definitions
This file automatically generated by lcm.
DO NOT MODIFY BY HAND!!!!
"""

try:
    import cStringIO.StringIO as BytesIO
except ImportError:
    from io import BytesIO
import struct

class motor_state_t(object):
    __slots__ = ["n", "ids", "enabled", "error"]

    __typenames__ = ["int32_t", "int64_t", "boolean", "boolean"]

    __dimensions__ = [None, ["n"], None, None]

    def __init__(self):
        self.n = 0
        self.ids = []
        self.enabled = False
        self.error = False

    def encode(self):
        buf = BytesIO()
        buf.write(motor_state_t._get_packed_fingerprint())
        self._encode_one(buf)
        return buf.getvalue()

    def _encode_one(self, buf):
        buf.write(struct.pack(">i", self.n))
        buf.write(struct.pack('>%dq' % self.n, *self.ids[:self.n]))
        buf.write(struct.pack(">bb", self.enabled, self.error))

    def decode(data):
        if hasattr(data, 'read'):
            buf = data
        else:
            buf = BytesIO(data)
        if buf.read(8) != motor_state_t._get_packed_fingerprint():
            raise ValueError("Decode error")
        return motor_state_t._decode_one(buf)
    decode = staticmethod(decode)

    def _decode_one(buf):
        self = motor_state_t()
        self.n = struct.unpack(">i", buf.read(4))[0]
        self.ids = struct.unpack('>%dq' % self.n, buf.read(self.n * 8))
        self.enabled = bool(struct.unpack('b', buf.read(1))[0])
        self.error = bool(struct.unpack('b', buf.read(1))[0])
        return self
    _decode_one = staticmethod(_decode_one)

    _hash = None
    def _get_hash_recursive(parents):
        if motor_state_t in parents: return 0
        tmphash = (0xe52a6608ce78823b) & 0xffffffffffffffff
        tmphash  = (((tmphash<<1)&0xffffffffffffffff) + (tmphash>>63)) & 0xffffffffffffffff
        return tmphash
    _get_hash_recursive = staticmethod(_get_hash_recursive)
    _packed_fingerprint = None

    def _get_packed_fingerprint():
        if motor_state_t._packed_fingerprint is None:
            motor_state_t._packed_fingerprint = struct.pack(">Q", motor_state_t._get_hash_recursive([]))
        return motor_state_t._packed_fingerprint
    _get_packed_fingerprint = staticmethod(_get_packed_fingerprint)

