from odoo import _, api, fields, models


class ProjectSrsExigenceFonctionnelleComposante(models.Model):
    _name = "project.srs.exigence_fonctionnelle.composante"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Composante exigence fonctionnelle"
    _order = "sequence"

    exigence_fonctionnelle = fields.Many2many(
        string="Exigence fonctionnelle",
        comodel_name="project.srs.exigence_fonctionnelle",
        relation="project_srs_exi_fonc_compo_rel",
    )

    active = fields.Boolean(default=True)

    description = fields.Text(track_visibility="onchange")

    name = fields.Char(
        string="Nom",
        track_visibility="onchange",
    )

    sequence = fields.Integer(
        string="Séquence",
        track_visibility="onchange",
        default=10,
    )
