import os

from odoo import SUPERUSER_ID, _, api, fields, models

MODULE_NAME = "project_workflow_design"


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

        # Add Project Workflow Design
        value = {
            "name": "project_workflow_design",
            "description": "Project workflow design",
            "model": "project.workflow.design",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design = env["ir.model"].create(value)

        # Module dependency
        code_generator_id.add_module_dependency("mail")

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design.add_model_inherit(lst_depend_model)

        ##### Begin Field
        value_field_link_wire_frame = {
            "name": "link_wire_frame",
            "model": "project.workflow.design",
            "field_description": "Lien vers design externe",
            "code_generator_sequence": 10,
            "code_generator_form_simple_view_sequence": 11,
            "force_widget": "link_button",
            "ttype": "char",
            "model_id": model_project_workflow_design.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_link_wire_frame)

        value_field_name = {
            "name": "name",
            "model": "project.workflow.design",
            "field_description": "Nom",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 16,
            "ttype": "char",
            "model_id": model_project_workflow_design.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_workflow_design.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Faiblesse
        value = {
            "name": "project_workflow_design_faiblesse",
            "description": "Project workflow design faiblesse",
            "model": "project.workflow.design.faiblesse",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design_faiblesse = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_faiblesse.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.faiblesse",
            "field_description": "Faiblesse",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_faiblesse.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_project_workflow_design = {
            "name": "project_workflow_design",
            "model": "project.workflow.design.faiblesse",
            "field_description": "Project Workflow Design",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 12,
            "ttype": "many2one",
            "relation": "project.workflow.design",
            "model_id": model_project_workflow_design_faiblesse.id,
        }
        env["ir.model.fields"].create(value_field_project_workflow_design)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.workflow.design.faiblesse",
            "field_description": "Séquence",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 11,
            "ttype": "integer",
            "model_id": model_project_workflow_design_faiblesse.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_workflow_design_faiblesse.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_faiblesse.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Force
        value = {
            "name": "project_workflow_design_force",
            "description": "Project workflow design force",
            "model": "project.workflow.design.force",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design_force = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_force.add_model_inherit(lst_depend_model)

        ##### Begin Field
        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.force",
            "field_description": "Force",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_force.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_project_workflow_design = {
            "name": "project_workflow_design",
            "model": "project.workflow.design.force",
            "field_description": "Project Workflow Design",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 12,
            "ttype": "many2one",
            "relation": "project.workflow.design",
            "model_id": model_project_workflow_design_force.id,
        }
        env["ir.model.fields"].create(value_field_project_workflow_design)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.workflow.design.force",
            "field_description": "Séquence",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 11,
            "ttype": "integer",
            "model_id": model_project_workflow_design_force.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_workflow_design_force.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_force.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Menace
        value = {
            "name": "project_workflow_design_menace",
            "description": "Project workflow design menace",
            "model": "project.workflow.design.menace",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design_menace = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_menace.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.menace",
            "field_description": "Menace",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_menace.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_project_workflow_design = {
            "name": "project_workflow_design",
            "model": "project.workflow.design.menace",
            "field_description": "Project Workflow Design",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 12,
            "ttype": "many2one",
            "relation": "project.workflow.design",
            "model_id": model_project_workflow_design_menace.id,
        }
        env["ir.model.fields"].create(value_field_project_workflow_design)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.workflow.design.menace",
            "field_description": "Séquence",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 11,
            "ttype": "integer",
            "model_id": model_project_workflow_design_menace.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_workflow_design_menace.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_menace.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Objectif
        value = {
            "name": "project_workflow_design_objectif",
            "description": "Project workflow design objectif",
            "model": "project.workflow.design.objectif",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design_objectif = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_objectif.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_description = {
            "name": "description",
            "model": "project.workflow.design.objectif",
            "field_description": "Description",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 11,
            "ttype": "char",
            "model_id": model_project_workflow_design_objectif.id,
        }
        env["ir.model.fields"].create(value_field_description)

        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.objectif",
            "field_description": "Objectif",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_objectif.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_project_workflow_design = {
            "name": "project_workflow_design",
            "model": "project.workflow.design.objectif",
            "field_description": "Project Workflow Design",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 13,
            "ttype": "many2one",
            "relation": "project.workflow.design",
            "model_id": model_project_workflow_design_objectif.id,
        }
        env["ir.model.fields"].create(value_field_project_workflow_design)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.workflow.design.objectif",
            "field_description": "Séquence",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 12,
            "ttype": "integer",
            "model_id": model_project_workflow_design_objectif.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_workflow_design_objectif.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_objectif.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Opportunite
        value = {
            "name": "project_workflow_design_opportunite",
            "description": "Project workflow design opportunité",
            "model": "project.workflow.design.opportunite",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design_opportunite = env["ir.model"].create(
            value
        )

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_opportunite.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.opportunite",
            "field_description": "Opportunité",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_opportunite.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_project_workflow_design = {
            "name": "project_workflow_design",
            "model": "project.workflow.design.opportunite",
            "field_description": "Project Workflow Design",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 12,
            "ttype": "many2one",
            "relation": "project.workflow.design",
            "model_id": model_project_workflow_design_opportunite.id,
        }
        env["ir.model.fields"].create(value_field_project_workflow_design)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.workflow.design.opportunite",
            "field_description": "Séquence",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 11,
            "ttype": "integer",
            "model_id": model_project_workflow_design_opportunite.id,
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
                    model_project_workflow_design_opportunite.id,
                ),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_opportunite.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Volet
        value = {
            "name": "project_workflow_design_volet",
            "description": "Project workflow design volet",
            "model": "project.workflow.design.volet",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "diagram_node_object": "project.workflow.design.volet.box",
            "diagram_node_xpos_field": "xpos",
            "diagram_node_ypos_field": "ypos",
            "diagram_node_shape_field": "rectangle:True",
            "diagram_node_form_view_ref": (
                "project_workflow_design_volet_box_view_form"
            ),
            "diagram_arrow_object": "project.workflow.design.volet.liaison",
            "diagram_arrow_src_field": "volet_box_src",
            "diagram_arrow_dst_field": "volet_box_dst",
            "diagram_arrow_label": "['name']",
            "diagram_label_string": "Créer vos relations.",
            "nomenclator": True,
        }
        model_project_workflow_design_volet = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_volet.add_model_inherit(lst_depend_model)

        ##### Begin Field
        value_field_description = {
            "name": "description",
            "model": "project.workflow.design.volet",
            "field_description": "Description",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 11,
            "ttype": "text",
            "model_id": model_project_workflow_design_volet.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_description)

        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.volet",
            "field_description": "Volet",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_volet.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_project_workflow_design = {
            "name": "project_workflow_design",
            "model": "project.workflow.design.volet",
            "field_description": "Project Workflow Design",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 15,
            "ttype": "many2one",
            "relation": "project.workflow.design",
            "model_id": model_project_workflow_design_volet.id,
        }
        env["ir.model.fields"].create(value_field_project_workflow_design)

        value_field_sequence = {
            "name": "sequence",
            "model": "project.workflow.design.volet",
            "field_description": "Séquence",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 15,
            "code_generator_tree_view_sequence": 14,
            "ttype": "integer",
            "model_id": model_project_workflow_design_volet.id,
            "default": 10,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_sequence)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_workflow_design_volet.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_volet.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Volet Box
        value = {
            "name": "project_workflow_design_volet_box",
            "description": "Project workflow design volet box",
            "model": "project.workflow.design.volet.box",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design_volet_box = env["ir.model"].create(value)

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_volet_box.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_description = {
            "name": "description",
            "model": "project.workflow.design.volet.box",
            "field_description": "Description",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 11,
            "ttype": "text",
            "model_id": model_project_workflow_design_volet_box.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_description)

        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.volet.box",
            "field_description": "Nom",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_volet_box.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_volet_id = {
            "name": "volet_id",
            "model": "project.workflow.design.volet.box",
            "field_description": "Volet",
            "code_generator_sequence": 9,
            "code_generator_form_simple_view_sequence": 16,
            "code_generator_tree_view_sequence": 16,
            "ttype": "many2one",
            "relation": "project.workflow.design.volet",
            "model_id": model_project_workflow_design_volet_box.id,
        }
        env["ir.model.fields"].create(value_field_volet_id)

        value_field_xpos = {
            "name": "xpos",
            "model": "project.workflow.design.volet.box",
            "field_description": "Diagram position x",
            "code_generator_sequence": 7,
            "code_generator_form_simple_view_sequence": 14,
            "code_generator_tree_view_sequence": 14,
            "ttype": "integer",
            "model_id": model_project_workflow_design_volet_box.id,
            "default": 50,
        }
        env["ir.model.fields"].create(value_field_xpos)

        value_field_ypos = {
            "name": "ypos",
            "model": "project.workflow.design.volet.box",
            "field_description": "Diagram position y",
            "code_generator_sequence": 8,
            "code_generator_form_simple_view_sequence": 15,
            "code_generator_tree_view_sequence": 15,
            "ttype": "integer",
            "model_id": model_project_workflow_design_volet_box.id,
            "default": 50,
        }
        env["ir.model.fields"].create(value_field_ypos)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                ("model_id", "=", model_project_workflow_design_volet_box.id),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_volet_box.rec_name = "name"
        field_x_name.unlink()
        ##### End Field

        # Add Project Workflow Design Volet Liaison
        value = {
            "name": "project_workflow_design_volet_liaison",
            "description": "Project workflow design volet liaison",
            "model": "project.workflow.design.volet.liaison",
            "m2o_module": code_generator_id.id,
            "rec_name": None,
            "enable_activity": True,
            "nomenclator": True,
        }
        model_project_workflow_design_volet_liaison = env["ir.model"].create(
            value
        )

        # Model inherit
        lst_depend_model = ["mail.thread", "mail.activity.mixin"]
        model_project_workflow_design_volet_liaison.add_model_inherit(
            lst_depend_model
        )

        ##### Begin Field
        value_field_name = {
            "name": "name",
            "model": "project.workflow.design.volet.liaison",
            "field_description": "Name",
            "code_generator_sequence": 3,
            "code_generator_form_simple_view_sequence": 10,
            "code_generator_tree_view_sequence": 10,
            "ttype": "char",
            "model_id": model_project_workflow_design_volet_liaison.id,
            "track_visibility": "onchange",
        }
        env["ir.model.fields"].create(value_field_name)

        value_field_volet_box_dst = {
            "name": "volet_box_dst",
            "model": "project.workflow.design.volet.liaison",
            "field_description": "Volet box dst",
            "code_generator_sequence": 4,
            "code_generator_form_simple_view_sequence": 11,
            "code_generator_tree_view_sequence": 11,
            "ttype": "many2one",
            "relation": "project.workflow.design.volet.box",
            "model_id": model_project_workflow_design_volet_liaison.id,
        }
        env["ir.model.fields"].create(value_field_volet_box_dst)

        value_field_volet_box_src = {
            "name": "volet_box_src",
            "model": "project.workflow.design.volet.liaison",
            "field_description": "Volet box src",
            "code_generator_sequence": 5,
            "code_generator_form_simple_view_sequence": 12,
            "code_generator_tree_view_sequence": 12,
            "ttype": "many2one",
            "relation": "project.workflow.design.volet.box",
            "model_id": model_project_workflow_design_volet_liaison.id,
        }
        env["ir.model.fields"].create(value_field_volet_box_src)

        value_field_volet_id = {
            "name": "volet_id",
            "model": "project.workflow.design.volet.liaison",
            "field_description": "Volet",
            "code_generator_sequence": 6,
            "code_generator_form_simple_view_sequence": 13,
            "code_generator_tree_view_sequence": 13,
            "ttype": "many2one",
            "relation": "project.workflow.design.volet",
            "model_id": model_project_workflow_design_volet_liaison.id,
        }
        env["ir.model.fields"].create(value_field_volet_id)

        # Hack to solve field name
        field_x_name = env["ir.model.fields"].search(
            [
                (
                    "model_id",
                    "=",
                    model_project_workflow_design_volet_liaison.id,
                ),
                ("name", "=", "x_name"),
            ]
        )
        model_project_workflow_design_volet_liaison.rec_name = "name"
        field_x_name.unlink()

        # Added one2many field, many2many need to be create before add one2many
        value_field_faiblesse_ids = {
            "name": "faiblesse_ids",
            "model": "project.workflow.design",
            "field_description": "Faiblesse",
            "ttype": "one2many",
            "relation": "project.workflow.design.faiblesse",
            "relation_field": "project_workflow_design",
            "model_id": model_project_workflow_design.id,
        }
        env["ir.model.fields"].create(value_field_faiblesse_ids)

        value_field_force_ids = {
            "name": "force_ids",
            "model": "project.workflow.design",
            "field_description": "Force",
            "ttype": "one2many",
            "relation": "project.workflow.design.force",
            "relation_field": "project_workflow_design",
            "model_id": model_project_workflow_design.id,
        }
        env["ir.model.fields"].create(value_field_force_ids)

        value_field_menace_ids = {
            "name": "menace_ids",
            "model": "project.workflow.design",
            "field_description": "Menace",
            "ttype": "one2many",
            "relation": "project.workflow.design.menace",
            "relation_field": "project_workflow_design",
            "model_id": model_project_workflow_design.id,
        }
        env["ir.model.fields"].create(value_field_menace_ids)

        value_field_objectif_ids = {
            "name": "objectif_ids",
            "model": "project.workflow.design",
            "field_description": "Objectif",
            "ttype": "one2many",
            "relation": "project.workflow.design.objectif",
            "relation_field": "project_workflow_design",
            "model_id": model_project_workflow_design.id,
        }
        env["ir.model.fields"].create(value_field_objectif_ids)

        value_field_objectif_volet = {
            "name": "objectif_volet",
            "model": "project.workflow.design",
            "field_description": "Volet",
            "ttype": "one2many",
            "relation": "project.workflow.design.volet",
            "relation_field": "project_workflow_design",
            "model_id": model_project_workflow_design.id,
        }
        env["ir.model.fields"].create(value_field_objectif_volet)

        value_field_opportunite_ids = {
            "name": "opportunite_ids",
            "model": "project.workflow.design",
            "field_description": "Opportunité",
            "ttype": "one2many",
            "relation": "project.workflow.design.opportunite",
            "relation_field": "project_workflow_design",
            "model_id": model_project_workflow_design.id,
        }
        env["ir.model.fields"].create(value_field_opportunite_ids)

        value_field_volet_box = {
            "name": "volet_box",
            "model": "project.workflow.design.volet",
            "field_description": "Boites",
            "ttype": "one2many",
            "relation": "project.workflow.design.volet.box",
            "relation_field": "volet_id",
            "model_id": model_project_workflow_design_volet.id,
        }
        env["ir.model.fields"].create(value_field_volet_box)

        value_field_volet_liaison = {
            "name": "volet_liaison",
            "model": "project.workflow.design.volet",
            "field_description": "Liaison",
            "ttype": "one2many",
            "relation": "project.workflow.design.volet.liaison",
            "relation_field": "volet_id",
            "model_id": model_project_workflow_design_volet.id,
        }
        env["ir.model.fields"].create(value_field_volet_liaison)

        value_field_volet_box_dst = {
            "name": "volet_box_dst",
            "model": "project.workflow.design.volet.box",
            "field_description": "Volet box dst",
            "ttype": "one2many",
            "relation": "project.workflow.design.volet.liaison",
            "relation_field": "volet_box_dst",
            "model_id": model_project_workflow_design_volet_box.id,
        }
        env["ir.model.fields"].create(value_field_volet_box_dst)

        value_field_volet_box_src = {
            "name": "volet_box_src",
            "model": "project.workflow.design.volet.box",
            "field_description": "Volet box src",
            "ttype": "one2many",
            "relation": "project.workflow.design.volet.liaison",
            "relation_field": "volet_box_src",
            "model_id": model_project_workflow_design_volet_box.id,
        }
        env["ir.model.fields"].create(value_field_volet_box_src)

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
