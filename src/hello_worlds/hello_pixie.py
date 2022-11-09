from direct.showbase.ShowBase import ShowBase


class Learning(ShowBase):

    def __init__(self):
        ShowBase.__init__(self)

        # Load one model.
        self.model_a = self.loader.loadModel("../models/character_a.glb")
        # Reparent the model to render.
        self.model_a.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.model_a.setScale(0.25, 0.25, 0.25)
        self.model_a.setPos(0, 14, 0)

        # Load second model.
        self.model_b = self.loader.loadModel("../models/mailbox.glb")
        # Reparent the model to render.
        self.model_b.reparentTo(self.render)
        # Apply scale and position transforms on the model.
        self.model_b.setScale(0.25, 0.25, 0.25)
        self.model_b.setPos(-1, 4, 0)


# app = HelloPixie()
# app.run()
