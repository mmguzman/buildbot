__author__ = 'MarceloM Guzman'

from selenium.webdriver.common.by import By

# ************************** Volume Types **********************************************************
no_db_volume = {'fpo': (By.NAME, 'v_afpdofpo'), 'web': (By.NAME, "v_afpdoweb")}

no_fpo_volume = {'web': (By.NAME, "v_afpdoweb"), 'db': (By.NAME, "v_dbena"), 'small': (By.NAME, "v_storesmallweb"),
                 'large': (By.NAME, "v_storebigweb"), 'multi': (By.NAME, "v_storepdfpages"),
                 'extract': (By.NAME, "v_storetext"), 'store': (By.NAME, "v_storemovieframes")}

wnv_volume = {'fpo': (By.NAME, 'v_afpdofpo'), 'web': (By.NAME, "v_afpdoweb"), 'db': (By.NAME, "v_dbena"),
              'small': (By.NAME, "v_storesmallweb"), 'large': (By.NAME, "v_storebigweb"),
              'multi': (By.NAME, "v_storepdfpages"), 'extract': (By.NAME, "v_storetext"),
              'store': (By.NAME, "v_storemovieframes"), 'office': (By.NAME, "v_storeoffice")}

#  ************************** Field Types ***********************************************************
field_type = {'text': 'Text', 'integer': 'Integer', 'float': 'Float', 'date': 'Date', 'boolean': 'Boolean'}

#  ************************** Permission Set Checkboxes *********************************************
perm_set_checkbox = {'visible': 'perm_visib', 'searchable': 'perm_searc', 'browse': 'perm_dataf',
                     'enabled': 'perm_uploa', 'required': 'perm_requp', 'push required': 'perm_pushr',
                     'editable': 'perm_flage', 'popup': 'perm_flagp', 'locked': 'perm_flagl'}

# ************************* Request Queue values ****************************************************
request_queue = {'FPO/WEB Preview': '',
                 'QuarkXPress & InDesign Documents': '0',
                 'XMP Sync': '1',
                 'PDF Sync': '2',
                 'Video & Audio Previews': '3',
                 'Office Documents': '4',
                 'WEB Browser Documents': '5',
                 'XMP Writeback': '6'}

# ************************* Facets *****************************************************************
facet_metadata = {'Big-integer':'xwnv:facet_big_int',
                  'Integer':'xwnv:facet_int',
                  'Small-integer':'xwnv:facet_small_int',
                  'Tiny-integer':'xwnv:facet_tiny_int',
                  'Float-2dec':'xwnv:facet_float_2dec'}
