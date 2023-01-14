from odoo import _, api, fields, models


class ProjectWorkflowDesignVoletLiaison(models.Model):
    _name = "project.workflow.design.volet.liaison"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design volet liaison"

    name = fields.Char(track_visibility="onchange")

    volet_box_dst = fields.Many2one(
        string="Volet box dst",
        comodel_name="project.workflow.design.volet.box",
    )

    volet_box_src = fields.Many2one(
        string="Volet box src",
        comodel_name="project.workflow.design.volet.box",
    )

    volet_id = fields.Many2one(
        string="Volet",
        comodel_name="project.workflow.design.volet",
    )
