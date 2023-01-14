from odoo import _, api, fields, models


class ProjectWorkflowDesign(models.Model):
    _name = "project.workflow.design"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design"

    faiblesse_ids = fields.One2many(
        string="Faiblesse",
        comodel_name="project.workflow.design.faiblesse",
        inverse_name="project_workflow_design",
    )

    force_ids = fields.One2many(
        string="Force",
        comodel_name="project.workflow.design.force",
        inverse_name="project_workflow_design",
    )

    menace_ids = fields.One2many(
        string="Menace",
        comodel_name="project.workflow.design.menace",
        inverse_name="project_workflow_design",
    )

    objectif_ids = fields.One2many(
        string="Objectif",
        comodel_name="project.workflow.design.objectif",
        inverse_name="project_workflow_design",
    )

    objectif_volet = fields.One2many(
        string="Volet",
        comodel_name="project.workflow.design.volet",
        inverse_name="project_workflow_design",
    )

    opportunite_ids = fields.One2many(
        string="Opportunité",
        comodel_name="project.workflow.design.opportunite",
        inverse_name="project_workflow_design",
    )

    name = fields.Char(
        string="Nom",
        track_visibility="onchange",
    )

    link_wire_frame = fields.Char(
        string="Lien vers design externe",
        track_visibility="onchange",
    )
