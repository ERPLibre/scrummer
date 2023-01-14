from odoo import _, api, fields, models


class ProjectSrsRole(models.Model):
    _name = "project.srs.role"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Rôles"
    _order = "sequence"

    active = fields.Boolean(default=True)

    description = fields.Text(track_visibility="onchange")

    name = fields.Char(
        string="Rôle",
        track_visibility="onchange",
    )

    sequence = fields.Integer(
        string="Séquence",
        track_visibility="onchange",
        default=10,
    )

    srs = fields.Many2one(
        string="SRS",
        comodel_name="project.srs",
    )
