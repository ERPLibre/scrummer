from odoo import _, api, fields, models


class ProjectSrsExigenceStatus(models.Model):
    _name = "project.srs.exigence_status"
    _description = "project_srs_exigence_status"

    name = fields.Char()
