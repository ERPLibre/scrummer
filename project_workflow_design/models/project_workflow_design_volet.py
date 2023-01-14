from odoo import _, api, fields, models


class ProjectWorkflowDesignVolet(models.Model):
    _name = "project.workflow.design.volet"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design volet"
    _order = "sequence"

    volet_box = fields.One2many(
        string="Boites",
        comodel_name="project.workflow.design.volet.box",
        inverse_name="volet_id",
    )

    volet_liaison = fields.One2many(
        string="Liaison",
        comodel_name="project.workflow.design.volet.liaison",
        inverse_name="volet_id",
    )

    name = fields.Char(
        string="Volet",
        track_visibility="onchange",
    )

    description = fields.Text(track_visibility="onchange")

    sequence = fields.Integer(
        string="Séquence",
        track_visibility="onchange",
        default=10,
    )

    project_workflow_design = fields.Many2one(
        comodel_name="project.workflow.design"
    )

    volet_box = fields.One2many(
        string="Boites",
        comodel_name="project.workflow.design.volet.box",
        inverse_name="volet_id",
    )

    volet_liaison = fields.One2many(
        string="Liaison",
        comodel_name="project.workflow.design.volet.liaison",
        inverse_name="volet_id",
    )
