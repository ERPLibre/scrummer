from odoo import _, api, fields, models


class ProjectSrs(models.Model):
    _name = "project.srs"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Expression"

    name = fields.Char(
        string="Nom",
        track_visibility="onchange",
    )

    analyse_non_fonctionnelle = fields.One2many(
        comodel_name="project.srs.analyse_non_fonctionnelle",
        inverse_name="srs",
        string="Analyse non-fonctionnelle",
    )

    exigence_fonctionnelle = fields.One2many(
        comodel_name="project.srs.exigence_fonctionnelle",
        inverse_name="srs",
        string="Exigence fonctionnelle",
    )

    exigence_non_fonctionnelle = fields.One2many(
        comodel_name="project.srs.exigence_non_fonctionnelle",
        inverse_name="srs",
        string="Exigence non-fonctionnelle",
    )

    lexique = fields.Html(help="Lexique dans le document. TODO faire une structure du mot exact avec définition ou traduction.")

    fct_contrainte_ids = fields.One2many(
        comodel_name="project.srs.fct_contrainte",
        inverse_name="project_srs",
        string="Fonction de contrainte",
    )

    role = fields.One2many(
        comodel_name="project.srs.role",
        inverse_name="srs",
        string="Rôle",
    )

    active = fields.Boolean(default=True)

    dans_quel_but = fields.Html(
        string="Dans quel but?",
        track_visibility="onchange",
        help="Validation",
    )

    pourquoi_besoin_existe = fields.Html(
        string="Pourquoi le besoin existe-t-il?",
        track_visibility="onchange",
        help="Validation",
    )

    qui_pourrait_faire_evoluer_besoin = fields.Html(
        string="Qu'est-ce qui pourrait faire évoluer le besoin?",
        track_visibility="onchange",
        help="Validation",
    )

    quoi_pourrait_faire_disparaitre = fields.Html(
        string=(
            "Qu'est-ce qui pourrait faire disparaître (remettre en cause) le"
            " besoin?"
        ),
        track_visibility="onchange",
        help="Validation",
    )

    quoi_produit_agit = fields.Html(
        string="Sur qui, quoi le produit agit-il?",
        track_visibility="onchange",
        help="Validation",
    )

    definition = fields.Html(
        string="Définition",
        track_visibility="onchange",
    )

    qui_rend_service = fields.Html(
        string="À qui le produit rend-il service?",
        track_visibility="onchange",
        help="Validation",
    )
