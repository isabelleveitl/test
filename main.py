import controller as c
import view as v
import model as m

ctrl = c.Controller(m.Model(), v.View())
ctrl.start()