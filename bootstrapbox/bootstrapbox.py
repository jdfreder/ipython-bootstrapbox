from IPython.html.widgets import Box
from IPython.utils.traitlets import Bool, Int, Unicode, CUnicode

class ResponsiveBox(Box):
    _view_module = Unicode('nbextensions/bootstrapbox/bootstrapbox', sync=True)
    visible_xs_block = Bool(False, sync=True)
    visible_xs_inline = Bool(False, sync=True)
    visible_xs_inline_block = Bool(False, sync=True)
    visible_sm_block = Bool(False, sync=True)
    visible_sm_inline = Bool(False, sync=True)
    visible_sm_inline_block = Bool(False, sync=True)
    visible_md_block = Bool(False, sync=True)
    visible_md_inline = Bool(False, sync=True)
    visible_md_inline_block = Bool(False, sync=True)
    visible_lg_block = Bool(False, sync=True)
    visible_lg_inline = Bool(False, sync=True)
    visible_lg_inline_block = Bool(False, sync=True)
    hidden_xs = Bool(False, sync=True)
    hidden_sm = Bool(False, sync=True)
    hidden_md = Bool(False, sync=True)
    hidden_lg = Bool(False, sync=True)
    visible_print_block = Bool(False, sync=True)
    visible_print_inline = Bool(False, sync=True)
    visible_print_inline_block = Bool(False, sync=True)
    hidden_print = Bool(False, sync=True)
    
class BootstrapContainer(ResponsiveBox):
    _view_name = Unicode('BootstrapContainerView', sync=True)
    fluid = Bool(True, sync=True, help="Uses percents instead of pixels for column widths.  Ensures proper proportions for key screen resolutions and devices.")
    width = CUnicode('100%', sync=True)
    
class BootstrapRow(ResponsiveBox):
    _view_name = Unicode('BootstrapRowView', sync=True)
    
class BootstrapCol(ResponsiveBox):
    _view_name = Unicode('BootstrapColView', sync=True)

    def _validate_change(self, name, old, new):
        setattr(self, name, new if new is None else min(max(1, new), 12))

    xs_width = Int(None, sync=True, allow_none=True)
    sm_width = Int(None, sync=True, allow_none=True)
    md_width = Int(None, sync=True, allow_none=True)
    lg_width = Int(None, sync=True, allow_none=True)
    _xs_width_changed = _validate_change
    _sm_width_changed = _validate_change
    _md_width_changed = _validate_change
    _lg_width_changed = _validate_change
    
    xs_offset = Int(None, sync=True, allow_none=True)
    sm_offset = Int(None, sync=True, allow_none=True)
    md_offset = Int(None, sync=True, allow_none=True)
    lg_offset = Int(None, sync=True, allow_none=True)
    _xs_offset_changed = _validate_change
    _sm_offset_changed = _validate_change
    _md_offset_changed = _validate_change
    _lg_offset_changed = _validate_change
    
    xs_push = Int(None, sync=True, allow_none=True)
    sm_push = Int(None, sync=True, allow_none=True)
    md_push = Int(None, sync=True, allow_none=True)
    lg_push = Int(None, sync=True, allow_none=True)
    _xs_push_changed = _validate_change
    _sm_push_changed = _validate_change
    _md_push_changed = _validate_change
    _lg_push_changed = _validate_change
    
    xs_pull = Int(None, sync=True, allow_none=True)
    sm_pull = Int(None, sync=True, allow_none=True)
    md_pull = Int(None, sync=True, allow_none=True)
    lg_pull = Int(None, sync=True, allow_none=True)
    _xs_pull_changed = _validate_change
    _sm_pull_changed = _validate_change
    _md_pull_changed = _validate_change
    _lg_pull_changed = _validate_change
    