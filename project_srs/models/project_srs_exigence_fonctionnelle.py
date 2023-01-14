from odoo import _, api, fields, models


class ProjectSrsExigenceFonctionnelle(models.Model):
    _name = "project.srs.exigence_fonctionnelle"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Exigence fonctionnelle"
    _order = "identifiant"
    _rec_name = "nom_complet"

    categorie = fields.Many2one(
        string="Catégorie",
        comodel_name="project.srs.exigence_fonctionnelle.categorie",
    )

    identifiant = fields.Char(
        string="ID",
        track_visibility="onchange",
    )

    importance = fields.Selection(
        selection=[
            ("triviale", "Triviale"),
            ("basse", "Basse"),
            ("normale", "Normale"),
            ("elevee", "Élevée"),
        ],
        track_visibility="onchange",
        default="normale",
    )

    composante = fields.Many2many(
        comodel_name="project.srs.exigence_fonctionnelle.composante",
        relation="project_srs_exi_fonc_compo_rel",
    )

    name = fields.Char(
        string="Exigence",
        track_visibility="onchange",
    )

    active = fields.Boolean(default=True)

    nom_complet = fields.Char(
        string="Nom complet",
        compute="_compute_nom_complet",
        store=True,
    )

    note = fields.Text(track_visibility="onchange")

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

    srs = fields.Many2one(
        string="SRS",
        comodel_name="project.srs",
    )

    srs_depend = fields.Many2many(
        string="Dépend de",
        comodel_name="project.srs.exigence_fonctionnelle",
        relation="depend_srs_rel",
        column1="srs_depend",
        colomn2="project_srs_exigence_fonctionnelle_id",
    )

    srs_depended = fields.Many2many(
        string="Est dépendant de",
        comodel_name="project.srs.exigence_fonctionnelle",
        relation="depend_srs_rel",
        column1="project_srs_exigence_fonctionnelle_id",
        colomn2="srs_depend",
        readonly=True,
    )

    srs_relate = fields.Many2many(
        string="Est en relation avec",
        comodel_name="project.srs.exigence_fonctionnelle",
        relation="related_srs_rel",
        column1="srs_relate",
        colomn2="project_srs_exigence_fonctionnelle_id",
    )

    srs_related = fields.Many2many(
        string="Est relié à",
        comodel_name="project.srs.exigence_fonctionnelle",
        relation="related_srs_rel",
        column1="project_srs_exigence_fonctionnelle_id",
        colomn2="srs_relate",
        readonly=True,
    )

    feature_url = fields.Char(string="URL de la fonctionnalité")

    @api.depends("name", "identifiant")
    def _compute_nom_complet(self):
        for rec in self:
            rec.nom_complet = False
            if rec.name and rec.identifiant:
                rec.nom_complet = f"{rec.identifiant} {rec.name}"
            elif rec.name:
                rec.nom_complet = f"{rec.name}"
            elif rec.identifiant:
                rec.nom_complet = f"{rec.identifiant}"
