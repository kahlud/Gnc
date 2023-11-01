# -*- coding: utf-8 -*-
from odoo import models,fields 

class vehiculos(models.Model):
    _name='client_vehicle.model_client'
    patented_vehicle=fields.Char(string='Patente')
    brand_vehicle=fields.Char(string='Marca')
    model_vehicle=fields.Char(string='Modelo')
    year_vehicle= fields.Integer(string='Año')
    owner_vehicle_client_id= fields.Many2one('client.model_client', string='Dueño' )
    service_vehicle_id=fields.One2many("vehicle_service.model_vehicle_client", "vehicle_id", string="Servicio realizado")
    gnc=fields.Boolean(string='GNC')
    wafer_gas=fields.One2many("wafers.model_wafers", "wafers_of_the_month", string='Oblea')
    equipament= fields.Selection([('quinta', 'Quinta generacion'),('cuarta', 'Cuarta generacion'),('carburado','Carburado')], string='Tipo de equipo')
    brand_equipament=fields.Selection([('tomasetto','Tomasetto achille')])


    def name_get(self):
        result=[]
        for vehicles in self:
            owner = vehicles.owner_vehicle_client_id.name_get()
            owner_vehicle=owner[0][1]
            brand=vehicles.brand_vehicle
            patented=vehicles.patented_vehicle
            vehicle_complete=f"{owner_vehicle} / {brand} - {patented}"
            result.append((vehicles.id, vehicle_complete))
        return result