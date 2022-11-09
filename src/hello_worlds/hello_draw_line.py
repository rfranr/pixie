from direct.showbase.ShowBase import ShowBase
from panda3d.core import LineSegs
from panda3d.core import NodePath


class Learning(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        ori_x = 0
        ori_y = 15
        ori_z = 0

        # Create Line Segs
        self.lines_z = LineSegs()

        # Define one line for the z-axis.
        self.lines_z.moveTo(ori_x, ori_y, ori_z)
        self.lines_z.drawTo(ori_x, ori_y, ori_z + 20)

        # Define one line for the y-axis.
        self.lines_z.moveTo(ori_x, ori_y, ori_z)
        self.lines_z.drawTo(ori_x, ori_y - 20, ori_z)

        # Define one line for the x-axis.
        self.lines_z.moveTo(ori_x, ori_y, ori_z)
        self.lines_z.drawTo(ori_x + 20, ori_y, ori_z)

        self.lines_z.setThickness(4)
        self.lines_z.setColor(200, 200, 200)
        
        self.node_z = self.lines_z.create()
        self.np_z = NodePath(self.node_z)

        # Reparent node lines to render.
        self.np_z.reparentTo(self.render)


# app = MyApp()
# app.run()
