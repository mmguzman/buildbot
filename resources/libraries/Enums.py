__author__ = 'MarceloM Guzman'

from enum import Enum


class FieldType(Enum):
    Text = "Text"
    Integer = "Integer"
    Float = "Float"
    Date = "Date"
    Boolean = "Boolean"

    def __str__(self):
        return '%s' % self._value_
    
    #===============================================================================================
    # def name(self):
    #     return self.name()
    # 
    # def value(self):
    #     return self.value()
    #===============================================================================================