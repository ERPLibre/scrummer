from odoo import _, api, fields, models


class ProjectWorkflowDesignOpportunite(models.Model):
    _name = "project.workflow.design.opportunite"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design opportunité"
    _order = "sequence"

    name = fields.Char(
        string="Opportunité",
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
