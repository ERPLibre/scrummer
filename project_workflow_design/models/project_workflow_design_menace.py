from odoo import _, api, fields, models


class ProjectWorkflowDesignMenace(models.Model):
    _name = "project.workflow.design.menace"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design menace"
    _order = "sequence"

    name = fields.Char(
        string="Menace",
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
