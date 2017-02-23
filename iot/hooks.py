# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from . import __version__ as app_version

app_name = "iot"
app_title = "IOT"
app_publisher = "Dirk Chang"
app_description = "App for SymLink IOT"
app_icon = "octicon octicon-cloud-upload"
app_color = "grey"
app_email = "dirk.chang@symid.com"
app_license = "MIT"
source_link = "https://github.com/srdgame/symlink_iot"

error_report_email = "dirk.chang@symid.com.com"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/iot/css/iot.css"
# app_include_js = "/assets/iot/js/iot.js"

# include js, css files in header of web template
# web_include_css = "/assets/iot/css/iot.css"
# web_include_js = "/assets/iot/js/iot.js"

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "iot_home"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Website user home page (by function)
# get_website_user_home_page = "iot.utils.get_home_page"

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "iot.install.before_install"
# after_install = "iot.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "iot.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"iot.tasks.all"
# 	],
# 	"daily": [
# 		"iot.tasks.daily"
# 	],
# 	"hourly": [
# 		"iot.tasks.hourly"
# 	],
# 	"weekly": [
# 		"iot.tasks.weekly"
# 	]
# 	"monthly": [
# 		"iot.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "iot.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "iot.event.get_events"
# }

# Website
website_route_rules = [
	{"from_route": "/iot_devices", "to_route": "IOT Devices"},
	{"from_route": "/iot_devices/<path:name>", "to_route": "iot_device",
		"defaults": {
			"doctype": "IOT Devices",
			"parents": [{"title": _("IOT Devices"), "name": "iot_devices"}]
		}
	},
	{"from_route": "/iot_enterprises", "to_route": "IOT Enterprise"},
	{"from_route": "/iot_enterprise/<path:name>", "to_route": "iot_enterpris",
		"defaults": {
			"doctype": "IOT Enterprise",
			"parents": [{"title": _("IOT Enterprises"), "name": "iot_enterprises"}]
		}
	},
]

default_roles = [
	{'role': 'IOT User', 'doctype':'IOT User', 'email_field': 'email_id'},
]

has_website_permission = {
	"IOT Enterprise": "iot.controllers.website_list_for_contact.has_website_permission",
	"IOT Device": "iot.controllers.website_list_for_contact.has_website_permission",
}

