from odoo import _, api, fields, models


class ProjectWorkflowDesignForce(models.Model):
    _name = "project.workflow.design.force"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design force"
    _order = "sequence"

    name = fields.Char(
        string="Force",
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
