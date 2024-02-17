
from odoo import models, fields, api

class Heroe(models.Model):
    _name = 'heroes.heroe'
    _description = 'Personas que se van a disfrazar de heroes'
    _rec_name = 'nombre'

    nombre= fields.Char(string='Nombre',required=True)
    apellidos= fields.Char(string='Apellidos',required=True)
    nombreCompleto= fields.Char(string='Nombre Completo', compute='_nombre_completo')
    nombreHeroe= fields.Char(string='Heroe',required=True)
    id_persona= fields.Many2one('res.users',  string='Trabajador')
    @api.depends('nombre', 'apellidos')
    def _nombre_completo(self):
        for heroe in self:
         heroe.nombreCompleto= f"{heroe.nombre} {heroe.apellidos}"
