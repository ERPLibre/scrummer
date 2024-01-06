from odoo import _, api, fields, models


class ProjectSrsExigenceFonctionnelleCategorie(models.Model):
    _name = "project.srs.exigence_fonctionnelle.categorie"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Catégorie exigence fonctionnelle"
    _order = "sequence"

    name = fields.Char(
        string="Nom",
        track_visibility="onchange",
    )

    exigence_fonctionnelle = fields.One2many(
        comodel_name="project.srs.exigence_fonctionnelle",
        inverse_name="categorie",
        string="Exigence fonctionnelle",
    )

    active = fields.Boolean(default=True)

    description = fields.Text(track_visibility="onchange")

    sequence = fields.Integer(
        string="Séquence",
        track_visibility="onchange",
        default=10,
    )
