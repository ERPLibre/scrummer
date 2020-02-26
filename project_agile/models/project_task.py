# Copyright 2017 - 2018 Modoolar <info@modoolar.com>
# License LGPLv3.0 or later (https://www.gnu.org/licenses/lgpl-3.0.en.html).

from odoo import models, fields, api, exceptions, _


class TaskResolution(models.Model):
    _name = "project.task.resolution"
    _description = "Task Resolution"
    _inherit = ["project.agile.code_item"]


class ProjectTaskLinkRelation(models.Model):
    _name = "project.task.link.relation"
    _description = "Project Task Link Relation Type"

    name = fields.Char(string="Name", required=True,)

    inverse_name = fields.Char(string="Reverse Name", required=True,)

    sequence = fields.Integer(string="Order", required=True,)


class ProjectTaskLink(models.Model):
    _name = "project.task.link"
    _description = "Project Task Link"

    name = fields.Char(string="Name", compute="_compute_display_name",)

    comment = fields.Char(string="Comment",)

    relation_id = fields.Many2one(
        comodel_name="project.task.link.relation",
        string="Relation",
        required=True,
    )

    task_left_id = fields.Many2one(
        comodel_name="project.task",
        string="Task on the left",
        required=True,
        ondelete="cascade",
    )

    task_right_id = fields.Many2one(
        comodel_name="project.task",
        string="Task on the right",
        required=True,
        ondelete="cascade",
    )

    relation_name = fields.Char(
        string="Relation", compute="_compute_relation_name",
    )

    related_task_id = fields.Many2one(
        comodel_name="project.task",
        string="Related task",
        compute="_compute_related_task_id",
    )

    @api.multi
    @api.depends()
    def _compute_display_name(self):
        for record in self:

            other_task = record.task_right_id
            if record.task_right_id:
                other_task = record.task_left_id

            record.name = "[%s] %s" % (other_task.key, other_task.name)

    @api.multi
    def _compute_relation_name(self):
        task_id = self.env.context.get("task_id", -1)
        for record in self:
            relation = record.relation_id

            rel_name = record.relation_id.name
            if task_id == record.task_right_id.id:
                rel_name = relation.inverse_name

            record.relation_name = rel_name

    @api.multi
    def _compute_related_task_id(self):
        task_id = self.env.context.get("task_id", -1)
        for record in self:
            other_task = record.task_right_id
            if task_id == record.task_right_id.id:
                other_task = record.task_left_id

            record.related_task_id = other_task

    @api.multi
    def delete_task_link(self):
        self.ensure_one()
        self.unlink()

    @api.multi
    def open_task_link(self):
        self.ensure_one()

        other_task = self.task_right_id
        if self.related_task_id.id == self.task_right_id.id:
            other_task = self.task_left_id

        return {
            "name": "Related task",
            "view_mode": "form",
            "view_type": "form",
            "view_id": self.env.ref("project.view_task_form2").id,
            "res_model": "project.task",
            "type": "ir.actions.act_window",
            "res_id": self.related_task_id.id,
            "context": {
                "active_model": "project.task",
                "active_ids": [self.related_task_id.id],
                "active_id": self.related_task_id.id,
                "task_id": other_task.id,
            },
        }


class TaskType(models.Model):
    _name = "project.task.type2"
    _description = "Task Type"
    _inherit = ["project.agile.code_item"]

    project_type_ids = fields.Many2many(
        comodel_name="project.type",
        relation="project_type_task_type_rel",
        column1="task_type_id",
        column2="project_type_id",
        string="Project Types",
    )

    icon = fields.Binary(string="Icon")

    priority_ids = fields.Many2many(
        comodel_name="project.task.priority",
        relation="project_task_type2_task_priority_rel",
        column1="type_id",
        column2="priority_id",
        string="Priorities",
    )

    default_priority_id = fields.Many2one(
        comodel_name="project.task.priority", string="Default Task Priority",
    )

    allow_story_points = fields.Boolean(
        string="Allow Story Points", default=True,
    )

    allow_sub_tasks = fields.Boolean(string="Allow Sub-Items", default=False,)

    type_ids = fields.Many2many(
        comodel_name="project.task.type2",
        relation="project_task_type2_sub_types_rel",
        column1="type_id",
        column2="sub_type_id",
        string="Sub Types",
    )

    parent_type_ids = fields.Many2many(
        comodel_name="project.task.type2",
        relation="project_task_type2_sub_types_rel",
        column1="sub_type_id",
        column2="type_id",
        string="Parent Types",
    )

    task_ids = fields.One2many(
        comodel_name="project.task",
        inverse_name="type_id",
        string="Related Tasks",
    )

    portal_visible = fields.Boolean(string="Visible on Portal", default=True,)

    is_default_type = fields.Boolean(string="Is Default Type", default=False)

    @api.multi
    def write(self, values):
        if values.get("is_default_type", False) and values["is_default_type"]:
            default_task_type = self.search([("is_default_type", "=", True)])
            default_task_type.write({"is_default_type": False})
        return super(TaskType, self).write(values)

    @api.constrains("is_default_type")
    def check_only_one_default_type(self):
        default_task_type = self.search([("is_default_type", "=", True)])
        if default_task_type and len(default_task_type.ids) > 1:
            raise exceptions.ValidationError(
                _("You can only have one default task type - %s.")
                % default_task_type.mapped("name")
            )

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        if args is None:
            args = []

        # The key 'selected_task_type_ids' is defined on the
        # project.type form view.
        if "selected_task_type_ids" in self.env.context:
            args.append(
                (
                    "id",
                    "in",
                    self.env.context["selected_task_type_ids"][0][2],
                )
            )

        if "board_project_ids" in self.env.context:
            project_ids = self.env.context.get("board_project_ids", [])
            if project_ids:
                args.append(
                    [
                        "id",
                        "in",
                        self.env["project.project"]
                        .browse(project_ids[0][2])
                        .mapped("type_id.task_type_ids")
                        .fetch_all(),
                    ]
                )

        return super(TaskType, self).name_search(
            name=name, args=args, operator=operator, limit=limit
        )

    @api.multi
    def apply_portal_status(self):
        self.ensure_one()
        self.task_ids.write({"portal_visible": self.portal_visible})

    @api.multi
    def fetch_all(self):
        task_type_ids = []

        def collect_task_types(tt):
            if tt.id in task_type_ids:
                return

            task_type_ids.append(tt.id)
            for subtype in tt.type_ids:
                collect_task_types(subtype)

        for task_type in self:
            collect_task_types(task_type)

        return task_type_ids


class TaskPriority(models.Model):
    _name = "project.task.priority"
    _description = "Task Priority"
    _inherit = ["project.agile.code_item"]

    type_ids = fields.Many2many(
        comodel_name="project.task.type2",
        relation="project_task_type2_task_priority_rel",
        column1="priority_id",
        column2="type_id",
        string="Types",
    )

    icon = fields.Binary(string="Icon")

    is_default_priority = fields.Boolean(
        string="Is Default Priority", default=False
    )

    _sql_constraints = [
        (
            "project_task_priority_name_unique",
            "unique(name)",
            "Priority name already exists",
        )
    ]

    @api.multi
    def write(self, values):
        if (
            values.get("is_default_priority", False)
            and values["is_default_priority"]
        ):
            default_task_priority = self.search(
                [("is_default_priority", "=", True)]
            )
            default_task_priority.write({"is_default_priority": False})
        return super(TaskPriority, self).write(values)

    @api.constrains("is_default_priority")
    def check_only_one_default_priority(self):
        default_task_priority = self.search(
            [("is_default_priority", "=", True)]
        )
        if default_task_priority and len(default_task_priority.ids) > 1:
            raise exceptions.ValidationError(
                _("You can only have one default task type - %s.")
                % default_task_priority.mapped("name")
            )

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        if args is None:
            args = []

        # The key 'selected_priority_ids' is defined on the
        # project.task.type2 form view.
        if "selected_priority_ids" in self.env.context:
            args.append(
                ("id", "in", self.env.context["selected_priority_ids"][0][2])
            )

        return super(TaskPriority, self).name_search(
            name=name, args=args, operator=operator, limit=limit
        )


class Task(models.Model):
    _name = "project.task"
    _inherit = ["project.task", "project.agile.mixin.id_search"]

    def _default_agile_order(self):
        self.env.cr.execute("SELECT MAX(agile_order) + 1 FROM project_task")
        r = self.env.cr.fetchone()
        return r[0]

    type_id = fields.Many2one(
        comodel_name="project.task.type2",
        string="Type",
        required=True,
        ondelete="restrict",
        default=lambda self: self.env["project.task.type2"].search(
            [("is_default_type", "=", True)], limit=1
        ),
        track_visibility='onchange',
    )

    agile_order = fields.Float(
        required=False, default=_default_agile_order
    )

    agile_enabled = fields.Boolean(related="project_id.agile_enabled", track_visibility='onchange', )

    resolution_id = fields.Many2one(
        comodel_name="project.task.resolution",
        string="Resolution",
        index=True,
        track_visibility='onchange',
    )

    allow_story_points = fields.Boolean(
        related="type_id.allow_story_points",
        string="Allow Story Points",
        readonly=True,
    )

    project_type_id = fields.Many2one(
        comodel_name="project.type",
        related="project_id.type_id",
        string="Project Type",
        readonly=True,
    )

    is_user_story = fields.Boolean(
        string="Is Story", compute="_compute_is_story", store=True,
    )

    is_epic = fields.Boolean(
        string="Is Epic", compute="_compute_is_epic", store=True,
    )

    epic_id = fields.Many2one(
        comodel_name="project.task",
        string="Epic",
        compute="_compute_epic_id",
        store=True,
        readonly=True,
        help="This field represents the first",
    )

    assigned_to_me = fields.Boolean(
        string="Assigned to Me", compute="_compute_assigned_to_me"
    )

    user_id = fields.Many2one(comodel_name="res.users", default=False,)

    create_uid = fields.Many2one(
        comodel_name="res.users", string="Reported By", readonly=True,
    )

    create_date = fields.Datetime(string="Created", readonly=True,)

    write_date = fields.Datetime(string="Updated", readonly=True,)

    team_id = fields.Many2one(
        comodel_name="project.agile.team", string="Committed team",
    )

    parent_id = fields.Many2one('project.task', track_visibility='onchange')

    type_ids = fields.Many2many(
        comodel_name="project.task.type2",
        related="type_id.type_ids",
        readonly=True,
        string="Allowed Subtypes",
    )

    task_count = fields.Integer(
        compute="_compute_task_count", string="Number of SubTasks"
    )

    allow_sub_tasks = fields.Boolean(
        related="type_id.allow_sub_tasks",
        string="Allow Sub-Tasks",
        stored=True,
    )

    priority_id = fields.Many2one(
        comodel_name="project.task.priority",
        string="Priority",
        required=True,
        ondelete="restrict",
        default=lambda self: self.env["project.task.priority"].search(
            [("is_default_priority", "=", True)], limit=1
        ),
        track_visibility='onchange',
    )

    story_points = fields.Integer(string="Story points", default=0, track_visibility='onchange')

    doc_count = fields.Integer(
        compute="_compute_doc_count", string="Number of documents attached"
    )

    link_ids = fields.One2many(
        comodel_name="project.task.link",
        compute="_compute_links",
        string="Links",
        syncer={"inverse_names": ["task_left_id", "task_right_id"]},
    )

    link_count = fields.Integer(
        compute="_compute_link_count", string="Number of Links"
    )

    activity_date_deadline = fields.Date(groups="")

    @api.multi
    @api.onchange("parent_id")
    def _onchange_parent_id(self):
        # Convert to sub-task/story when actually task/story and parent is task/story
        # TODO use wizard to ask the user which sub-task to be converted
        # Take the first sub_type in list
        if self.parent_id and not self.parent_id.is_epic and self.parent_id.allow_sub_tasks and \
                self.parent_id.type_id.type_ids and self.type_id not in self.parent_id.type_id.type_ids:
            # force change type_id with first sub_tasks type_id
            self.type_id = self.parent_id.type_id.type_ids[0]

        return super()._onchange_parent_id()  # pragma: no cover

    @api.multi
    @api.depends("type_id")
    def _compute_is_story(self):
        ptts = self.env.ref(
            "project_agile.project_task_type_story", raise_if_not_found=False
        )
        for record in self:
            record.is_user_story = ptts and record.type_id.id == ptts.id

    @api.multi
    @api.depends("type_id")
    def _compute_is_epic(self):
        ptte = self.env.ref(
            "project_agile.project_task_type_epic", raise_if_not_found=False
        )
        for record in self:
            record.is_epic = ptte and record.type_id.id == ptte.id

    @api.multi
    @api.depends("parent_id", "parent_id.epic_id")
    def _compute_epic_id(self):
        epic_type = self.env.ref(
            "project_agile.project_task_type_epic", raise_if_not_found=False
        )

        if epic_type:
            for record in self:
                epic_id = False

                current = record.parent_id
                while current:
                    if current.type_id.id == epic_type.id:
                        epic_id = current.id
                        break
                    current = current.parent_id
                record.epic_id = epic_id
        else:
            for record in self:
                record.epic_id = False

    @api.multi
    @api.depends("user_id")
    def _compute_assigned_to_me(self):
        for task in self:
            task.assigned_to_me = task.user_id.id == self.env.user.id

    @api.multi
    def _compute_task_count(self):
        data = self.env["project.task"].read_group(
            [("parent_id", "in", self.ids)], ["parent_id"], ["parent_id"]
        )

        data = dict([(m["parent_id"], m["parent_id_count"]) for m in data])

        for record in self:
            record.task_count = data.get(record.id, 0)

    @api.multi
    def _compute_doc_count(self):
        attachment_data = self.env["ir.attachment"].read_group(
            [("res_model", "=", self._name), ("res_id", "in", self.ids)],
            ["res_id", "res_model"],
            ["res_id", "res_model"],
        )

        mapped_data = dict(
            [(m["res_id"], m["res_id_count"]) for m in attachment_data]
        )

        for record in self:
            record.doc_count = mapped_data.get(record.id, 0)

    @api.multi
    def _compute_links(self):
        for record in self:
            record.link_ids = self.env["project.task.link"].search(
                [
                    "|",
                    ("task_left_id", "=", record.id),
                    ("task_right_id", "=", record.id),
                ]
            )

    @api.multi
    def _compute_link_count(self):
        for record in self:
            record.link_count = len(record.link_ids)

    @api.onchange("project_id")
    def _onchange_project(self):
        super(Task, self)._onchange_project()

        default_type_id = self.env.context.get("default_type_id", False)

        if self.project_id:
            task_type_id = self.project_id.type_id.default_task_type_id.id
            if default_type_id and self.project_id.type_id.has_task_type(
                default_type_id
            ):
                task_type_id = default_type_id

            self.type_id = task_type_id
        else:
            self.type_id = False

    @api.onchange("type_id")
    def _onchange_type_id(self):
        self.priority_id = False
        self.portal_visible = False
        if self.type_id:
            if self.type_id.default_priority_id:
                self.priority_id = self.type_id.default_priority_id.id

            self.portal_visible = self.type_id.portal_visible

    @api.model_create_multi
    @api.returns("self", lambda value: value.id)
    def create(self, vals_list):
        for vals in vals_list:
            project_id = vals.get(
                "project_id", self.env.context.get("default_project_id", False)
            )

            if project_id:
                project = self.env["project.project"].browse(project_id)

                if not vals.get("type_id", False):
                    default_type_id = self.env.context.get(
                        "default_type_id", False
                    )
                    if default_type_id:
                        vals["type_id"] = default_type_id
                    else:
                        dtt = project.type_id.default_task_type_id
                        vals["type_id"] = dtt and dtt.id or False

                if "portal_visible" not in vals:
                    vals["portal_visible"] = (
                        self.env["project.task.type2"]
                        .browse(vals["type_id"])
                        .portal_visible
                    )

                if not vals.get("priority_id", False) and vals.get("type_id"):
                    task_type = self.env["project.task.type2"].browse(
                        vals.get("type_id")
                    )
                    vals["priority_id"] = task_type.default_priority_id.id or False

        new = super(Task, self).create(vals_list)

        if new.parent_id and new.parent_id.stage_id:
            new._write({"stage_id": new.parent_id.stage_id.id})

        return new

    @api.multi
    def write(self, vals):
        result = super(Task, self).write(vals)
        if "type_id" in vals.keys():
            # Convert children type_id
            # Convert to sub-task/story when actually task/story and parent is task/story
            # Convert to task/story when parent become epic
            # TODO use wizard to ask the user which sub-task to be converted
            # Take the first sub_type in list
            if self.allow_sub_tasks and self.type_id.type_ids:
                if self.is_epic:
                    for child_id in self.child_ids:
                        if not child_id.type_id.allow_sub_tasks and child_id.type_id.parent_type_ids:
                            child_id.type_id = child_id.type_id.parent_type_ids[0]
                else:
                    for child_id in self.child_ids:
                        if child_id.type_id not in self.type_id.type_ids:
                            child_id.type_id = self.type_id.type_ids[0]
        return result

    @api.model
    def name_search(self, name="", args=None, operator="ilike", limit=100):
        if args is None:
            args = []

        if "filter_user_stories" in self.env.context:
            args.append(
                (
                    "type_id",
                    "=",
                    self.env.ref_id("project_agile.project_task_type_story"),
                )
            )

        return super(Task, self).name_search(
            name=name, args=args, operator=operator, limit=limit
        )

    @api.model
    def search(self, args, offset=0, limit=None, order=None, count=False):
        if args is None:
            args = []

        if "filter_user_stories" in self.env.context:
            args.append(
                (
                    "type_id",
                    "=",
                    self.env.ref_id(
                        self, "project_agile.project_task_type_story"
                    ),
                )
            )

        if "filter_tasks" in self.env.context:
            args.append(
                (
                    "type_id",
                    "=",
                    self.env.ref_id(
                        self, "project_agile.project_task_type_task"
                    ),
                )
            )

        return super(Task, self).search(args, offset, limit, order, count)

    @api.multi
    def open_sub_task(self):
        self.ensure_one()
        ctx = self._context.copy()
        ctx.update(
            {
                "active_model": "project.task",
                "active_ids": [self.id],
                "active_id": self.id,
            }
        )
        return {
            "name": "Sub-Task",
            "view_mode": "form",
            "view_type": "form",
            "view_id": self.env.ref("project.view_task_form2").id,
            "res_model": "project.task",
            "type": "ir.actions.act_window",
            "res_id": self.id,
            "context": ctx,
        }

    @api.multi
    def attachment_tree_view(self):
        self.ensure_one()

        action = self.env.ref_action("base.action_attachment")

        action["domain"] = [
            ("res_model", "=", "project.task"),
            ("res_id", "=", self.id),
        ]

        action["context"] = {
            "default_res_model": self._name,
            "default_res_id": self.id,
        }

        return action

    # Following methods will be called from hooks file,
    # so we can leave project.task in valid state.
    @api.model
    def _set_default_task_priority_id(self):
        for res in self.with_context(active_test=False).search(
            [("priority_id", "=", False)]
        ):
            res.priority_id = res.type_id.default_priority_id or False

    @api.model
    def _set_default_task_type_id(self):
        for task in self.with_context(active_test=False).search(
            [("type_id", "=", False)]
        ):
            dtt = task.project_id.type_id.default_task_type_id
            task.type_id = dtt and dtt.id or False


class PortalTask(models.Model):
    _inherit = "project.task"

    portal_visible = fields.Boolean(
        string="Visible on Portal",
        default=False,
        help="This field enables you to override settings from task type"
        " and display this task on portal",
    )

    @api.model
    def create_task_portal(self, values):
        if not (self.task_portal_check_mandatory_fields(values)):
            return {"errors": _('Fields marked with "*" are required!')}

        vals = {
            "name": values["name"],
            "priority_id": values["priority_id"],
            "project_id": values["project_id"],
            "type_id": values["type_id"],
        }

        for field in ["date_deadline", "description"]:
            if values[field]:
                vals[field] = values[field]

        task = self.create(vals)

        return {"id": task.id}

    @api.multi
    def update_task_portal(self, values):
        task_values = {
            "name": values["name"],
            "date_deadline": values["date_deadline"] or False,
            "description": values["description"],
            "type_id": values["type_id"],
            "priority_id": values["priority_id"],
        }
        self.write(task_values)

    def task_portal_check_mandatory_fields(self, values):
        for fname in ["name", "type_id", "priority_id", "project_id"]:
            if not values[fname]:
                return False
        return True


class Timesheet(models.Model):
    _inherit = "account.analytic.line"

    portal_approved = fields.Boolean(
        string="Portal Approved?", default=False, index=True,
    )

    portal_approved_by = fields.Many2one(
        comodel_name="res.users", string="Portal Approved By", index=True,
    )

    @api.multi
    def button_portal_open(self):
        self.ensure_one()
        if self.portal_approved:
            return

        self.sudo().write(
            dict(portal_approved=True, portal_approved_by=self.env.user.id)
        )

    @api.multi
    def button_portal_close(self):
        self.ensure_one()
        if not self.portal_approved:
            return

        self.sudo().write(dict(portal_approved=False,))
