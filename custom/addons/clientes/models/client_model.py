# -*- coding: utf-8 -*-
from odoo import models,fields,api 
# from odoo import models, fields, api

class client(models.Model):
    _name= 'client.model_client'
    name_client= fields.Char(string='Nombre')
    last_name_client= fields.Char(string='Apellido')
    phone_client=fields.Char(string='Telefono')
    email_client=fields.Char(string='E_Mail')
    vehicle_id=fields.One2many('client_vehicle.model_client','owner_vehicle_client_id', string='Registro de vehiculos')
    shift_finalized=fields.Integer(compute="shift_client", string='Finalizados')
    shift_cancelled=fields.Integer(compute='shift_client',string='Cancelados') 
    shift_list=fields.One2many('shift.model_shift', 'client_id', string='Turnos')

    def name_get(self):
        result=[]
        for client in self:
            name= client.name_client
            last_name= client.last_name_client
            complete_name= f"{name} {last_name}"
            result.append((client.id, complete_name))
        return result

    @api.depends('shift_list')
    def shift_client(self):
        self_env=self.env['shift.model_shift']
        for record in self:
            record.shift_finalized=self_env.search_count(['&',('client_id', '=', record.id), ('shift_status', '=', 'finalized')])
            record.shift_cancelled=self_env.search_count(['&', ('client_id', '=',record.id),('shift_status', '=', 'cancelled')])
            

    def action_view_cancelled(self):
        return{
            'name':'Cancelados'
        }

    def action_view_finalized(self):
        return{
            'name':'Finalizados'
        }