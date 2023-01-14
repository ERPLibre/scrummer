from odoo import _, api, fields, models


class ProjectSrsAnalyseNonFonctionnelle(models.Model):
    _name = "project.srs.analyse_non_fonctionnelle"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Analyse non-fonctionnelle"
    _order = "sequence"

    cas = fields.Text(
        track_visibility="onchange",
        help="- Raison du choix - Mesure",
    )

    importance = fields.Selection(
        selection=[("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5")],
        track_visibility="onchange",
        help="1 pour moins important, 5 pour plus important.",
    )

    active = fields.Boolean(default=True)

    name = fields.Char(
        string="Caractéristique",
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
