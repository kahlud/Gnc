from datetime import timedelta
from odoo import models, fields, api

class shift(models.Model):
    _name='shift.model_shift'

    client_id= fields.Many2one('client.model_client', string='Cliente')
    vehicle_id= fields.Many2one('client_vehicle.model_client', string='Vehiculo', domain="[('owner_vehicle_client_id', '=', client_id)]")
    type_service= fields.Selection([('oblea','Oblea'),('gnc','GNC'),('mecanica','Mecanica')], string='Tipo de servicio')
    info_service=fields.Text('Detalles del servicio')
    date_time= fields.Datetime(string='Fecha')
    date_time_end=fields.Datetime(compute='time_end')
    shift_status= fields.Selection([('waiting', 'En espera'), ('finalized', 'Finalizado'), ('cancelled', 'Cancelado')], string='Estado' , default='waiting')


    def name_get(self):
        result=[]
        for shift in self:
            shift_client= shift.client_id.name_get()
            result.append((shift.id,shift_client[0][1]))
        return result

    @api.depends('date_time')
    def time_end(self):
        for shift in self:
            shift.date_time_end= shift.date_time + timedelta(hours=3)

    @api.onchange('shift_status')
    def change_status(self):
        for obj in self:
            status_old = obj._origin.shift_status
            status_new = obj.shift_status
            if status_new == 'finalized':
                self.env["vehicle_service.model_vehicle_client"].create([{
                    'shift_id': obj.id,
                    'date_time_service': obj.date_time,
                    'service_performed': obj.type_service,
                    'description_service': obj.info_service,
                    'vehicle_id':obj.vehicle_id.id
                }])
            elif status_new == 'waiting' and status_old == 'finalized':
                shift_search = self.env["vehicle_service.model_vehicle_client"].search([('shift_id', '=', obj.id)])
                if not shift_search:
                    print('No se encontro el registro - En espera')
                else: shift_search[0].unlink() 
                print('Se borro el registro - En espera ')
            elif status_new == 'cancelled' and status_old == 'finalized':
                shift_search = self.env["vehicle_service.model_vehicle_client"].search([('shift_id', '=', obj.id)])
                if not shift_search:
                    print('No se encontro el registro - Cancelado')
                else: shift_search[0].unlink() 
                print('Se borro el registro - Cancelado')


