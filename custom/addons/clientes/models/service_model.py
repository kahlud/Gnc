from odoo import models,fields

class service(models.Model):
    _name='vehicle_service.model_vehicle_client'

    shift_id=fields.Char()
    date_time_service= fields.Datetime(string='Fecha')
    service_performed=fields.Selection([('oblea','Oblea'),('gnc','GNC'),('mecanica','Mecanica')], string='Tipo de servicio')
    description_service=fields.Text(string='Detalles del servicio')
    vehicle_id= fields.Many2one("client_vehicle.model_client", string='Vehiculo')

    