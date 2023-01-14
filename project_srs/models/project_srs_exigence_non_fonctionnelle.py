from odoo import _, api, fields, models


class ProjectSrsExigenceNonFonctionnelle(models.Model):
    _name = "project.srs.exigence_non_fonctionnelle"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Exigence non-fonctionnelle"
    _order = "identifiant"

    active = fields.Boolean(default=True)

    identifiant = fields.Char(
        string="ID",
        track_visibility="onchange",
    )

    etat = fields.Selection(
        selection=[
            ("nouveau", "Nouveau"),
            ("en conception", "En conception"),
            ("en developpement", "En développement"),
            ("a valide", "À valider"),
            ("termine", "Terminé"),
        ],
        string="État",
        required=True,
        track_visibility="onchange",
        default="nouveau",
        help="État de l'avancement du requis.",
    )

    name = fields.Char(
        string="Exigence",
        track_visibility="onchange",
        help=(
            "Les exigences non-fonctionnelles comprennent les fonctions de"
            " services du produit, veuillez vous référer aux critères de la"
            " section des caractéristiques de qualité."
        ),
    )

    note = fields.Text(track_visibility="onchange")

    srs = fields.Many2one(
        string="SRS",
        comodel_name="project.srs",
    )
