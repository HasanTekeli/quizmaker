# views.py 54. satırdan:
from reportlab.platypus import Spacer


class ConditionalSpacer(Spacer):
    def wrap(self, avail_width, avail_height):
        height = min(self.height, avail_height-1e-8)
        return (avail_width, height)