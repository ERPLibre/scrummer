from odoo import _, api, fields, models


class ProjectWorkflowDesignVoletBox(models.Model):
    _name = "project.workflow.design.volet.box"
    _inherit = ["mail.activity.mixin", "mail.thread"]
    _description = "Project workflow design volet box"

    volet_box_dst = fields.One2many(
        string="Volet box dst",
        comodel_name="project.workflow.design.volet.liaison",
        inverse_name="volet_box_dst",
    )

    volet_box_src = fields.One2many(
        string="Volet box src",
        comodel_name="project.workflow.design.volet.liaison",
        inverse_name="volet_box_src",
    )

    name = fields.Char(
        string="Nom",
        track_visibility="onchange",
    )

    description = fields.Text(track_visibility="onchange")

    select_color = fields.Selection(
        selection=[
            ("green", "Vert"),
            ("blue", "Bleu"),
            ("red", "Rouge"),
            ("orange", "Orange"),
            ("yellow", "Jaune"),
            ("purple", "Mauve"),
            ("white", "Blanc"),
            ("gray", "Gris"),
            ("black", "Noir"),
        ],
        string="Couleur",
        default="green",
    )

    xpos = fields.Integer(
        string="Diagram position x",
        default=50,
    )

    ypos = fields.Integer(
        string="Diagram position y",
        default=50,
    )

    volet_id = fields.Many2one(
        string="Volet",
        comodel_name="project.workflow.design.volet",
    )
