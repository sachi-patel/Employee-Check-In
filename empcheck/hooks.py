from . import __version__ as app_version

app_name = "empcheck"
app_title = "Empcheck"
app_publisher = "empcheck"
app_description = "empcheck"
app_email = "empcheck"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/empcheck/css/empcheck.css"
# app_include_js = "/assets/empcheck/js/empcheck.js"

fixtures = fixtures = [
		{"dt":"Custom Field", "filters": [["name", "in",(
            "Employee-latitude",
            "Employee-longitude",
            "Employee-coordinates",
            "Employee Checkin-coordinates",
            "Employee Checkin-latitude",
            "Employee Checkin-longitude",
            "Employee Checkin-map",
            "Employee Checkin-location_status"
        )]]}
]
# include js, css files in header of web template
# web_include_css = "/assets/empcheck/css/empcheck.css"
# web_include_js = "/assets/empcheck/js/empcheck.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "empcheck/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
doctype_js = {"Employee Checkin" : "public/js/emp.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Jinja
# ----------

# add methods and filters to jinja environment
# jinja = {
#	"methods": "empcheck.utils.jinja_methods",
#	"filters": "empcheck.utils.jinja_filters"
# }

# Installation
# ------------

# before_install = "empcheck.install.before_install"
# after_install = "empcheck.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "empcheck.uninstall.before_uninstall"
# after_uninstall = "empcheck.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "empcheck.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	
"Employee Checkin":{
    "validate": "empcheck.empcheck.emp.custom_validate"
}
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"empcheck.tasks.all"
#	],
#	"daily": [
#		"empcheck.tasks.daily"
#	],
#	"hourly": [
#		"empcheck.tasks.hourly"
#	],
#	"weekly": [
#		"empcheck.tasks.weekly"
#	],
#	"monthly": [
#		"empcheck.tasks.monthly"
#	],
# }

# Testing
# -------

# before_tests = "empcheck.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "empcheck.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "empcheck.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Ignore links to specified DocTypes when deleting documents
# -----------------------------------------------------------

# ignore_links_on_delete = ["Communication", "ToDo"]

# Request Events
# ----------------
# before_request = ["empcheck.utils.before_request"]
# after_request = ["empcheck.utils.after_request"]

# Job Events
# ----------
# before_job = ["empcheck.utils.before_job"]
# after_job = ["empcheck.utils.after_job"]

# User Data Protection
# --------------------

# user_data_fields = [
#	{
#		"doctype": "{doctype_1}",
#		"filter_by": "{filter_by}",
#		"redact_fields": ["{field_1}", "{field_2}"],
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_2}",
#		"filter_by": "{filter_by}",
#		"partial": 1,
#	},
#	{
#		"doctype": "{doctype_3}",
#		"strict": False,
#	},
#	{
#		"doctype": "{doctype_4}"
#	}
# ]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"empcheck.auth.validate"
# ]
