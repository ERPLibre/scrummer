import os

from odoo import SUPERUSER_ID, _, api, fields, models

MODULE_NAME = "project_srs"


def post_init_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})

        # The path of the actual file
        path_module_generate = os.path.normpath(
            os.path.join(
                os.path.dirname(__file__),
                "..",
                "..",
                "MathBenTech_scrummer",
            )
        )

        short_name = MODULE_NAME.replace("_", " ").title()

        # Add code generator
        categ_id = env["ir.module.category"].search(
            [("name", "=", "Project")], limit=1
        )
        value = {
            "shortdesc": short_name,
            "name": MODULE_NAME,
            "license": "AGPL-3",
            "category_id": categ_id.id,
            "summary": "",
            "author": "TechnoLibre",
            "website": "https://technolibre.ca",
            "application": True,
            "enable_sync_code": True,
            "path_sync_code": path_module_generate,
            "icon": os.path.join(
                os.path.dirname(__file__),
                "static",
                "description",
                "code_generator_icon.png",
            ),
        }

        # TODO HUMAN: enable your functionality to generate
        value["enable_sync_template"] = True
        value["ignore_fields"] = ""
        value["post_init_hook_show"] = False
        value["uninstall_hook_show"] = False
        value["post_init_hook_feature_code_generator"] = False
        value["uninstall_hook_feature_code_generator"] = False

        value["hook_constant_code"] = f'MODULE_NAME = "{MODULE_NAME}"'

        code_generator_id = env["code.generator.module"].create(value)

        # Add Project Srs
        value = {
            "name": "project_srs",
            "description": "Expression",
            "model": "project.srs",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs = env["ir.model"].create(value)

        # Module dependency
        code_generator_id.add_module_dependency("mail")

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs.add_model_inherit(lst_depend_model)

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs",
            "field_description": "Active",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_dans_quel_but = {
            "name": "dans_quel_but",
            "model": "project.srs",
            "field_description": "Dans quel but?",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 15,
            "code_generator_tree_view_sequence": 14,
            "ttype": "text",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
            "help": "Validation",
        }
        env["ir.model.fields"].create(value_field_dans_quel_but)

        value_field_definition = {
            "name": "definition",
            "model": "project.srs",
            "field_description": "Définition",
            "code_generator_sequence": 14,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "text",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_definition)

        value_field_name = {
            "name": "name",
            "model": "project.srs",
            "field_description": "Nom",
            "code_generator_sequence": 15,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_pourquoi_besoin_existe = {
            "name": "pourquoi_besoin_existe",
            "model": "project.srs",
            "field_description": "Pourquoi le besoin existe-t-il?",
            "code_generator_sequence": 10,
            "code_generator_form_simple_view_sequence": 17,
            "code_generator_tree_view_sequence": 16,
            "ttype": "text",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
            "help": "Validation",
        }
        env["ir.model.fields"].create(value_field_pourquoi_besoin_existe)

        value_field_qui_pourrait_faire_evoluer_besoin = {
            "name": "qui_pourrait_faire_evoluer_besoin",
            "model": "project.srs",
            "field_description": (
                "Qu'est-ce qui pourrait faire évoluer le besoin?"
            ),
            "code_generator_sequence": 11,
            "code_generator_form_simple_view_sequence": 18,
            "code_generator_tree_view_sequence": 17,
            "ttype": "text",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
            "help": "Validation",
        }
        env["ir.model.fields"].create(
            value_field_qui_pourrait_faire_evoluer_besoin
        )

        value_field_qui_rend_service = {
            "name": "qui_rend_service",
            "model": "project.srs",
            "field_description": "À qui le produit rend-il service?",
            "code_generator_sequence": 16,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "text",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
            "help": "Validation",
        }
        env["ir.model.fields"].create(value_field_qui_rend_service)

        value_field_quoi_pourrait_faire_disparaitre = {
            "name": "quoi_pourrait_faire_disparaitre",
            "model": "project.srs",
            "field_description": (
                "Qu'est-ce qui pourrait faire disparaître (remettre en cause)"
                " le besoin?"
            ),
            "code_generator_sequence": 12,
            "code_generator_form_simple_view_sequence": 16,
            "code_generator_tree_view_sequence": 15,
            "ttype": "text",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
            "help": "Validation",
        }
        env["ir.model.fields"].create(
            value_field_quoi_pourrait_faire_disparaitre
        )

        value_field_quoi_produit_agit = {
            "name": "quoi_produit_agit",
            "model": "project.srs",
            "field_description": "Sur qui, quoi le produit agit-il?",
            "code_generator_sequence": 13,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 13,
            "ttype": "text",
            "model_id": model_project_srs.id,
            "track_visibility": "onchange",
            "help": "Validation",
        }
        env["ir.model.fields"].create(value_field_quoi_produit_agit)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [("model_id", "=", model_project_srs.id), ("name", "=", "x_name")]
        )
        model_project_srs.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Srs Role
        value = {
            "name": "project_srs_role",
            "description": "Rôles",
            "model": "project.srs.role",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs_role = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs_role.add_model_inherit(lst_depend_model)

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs.role",
            "field_description": "Active",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs_role.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_description = {
            "name": "description",
            "model": "project.srs.role",
            "field_description": "Description",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "text",
            "model_id": model_project_srs_role.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_description)

        value_field_name = {
            "name": "name",
            "model": "project.srs.role",
            "field_description": "Rôle",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_srs_role.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.srs.role",
            "field_description": "Séquence",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "integer",
            "model_id": model_project_srs_role.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        value_field_srs = {
            "name": "srs",
            "model": "project.srs.role",
            "field_description": "SRS",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 13,
            "ttype": "many2one",
            "relation": "project.srs",
            "model_id": model_project_srs_role.id,
        }
        env["ir.model.fields"].create(value_field_srs)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_srs_role.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_srs_role.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Srs Analyse Non Fonctionnelle
        value = {
            "name": "project_srs_analyse_non_fonctionnelle",
            "description": "Analyse non-fonctionnelle",
            "model": "project.srs.analyse_non_fonctionnelle",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs_analyse_non_fonctionnelle = env["ir.model"].create(
            value
        )

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs_analyse_non_fonctionnelle.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs.analyse_non_fonctionnelle",
            "field_description": "Active",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs_analyse_non_fonctionnelle.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_cas = {
            "name": "cas",
            "model": "project.srs.analyse_non_fonctionnelle",
            "field_description": "Cas",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "text",
            "model_id": model_project_srs_analyse_non_fonctionnelle.id,
            "track_visibility": "onchange",
            "help": "- Raison du choix - Mesure",
        }
        env["ir.model.fields"].create(value_field_cas)

        value_field_importance = {
            "name": "importance",
            "model": "project.srs.analyse_non_fonctionnelle",
            "field_description": "Importance",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "selection",
            "selection": (
                "[('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5')]"
            ),
            "model_id": model_project_srs_analyse_non_fonctionnelle.id,
            "track_visibility": "onchange",
            "help": "1 pour moins important, 5 pour plus important.",
        }
        env["ir.model.fields"].create(value_field_importance)

        value_field_name = {
            "name": "name",
            "model": "project.srs.analyse_non_fonctionnelle",
            "field_description": "Caractéristique",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_srs_analyse_non_fonctionnelle.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.srs.analyse_non_fonctionnelle",
            "field_description": "Séquence",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 13,
            "ttype": "integer",
            "model_id": model_project_srs_analyse_non_fonctionnelle.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        value_field_srs = {
            "name": "srs",
            "model": "project.srs.analyse_non_fonctionnelle",
            "field_description": "SRS",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 15,
            "code_generator_tree_view_sequence": 14,
            "ttype": "many2one",
            "relation": "project.srs",
            "model_id": model_project_srs_analyse_non_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_srs)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                (
                    "model_id",
                    "=",
                    model_project_srs_analyse_non_fonctionnelle.id,
                ),
                ("name", "=", "x_name"),
            ]
        )
        model_project_srs_analyse_non_fonctionnelle.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Srs Exigence Non Fonctionnelle
        value = {
            "name": "project_srs_exigence_non_fonctionnelle",
            "description": "Exigence non-fonctionnelle",
            "model": "project.srs.exigence_non_fonctionnelle",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs_exigence_non_fonctionnelle = env["ir.model"].create(
            value
        )

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs_exigence_non_fonctionnelle.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs.exigence_non_fonctionnelle",
            "field_description": "Active",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs_exigence_non_fonctionnelle.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_etat = {
            "name": "etat",
            "model": "project.srs.exigence_non_fonctionnelle",
            "field_description": "État",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "selection",
            "selection": (
                "[('nouveau', 'Nouveau'), ('en conception', 'En conception'),"
                " ('en developpement', 'En développement'), ('a valide', 'À"
                " valider'), ('termine', 'Terminé')]"
            ),
            "model_id": model_project_srs_exigence_non_fonctionnelle.id,
            "default": "nouveau",
            "track_visibility": "onchange",
            "required": True,
            "help": "État de l'avancement du requis.",
        }
        env["ir.model.fields"].create(value_field_etat)

        value_field_identifiant = {
            "name": "identifiant",
            "model": "project.srs.exigence_non_fonctionnelle",
            "field_description": "ID",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "char",
            "model_id": model_project_srs_exigence_non_fonctionnelle.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_identifiant)

        value_field_name = {
            "name": "name",
            "model": "project.srs.exigence_non_fonctionnelle",
            "field_description": "Exigence",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "char",
            "model_id": model_project_srs_exigence_non_fonctionnelle.id,
            "track_visibility": "onchange",
            "help": (
                "Les exigences non-fonctionnelles comprennent les fonctions de"
                " services du produit, veuillez vous référer aux critères de"
                " la section des caractéristiques de qualité."
            ),
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_note = {
            "name": "note",
            "model": "project.srs.exigence_non_fonctionnelle",
            "field_description": "Note",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 13,
            "ttype": "text",
            "model_id": model_project_srs_exigence_non_fonctionnelle.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_note)

        value_field_srs = {
            "name": "srs",
            "model": "project.srs.exigence_non_fonctionnelle",
            "field_description": "SRS",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 15,
            "code_generator_tree_view_sequence": 14,
            "ttype": "many2one",
            "relation": "project.srs",
            "model_id": model_project_srs_exigence_non_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_srs)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                (
                    "model_id",
                    "=",
                    model_project_srs_exigence_non_fonctionnelle.id,
                ),
                ("name", "=", "x_name"),
            ]
        )
        model_project_srs_exigence_non_fonctionnelle.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Srs Exigence Fonctionnelle
        value = {
            "name": "project_srs_exigence_fonctionnelle",
            "description": "Exigence fonctionnelle",
            "model": "project.srs.exigence_fonctionnelle",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs_exigence_fonctionnelle = env["ir.model"].create(
            value
        )

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs_exigence_fonctionnelle.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Active",
            "code_generator_sequence": 10,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_categorie = {
            "name": "categorie",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Catégorie",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 15,
            "code_generator_tree_view_sequence": 14,
            "ttype": "many2one",
            "relation": "project.srs.exigence_fonctionnelle.categorie",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_categorie)

        value_field_composante = {
            "name": "composante",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Composante",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 16,
            "code_generator_tree_view_sequence": 15,
            "force_widget": "many2many_tags",
            "ttype": "many2many",
            "relation": "project.srs.exigence_fonctionnelle.composante",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_composante)

        value_field_etat = {
            "name": "etat",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "État",
            "code_generator_sequence": 13,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "selection",
            "selection": (
                "[('nouveau', 'Nouveau'), ('en conception', 'En conception'),"
                " ('en developpement', 'En développement'), ('a valide', 'À"
                " valider'), ('termine', 'Terminé')]"
            ),
            "model_id": model_project_srs_exigence_fonctionnelle.id,
            "default": "nouveau",
            "track_visibility": "onchange",
            "help": "État de l'avancement du requis.",
        }
        env["ir.model.fields"].create(value_field_etat)

        value_field_feature_url = {
            "name": "feature_url",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "URL de la fonctionnalité",
            "code_generator_sequence": 19,
            "code_generator_form_simple_view_sequence": 18,
            "code_generator_tree_view_sequence": 17,
            "force_widget": "link_button",
            "ttype": "char",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_feature_url)

        value_field_identifiant = {
            "name": "identifiant",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "ID",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "char",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_identifiant)

        value_field_importance = {
            "name": "importance",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Importance",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 13,
            "ttype": "selection",
            "selection": (
                "[('triviale', 'Triviale'), ('basse', 'Basse'), ('normale',"
                " 'Normale'), ('elevee', 'Élevée')]"
            ),
            "model_id": model_project_srs_exigence_fonctionnelle.id,
            "default": "normale",
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_importance)

        value_field_name = {
            "name": "name",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Exigence",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "char",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_nom_complet = {
            "name": "nom_complet",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Nom complet",
            "code_generator_sequence": 11,
            "ttype": "char",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
            "store": True,
            "code_generator_compute": "_compute_nom_complet",
        }
        env["ir.model.fields"].create(value_field_nom_complet)

        value_field_note = {
            "name": "note",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Note",
            "code_generator_sequence": 12,
            "code_generator_form_simple_view_sequence": 17,
            "code_generator_tree_view_sequence": 16,
            "ttype": "text",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_note)

        value_field_srs = {
            "name": "srs",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "SRS",
            "code_generator_sequence": 14,
            "code_generator_form_simple_view_sequence": 23,
            "code_generator_tree_view_sequence": 22,
            "ttype": "many2one",
            "relation": "project.srs",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_srs)

        value_field_srs_depend = {
            "name": "srs_depend",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Dépend de",
            "code_generator_sequence": 15,
            "code_generator_form_simple_view_sequence": 19,
            "code_generator_tree_view_sequence": 18,
            "force_widget": "many2many_tags",
            "ttype": "many2many",
            "relation": "project.srs.exigence_fonctionnelle",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_srs_depend)

        value_field_srs_depended = {
            "name": "srs_depended",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Est dépendant de",
            "code_generator_sequence": 16,
            "code_generator_form_simple_view_sequence": 20,
            "code_generator_tree_view_sequence": 19,
            "force_widget": "many2many_tags",
            "ttype": "many2many",
            "relation": "project.srs.exigence_fonctionnelle",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_srs_depended)

        value_field_srs_relate = {
            "name": "srs_relate",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Est en relation avec",
            "code_generator_sequence": 17,
            "code_generator_form_simple_view_sequence": 21,
            "code_generator_tree_view_sequence": 20,
            "force_widget": "many2many_tags",
            "ttype": "many2many",
            "relation": "project.srs.exigence_fonctionnelle",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_srs_relate)

        value_field_srs_related = {
            "name": "srs_related",
            "model": "project.srs.exigence_fonctionnelle",
            "field_description": "Est relié à",
            "code_generator_sequence": 18,
            "code_generator_form_simple_view_sequence": 22,
            "code_generator_tree_view_sequence": 21,
            "force_widget": "many2many_tags",
            "ttype": "many2many",
            "relation": "project.srs.exigence_fonctionnelle",
            "model_id": model_project_srs_exigence_fonctionnelle.id,
        }
        env["ir.model.fields"].create(value_field_srs_related)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_srs_exigence_fonctionnelle.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_srs_exigence_fonctionnelle.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Srs Exigence Fonctionnelle Categorie
        value = {
            "name": "project_srs_exigence_fonctionnelle_categorie",
            "description": "Catégorie exigence fonctionnelle",
            "model": "project.srs.exigence_fonctionnelle.categorie",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs_exigence_fonctionnelle_categorie = env[
            "ir.model"
        ].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs_exigence_fonctionnelle_categorie.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs.exigence_fonctionnelle.categorie",
            "field_description": "Active",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs_exigence_fonctionnelle_categorie.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_description = {
            "name": "description",
            "model": "project.srs.exigence_fonctionnelle.categorie",
            "field_description": "Description",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "text",
            "model_id": model_project_srs_exigence_fonctionnelle_categorie.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_description)

        value_field_name = {
            "name": "name",
            "model": "project.srs.exigence_fonctionnelle.categorie",
            "field_description": "Nom",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_srs_exigence_fonctionnelle_categorie.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.srs.exigence_fonctionnelle.categorie",
            "field_description": "Séquence",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "integer",
            "model_id": model_project_srs_exigence_fonctionnelle_categorie.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                (
                    "model_id",
                    "=",
                    model_project_srs_exigence_fonctionnelle_categorie.id,
                ),
                ("name", "=", "x_name"),
            ]
        )
        model_project_srs_exigence_fonctionnelle_categorie.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Srs Fct Contrainte
        value = {
            "name": "project_srs_fct_contrainte",
            "description": "Fonction de contrainte",
            "model": "project.srs.fct_contrainte",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs_fct_contrainte = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs_fct_contrainte.add_model_inherit(lst_depend_model)

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs.fct_contrainte",
            "field_description": "Active",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs_fct_contrainte.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_etat = {
            "name": "etat",
            "model": "project.srs.fct_contrainte",
            "field_description": "État",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "selection",
            "selection": (
                "[('nouveau', 'Nouveau'), ('en conception', 'En conception'),"
                " ('en developpement', 'En développement'), ('a valide', 'À"
                " valider'), ('termine', 'Terminé')]"
            ),
            "model_id": model_project_srs_fct_contrainte.id,
            "default": "nouveau",
            "track_visibility": "onchange",
            "help": "État de l'avancement du requis.",
        }
        env["ir.model.fields"].create(value_field_etat)

        value_field_identifiant = {
            "name": "identifiant",
            "model": "project.srs.fct_contrainte",
            "field_description": "ID",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "char",
            "model_id": model_project_srs_fct_contrainte.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_identifiant)

        value_field_name = {
            "name": "name",
            "model": "project.srs.fct_contrainte",
            "field_description": "Contrainte",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "char",
            "model_id": model_project_srs_fct_contrainte.id,
            "track_visibility": "onchange",
            "help": (
                "Les fonctions qui répondent à des attentes obligatoires"
                " (normes, textes de lois, brevets, …)"
            ),
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_project_srs = {
            "name": "project_srs",
            "model": "project.srs.fct_contrainte",
            "field_description": "SRS",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 15,
            "code_generator_tree_view_sequence": 14,
            "ttype": "many2one",
            "relation": "project.srs",
            "model_id": model_project_srs_fct_contrainte.id,
        }
        env["ir.model.fields"].create(value_field_project_srs)

        value_field_reference = {
            "name": "reference",
            "model": "project.srs.fct_contrainte",
            "field_description": "Référence",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 13,
            "ttype": "text",
            "model_id": model_project_srs_fct_contrainte.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_reference)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_srs_fct_contrainte.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_srs_fct_contrainte.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Srs Exigence Fonctionnelle Composante
        value = {
            "name": "project_srs_exigence_fonctionnelle_composante",
            "description": "Composante exigence fonctionnelle",
            "model": "project.srs.exigence_fonctionnelle.composante",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_srs_exigence_fonctionnelle_composante = env[
            "ir.model"
        ].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_srs_exigence_fonctionnelle_composante.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_active = {
            "name": "active",
            "model": "project.srs.exigence_fonctionnelle.composante",
            "field_description": "Active",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 10,
            "force_widget": "boolean_button",
            "ttype": "boolean",
            "model_id": model_project_srs_exigence_fonctionnelle_composante.id,
            "default": True,
        }
        env["ir.model.fields"].create(value_field_active)

        value_field_description = {
            "name": "description",
            "model": "project.srs.exigence_fonctionnelle.composante",
            "field_description": "Description",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 11,
            "ttype": "text",
            "model_id": model_project_srs_exigence_fonctionnelle_composante.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_description)

        value_field_exigence_fonctionnelle = {
            "name": "exigence_fonctionnelle",
            "model": "project.srs.exigence_fonctionnelle.composante",
            "field_description": "Exigence fonctionnelle",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 13,
            "ttype": "many2many",
            "relation": "project.srs.exigence_fonctionnelle",
            "model_id": model_project_srs_exigence_fonctionnelle_composante.id,
        }
        env["ir.model.fields"].create(value_field_exigence_fonctionnelle)

        value_field_name = {
            "name": "name",
            "model": "project.srs.exigence_fonctionnelle.composante",
            "field_description": "Nom",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_srs_exigence_fonctionnelle_composante.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.srs.exigence_fonctionnelle.composante",
            "field_description": "Séquence",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 12,
            "ttype": "integer",
            "model_id": model_project_srs_exigence_fonctionnelle_composante.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                (
                    "model_id",
                    "=",
                    model_project_srs_exigence_fonctionnelle_composante.id,
                ),
                ("name", "=", "x_name"),
            ]
        )
        model_project_srs_exigence_fonctionnelle_composante.rec_name = "name"
        field_x_name.unlink()

        # Added one2many field, many2many need to be create before add one2many
        value_field_analyse_non_fonctionnelle = {
            "name": "analyse_non_fonctionnelle",
            "model": "project.srs",
            "field_description": "Analyse non-fonctionnelle",
            "ttype": "one2many",
            "relation": "project.srs.analyse_non_fonctionnelle",
            "relation_field": "srs",
            "model_id": model_project_srs.id,
        }
        env["ir.model.fields"].create(value_field_analyse_non_fonctionnelle)

        value_field_exigence_fonctionnelle = {
            "name": "exigence_fonctionnelle",
            "model": "project.srs",
            "field_description": "Exigence fonctionnelle",
            "ttype": "one2many",
            "relation": "project.srs.exigence_fonctionnelle",
            "relation_field": "srs",
            "model_id": model_project_srs.id,
        }
        env["ir.model.fields"].create(value_field_exigence_fonctionnelle)

        value_field_exigence_non_fonctionnelle = {
            "name": "exigence_non_fonctionnelle",
            "model": "project.srs",
            "field_description": "Exigence non-fonctionnelle",
            "ttype": "one2many",
            "relation": "project.srs.exigence_non_fonctionnelle",
            "relation_field": "srs",
            "model_id": model_project_srs.id,
        }
        env["ir.model.fields"].create(value_field_exigence_non_fonctionnelle)

        value_field_fct_contrainte_ids = {
            "name": "fct_contrainte_ids",
            "model": "project.srs",
            "field_description": "Fonction de contrainte",
            "ttype": "one2many",
            "relation": "project.srs.fct_contrainte",
            "relation_field": "project_srs",
            "model_id": model_project_srs.id,
        }
        env["ir.model.fields"].create(value_field_fct_contrainte_ids)

        value_field_role = {
            "name": "role",
            "model": "project.srs",
            "field_description": "Rôle",
            "ttype": "one2many",
            "relation": "project.srs.role",
            "relation_field": "srs",
            "model_id": model_project_srs.id,
        }
        env["ir.model.fields"].create(value_field_role)

        value_field_exigence_fonctionnelle = {
            "name": "exigence_fonctionnelle",
            "model": "project.srs.exigence_fonctionnelle.categorie",
            "field_description": "Exigence fonctionnelle",
            "ttype": "one2many",
            "relation": "project.srs.exigence_fonctionnelle",
            "relation_field": "categorie",
            "model_id": model_project_srs_exigence_fonctionnelle_categorie.id,
        }
        env["ir.model.fields"].create(value_field_exigence_fonctionnelle)

        ##### End Field

        # Generate view
        # Action generate view
        wizard_view = env["code.generator.generate.views.wizard"].create(
            {
                "code_generator_id": code_generator_id.id,
                "enable_generate_all": True,
            }
        )

        wizard_view.button_generate_views()

        # Generate module
        value = {"code_generator_ids": code_generator_id.ids}
        env["code.generator.writer"].create(value)


def uninstall_hook(cr, e):
    with api.Environment.manage():
        env = api.Environment(cr, SUPERUSER_ID, {})
        code_generator_id = env["code.generator.module"].search(
            [("name", "=", MODULE_NAME)]
        )
        if code_generator_id:
            code_generator_id.unlink()
