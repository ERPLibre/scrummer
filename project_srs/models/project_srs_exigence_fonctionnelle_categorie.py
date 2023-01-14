from odoo import _, api, fields, models


class ProjectSrsExigenceFonctionnelleCategorie(models.Model):
    _name = "project.srs.exigence_fonctionnelle.categorie"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Catégorie exigence fonctionnelle"
    _order = "sequence"

    exigence_fonctionnelle = fields.One2many(
        string="Exigence fonctionnelle",
        comodel_name="project.srs.exigence_fonctionnelle",
        inverse_name="categorie",
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
