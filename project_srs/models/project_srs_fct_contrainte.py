from odoo import _, api, fields, models


class ProjectSrsFctContrainte(models.Model):
    _name = "project.srs.fct_contrainte"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Fonction de contrainte"
    _order = "identifiant"

    name = fields.Char(
        string="Contrainte",
        track_visibility="onchange",
        help=(
            "Les fonctions qui répondent à des attentes obligatoires (normes,"
            " textes de lois, brevets, …)"
        ),
    )

    active = fields.Boolean(default=True)

    identifiant = fields.Char(
        string="Key",
        compute="_compute_identifiant",
        store=True,
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
        track_visibility="onchange",
        default="nouveau",
        help="État de l'avancement du requis.",
    )

    dev_note = fields.Html(string="Dev note", help="Note de développement pour comprendre le status.")

    project_srs = fields.Many2one(
        comodel_name="project.srs",
        string="SRS",
    )

    reference = fields.Text(
        string="Référence",
        track_visibility="onchange",
    )

    @api.depends("project_srs", "name")
    def _compute_identifiant(self):
        for rec in self:
            if not isinstance(rec.id, models.NewId):
                rec.identifiant = f"FCTC-{rec.id}"
            else:
                rec.identifiant = ""
