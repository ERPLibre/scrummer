from odoo import _, api, fields, models


class ProjectWorkflowDesignObjectif(models.Model):
    _name = "project.workflow.design.objectif"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design objectif"
    _order = "sequence"

    description = fields.Char()

    name = fields.Char(
        string="Objectif",
        track_visibility="onchange",
    )

    sequence = fields.Integer(
        string="Séquence",
        track_visibility="onchange",
    )

    project_workflow_design = fields.Many2one(
        comodel_name="project.workflow.design"
    )
