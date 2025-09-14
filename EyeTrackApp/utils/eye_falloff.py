import numpy as np

from eye import EyeId


def velocity_falloff(self, var, out_x, out_y):

    if (
        self.settings.gui_right_eye_dominant
        or self.settings.gui_left_eye_dominant
        or self.settings.gui_outer_side_falloff
        or self.settings.gui_automatic_dominant_eye
    ):

        # Check if the the eyes are looking left or right for automatic dominant eye
        force_left_eye_dominant = False
        force_right_eye_dominant = False
        if self.settings.gui_automatic_dominant_eye:
            looking_left = (var.l_eye_x + var.r_eye_x) / 2 < 0
            # Also check that the eye isn't closed
            if (looking_left and var.l_eyeopen > 0) or (var.l_eyeopen > 0 and var.r_eyeopen <= 0):
                # print("LEFT")
                force_left_eye_dominant = True

            if (not looking_left and var.r_eyeopen > 0) or (var.r_eyeopen > 0 and var.l_eyeopen <= 0):
                # print("RIGHT")
                force_right_eye_dominant = True
            
            # If both eyes are closed no dominant eyes
                         
        # Calculate the distance between the two eyes
        dist = np.sqrt(np.square(var.l_eye_x - var.r_eye_x) + np.square(var.left_y - var.right_y))
        if self.eye_id == EyeId.LEFT:
            var.l_eye_x = out_x
            var.left_y = out_y

        if self.eye_id == EyeId.RIGHT:
            var.r_eye_x = out_x
            var.right_y = out_y

        # Check if the distance is greater than the threshold
        if dist > self.settings.gui_eye_dominant_diff_thresh:

            if self.settings.gui_right_eye_dominant or force_right_eye_dominant:
                out_x, out_y = var.r_eye_x, var.right_y

            elif self.settings.gui_left_eye_dominant or force_left_eye_dominant:
                out_x, out_y = var.l_eye_x, var.left_y

            else:
                # If the distance is too large, identify the eye with the lower velocity
                if var.l_eye_velocity < var.r_eye_velocity:
                    # Mirror the position of the eye with lower velocity to the other eye
                    out_x, out_y = var.r_eye_x, var.right_y
                else:
                    # Mirror the position of the eye with lower velocity to the other eye
                    out_x, out_y = var.l_eye_x, var.left_y
        else:
            # If the distance is within the threshold, do not mirror the eyes
            pass
    else:
        pass
    return out_x, out_y
