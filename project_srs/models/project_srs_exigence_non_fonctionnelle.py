from odoo import _, api, fields, models


class ProjectSrsExigenceNonFonctionnelle(models.Model):
    _name = "project.srs.exigence_non_fonctionnelle"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Exigence non-fonctionnelle"
    _order = "identifiant"

    name = fields.Char(
        string="Exigence",
        track_visibility="onchange",
        help=(
            "Les exigences non-fonctionnelles comprennent les fonctions de"
            " services du produit, veuillez vous référer aux critères de la"
            " section des caractéristiques de qualité."
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
        required=True,
        track_visibility="onchange",
        default="nouveau",
        help="État de l'avancement du requis.",
    )

    dev_note = fields.Html(string="Dev note", help="Note de développement pour comprendre le status.")

    note = fields.Text(track_visibility="onchange")

    srs = fields.Many2one(
        comodel_name="project.srs",
        string="SRS",
    )

    @api.depends("srs", "name")
    def _compute_identifiant(self):
        # TODO no need depends, how force compute when finish to create? Move this into create/write
        for rec in self:
            if not isinstance(rec.id, models.NewId):
                rec.identifiant = f"NON-{rec.id}"
            else:
                rec.identifiant = ""
