# -*- coding: utf-8 -*-
# © <2016> <Felipe Fernandes>
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl).

from openerp import models, fields, api

class Course(models.Model):

    _name = "course.openacademy"
    description = "Cursos"

    name = fields.Char(string="Nome do Curso", required=True)

    description = fields.Text(string="Descrição")

    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="Coordenador",
                                     index=True)
    session_ids = fields.One2many('session.openacademy',
                                  'course_id', string="Aulas")

class Session(models.Model):

    _name = "session.openacademy"
    _description = "Aulas"

    name = fields.Char(string="Nome da Aula", required=True)
    start_date = fields.Date(default=fields.Date.today, string="Data Inicio")
    end_date = fields.Date(string="Data Fim")

    duration = fields.Float(help="Duração em dias")

    seats = fields.Integer(string="Numero de vagas")

    description = fields.Text(string="Descrição")

    instructor_id = fields.Many2one('res.partner', string="Instrutor",
                                    domain=[("is_instructor", "=", True)])

    course_id = fields.Many2one('course.openacademy',
                                ondelete='cascade', string="Curso",
                                required=True)

    attendee_ids = fields.One2many(
        'attendee.openacademy', 'session_id', string="Alunos"
    )

class Attendee(models.Model):

    _name = "attendee.openacademy"
    _description = "Alunos"

    name = fields.Char(string="Alunos")

    description = fields.Text(string="Descrição")

    partner_id = fields.Many2one('res.partner', string="Parceiros")
    session_id = fields.Many2one('session.openacademy',
                                 ondelete='cascade', string="Aula")

class Partner(models.Model):
    _inherit = "res.partner"

    _description = "Instrutores"

    is_instructor = fields.Boolean("Instrutores", default=False)
    courses_id = fields.One2many("session.openacademy","instructor_id", ondelete="set Null", string="Aulas")