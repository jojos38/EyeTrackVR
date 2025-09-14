from eye import EyeId

def lerp(a, b, t):
    return a + (b - a) * t

def smart_eyelids_syncing(self, var):
    if self.eye_id == EyeId.LEFT:
        var.l_eyeopen = self.eyeopen

    if self.eye_id == EyeId.RIGHT:
        var.r_eyeopen = self.eyeopen
        
    if (abs(var.l_eyeopen - var.r_eyeopen) < self.settings.gui_smart_eyelids_syncing_thres):
        var.synced_eyeopen = (var.l_eyeopen + var.r_eyeopen) / 2
        return var.synced_eyeopen
    else:
        return self.eyeopen