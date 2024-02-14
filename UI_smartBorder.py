import flet as ft


class SmartRadiusBorder(ft.UserControl):
    def __init__(self,inner_radius=5, outer_radius=20,controls=[],spacing=5,layout_row=False):
        super().__init__()
        self.layout_row = layout_row
        self.inner_radius = inner_radius
        self.outer_radius = outer_radius
        self.controls = controls
        self.spacing = spacing
    @classmethod
    def ROW(cls, controls=[], spacing=1, inner_radius=4, outer_radius=10):
        return cls(inner_radius=inner_radius, outer_radius=outer_radius, controls=controls, spacing=spacing, layout_row=True)

    @classmethod
    def COLUMN(cls, controls=[], spacing=1, inner_radius=4, outer_radius=10):
        return cls(inner_radius=inner_radius, outer_radius=outer_radius, controls=controls, spacing=spacing, layout_row=False)

    def build(self):
        _controls_ = []
        
        if self.layout_row==True:
            for i, control in enumerate(self.controls):
                if i == 0:
                    control.border_radius = ft.border_radius.only(top_left=self.outer_radius,bottom_left=self.outer_radius,top_right=self.inner_radius,bottom_right=self.inner_radius)
                elif i == len(self.controls) - 1:
                    control.border_radius = ft.border_radius.only(bottom_right=self.outer_radius,top_right=self.outer_radius,bottom_left=self.inner_radius,top_left=self.inner_radius)
                else:
                    control.border_radius = self.inner_radius
                _controls_.append(control)
        elif self.layout_row==False:
            for i, control in enumerate(self.controls):
                if i == 0:
                    control.border_radius = ft.border_radius.only(top_left=self.outer_radius,top_right=self.outer_radius,bottom_left=self.inner_radius,bottom_right=self.inner_radius)
                elif i == len(self.controls) - 1:
                    control.border_radius = ft.border_radius.only(top_left=self.inner_radius,top_right=self.inner_radius,bottom_left=self.outer_radius,bottom_right=self.outer_radius)
                else:
                    control.border_radius = self.inner_radius
                _controls_.append(control)

        if self.layout_row==True:
            col = ft.Row([*_controls_],spacing=self.spacing)
            return col
        else:
            col = ft.Column([*_controls_],spacing=self.spacing)
            return col


