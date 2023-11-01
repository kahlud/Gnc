from odoo import models,fields,api

class wafers(models.Model):
    _name='wafers.model_wafers'

    wafers_of_the_month= fields.Many2one("client_vehicle.model_client", string='Vehiculo')
    wafer_expiration=fields.Datetime(string="Vencimiento de oblea")
    number_tubes=fields.Integer(string='Tubos')
    hydraulic_test=fields.Datetime(string='Prueba hidraulica')
    status_wafers=fields.Selection([('current','Vigente'),('defeated','Vencida'),('in_progress','En curso'),('on_hold','En espera'),('renewed','Renovada')])
    


  