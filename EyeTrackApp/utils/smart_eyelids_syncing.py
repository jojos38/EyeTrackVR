from eye import EyeId

def smart_eyelids_syncing(self, var):        
    if (abs(var.l_eyeopen - var.r_eyeopen) < self.settings.gui_smart_eyelids_syncing_thres):
        var.synced_eyeopen = (var.l_eyeopen + var.r_eyeopen) / 2
        return var.synced_eyeopen
    else:
        return self.eyeopen