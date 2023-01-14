from odoo import _, api, fields, models


class ProjectSrsFctContrainte(models.Model):
    _name = "project.srs.fct_contrainte"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Fonction de contrainte"
    _order = "identifiant"

    active = fields.Boolean(default=True)

    identifiant = fields.Char(
        string="ID",
        track_visibility="onchange",
    )

    name = fields.Char(
        string="Contrainte",
        track_visibility="onchange",
        help=(
            "Les fonctions qui répondent à des attentes obligatoires (normes,"
            " textes de lois, brevets, …)"
        ),
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
        track_visibility="onchange",
        default="nouveau",
        help="État de l'avancement du requis.",
    )

    project_srs = fields.Many2one(
        string="SRS",
        comodel_name="project.srs",
    )

    reference = fields.Text(
        string="Référence",
        track_visibility="onchange",
    )
