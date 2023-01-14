from odoo import _, api, fields, models


class ProjectWorkflowDesignFaiblesse(models.Model):
    _name = "project.workflow.design.faiblesse"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design faiblesse"
    _order = "sequence"

    name = fields.Char(
        string="Faiblesse",
        track_visibility="onchange",
    )

    sequence = fields.Integer(
        string="Séquence",
        track_visibility="onchange",
        default=10,
    )

    project_workflow_design = fields.Many2one(
        comodel_name="project.workflow.design"
    )
