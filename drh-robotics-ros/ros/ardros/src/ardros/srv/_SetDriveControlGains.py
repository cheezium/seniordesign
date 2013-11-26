"""autogenerated by genpy from ardros/SetDriveControlGainsRequest.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetDriveControlGainsRequest(genpy.Message):
  _md5sum = "7ef02095d661072b02e76d2e1f6bddf8"
  _type = "ardros/SetDriveControlGainsRequest"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """float32 velocityPParam
float32 velocityIParam
float32 turnPParam
float32 turnIParam

"""
  __slots__ = ['velocityPParam','velocityIParam','turnPParam','turnIParam']
  _slot_types = ['float32','float32','float32','float32']

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       velocityPParam,velocityIParam,turnPParam,turnIParam

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetDriveControlGainsRequest, self).__init__(*args, **kwds)
      #message fields cannot be None, assign default values for those that are
      if self.velocityPParam is None:
        self.velocityPParam = 0.
      if self.velocityIParam is None:
        self.velocityIParam = 0.
      if self.turnPParam is None:
        self.turnPParam = 0.
      if self.turnIParam is None:
        self.turnIParam = 0.
    else:
      self.velocityPParam = 0.
      self.velocityIParam = 0.
      self.turnPParam = 0.
      self.turnIParam = 0.

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      _x = self
      buff.write(_struct_4f.pack(_x.velocityPParam, _x.velocityIParam, _x.turnPParam, _x.turnIParam))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.velocityPParam, _x.velocityIParam, _x.turnPParam, _x.turnIParam,) = _struct_4f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      _x = self
      buff.write(_struct_4f.pack(_x.velocityPParam, _x.velocityIParam, _x.turnPParam, _x.turnIParam))
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      _x = self
      start = end
      end += 16
      (_x.velocityPParam, _x.velocityIParam, _x.turnPParam, _x.turnIParam,) = _struct_4f.unpack(str[start:end])
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
_struct_4f = struct.Struct("<4f")
"""autogenerated by genpy from ardros/SetDriveControlGainsResponse.msg. Do not edit."""
import sys
python3 = True if sys.hexversion > 0x03000000 else False
import genpy
import struct


class SetDriveControlGainsResponse(genpy.Message):
  _md5sum = "d41d8cd98f00b204e9800998ecf8427e"
  _type = "ardros/SetDriveControlGainsResponse"
  _has_header = False #flag to mark the presence of a Header object
  _full_text = """

"""
  __slots__ = []
  _slot_types = []

  def __init__(self, *args, **kwds):
    """
    Constructor. Any message fields that are implicitly/explicitly
    set to None will be assigned a default value. The recommend
    use is keyword arguments as this is more robust to future message
    changes.  You cannot mix in-order arguments and keyword arguments.

    The available fields are:
       

    :param args: complete set of field values, in .msg order
    :param kwds: use keyword arguments corresponding to message field names
    to set specific fields.
    """
    if args or kwds:
      super(SetDriveControlGainsResponse, self).__init__(*args, **kwds)

  def _get_types(self):
    """
    internal API method
    """
    return self._slot_types

  def serialize(self, buff):
    """
    serialize message into buffer
    :param buff: buffer, ``StringIO``
    """
    try:
      pass
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize(self, str):
    """
    unpack serialized message in str into this message instance
    :param str: byte array of serialized message, ``str``
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill


  def serialize_numpy(self, buff, numpy):
    """
    serialize message with numpy array types into buffer
    :param buff: buffer, ``StringIO``
    :param numpy: numpy python module
    """
    try:
      pass
    except struct.error as se: self._check_types(se)
    except TypeError as te: self._check_types(te)

  def deserialize_numpy(self, str, numpy):
    """
    unpack serialized message in str into this message instance using numpy for array types
    :param str: byte array of serialized message, ``str``
    :param numpy: numpy python module
    """
    try:
      end = 0
      return self
    except struct.error as e:
      raise genpy.DeserializationError(e) #most likely buffer underfill

_struct_I = genpy.struct_I
class SetDriveControlGains(object):
  _type          = 'ardros/SetDriveControlGains'
  _md5sum = '7ef02095d661072b02e76d2e1f6bddf8'
  _request_class  = SetDriveControlGainsRequest
  _response_class = SetDriveControlGainsResponse
