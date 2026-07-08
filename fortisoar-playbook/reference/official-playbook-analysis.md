# FortiSOAR OFFICIAL Exports — Analysis Report

Files analyzed: Sample.json (68 collections, 1153 workflows), UseCase.json (28 collections, 214 workflows). Total 1367 workflows.

## 1. Step Types

### 1.1 Distinct stepType UUIDs observed

| stepType UUID | Count | Distinct step names (sample) | Documented? | Label in quickref |
|---|---|---|---|---|
| `0bfed618-0316-11e7-93ae-92361f002671` | 1326 | ADOM Level Block IP Address, ADOM Level Get Blocked IP Addresses, ADOM Level Unblock IP Address, Acknowledge Breach, Add Annotation, Add Comment to Alert, Add Custom Tag to Endpoint, Add Email Categor | YES | Connector external |
| `f414d039-bb0d-4e59-9c39-a8f1e880b18a` | 753 | Alert, Alerts, Start | YES | Manual button trigger |
| `b348f017-9a94-471f-87f8-ce88b6a7ad62` | 583 | Start | YES | Referenced (sub-playbook) |
| `04d0cf46-b6a8-42c4-8683-60a7eaa69e8f` | 543 | Abort Further Setup Steps for Dev, Abort Further Setup Steps for Prod, Accumulated Incidents, Additional Info From Relations, Aggregate results list, Alert Field Mapping, Alert Form Empty, Alert IRI b | YES | Set Variable / for_each |
| `2597053c-e718-44b4-8394-4d40fe26d357` | 314 | Add Attachment Guiding Comment, Add Attachment Hinting Comment, Add Changes to Remote Repo Comment, Add Closed PR Comment, Add Comment On KEV Alert, Add Comment Playbook Is Active, Add Comment Push Ch | YES | Create Record/Comment/Feed |
| `0109f35d-090b-4a2b-bd8a-94cbc3508562` | 237 | Abort Push Operation, Activate Source Control Sync Status Schedule, Buffer Step, Check Active Playbook, Check Awaiting Playbook, Check if Demo Record Exists, Clean up Created Records ID Field, Clear C | YES | Connector cyops_utilities |
| `74932bdc-b8b6-4d24-88c4-1a4dfbc524f3` | 231 | AD User Enrichment, Add Email File to Alert, Add PR Reviewers, Add Pull Request Review, Add Repository Collaborator, Add Source Control Repository Collaborator, Add User Email as Indicator, Analyze Ex | YES | Reference a Playbook |
| `b593663d-7d13-40ce-a3a3-96dece928722` | 210 | Add Drive By Download Tag, Add Spoofing Tag, Add unified results to chart record, Clear Scenario Comments, Close Alert, Close Alert Post Escalation, Close Incident, Close Task, Close the Alert, Correl | YES | Update Record |
| `12254cf5-5db7-4b1a-8cb1-3af081924b28` | 188 | Action, All Connectors Configured, Are Arguments Passed, Are Parameters Passed, Are Repo Created Manually, Are Repositories Created, Asset Exists, Assets Exists, Attachment is msg or eml, CVE Data Fou | YES | Condition |
| `b593663d-7d13-40ce-a3a3-96dece928770` | 124 | Check OT Asset Simulation, Fetch Assets Details, Find Affected Asset, Find Affected IP Address, Find Apply Latest Changes Record, Find Apply Latest Content Record, Find CVEs Record, Find Comments Asso | YES | Find Records |
| `fc04082a-d7dc-4299-96fb-6837b1baa0fe` | 61 | Add Development Collaborator, Add Production Collaborator, Add Task Details, Alert Manual Input Form, Approval to Block Malicious Indicators, Assignee And Approver Name, Block External IP, Calculation | YES | User Input/Approval (rich) |
| `dc6ac63d-c5a5-472f-9eb4-6b18473a98b8` | 47 | Approver Approval To Implement, Approver Approval To Test, Assignee Approval To Implement, Assignee Approval To Test, Identify Security Control, Implement Change, Manual Task for Inline Block on Cloud | **NO (NEW)** |  |
| `6832e556-b9c7-497a-babe-feda3bd27dbf` | 17 | Wait, Wait For DbAdmin Offboard, Wait For DbAdmin Onboard, Wait For SysAdmin Offboard, Wait SLA, Wait for 1 hour, Wait for Alert Creation, Wait for Hunts, Wait for Publish, Wait for Quarantine | YES | Wait/Pause |
| `9300bf69-5063-486d-b3a6-47eb9da24872` | 16 | Start | YES | Field/status-change trigger |
| `4c0019b2-055c-44d0-968c-678a0c2d762e` | 15 | CPU warning notification, Disk space warning notification, Notify Affected User, Notify Recipients, Notify Reporter Email is Safe, Notify Sender, Send Email, Send Email Via SMTP, Send Error Notificati | YES | SMTP/Send Email |
| `ea155646-3821-4542-9702-b246da430a8d` | 12 | Start | YES | On Create trigger |
| `7b221880-716b-4726-a2ca-5e568d330b3e` | 9 | Bulk Ingest Asset Records, Bulk Ingest Vulnerability Records, Create Indicator, Create Record, INSERT Alert, INSERT Incident | YES | Bulk ingest-feed insert |
| `df26c7a2-4166-4ca5-91e5-548e24c01b5f` | 3 | Start | YES | REST API inbound trigger |
| `a19333c2-c822-11ed-afa1-0242ac120002` | 2 | Approval to Block Malicious IPs, Send Approval for Login Disable | YES | Approval (simple/older) |
| `1fdd14cc-d6b4-4335-a3af-ab49c8ed2fd8` | 1 | Remove Special Character | YES | Code Snippet |

### 1.2 Documented UUIDs that NEVER appear in real exports

- `ab3b2e02-5e77-4ed6-8ebd-580f390063a5` — Cross-tenant call (MSSP)
- `ee73e569-2188-43fe-a7f0-1964ba82a4de` — Parent type (NEVER use)

### 1.3 NEW UUIDs not in existing quickref

#### `dc6ac63d-c5a5-472f-9eb4-6b18473a98b8` (count=47)
Distinct names: Approver Approval To Implement, Approver Approval To Test, Assignee Approval To Implement, Assignee Approval To Test, Identify Security Control, Implement Change, Manual Task for Inline Block on Cloud SOC, Manual Task for Revoking File permission, Test Security Controls, Update Baseline, Verify Security Controls, Verify Software Source
Example (from UseCase.json, workflow "Add Cyber Asset"):
```json
{
  "@type": "WorkflowStep",
  "name": "Approver Approval To Implement",
  "description": null,
  "arguments": {
    "message": {
      "tags": [],
      "type": "/api/3/picklists/ff599189-3eeb-4c86-acb0-a7915e85ac3b",
      "tenant": "",
      "content": "<p>Added task <a href=\"/modules/tasks/{{vars.steps.Approver_Approval_To_Implement.uuid}}\" target=\"_blank\" rel=\"noopener\">{{vars.steps.Approver_Approval_To_Implement.name}}</a> to <strong>'Approver Approval To Implement'</strong></p>",
      "records": "{{vars.input.records[0]['@id']}}",
      "parentstepid": "/api/3/workflow_steps/890ce319-249e-477b-9523-1de9ca1c30f7"
    },
    "resource": {
      "name": "Approver Approval To Implement - {{vars.input.records[0].title}}",
      "dueBy": "{{vars.input.records[0].dueDate}}",
      "assets": "{{vars.assetIRI}}",
      "status": "/api/3/picklists/7669725a-28cc-4b19-98a3-9ca71e0f88f4",
      "priority": "/api/3/picklists/539083a6-01f6-4ff9-a588-778cfdad4671",
      "recordTags": [
        "/api/3/tags/AssetChangeActivity"
      ],
      "description": "Approval to proceed with the implementation.",
      "assignedOnDate": "{{arrow.utcnow().int_timestamp}}",
      "assignedToPerson": "{{vars.steps.Assignee_And_Approver_Name.input.approverApprovalToImplement}}",
      "assetChangeActivities": "{{vars.input.records[0]['@id']}}"
    },
    "collection": "tasks",
    "step_variables": []
  },
  "status": null,
  "top": "1515",
  "left": "568",
  "stepType": "/api/3/workflow_st
```


## 2. Connector Operations

### 2.1 Connector × operation × title (counts)

| Connector | Operation | operationTitle(s) | Count |
|---|---|---|---|
| `activedirectory` | `get_specific_object_details` | Get Specific Object Details | 8 |
| `activedirectory` | `disable_user_account` | Disable User Account; Disable User Account  | 4 |
| `activedirectory` | `global_search` | Global Search | 4 |
| `activedirectory` | `get_all_object_details` | Get All Objects Details | 2 |
| `activedirectory` | `advanced_search` | Advanced Search | 2 |
| `activedirectory` | `reset_password` | Reset Password | 2 |
| `activedirectory` | `add_group_members` | Add Group Members | 1 |
| `activedirectory` | `add_object` | Add Object | 1 |
| `alienvault-otx` | `get_file_reputation` | Get File Reputation | 1 |
| `aws` | `detach_volume` | Detach Volume To Instance | 1 |
| `aws` | `detach_instance_from_autoscaling_group` | Detach Instance From Auto Scaling Group | 1 |
| `aws` | `attach_instance_to_auto_scaling_group` | Attach Instance To Auto Scaling Group | 1 |
| `aws` | `reboot_instance` | Reboot Instance | 1 |
| `aws` | `stop_instance` | Stop Instance | 1 |
| `aws` | `revoke_ingress` | Revoke Ingress | 1 |
| `aws` | `deregister_instance_from_elb` | Deregister Instance from ELB | 1 |
| `aws` | `get_details_for_all_images` | Get Details for All Images | 1 |
| `aws` | `attach_volume` | Attach Volume To Instance | 1 |
| `aws` | `add_tag_to_instance` | Add Tag to Instance | 1 |
| `aws` | `launch_instance` | Launch New Instance | 1 |
| `aws` | `delete_network_acl` | Delete Network ACL | 1 |
| `aws` | `delete_network_acl_rule` | Delete Network ACL Rule | 1 |
| `aws` | `add_security_group_to_instance` | Add Security Group to Instance | 1 |
| `aws` | `get_details_of_security_group` | Get Details of Security Group | 1 |
| `aws` | `describe_network_acls` | Get Details of Network ACLs | 1 |
| `aws` | `delete_security_group` | Delete Security Groups | 1 |
| `aws` | `register_instance_to_elb` | Register Instance To ELB | 1 |
| `aws` | `describe_user` | Describe User | 1 |
| `aws` | `start_instance` | Start Instance | 1 |
| `aws` | `get_security_groups` | Get Security Groups | 1 |
| `aws` | `authorize_egress` | Authorize Egress | 1 |
| `aws` | `add_network_acl_rule` | Add Network ACL Rule | 1 |
| `aws` | `revoke_egress` | Revoke Egress | 1 |
| `aws` | `delete_volume` | Delete Volume | 1 |
| `aws` | `instance_api_termination` | Instance API Termination | 1 |
| `aws` | `terminate_instance` | Terminate Instance | 1 |
| `aws` | `authorize_ingress` | Authorize Ingress | 1 |
| `aws` | `describe_instance` | Describe Instance | 1 |
| `aws` | `snapshot_volume` | Capture Volume Snapshot | 1 |
| `aws` | `create_security_group` | Create Security Groups | 1 |
| `aws` | `create_network_acl` | Create Network ACL | 1 |
| `aws-commands` | `authorize_ingress` | Authorize Ingress | 1 |
| `aws-commands` | `attach_volume` | Attach Volume | 1 |
| `aws-commands` | `detach_volume` | Detach Volume | 1 |
| `aws-commands` | `launch_instance` | Launch Instance | 1 |
| `aws-commands` | `describe_instance` | Get Instance Details | 1 |
| `aws-commands` | `delete_volume` | Delete Volume | 1 |
| `aws-commands` | `get_details_for_all_images` | Get AMIs Detail | 1 |
| `aws-commands` | `describe_user` | Get User Details | 1 |
| `aws-commands` | `get_details_of_security_group` | Get Details of Security Group | 1 |
| `aws-commands` | `revoke_egress` | Revoke Egress | 1 |
| `aws-commands` | `add_network_acl_rule` | Add Network ACL Rule | 1 |
| `aws-commands` | `add_security_group_to_instance` | Add Security Group To Instance | 1 |
| `aws-commands` | `authorize_egress` | Authorize Egress | 1 |
| `aws-commands` | `create_network_acl` | Create Network ACL | 1 |
| `aws-commands` | `generic_command` | Execute AWS Command | 1 |
| `aws-commands` | `terminate_instance` | Terminate Instance | 1 |
| `aws-commands` | `get_security_groups` | Get Security Groups | 1 |
| `aws-commands` | `revoke_all_active_sessions` | Revoke All Active Sessions | 1 |
| `aws-commands` | `instance_api_termination` | Instance API Termination  | 1 |
| `aws-commands` | `delete_security_group` | Delete Security Groups | 1 |
| `aws-commands` | `attach_instance_to_auto_scaling_group` | Attach Instance To Auto Scaling Group | 1 |
| `aws-commands` | `register_instance_to_elb` | Register Instance To ELB | 1 |
| `aws-commands` | `delete_network_acl` | Delete Network ACL | 1 |
| `aws-commands` | `deregister_instance_from_elb` | Deregister Instance from ELB | 1 |
| `aws-commands` | `revoke_ingress` | Revoke Ingress | 1 |
| `aws-commands` | `stop_instance` | Stop Instance | 1 |
| `aws-commands` | `create_security_group` | Create Security Groups | 1 |
| `aws-commands` | `reboot_instance` | Reboot Instance | 1 |
| `aws-commands` | `add_tag_to_instance` | Add Instance Tag | 1 |
| `aws-commands` | `delete_network_acl_rule` | Delete Network ACL Rule | 1 |
| `aws-commands` | `describe_network_acls` | Get Details of Network ACLs | 1 |
| `aws-commands` | `detach_instance_from_autoscaling_group` | Detach Instance From Auto Scaling Group | 1 |
| `aws-commands` | `snapshot_volume` | Capture Volume Snapshot | 1 |
| `aws-commands` | `start_instance` | Start Instance | 1 |
| `axios-assyst` | `close_ticket` | Close Ticket | 1 |
| `axios-assyst` | `update_ticket` | Update Ticket | 1 |
| `axios-assyst` | `get_ticket_details` | Get Ticket Details | 1 |
| `axios-assyst` | `search_tickets` | Search Tickets | 1 |
| `axios-assyst` | `create_ticket` | Create Ticket | 1 |
| `axonius` | `get_user_assets` | Get User Assets | 1 |
| `axonius` | `get_device_assets` | Get Device Assets | 1 |
| `carbonblack-response` | `get_process_list` | Get All Processes | 1 |
| `carbonblack-response` | `terminate_process` | Terminate Process | 1 |
| `cicd-utils` | `import_fortisoar_template` | Import FortiSOAR Template | 2 |
| `cicd-utils` | `review_import_fortisoar_template` | Review & Import FortiSOAR Template | 1 |
| `cicd-utils` | `export_fortisoar_template` | Export FortiSOAR Template | 1 |
| `cisa-advisory` | `get_advisory` | Get Advisory | 5 |
| `cisa-advisory` | `get_known_exploited_vulnerability_cves` | Get Known Exploited Vulnerability CVEs | 1 |
| `cisa-advisory` | `get_advisory_by_product` | Get Advisory By Product | 1 |
| `cisa-advisory` | `get_advisory_by_year` | Get Advisory By Year | 1 |
| `cisa-advisory` | `get_advisory_by_vendor` | Get Advisory By Vendor | 1 |
| `cisco-catalyst` | `get_version` | Get Version | 1 |
| `cisco-catalyst` | `configure_vlan` | Configure VLAN | 1 |
| `cisco-catalyst` | `get_config` | Get Configuration | 1 |
| `code-snippet` | `python_inline_code_editor` | Execute Python Code | 4 |
| `crowd-strike-falcon` | `alert_search` | Alert Search | 3 |
| `crowd-strike-falcon` | `get_detection_details` | Get Detection Details | 3 |
| `crowd-strike-falcon` | `detection_search` | Detection Search | 3 |
| `crowd-strike-falcon` | `get_alert_details` | Get Alert Details | 3 |
| `crowd-strike-falcon` | `process_details` | Get Process Details | 1 |
| `crowd-strike-falcon` | `get_quarantine_files_count` | Get Quarantine Files Count | 1 |
| `crowd-strike-falcon` | `search_vulnerabilities` | Spotlight: Search Vulnerabilities | 1 |
| `crowd-strike-falcon` | `hunt_file` | Hunt File | 1 |
| `crowd-strike-falcon` | `list_ioc` | Get IOCs | 1 |
| `crowd-strike-falcon` | `search_devices` | Search Devices | 1 |
| `crowd-strike-falcon` | `incidents_get_details` | Get Incident Details | 1 |
| `crowd-strike-falcon` | `list_usernames` | Get Usernames List | 1 |
| `crowd-strike-falcon` | `get_uid` | Get User ID | 1 |
| `crowd-strike-falcon` | `admin_cmd_run` | Run Admin Command | 1 |
| `crowd-strike-falcon` | `get_custom_ioa_rule_name` | Get Custom IOA Rule Name | 1 |
| `crowd-strike-falcon` | `incidents_get_crowdscores` | Get Incidents Crowdstrike Score | 1 |
| `crowd-strike-falcon` | `apply_action_on_quarantine_files_by_query` | Apply Action On Quarantine Files By Query | 1 |
| `crowd-strike-falcon` | `put_files_list` | Get Executable List | 1 |
| `crowd-strike-falcon` | `get_ioc` | Get IOC Details | 1 |
| `crowd-strike-falcon` | `session_file_list` | Download Session File List | 1 |
| `crowd-strike-falcon` | `remove_containment` | Remove Containment | 1 |
| `crowd-strike-falcon` | `alert_aggregates` | Alert Aggregates | 1 |
| `crowd-strike-falcon` | `update_alert` | Update Alert | 1 |
| `crowd-strike-falcon` | `get_cve_list_by_vulnerability` | Spotlight: Get CVE List by Vulnerability | 1 |
| `crowd-strike-falcon` | `session_file_download` | Download Session File | 1 |
| `crowd-strike-falcon` | `list_user_id` | Get User IDs List | 1 |
| `crowd-strike-falcon` | `upload_ioc` | Create IOC | 1 |
| `crowd-strike-falcon` | `remove_host_from_host_group` | Remove Host From Host Group | 1 |
| `crowd-strike-falcon` | `get_host_list_by_vulnerability` | Spotlight: Get Host List by Vulnerability | 1 |
| `crowd-strike-falcon` | `get_quarantine_files` | Get Quarantine Files List | 1 |
| `crowd-strike-falcon` | `get_host_group_list` | Get Host Group List | 1 |
| `crowd-strike-falcon` | `get_quarantine_files_metadata` | Get Quarantine Files Metadata | 1 |
| `crowd-strike-falcon` | `get_quarantine_files_aggregates` | Get Quarantine Files Aggregates | 1 |
| `crowd-strike-falcon` | `get_user_details` | Get User Details | 1 |
| `crowd-strike-falcon` | `apply_action_on_quarantine_files_by_file_id` | Apply Action On Quarantine Files By File ID | 1 |
| `crowd-strike-falcon` | `delete_ioc` | Delete IOC | 1 |
| `crowd-strike-falcon` | `update_detection` | Update Detection | 1 |
| `crowd-strike-falcon` | `scripts_get` | Get Scripts Details by IDs | 1 |
| `crowd-strike-falcon` | `put_files_get` | Get Executables Details by IDs | 1 |
| `crowd-strike-falcon` | `create_on_demand_scan` | Create On Demand Scan | 1 |
| `crowd-strike-falcon` | `admin_cmd_result` | Get Admin Command Result | 1 |
| `crowd-strike-falcon` | `incidents_query` | Search Incidents | 1 |
| `crowd-strike-falcon` | `detection_aggregates` | Detection Aggregates | 1 |
| `crowd-strike-falcon` | `hunt_domain` | Hunt Domain | 1 |
| `crowd-strike-falcon` | `get_device_online_status` | Get Device Online Status | 1 |
| `crowd-strike-falcon` | `update_incidents` | Update Incidents Status | 1 |
| `crowd-strike-falcon` | `get_scan_by_id` | Get Scan By ID | 1 |
| `crowd-strike-falcon` | `list_endpoint` | Get Endpoint List | 1 |
| `crowd-strike-falcon` | `add_host_to_host_group` | Add Host To Host Group | 1 |
| `crowd-strike-falcon` | `device_details` | Get Device Details | 1 |
| `crowd-strike-falcon` | `scripts_list` | Get Scripts List | 1 |
| `crowd-strike-falcon` | `get_list_of_processes` | Get Processes Related to IOC | 1 |
| `crowd-strike-falcon` | `quarantine_device` | Contain the Host | 1 |
| `crowd-strike-falcon` | `execute_an_api_request` | Execute an API Request | 1 |
| `crowd-strike-falcon` | `update_ioc` | Update IOC | 1 |
| `csv-data-management` | `extract_data_from_csv` | Extract Data from Single CSV | 10 |
| `csv-data-management` | `merge_two_csv_and_extract_data` | Merge and Extract Data from two CSV | 2 |
| `csv-data-management` | `join_two_csv_and_extract_data` | Join and Extract Data from two CSV | 2 |
| `csv-data-management` | `concat_two_csv_and_extract_data` | Concat and Extract Data from two CSV | 1 |
| `csv-data-management` | `convert_json_to_csv_file` | Convert JSON to CSV File | 1 |
| `cyops-schedule-report` | `schedule_report_manual` | Generate Report From Report ID | 2 |
| `cyops-system-monitoring` | `cpu_percent` | CPU Utilization | 1 |
| `cyops-system-monitoring` | `disk_utilization` | Disk Utilization | 1 |
| `cyops-system-monitoring` | `service_status` | Service Status | 1 |
| `cyops-system-monitoring` | `virtual_memory` | Virtual Memory Utilization | 1 |
| `cyops_utilities` | `make_cyops_request` | CyOPs: Make CyOPs API Call; FSR: Make FortiSOAR API Call | 71 |
| `cyops_utilities` | `no_op` | Utils: No Operation | 66 |
| `cyops_utilities` | `updatemacro` | CyOPs: Update Global Variables; CyOPs: Update Macro; FSR: Create/Update Global Variables; FSR: Update Global Variables | 30 |
| `cyops_utilities` | `format_richtext` | Utils: Format as RichText; Utils: Format as RichText (Markdown) | 28 |
| `cyops_utilities` | `json_to_html` | Utils: Convert JSON into a HTML Table | 13 |
| `cyops_utilities` | `raise_exception` | Utils: Raise Exception | 5 |
| `cyops_utilities` | `download_file_from_cyops` | File: Compute Hash | 4 |
| `cyops_utilities` | `upload_file_to_cyops` | File: Upload a file in the system and Create an Attachment; File: Upload a file to CyOPs and Create an Attachment | 4 |
| `cyops_utilities` | `create_cyops_attachment` | File: Create Attachment from File; File: Create CyOPs Attachment from File | 4 |
| `cyops_utilities` | `ip_cidr_check` | Utils: Is IP in CIDR | 4 |
| `cyops_utilities` | `extract_email_metadata_new` | Email: Extracts email's metadata from email file | 3 |
| `cyops_utilities` | `download_file_from_url` | File: Download File from URL | 3 |
| `cyops_utilities` | `query_cyops_resource` | FSR: Find Record | 3 |
| `cyops_utilities` | `parse_cef` | FSR: Parse CEF String to JSON. | 2 |
| `cyops_utilities` | `extract_artifacts` | FSR: Extract Artifacts from String | 1 |
| `cyops_utilities` | `html_table_to_dictionary` | Utils: Convert HTML Table to Dictionary | 1 |
| `cyops_utilities` | `create_file_from_string` | File: Create File from String | 1 |
| `cyops_utilities` | `format_richtext_html` | Utils: Format as RichText (HTML) | 1 |
| `darktrace` | `execute_api_request` | Execute an API Request | 1 |
| `darktrace` | `get_incidents` | Get Incidents | 1 |
| `darktrace` | `get_enums` | Get Enums | 1 |
| `darktrace` | `search_query` | Search Query | 1 |
| `darktrace` | `get_models` | Get Models | 1 |
| `darktrace` | `get_entity_details` | Get Entity Details | 1 |
| `darktrace` | `get_components` | Get Components | 1 |
| `darktrace` | `get_breach_details` | Get Breach Details | 1 |
| `darktrace` | `get_similar_devices` | Get Similar Devices | 1 |
| `darktrace` | `create_manual_antigena` | Create Manual Antigena | 1 |
| `darktrace` | `get_watch_list` | Get Watch List | 1 |
| `darktrace` | `get_antigena_summary` | Get Antigena Summary | 1 |
| `darktrace` | `remove_from_list` | Remove From Watch List | 1 |
| `darktrace` | `get_antigena` | Get Antigena List | 1 |
| `darktrace` | `get_mb_comments` | Get Model Breach Comments | 1 |
| `darktrace` | `acknowledge_breach` | Acknowledge Breach | 1 |
| `darktrace` | `get_model_breaches` | Get Model Breaches | 1 |
| `darktrace` | `update_antigena` | Update Antigena | 1 |
| `darktrace` | `get_external_endpoint_details` | Get External Endpoint Details | 1 |
| `darktrace` | `add_to_list` | Add To Watch List | 1 |
| `darktrace` | `get_device_information` | Get Device Information | 1 |
| `darktrace` | `get_devices` | Get Devices | 1 |
| `darktrace` | `get_comments` | Get Comments | 1 |
| `darktrace` | `unacknowledge_breach` | Unacknowledge Breach | 1 |
| `dns` | `lookup_ip` | Lookup IP | 1 |
| `dns` | `lookup_domain` | Lookup FQDN/Domain | 1 |
| `exchange` | `send_email` | Send Email | 7 |
| `exchange` | `delete_email` | Delete Email | 1 |
| `exchange` | `run_query` | Search Email | 1 |
| `exploit-prediction-scoring-system` | `get_epss_score_by_cve_id` | Get EPSS Score By CVE ID | 2 |
| `exploit-prediction-scoring-system` | `get_epss_score` | Get EPSS Score | 1 |
| `file-content-extraction` | `extract_text` | Extract Text | 4 |
| `file-content-extraction` | `get_backend_config` | Get Backend Config | 1 |
| `file-content-extraction` | `create_xslx_file_from_json_data` | Create XSLX file as attachment from JSON Data | 1 |
| `file-content-extraction` | `extract_indicators_from_file` | Extract Artifacts Extended | 1 |
| `fortigate-firewall` | `block_ip` | Block IP Address | 6 |
| `fortigate-firewall` | `quarantine_host` | Quarantine Host | 2 |
| `fortigate-firewall` | `update_policy` | Update Policy | 2 |
| `fortigate-firewall` | `block_url` | Block URL | 2 |
| `fortigate-firewall` | `get_system_events` | Get System Events | 1 |
| `fortigate-firewall` | `unquarantine_host` | Unquarantine Host | 1 |
| `fortigate-firewall` | `delete_policy` | Delete Policy | 1 |
| `fortigate-firewall` | `get_address_groups` | Get Address Groups | 1 |
| `fortigate-firewall` | `get_users` | Get Users | 1 |
| `fortigate-firewall` | `get_blocked_urls` | Get Blocked URLs | 1 |
| `fortigate-firewall` | `unblock_ip` | Unblock IP Address | 1 |
| `fortigate-firewall` | `create_address` | Create Address | 1 |
| `fortigate-firewall` | `block_ip_new` | Block IP Address | 1 |
| `fortigate-firewall` | `update_address` | Update Address | 1 |
| `fortigate-firewall` | `delete_address_group` | Delete Address Group | 1 |
| `fortigate-firewall` | `unblock_url` | Unblock URL | 1 |
| `fortigate-firewall` | `get_firewall_services` | Get Firewall Services | 1 |
| `fortigate-firewall` | `get_addresses` | Get Addresses | 1 |
| `fortigate-firewall` | `create_service_group` | Create Service Group | 1 |
| `fortigate-firewall` | `get_list_of_policies` | Get List of Policies | 1 |
| `fortigate-firewall` | `update_firewall_service` | Update Firewall Service | 1 |
| `fortigate-firewall` | `create_firewall_service` | Create Firewall Service | 1 |
| `fortigate-firewall` | `update_service_group` | Update Service Group | 1 |
| `fortigate-firewall` | `block_applications` | Block Application | 1 |
| `fortigate-firewall` | `create_address_group` | Create Address Group | 1 |
| `fortigate-firewall` | `create_policy` | Create Policy | 1 |
| `fortigate-firewall` | `delete_user` | Delete User | 1 |
| `fortigate-firewall` | `get_service_groups` | Get Service Groups | 1 |
| `fortigate-firewall` | `unblock_applications` | Unblock Application | 1 |
| `fortigate-firewall` | `get_entries_from_edl` | Get Entries from External Dynamic List | 1 |
| `fortigate-firewall` | `get_blocked_applications` | Get Blocked Applications | 1 |
| `fortigate-firewall` | `update_address_group` | Update Address Group | 1 |
| `fortigate-firewall` | `modify_entries_in_edl` | Modify Entries in External Dynamic List | 1 |
| `fortigate-firewall` | `delete_service_group` | Delete Service Group | 1 |
| `fortigate-firewall` | `get_quarantine_hosts` | Get Quarantine Hosts | 1 |
| `fortigate-firewall` | `create_user` | Create User | 1 |
| `fortigate-firewall` | `delete_firewall_service` | Delete Firewall Service | 1 |
| `fortigate-firewall` | `delete_address` | Delete Address | 1 |
| `fortigate-firewall` | `get_list_of_applications` | Get Applications Detail | 1 |
| `fortigate-firewall` | `get_blocked_ip` | Get Blocked IP Addresses | 1 |
| `fortigate-firewall` | `execute_command` | Execute Command | 1 |
| `fortigate-firewall` | `get_user_list_login_details` | Get User Last Login Details | 1 |
| `fortigate-firewall` | `update_user` | Update User | 1 |
| `fortinet-fortiai` | `submit_file` | Submit File | 1 |
| `fortinet-fortiai` | `get_file_verdict_results` | Get File Verdict Result | 1 |
| `fortinet-fortiai` | `get_events` | Get Events | 1 |
| `fortinet-fortiai-proxy` | `create_responses` | Create Response | 1 |
| `fortinet-fortiai-proxy` | `chat_completion` | Make a chat_completion API call | 1 |
| `fortinet-fortiai-proxy` | `get_token_balance_info` | Get Token Balance Information | 1 |
| `fortinet-fortianalyzer` | `get_alerts_for_multiple_adoms` | Get Event for Multiple ADOMs | 3 |
| `fortinet-fortianalyzer` | `get_reports` | Get Reports | 2 |
| `fortinet-fortianalyzer` | `get_device_info` | Get Device Information | 2 |
| `fortinet-fortianalyzer` | `count_alerts_for_multiple_adoms` | Count Events for Multiple ADOMs | 2 |
| `fortinet-fortianalyzer` | `get_schedules` | List Schedules | 2 |
| `fortinet-fortianalyzer` | `start_and_fetch_bulk_device_logs` | Start and fetch bulk device logs | 1 |
| `fortinet-fortianalyzer` | `get_events_for_incident` | Get Events For Incident | 1 |
| `fortinet-fortianalyzer` | `get_log_file_content` | Get Log-File Content | 1 |
| `fortinet-fortianalyzer` | `list_incidents_for_multiple_adoms` | Get Incident for Multiple ADOMs | 1 |
| `fortinet-fortianalyzer` | `get_attachments_for_incident` | Get Attachments For Incident | 1 |
| `fortinet-fortianalyzer` | `fetch_log_search_result_by_task_id` | Fetch Log Search Result by Task ID | 1 |
| `fortinet-fortianalyzer` | `list_incidents` | Fetch Incidents | 1 |
| `fortinet-fortianalyzer` | `start_bulk_device_log_search_request` | Start bulk device log Search Request | 1 |
| `fortinet-fortianalyzer` | `update_incident_details` | Update Incident | 1 |
| `fortinet-fortianalyzer` | `authorize_device` | Authorize Device | 1 |
| `fortinet-fortianalyzer` | `add_slave_device` | Add a Secondary Device | 1 |
| `fortinet-fortianalyzer` | `get_log_status` | Get Log Status | 1 |
| `fortinet-fortianalyzer` | `get_devices` | Get Devices | 1 |
| `fortinet-fortianalyzer` | `list_log_fields` | List Log Fields | 1 |
| `fortinet-fortianalyzer` | `add_attachment` | Add Incident Attachment | 1 |
| `fortinet-fortianalyzer` | `get_endpoints` | List Endpoints | 1 |
| `fortinet-fortianalyzer` | `get_alert_event_logs` | Get Alert Event Logs | 1 |
| `fortinet-fortianalyzer` | `log_search_over_log_file` | Log Search over Log-File | 1 |
| `fortinet-fortianalyzer` | `add_new_device` | Add a New Device | 1 |
| `fortinet-fortianalyzer` | `get_outbreak_alerts_summary` | Get Outbreak Alerts Summary | 1 |
| `fortinet-fortianalyzer` | `get_users` | List Users | 1 |
| `fortinet-fortianalyzer` | `get_adoms` | Get ADOMs | 1 |
| `fortinet-fortianalyzer` | `create_incident` | Create Incident | 1 |
| `fortinet-fortianalyzer` | `get_incident_assets` | Get Incident Assets | 1 |
| `fortinet-fortianalyzer` | `count_incidents_for_multiple_adoms` | Count Incidents for Multiple ADOMs | 1 |
| `fortinet-fortianalyzer` | `delete_device` | Delete a Device | 1 |
| `fortinet-fortianalyzer` | `start_log_search_request` | Start Log Search Request | 1 |
| `fortinet-fortianalyzer` | `json_rpc_freeform` | Execute an API Request | 1 |
| `fortinet-fortianalyzer` | `get_log_file_state` | Get Log-File State | 1 |
| `fortinet-fortianalyzer` | `get_generated_report` | Get Generated Report | 1 |
| `fortinet-fortianalyzer` | `get_alerts` | Get Alerts | 1 |
| `fortinet-fortianalyzer` | `run_report` | Run Report | 1 |
| `fortinet-fortianalyzer` | `add_master_device` | Add a Primary Device | 1 |
| `fortinet-fortianalyzer` | `update_attachment` | Update Incident Attachment | 1 |
| `fortinet-fortiauthenticator` | `get_users` | Get Local User List; Get Local Users | 2 |
| `fortinet-fortiauthenticator` | `get_ldap_user_list` | Get LDAP User List | 2 |
| `fortinet-fortiauthenticator` | `get_schema` | Get Schema | 2 |
| `fortinet-fortiauthenticator` | `get_ldap_user` | Get Specific LDAP User | 2 |
| `fortinet-fortiauthenticator` | `update_ldapuser_status` | Update LDAP User Status | 2 |
| `fortinet-fortiauthenticator` | `update_radiususer_status` | Update Radius User Status | 1 |
| `fortinet-fortiauthenticator` | `get_radius_user` | Get Specific Radius User | 1 |
| `fortinet-fortiauthenticator` | `create_local_user` | Create Local User | 1 |
| `fortinet-fortiauthenticator` | `update_user_status` | Update Local User Status | 1 |
| `fortinet-fortiauthenticator` | `get_userlockout_policy` | Get User Lockout Policy Info | 1 |
| `fortinet-fortiauthenticator` | `get_local_user` | Get Specific Local User | 1 |
| `fortinet-fortiauthenticator` | `get_radius_user_list` | Get Radius User List | 1 |
| `fortinet-forticlient-ems` | `delete_custom_tag` | Delete Custom Tag | 1 |
| `fortinet-forticlient-ems` | `get_zero_trust_rule_sets` | Get Zero Trust Rule Sets List | 1 |
| `fortinet-forticlient-ems` | `get_zero_trust_tag_by_id` | Get Zero Trust Tag By ID | 1 |
| `fortinet-forticlient-ems` | `remove_custom_tag` | Remove Custom Tag From Endpoint | 1 |
| `fortinet-forticlient-ems` | `get_endpoints` | Get All Endpoints | 1 |
| `fortinet-forticlient-ems` | `create_custom_tag` | Create Custom Tag | 1 |
| `fortinet-forticlient-ems` | `add_custom_tag` | Add Custom Tag to Endpoint | 1 |
| `fortinet-forticlient-ems` | `delete_zero_trust_tag` | Delete Zero Trust Tag | 1 |
| `fortinet-forticlient-ems` | `get_zero_trust_rule_tags` | Get Zero Trust Rule Tags List | 1 |
| `fortinet-forticlient-ems` | `unquarantine_endpoints` | Unquarantine Endpoints | 1 |
| `fortinet-forticlient-ems` | `create_zero_trust_tag` | Create Zero Trust Tag | 1 |
| `fortinet-forticlient-ems` | `get_endpoint_details` | Get Endpoint Details | 1 |
| `fortinet-forticlient-ems` | `quarantine_endpoints` | Quarantine Endpoints | 1 |
| `fortinet-forticnapp` | `search_alerts` | Search Alerts | 3 |
| `fortinet-forticnapp` | `add_comment_to_alert` | Add Comment to Alert | 1 |
| `fortinet-forticnapp` | `close_alert` | Close Alert | 1 |
| `fortinet-forticnapp` | `send_custom_request` | Execute an API Call | 1 |
| `fortinet-forticnapp` | `get_alert_details` | Get Alerts Details | 1 |
| `fortinet-forticnapp` | `get_alert_entities` | Get Alert Entities | 1 |
| `fortinet-forticnapp` | `search_configuration` | Search Configuration | 1 |
| `fortinet-forticnapp` | `search_container_vulnerabilities` | Search Container Vulnerabilities | 1 |
| `fortinet-forticnapp` | `search_host_vulnerabilities` | Search Host Vulnerabilities | 1 |
| `fortinet-forticnapp` | `lql_query` | Run LQL Query | 1 |
| `fortinet-forticnapp` | `get_alert_entity_details` | Get Alert Entity Details | 1 |
| `fortinet-fortideceptor` | `decoy_stop` | Stop Decoy | 1 |
| `fortinet-fortideceptor` | `decoy_start` | Start Decoy | 1 |
| `fortinet-fortideceptor` | `get_attack_events` | Get Attack Events | 1 |
| `fortinet-fortideceptor` | `decoy_deploy` | Deploy Decoy | 1 |
| `fortinet-fortideceptor` | `decoy_delete` | Delete Decoy | 1 |
| `fortinet-fortideceptor` | `get_templates` | Get Templates | 1 |
| `fortinet-fortideceptor` | `deploy_nets` | Get Deployment Networks | 1 |
| `fortinet-fortideceptor` | `get_attack_incidents` | Get Attack Incidents | 1 |
| `fortinet-fortideceptor` | `get_decoy` | Get Decoy | 1 |
| `fortinet-fortidlp` | `get_incidents_list` | Get Incidents List | 4 |
| `fortinet-fortidlp` | `get_users_list` | Get Users List | 1 |
| `fortinet-fortidlp` | `add_labels_to_agents` | Add Labels to Agents | 1 |
| `fortinet-fortidlp` | `get_label_details` | Get Label Details | 1 |
| `fortinet-fortidlp` | `update_incidents_by_id` | Update Incidents | 1 |
| `fortinet-fortidlp` | `get_user_details` | Get User Details | 1 |
| `fortinet-fortidlp` | `get_pending_in_flight_actions_list` | Get Pending In-Flight Actions List | 1 |
| `fortinet-fortidlp` | `agent_action_request` | Agent Action Request | 1 |
| `fortinet-fortidlp` | `get_incidents_by_id` | Get Incidents By ID | 1 |
| `fortinet-fortidlp` | `get_available_actions_list` | Get Available Actions List | 1 |
| `fortinet-fortidlp` | `get_agent_details` | Get Agent Details | 1 |
| `fortinet-fortidlp` | `send_custom_request` | Execute an API Request | 1 |
| `fortinet-fortidlp` | `get_labels_list` | Get Labels List | 1 |
| `fortinet-fortidlp` | `add_labels_to_users` | Add Labels to Users | 1 |
| `fortinet-fortidlp` | `get_events_from_event_streaming` | Get Events from Event Streaming | 1 |
| `fortinet-fortidlp` | `get_agents_list` | Get Agents List | 1 |
| `fortinet-fortidlp` | `get_audit_logs` | Get Audit Logs | 1 |
| `fortinet-fortidlp` | `get_configured_streams_list` | Get Configured Streams List | 1 |
| `fortinet-fortiedr` | `get_event_list` | Get Events | 2 |
| `fortinet-fortiedr` | `isolate_collector` | Isolate Collector | 2 |
| `fortinet-fortiedr` | `update_ipset` | Update IPSet | 1 |
| `fortinet-fortiedr` | `remediate_device` | Remediate Device | 1 |
| `fortinet-fortiedr` | `update_collector_installer` | Update Collector Installer | 1 |
| `fortinet-fortiedr` | `count_events` | Get Event Count | 1 |
| `fortinet-fortiedr` | `get_agent_group` | Get Agent Groups | 1 |
| `fortinet-fortiedr` | `get_system_summary` | Get System Summary | 1 |
| `fortinet-fortiedr` | `get_event_list_extended` | Get Event List Extended | 1 |
| `fortinet-fortiedr` | `update_event` | Update Events | 1 |
| `fortinet-fortiedr` | `update_exception` | Update Exception | 1 |
| `fortinet-fortiedr` | `search_ioc` | Search IOC | 1 |
| `fortinet-fortiedr` | `get_event_by_id` | Get Event by ID | 1 |
| `fortinet-fortiedr` | `get_event_file` | Retrieve File or Memory | 1 |
| `fortinet-fortiedr` | `get_file` | Get File | 1 |
| `fortinet-fortiedr` | `create_ipset` | Create IPSet | 1 |
| `fortinet-fortiedr` | `generic_rest_api_call` | Execute an API Request | 1 |
| `fortinet-fortiedr` | `list_exception` | Get Exception List | 1 |
| `fortinet-fortiedr` | `set_collector_state` | Set Collector State | 1 |
| `fortinet-fortiedr` | `unisolate_collector` | Unisolate Collector | 1 |
| `fortinet-fortiedr` | `delete_ipset` | Delete IPSet | 1 |
| `fortinet-fortiedr` | `get_event_exceptions` | Get Event Exceptions | 1 |
| `fortinet-fortiedr` | `get_raw_json_event_data` | Get Raw JSON Event Data | 1 |
| `fortinet-fortiedr` | `move_collectors` | Move Collectors | 1 |
| `fortinet-fortiedr` | `search` | Search Filehash | 1 |
| `fortinet-fortiedr` | `get_ipset_list` | Get IPSet List | 1 |
| `fortinet-fortiedr` | `get_organizations` | Get Organizations | 1 |
| `fortinet-fortiedr` | `get_raw_data_items` | Get Raw Data Items | 1 |
| `fortinet-fortiedr` | `create_exception` | Create Exception | 1 |
| `fortinet-fortiedr` | `get_collector_installers` | Get Collector Installers | 1 |
| `fortinet-fortiedr` | `get_collector_list` | Get Collector List | 1 |
| `fortinet-fortiguard-ioc` | `get_selected_ioc_fields` | Get Selected IOC Fields | 1 |
| `fortinet-fortiguard-ioc` | `get_visiting_countries` | Get Visiting Countries | 1 |
| `fortinet-fortiguard-ioc` | `get_risk_distribution` | Get Risk Distribution | 1 |
| `fortinet-fortiguard-ioc` | `execute_an_api_request` | Execute an API Request | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_alert_threat_actor_details_by_id` | Get Outbreak Alert Threat Actor Details by ID | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_alert_details_by_slug_name` | Get Outbreak Alert Details by Slug Name | 1 |
| `fortinet-fortiguard-outbreak` | `list_threat_actors` | List Threat Actors | 1 |
| `fortinet-fortiguard-outbreak` | `list_outbreak_alert_details` | List Outbreak Alert Details | 1 |
| `fortinet-fortiguard-outbreak` | `bulk_ingest_outbreak_alert_iocs` | Bulk Ingest Outbreak Alert IOCs | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_alert_iocs` | Get Outbreak Alert IOCs | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_threat_heat_map_details` | Get Outbreak Threat Heat Map Details | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_threat_live_map_details` | Get Outbreak Threat Live Map Details | 1 |
| `fortinet-fortiguard-outbreak` | `list_outbreak_alert_tags` | List Outbreak Alert Tags | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_top_threats` | Get Outbreak Top Threats | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_top_industries` | Get Outbreak Top Industries | 1 |
| `fortinet-fortiguard-outbreak` | `get_outbreak_top_countries` | Get Outbreak Top Countries | 1 |
| `fortinet-fortiguard-threat-intelligence` | `threat_intel_search` | Threat Intel Search | 2 |
| `fortinet-fortiguard-threat-intelligence` | `threat_activities_statistics_by_country` | Get Threat Activity Statistics By Country | 2 |
| `fortinet-fortiguard-threat-intelligence` | `ingest_feeds` | Fetch Threat Intel Feeds | 2 |
| `fortinet-fortiguard-threat-intelligence` | `threat_activities_statistics` | Get Threat Activity Statistics | 2 |
| `fortinet-fortiguard-threat-intelligence` | `threat_activities_statistics_by_industry` | Get Threat Activity Statistics By Industry | 2 |
| `fortinet-fortiguard-threat-intelligence` | `threat_activities_statistics_by_country_and_industry` | Get Threat Activity Statistics By Country and Industry | 2 |
| `fortinet-fortiguard-threat-intelligence` | `ioc_search` | IOC Search | 2 |
| `fortinet-fortiguard-threat-intelligence` | `get_industry_list` | Get Industry List | 1 |
| `fortinet-fortiguard-threat-intelligence` | `threat_count_country_threat` | Get Threat Count by Country and Threat | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_threats_by_country` | Get Top Threats by Country | 1 |
| `fortinet-fortiguard-threat-intelligence` | `kill_chain_metrics_industry` | Get Kill Chain Metrics by Industry | 1 |
| `fortinet-fortiguard-threat-intelligence` | `kill_chain_metrics_country_industry` | Get Kill Chain Metrics by Country & Industry | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_countries_industry` | Get Top Countries by Industry | 1 |
| `fortinet-fortiguard-threat-intelligence` | `threat_count_industry_threat` | Get Threat Count by Industry and Threat | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_threats` | Get Top Threats | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_industries_threat` | Top Industries by Threat | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_industries_country` | Get Top Industries by Country | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_threat_countries` | Get Top Threat Countries | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_threat_industries` | Get Top Threat Industries | 1 |
| `fortinet-fortiguard-threat-intelligence` | `kill_chain_metrics` | Get Kill Chain Metrics | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_threats_country_industry` | Get Top Threats by Country and Industry | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_threats_by_industry` | Get Top Threats by Industry | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_countries_industry_threat` | Get Top Countries by Industry and Threat | 1 |
| `fortinet-fortiguard-threat-intelligence` | `get_encyclopedia_lookup` | Get Encyclopedia Lookup | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_industries_country_threat` | Get Top Industries by Country and Threat | 1 |
| `fortinet-fortiguard-threat-intelligence` | `threat_count_industry_country_threat` | Get Threat Count by Industry and Country and Threat | 1 |
| `fortinet-fortiguard-threat-intelligence` | `get_threat_categories` | Get Threat Categories | 1 |
| `fortinet-fortiguard-threat-intelligence` | `get_threat_signal_report` | Get Threat Signal Report by Slug Name | 1 |
| `fortinet-fortiguard-threat-intelligence` | `kill_chain_metrics_country` | Get Kill Chain Metrics by Country | 1 |
| `fortinet-fortiguard-threat-intelligence` | `get_country_list` | Get Country List | 1 |
| `fortinet-fortiguard-threat-intelligence` | `fetch_fortiguard_reports` | Fetch FortiGuard Reports | 1 |
| `fortinet-fortiguard-threat-intelligence` | `get_secnews` | Get Cybersecurity News | 1 |
| `fortinet-fortiguard-threat-intelligence` | `top_countries_threat` | Top Countries by Threat | 1 |
| `fortinet-fortimail` | `block_sender_address` | Block Sender Address | 1 |
| `fortinet-fortimanager` | `get_incidents` | List Incident | 3 |
| `fortinet-fortimanager` | `get_incident_events` | Get Events Related to Incident | 2 |
| `fortinet-fortimanager` | `update_policy_package` | Update Policy Package | 1 |
| `fortinet-fortimanager` | `create_ldap_server` | Create LDAP Server | 1 |
| `fortinet-fortimanager` | `update_custom_service` | Update Custom Service | 1 |
| `fortinet-fortimanager` | `delete_address_group` | Delete Address Group | 1 |
| `fortinet-fortimanager` | `delete_policy_package` | Delete Policy Package | 1 |
| `fortinet-fortimanager` | `get_service_categories` | Get Service Categories List | 1 |
| `fortinet-fortimanager` | `create_address` | Create Address | 1 |
| `fortinet-fortimanager` | `reinstall_policy` | Re-install Policy | 1 |
| `fortinet-fortimanager` | `global_block_ip` | Global Level Block IP Address | 1 |
| `fortinet-fortimanager` | `adom_block_ip` | ADOM Level Block IP Address | 1 |
| `fortinet-fortimanager` | `update_address_group` | Update Address Group | 1 |
| `fortinet-fortimanager` | `delete_service_group` | Delete Service Group | 1 |
| `fortinet-fortimanager` | `update_service_group` | Update Service Group | 1 |
| `fortinet-fortimanager` | `get_devices` | Get Device List | 1 |
| `fortinet-fortimanager` | `get_device_groups` | Get Device Groups List | 1 |
| `fortinet-fortimanager` | `update_ldap_server` | Update LDAP Server | 1 |
| `fortinet-fortimanager` | `get_adom_policy_package` | List ADOM Policy Package | 1 |
| `fortinet-fortimanager` | `get_list_of_applications` | Get Applications Detail | 1 |
| `fortinet-fortimanager` | `delete_address` | Delete Address | 1 |
| `fortinet-fortimanager` | `get_ldap_server` | Get LDAP Server List | 1 |
| `fortinet-fortimanager` | `get_dynamic_interface` | Get Dynamic Interface List | 1 |
| `fortinet-fortimanager` | `update_user_group` | Update User Group | 1 |
| `fortinet-fortimanager` | `get_application_control_list` | Get Applications Control List | 1 |
| `fortinet-fortimanager` | `create_user_group` | Create User Group | 1 |
| `fortinet-fortimanager` | `update_incident` | Update Incident | 1 |
| `fortinet-fortimanager` | `create_custom_service` | Create Custom Service | 1 |
| `fortinet-fortimanager` | `get_alert_event` | Get Events | 1 |
| `fortinet-fortimanager` | `global_unblock_ip` | Global Level Unblock IP Address | 1 |
| `fortinet-fortimanager` | `get_global_policy_package` | List Global Policy Package | 1 |
| `fortinet-fortimanager` | `create_address_group` | Create Address Group | 1 |
| `fortinet-fortimanager` | `get_adom_blocked_ip` | ADOM Level Get Blocked IP Addresses | 1 |
| `fortinet-fortimanager` | `get_addresses` | Get Addresses List | 1 |
| `fortinet-fortimanager` | `update_ssl_vpn` | Update SSL VPN Settings | 1 |
| `fortinet-fortimanager` | `install_policy` | Install Policy | 1 |
| `fortinet-fortimanager` | `update_policy` | Update Firewall Policy | 1 |
| `fortinet-fortimanager` | `get_web_filter` | Get Web Filter List | 1 |
| `fortinet-fortimanager` | `get_global_policy` | List Global Firewall Policy | 1 |
| `fortinet-fortimanager` | `get_custom_service` | Get Custom Services List | 1 |
| `fortinet-fortimanager` | `update_address` | Update Address | 1 |
| `fortinet-fortimanager` | `install_policy_status` | Get Installation Policy Package Status | 1 |
| `fortinet-fortimanager` | `create_policy` | Create Firewall Policy | 1 |
| `fortinet-fortimanager` | `get_global_blocked_ip` | Global Level Get Blocked IP Addresses | 1 |
| `fortinet-fortimanager` | `block_applications` | Block Application | 1 |
| `fortinet-fortimanager` | `unblock_applications` | Unblock Application | 1 |
| `fortinet-fortimanager` | `block_url` | Block URL | 1 |
| `fortinet-fortimanager` | `global_assign_policy` | Assign Global Policy Package | 1 |
| `fortinet-fortimanager` | `get_service_group` | Get Service Groups List | 1 |
| `fortinet-fortimanager` | `delete_ldap_server` | Delete LDAP Server | 1 |
| `fortinet-fortimanager` | `delete_user_group` | Delete User Group | 1 |
| `fortinet-fortimanager` | `create_service_group` | Create Service Group | 1 |
| `fortinet-fortimanager` | `create_policy_package` | Create Policy Package | 1 |
| `fortinet-fortimanager` | `get_address_groups` | Get Address Groups List | 1 |
| `fortinet-fortimanager` | `get_blocked_urls` | Get Blocked URLs | 1 |
| `fortinet-fortimanager` | `get_ssl_vpn` | Get SSL VPN Settings | 1 |
| `fortinet-fortimanager` | `unblock_url` | Unblock URL | 1 |
| `fortinet-fortimanager` | `delete_policy` | Delete Firewall Policy | 1 |
| `fortinet-fortimanager` | `adom_unblock_ip` | ADOM Level Unblock IP Address | 1 |
| `fortinet-fortimanager` | `get_blocked_applications` | Get Blocked Applications | 1 |
| `fortinet-fortimanager` | `get_adom_policy` | List ADOM Firewall Policies | 1 |
| `fortinet-fortimanager` | `create_incident` | Create Incident | 1 |
| `fortinet-fortimanager` | `delete_custom_service` | Delete Custom Service | 1 |
| `fortinet-fortimanager` | `get_user_group` | Get User Groups List | 1 |
| `fortinet-fortimanager` | `move_policy` | Move Firewall Policy | 1 |
| `fortinet-fortimanager` | `get_alert_logs` | Get Event Details | 1 |
| `fortinet-fortimanager-json-rpc` | `json_rpc_get` | JSON RPC Get | 1 |
| `fortinet-fortimanager-json-rpc` | `json_rpc_set` | JSON RPC Set | 1 |
| `fortinet-fortimanager-json-rpc` | `json_rpc_add` | JSON RPC Add | 1 |
| `fortinet-fortimanager-json-rpc` | `json_rpc_freeform` | JSON RPC Freeform | 1 |
| `fortinet-fortimanager-json-rpc` | `json_rpc_delete` | JSON RPC Delete | 1 |
| `fortinet-fortimanager-json-rpc` | `json_rpc_execute` | JSON RPC Exec | 1 |
| `fortinet-fortindr-cloud` | `get_detections` | Get Detections List | 2 |
| `fortinet-fortindr-cloud` | `get_detection_rules` | Get Detection Rules List | 2 |
| `fortinet-fortindr-cloud` | `get_detection_events` | Get Detection Events | 2 |
| `fortinet-fortindr-cloud` | `get_detection_rule_indicators` | Get Detection Rule Indicators | 1 |
| `fortinet-fortindr-cloud` | `retrieve_annotation_for_entities` | Retrieve Annotation for Entities | 1 |
| `fortinet-fortindr-cloud` | `add_or_replace_entities_to_annotation` | Add or Replace Entities to Annotation | 1 |
| `fortinet-fortindr-cloud` | `resolve_detection` | Resolve Detection | 1 |
| `fortinet-fortindr-cloud` | `get_telemetry_bandwidth` | Get Telemetry Bandwidth | 1 |
| `fortinet-fortindr-cloud` | `modify_annotation` | Modify Annotation | 1 |
| `fortinet-fortindr-cloud` | `delete_annotation` | Delete Annotation | 1 |
| `fortinet-fortindr-cloud` | `get_sensors` | Get Sensors List | 1 |
| `fortinet-fortindr-cloud` | `get_entity_tracking` | Get Entity Tracking | 1 |
| `fortinet-fortindr-cloud` | `add_annotation` | Add Annotation | 1 |
| `fortinet-fortindr-cloud` | `get_detection_rule_events` | Get Detection Rule Events List | 1 |
| `fortinet-fortindr-cloud` | `terminate_pcap_task` | Terminate PCAP Task | 1 |
| `fortinet-fortindr-cloud` | `get_devices_with_detection` | Get Devices with Detection | 1 |
| `fortinet-fortindr-cloud` | `get_pcap_tasks` | Get PCAP Tasks | 1 |
| `fortinet-fortindr-cloud` | `get_detection_rule_details` | Get Detection Rule Details | 1 |
| `fortinet-fortindr-cloud` | `delete_pcap_task` | Delete PCAP Task | 1 |
| `fortinet-fortindr-cloud` | `get_entity_pdns` | Get Passive DNS Details | 1 |
| `fortinet-fortindr-cloud` | `get_telemetry_events` | Get Telemetry Events | 1 |
| `fortinet-fortindr-cloud` | `download_pcap_task_file` | Download PCAP Task File | 1 |
| `fortinet-fortindr-cloud` | `get_entity_summary` | Get Entity Summary | 1 |
| `fortinet-fortindr-cloud` | `get_telemetry_packetstats` | Get Telemetry Packetstats | 1 |
| `fortinet-fortindr-cloud` | `retrieve_annotations` | Retrieve Annotations | 1 |
| `fortinet-fortindr-cloud` | `execute_an_api_call` | Execute an API Request | 1 |
| `fortinet-fortipam` | `update_user` | Update User | 1 |
| `fortinet-fortipam` | `execute_an_api_request` | Execute an API Request | 1 |
| `fortinet-fortipam` | `get_all_users` | Get All Users | 1 |
| `fortinet-fortipam` | `delete_user` | Delete User | 1 |
| `fortinet-fortipam` | `get_user_details` | Get User Details | 1 |
| `fortinet-fortirecon-aci` | `get_intel_reports` | Get Adversary Centric Intelligence ACI Reports | 4 |
| `fortinet-fortirecon-aci` | `get_intel_iocs` | Get Intel IOCs | 2 |
| `fortinet-fortirecon-aci` | `get_ransomware_victims` | Get Ransomware Victims | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_group_info` | Get Ransomware Group Information | 1 |
| `fortinet-fortirecon-aci` | `get_vulnerability_intelligence_vulnerable_vendors` | Get Vulnerability Intelligence vulnerable vendors | 1 |
| `fortinet-fortirecon-aci` | `update_stealers_leaked_status` | Update Stealers Leaked Status | 1 |
| `fortinet-fortirecon-aci` | `get_vendor_watchlist` | Get Vendor Watchlist | 1 |
| `fortinet-fortirecon-aci` | `get_intel_report` | Get Specific Adversary Centric Intelligence ACI Report | 1 |
| `fortinet-fortirecon-aci` | `get_vulnerability_intelligence_cves` | Get Vulnerability Intelligence CVEs | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_intel_org_watchlist_matched` | Get The Matched Organizations For Ransomware Intelligence Monitoring | 1 |
| `fortinet-fortirecon-aci` | `get_vulnerability_intelligence_vulnerable_products` | Get Vulnerability Intelligence vulnerable products | 1 |
| `fortinet-fortirecon-aci` | `get_osint_feeds` | Get OSINT Feeds | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_intel_vendors_watchlist` | Get Ransomware Vendors Added For Ransomware Intelligence Monitoring | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_victims_details_by_id` | Get Ransomware Victim Details By ID | 1 |
| `fortinet-fortirecon-aci` | `get_technical_indicators_for_given_ransomware_group` | Get The Technical Indicators For The Given Ransomware Group | 1 |
| `fortinet-fortirecon-aci` | `get_leaked_stealers_infections` | Get Leaked Stealers Infections | 1 |
| `fortinet-fortirecon-aci` | `get_vendor_details_by_id` | Get Vendor Details By ID | 1 |
| `fortinet-fortirecon-aci` | `get_intel_ioc` | Get Specific Adversary Centric Intelligence ACI IOCs | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_potential_victims` | Get Potential Ransomware Victims | 1 |
| `fortinet-fortirecon-aci` | `get_stealers_infections_on_sale` | Get Stealers Infections On Sale | 1 |
| `fortinet-fortirecon-aci` | `update_stealers_on_sale_status` | Update Stealers On Sale(Marketplaces) Status | 1 |
| `fortinet-fortirecon-aci` | `get_stealers_infections_on_sale_count` | Get Stealers Infections On Sale Count | 1 |
| `fortinet-fortirecon-aci` | `get_icl_saved_searches` | Get ICL Saved Searches | 1 |
| `fortinet-fortirecon-aci` | `get_vulnerability_intelligence_hits_by_cve_id` | Get Vulnerability Intelligence hits By CVE ID | 1 |
| `fortinet-fortirecon-aci` | `get_vulnerability_intelligence_cves_by_id` | Get Vulnerability Intelligence CVEs By ID | 1 |
| `fortinet-fortirecon-aci` | `get_vulnerability_intelligence_stats_for_cve_id` | Get Vulnerability Intelligence Stats For CVE ID | 1 |
| `fortinet-fortirecon-aci` | `get_leaked_cards` | Get Leaked Cards | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_intel_vendors_watchlist_matched` | Get Ransomware Vendors Matched | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_threat_campaigns` | Get Ransomware Threat Campaign | 1 |
| `fortinet-fortirecon-aci` | `get_widgets` | Get Widgets | 1 |
| `fortinet-fortirecon-aci` | `get_icl_saved_searches_by_id` | Get ICL Saved Searches By ID | 1 |
| `fortinet-fortirecon-aci` | `get_stealers_infections_leaked_count` | Get Stealers Infections Leaked Count | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_intel_org_watchlist` | Get Ransomware Intelligence Orgs Watchlist To Monitor | 1 |
| `fortinet-fortirecon-aci` | `get_vendor_exposures_by_id` | Get Vendor Exposures By Vendor ID | 1 |
| `fortinet-fortirecon-aci` | `get_ransomware_intelligence_statistics` | Get Ransomware Intelligence Stats | 1 |
| `fortinet-fortirecon-brand-protection` | `get_code_repos` | Get Code Repositories | 1 |
| `fortinet-fortirecon-brand-protection` | `update_code_repo_status` | Update Code Repo Status | 1 |
| `fortinet-fortirecon-brand-protection` | `get_social_media_threats` | Get Social Media Threats | 1 |
| `fortinet-fortirecon-brand-protection` | `get_rogue_apps` | Get Rogue Apps | 1 |
| `fortinet-fortirecon-brand-protection` | `update_social_media_threat_status` | Update Social Media Threat Status | 1 |
| `fortinet-fortirecon-brand-protection` | `get_original_domains_stats` | Get Original Domains Statistics | 1 |
| `fortinet-fortirecon-brand-protection` | `get_rogue_app_by_id` | Get Rogue App By ID | 1 |
| `fortinet-fortirecon-brand-protection` | `get_takedown_requests` | Get Takedown Requests | 1 |
| `fortinet-fortirecon-brand-protection` | `update_rogue_app_exposure_status` | Update Rogue App Status | 1 |
| `fortinet-fortirecon-brand-protection` | `get_tags` | Get Tags | 1 |
| `fortinet-fortirecon-brand-protection` | `get_domain_threats` | Get Domain Threats | 1 |
| `fortinet-fortirecon-brand-protection` | `get_open_bucket_exposures_stats` | Get Open Bucket Exposures Statistics | 1 |
| `fortinet-fortirecon-brand-protection` | `get_social_media_threats_stats` | Get Social Media Threats Statistics | 1 |
| `fortinet-fortirecon-brand-protection` | `update_domain_threat_status` | Update Domain Threat Status | 1 |
| `fortinet-fortirecon-brand-protection` | `get_executive_profiles` | Get Executive Profiles | 1 |
| `fortinet-fortirecon-brand-protection` | `get_code_repo_exposures` | Get Code Repo Exposures | 1 |
| `fortinet-fortirecon-brand-protection` | `get_open_bucket_exposures` | Get Open Bucket Exposures | 1 |
| `fortinet-fortirecon-brand-protection` | `get_code_repos_stats` | Get Code Repos Statistics | 1 |
| `fortinet-fortirecon-brand-protection` | `get_code_repo_matched_domains_stats` | Get Code Repo Matched Domains Statistics | 1 |
| `fortinet-fortirecon-brand-protection` | `get_executive_exposures` | Get Executive Exposures | 1 |
| `fortinet-fortirecon-brand-protection` | `get_domain_threats_stats` | Get Domain Threats Statistics | 1 |
| `fortinet-fortirecon-brand-protection` | `get_domain_threats_by_id` | Get Domain Threats By ID | 1 |
| `fortinet-fortirecon-brand-protection` | `update_open_bucket_exposure_status` | Update Open Bucket Exposure Status | 1 |
| `fortinet-fortirecon-easm` | `get_subdomains` | Get Subdomains | 2 |
| `fortinet-fortirecon-easm` | `get_issues_discovered` | Get Issues Discovered | 2 |
| `fortinet-fortirecon-easm` | `update_archived_issue` | Mark Archived Issue as Active | 1 |
| `fortinet-fortirecon-easm` | `update_leaked_credential_status` | Update Leaked Credential Status | 1 |
| `fortinet-fortirecon-easm` | `get_asset_asns` | Get Asset ASNs | 1 |
| `fortinet-fortirecon-easm` | `get_group_by_id` | Get Group Details | 1 |
| `fortinet-fortirecon-easm` | `update_archived_asset` | Update Archived Asset | 1 |
| `fortinet-fortirecon-easm` | `get_scan_statistics` | Get Scan Statistics | 1 |
| `fortinet-fortirecon-easm` | `get_tag_by_id` | Get Tag Details | 1 |
| `fortinet-fortirecon-easm` | `get_cloud_integrations` | Get Cloud Integrations | 1 |
| `fortinet-fortirecon-easm` | `get_issue_comments` | Get Issue Comments | 1 |
| `fortinet-fortirecon-easm` | `get_breaches_by_id` | Get Breaches by ID | 1 |
| `fortinet-fortirecon-easm` | `update_domain_asset_status_to_false_positive` | Update Domain Asset To False Positive | 1 |
| `fortinet-fortirecon-easm` | `get_archived_issues` | Get Archived Issues | 1 |
| `fortinet-fortirecon-easm` | `get_prefixes` | Get Prefixes | 1 |
| `fortinet-fortirecon-easm` | `get_asset_statistics` | Get Asset Statistics | 1 |
| `fortinet-fortirecon-easm` | `get_archived_assets` | Get Archived Assets | 1 |
| `fortinet-fortirecon-easm` | `update_subdomain_asset_status_to_false_positive` | Update Sub-Domain Asset To False Positive | 1 |
| `fortinet-fortirecon-easm` | `get_asns_by_asset_id` | Get ASNs by Asset ID | 1 |
| `fortinet-fortirecon-easm` | `update_asn_asset_status_to_false_positive` | Update ASN Asset To False Positive | 1 |
| `fortinet-fortirecon-easm` | `get_issue_summary` | Get Issue Summary | 1 |
| `fortinet-fortirecon-easm` | `get_report` | Get Report | 1 |
| `fortinet-fortirecon-easm` | `get_domain_by_asset_id` | Get Domain by Asset ID | 1 |
| `fortinet-fortirecon-easm` | `update_issue_status` | Update Issue Status | 1 |
| `fortinet-fortirecon-easm` | `get_security_insights` | Get Security Insights | 1 |
| `fortinet-fortirecon-easm` | `get_archived_issue_comments` | Get Archived Issue Comments | 1 |
| `fortinet-fortirecon-easm` | `get_ips` | Get IPs | 1 |
| `fortinet-fortirecon-easm` | `get_domains` | Get Domains | 1 |
| `fortinet-fortirecon-easm` | `get_leaked_credentials` | Get Leaked Credentials | 1 |
| `fortinet-fortirecon-easm` | `get_issue_by_id` | Get Issue By ID | 1 |
| `fortinet-fortirecon-easm` | `get_groups` | Get Groups | 1 |
| `fortinet-fortirecon-easm` | `get_tags` | Get Tags | 1 |
| `fortinet-fortirecon-easm` | `update_prefix_asset_status_to_false_positive` | Update IP Prefix Asset To False Positive | 1 |
| `fortinet-fortirecon-easm` | `get_ips_by_asset_id` | Get IP by Asset ID | 1 |
| `fortinet-fortirecon-easm` | `generate_report` | Generate Report | 1 |
| `fortinet-fortirecon-easm` | `get_fgt_integrations` | Get FortiGate Integrations | 1 |
| `fortinet-fortirecon-easm` | `get_exposed_services` | Get Exposed Services | 1 |
| `fortinet-fortirecon-easm` | `get_prefixes_by_asset_id` | Get Prefixes by Asset ID | 1 |
| `fortinet-fortirecon-easm` | `get_subdomain_by_asset_id` | Get Subdomain by Asset ID | 1 |
| `fortinet-fortirecon-easm` | `get_breaches` | Get Breaches | 1 |
| `fortinet-fortirecon-easm` | `update_ip_asset_status_to_false_positive` | Update IP Asset To False Positive | 1 |
| `fortinet-fortisandbox` | `get_scan_result_job` | Get Job Verdict Detail | 4 |
| `fortinet-fortisandbox` | `get_submission_job_list` | Get Submission Job List | 4 |
| `fortinet-fortisandbox` | `submit_urlfile` | Submit URL; Submit URL File | 3 |
| `fortinet-fortisandbox` | `submit_file` | Submit File | 2 |
| `fortinet-fortisandbox` | `get_file_verdict` | Get File Verdict | 2 |
| `fortinet-fortisandbox` | `get_url_rating` | Get URL Rating | 1 |
| `fortinet-fortisandbox` | `handle_allow_block_list` | Update Allow or Block List | 1 |
| `fortinet-fortisandbox` | `get_scan_stats` | Get Scan Stats | 1 |
| `fortinet-fortisandbox` | `get_avrescan` | Get AV-Rescan Result | 1 |
| `fortinet-fortisandbox` | `download_hashes_url_from_mwpkg` | List Filehash or URL From Malware Package or URL Package | 1 |
| `fortinet-fortisandbox` | `get_system_status` | Get System Status | 1 |
| `fortinet-fortisandbox` | `get_installed_vm` | Get All Installed VM | 1 |
| `fortinet-fortisandbox` | `handle_white_black_list` | Update White or Black List | 1 |
| `fortinet-fortisandbox` | `get_pdf_report` | Get PDF Report | 1 |
| `fortinet-fortisandbox` | `get_file_rating` | Get File Rating | 1 |
| `fortinet-fortisandbox` | `get_job_behaviour` | Get Job Behaviour | 1 |
| `fortinet-fortisandbox` | `mark_sample_fp_fn` | Toggle FPN State | 1 |
| `fortinet-fortisiem` | `run_report` | Run Advanced Search Query | 5 |
| `fortinet-fortisiem` | `search_events` | Search Events | 5 |
| `fortinet-fortisiem` | `get_incident_details` | Get Incident Details | 3 |
| `fortinet-fortisiem` | `get_incidents` | List Incidents | 2 |
| `fortinet-fortisiem` | `get_device_info` | Get Device Information | 2 |
| `fortinet-fortisiem` | `get_associated_events_new` | Get Events For Incident | 2 |
| `fortinet-fortisiem` | `get_watch_list_entry` | Get Watch List Entry | 1 |
| `fortinet-fortisiem` | `delete_watch_list_entry` | Delete Watch List Entry | 1 |
| `fortinet-fortisiem` | `get_watch_list_entries_count` | Get Watch List Entries Count | 1 |
| `fortinet-fortisiem` | `execute_api_request` | Execute an API Request | 1 |
| `fortinet-fortisiem` | `clear_incident` | Clear Incident With Reason | 1 |
| `fortinet-fortisiem` | `delete_lookup_table` | Delete Lookup Table | 1 |
| `fortinet-fortisiem` | `create_lookup_table` | Create Lookup Table | 1 |
| `fortinet-fortisiem` | `get_host_context` | Get Host Context | 1 |
| `fortinet-fortisiem` | `get_org_name_by_org_id` | Get Organization Details | 1 |
| `fortinet-fortisiem` | `get_user_context` | Get User Context | 1 |
| `fortinet-fortisiem` | `get_monitored_devices` | List Monitored Devices and Attributes | 1 |
| `fortinet-fortisiem` | `get_event_details` | Get Event Details | 1 |
| `fortinet-fortisiem` | `get_devices_details_in_address` | Get All Devices For Specified IP Address Range | 1 |
| `fortinet-fortisiem` | `get_case_analysts` | Get Case Analysts | 1 |
| `fortinet-fortisiem` | `create_case` | Create Case | 1 |
| `fortinet-fortisiem` | `delete_lookup_table_data` | Delete Lookup Table Data | 1 |
| `fortinet-fortisiem` | `get_watch_lists` | Get Watch Lists | 1 |
| `fortinet-fortisiem` | `upload_attachment_for_case` | Upload Attachment for Case | 1 |
| `fortinet-fortisiem` | `get_list_cases` | Get List Cases | 1 |
| `fortinet-fortisiem` | `get_devices_details` | Get All Devices | 1 |
| `fortinet-fortisiem` | `get_monitored_organizations` | List Monitored Organizations | 1 |
| `fortinet-fortisiem` | `incident_comment` | Comment Incident | 1 |
| `fortinet-fortisiem` | `update_lookup_table_data` | Update Lookup Table Data | 1 |
| `fortinet-fortisiem` | `add_watch_list_entries_to_watch_list_groups` | Add Watch List Entries to Watch List | 1 |
| `fortinet-fortisiem` | `update_watch_list_entry` | Update Watch List Entry | 1 |
| `fortinet-fortisiem` | `get_lookup_table_data` | Get Lookup Table Data | 1 |
| `fortinet-fortisiem` | `update_incident` | Update Incident | 1 |
| `fortinet-fortisiem` | `get_incident_attributes` | Get Event Attributes | 1 |
| `fortinet-fortisiem` | `update_cases` | Update Cases | 1 |
| `fortinet-fortisiem` | `get_case_field_schema` | Get Case Field Schema | 1 |
| `fortinet-fortisiem` | `import_lookup_table_data` | Import Lookup Table Data | 1 |
| `fortinet-fortisiem` | `get_events_by_query_id` | Get Events Data By Query ID | 1 |
| `fortinet-fortisiem` | `delete_watch_list` | Delete Watch List | 1 |
| `fortinet-fortisiem` | `create_watchlist_group` | Create Watch List | 1 |
| `fortinet-fortisiem` | `get_ip_context` | Get IP Context | 1 |
| `fortinet-fortisiem` | `check_import_task_status` | Check Import Task Status | 1 |
| `fortinet-fortisiem` | `get_all_lookup_tables` | Get All Lookup Table | 1 |
| `fortinet-web-filter-lookup` | `url_review` | Check Category of Domain or URL | 2 |
| `fortisoar-ml-engine` | `train` | Train | 1 |
| `fortisoar-ml-engine` | `predict` | Predict | 1 |
| `fortisoar-ml-engine` | `similar` | Fetch similar record(s) | 1 |
| `fortisoar-soc-simulator` | `create_simulated_alert` | Create Simulated Alert | 4 |
| `fortisoar-soc-simulator` | `malicious_file_indicator` | Create Malicious File Indicator | 3 |
| `fortisoar-soc-simulator` | `bad_url` | Fetch Malicious URL | 3 |
| `fortisoar-soc-simulator` | `replace_variables` | Replace Variables | 1 |
| `fuzzy-search` | `filter_json_by_key_value` | Filter JSON by Key Value | 3 |
| `fuzzy-search` | `search_keyword_in_text` | Search Keyword In Text | 1 |
| `github` | `list_pull_request` | List Pull Request | 3 |
| `github` | `create_repository` | Create Repository | 2 |
| `github` | `get_web_url` | Get Server URL | 2 |
| `github` | `update_clone_repository` | Update Remote Repository | 2 |
| `github` | `list_repository_collaborator` | List Repository Collaborator | 2 |
| `github` | `add_pr_review` | Add Pull Request Review | 2 |
| `github` | `push_repository` | Push Changes | 2 |
| `github` | `clone_repository` | Clone Repository | 2 |
| `github` | `create_issue_comment` | Create Issue Comment | 2 |
| `github` | `create_issue` | Create Issue | 2 |
| `github` | `add_reviewers` | Add Reviewers for a Pull Request | 2 |
| `github` | `create_pull_request` | Create Pull Request | 2 |
| `github` | `create_update_file_contents` | Create or Update File Contents | 2 |
| `github` | `list_repository_issue` | List Repository Issue | 2 |
| `github` | `update_issue` | Update Issue | 2 |
| `github` | `list_pr_reviews` | List Pull Request Reviews | 2 |
| `github` | `create_branch` | Create Branch | 2 |
| `github` | `create_release` | Create Release | 2 |
| `github` | `merge_pull_request` | Merge Pull Request | 2 |
| `github` | `add_repository_collaborator` | Add Repository Collaborator | 2 |
| `github` | `delete_branch` | Delete Branch | 2 |
| `github` | `list_releases` | List Releases | 2 |
| `github` | `create_repository_using_template` | Create Repository Using Template | 1 |
| `github` | `delete_file_from_repository` | Delete File | 1 |
| `github` | `set_repo_subscription` | Set Repository Subscription | 1 |
| `github` | `get_commit` | Get Commit | 1 |
| `github` | `list_watchers` | List Watchers | 1 |
| `github` | `get_repository` | Get Repository | 1 |
| `github` | `fetch_upstream` | Fetch Upstream | 1 |
| `github` | `get_branch_revision` | Get Branch Revision | 1 |
| `github` | `list_user_repositories` | List User Repositories | 1 |
| `github` | `update_repository` | Update Repository | 1 |
| `github` | `fork_organization_repository` | Fork Organization Repository | 1 |
| `github` | `get_file_from_repository` | Get File | 1 |
| `github` | `list_organization_repositories` | List Organization Repositories | 1 |
| `github` | `list_stargazers` | List Stargazers | 1 |
| `github` | `list_authenticated_user_repositories` | List Authenticated User Repositories | 1 |
| `github` | `compare_commit` | Get Commit Comparison | 1 |
| `github` | `search_code` | Search Code | 1 |
| `github` | `list_branches` | List Branches | 1 |
| `github` | `star_repository` | Star Repository | 1 |
| `github` | `merge_branch` | Merge Branch | 1 |
| `github` | `list_fork_repositories` | List Fork Repositories | 1 |
| `github` | `delete_repository` | Delete Repository | 1 |
| `github` | `list_review_comments` | List Review Comments on a Pull Request | 1 |
| `gitlab` | `create_issue_comment` | Create Issue Comment | 4 |
| `gitlab` | `list_project_merge_requests` | List Repository Merge Requests | 4 |
| `gitlab` | `clone_repository` | Clone Repository | 3 |
| `gitlab` | `merge_merge_request` | Merge a Merge Request | 2 |
| `gitlab` | `create_repository_branch` | Create Repository Branch | 2 |
| `gitlab` | `create_project` | Create Repository | 2 |
| `gitlab` | `update_clone_repository` | Update Remote Repository | 2 |
| `gitlab` | `review_merge_request` | Review Merge Request | 2 |
| `gitlab` | `list_releases` | List Releases | 2 |
| `gitlab` | `get_member_list_of_project` | Get Member List of Repository | 2 |
| `gitlab` | `update_file_in_repository` | Update File | 2 |
| `gitlab` | `get_web_url` | Get Server URL | 2 |
| `gitlab` | `create_merge_request` | Create Merge Request | 2 |
| `gitlab` | `update_issue` | Update Issue | 2 |
| `gitlab` | `create_new_file_in_repository` | Create File | 2 |
| `gitlab` | `create_issue` | Create Issue | 2 |
| `gitlab` | `push_repository` | Push Changes | 2 |
| `gitlab` | `create_release` | Create Release | 2 |
| `gitlab` | `list_project_issues` | List Repository Issues | 2 |
| `gitlab` | `add_member_to_project_or_group` | Add Member to Repository | 2 |
| `gitlab` | `delete_repository_branch` | Delete Repository Branch; Delete repository Branch | 2 |
| `gitlab` | `update_merge_request` | Update Merge Request | 2 |
| `gitlab` | `edit_project` | Update Repository | 1 |
| `gitlab` | `list_repository_branches` | List Repository Branches | 1 |
| `gitlab` | `create_merge_request_comment` | Create Merge Request Comment | 1 |
| `gitlab` | `get_single_repository_branch` | Get Repository Branch | 1 |
| `gitlab` | `get_merge_request_approval_state` | Get Approval State of Merge Request | 1 |
| `gitlab` | `list_merge_requests_comments` | List Merge Request Comments | 1 |
| `gitlab` | `list_fork_projects` | List Fork Repositories | 1 |
| `gitlab` | `list_group_projects` | List Group Repositories | 1 |
| `gitlab` | `star_project` | Star Repository | 1 |
| `gitlab` | `delete_project` | Delete Repository | 1 |
| `gitlab` | `fork_project` | Fork Repository | 1 |
| `gitlab` | `set_project_notification_level` | Update Repository Notification Level | 1 |
| `gitlab` | `create_project_using_templates` | Create Repository Using Templates | 1 |
| `gitlab` | `list_starrers` | List Starrers | 1 |
| `gitlab` | `list_authenticated_user_projects` | List Authenticated User Repositories | 1 |
| `gitlab` | `get_commit` | Get Commit | 1 |
| `gitlab` | `get_file_from_repository` | Get File | 1 |
| `gitlab` | `fetch_upstream` | Fetch Upstream | 1 |
| `gitlab` | `list_user_projects` | List User Repositories | 1 |
| `gitlab` | `delete_existing_file_in_repository` | Delete File | 1 |
| `gitlab` | `list_merge_requests_reviewers` | List Merge Request Reviewers | 1 |
| `gitlab` | `compare_commit` | Get Commit Comparison | 1 |
| `gitlab` | `get_project` | Get Repository | 1 |
| `icanhazdadjoke` | `get_joke` | Get Joke | 1 |
| `imap` | `fetch_email_new` | Fetch Email(s) | 1 |
| `ip-quality-score` | `get_url_reputation` | Get URL Reputation | 2 |
| `ip-quality-score` | `get_email_reputation` | Get Email Reputation | 2 |
| `ip-quality-score` | `get_ip_reputation` | Get IP Reputation | 2 |
| `ipstack` | `ip_locate` | Geolocate IP | 2 |
| `malsilo` | `get_ipv4_feed` | Get IPv4 Feeds | 2 |
| `malsilo` | `get_domain_feed` | Get Domain Feeds | 2 |
| `malsilo` | `get_url_feed` | Get URL Feeds | 2 |
| `microsoft-graph-mail` | `search_emails` | Search Emails | 2 |
| `microsoft-graph-mail` | `delete_email` | Delete Email | 1 |
| `microsoft-graph-mail` | `add_email_category` | Add Email Category | 1 |
| `microsoft-graph-mail` | `copy_email` | Copy Email | 1 |
| `microsoft-graph-mail` | `get_folders` | Get Folders | 1 |
| `microsoft-graph-mail` | `forward_email` | Forward Email | 1 |
| `microsoft-graph-mail` | `execute_api_request` | Execute an API Request | 1 |
| `microsoft-graph-mail` | `move_email` | Move Email | 1 |
| `microsoft-graph-mail` | `get_email_categories` | Get Email Categories | 1 |
| `microsoft-graph-mail` | `get_child_folders` | Get Child Folders | 1 |
| `microsoft-graph-mail` | `send_email` | Send Email | 1 |
| `microsoft-graph-mail` | `send_email_as_reply` | Send Email as Reply | 1 |
| `microsoft-graph-mail` | `create_email_threat_submission` | Create Email Threat Submission | 1 |
| `microsoft-graph-mail` | `get_unread_emails` | Get Unread Emails | 1 |
| `microsoft-graph-mail` | `remove_email_category` | Remove Email Category | 1 |
| `microsoft-teams` | `get_users_all_messages` | Get User's all Chat Messages | 2 |
| `microsoft-teams` | `send_message` | Send Message; Send Message to Channel | 2 |
| `microsoft-teams` | `get_channel` | Get Channel; Get Channel Details | 2 |
| `microsoft-teams` | `unarchive_team` | Unarchive Team | 1 |
| `microsoft-teams` | `remove_group_owner` | Remove Group Owner | 1 |
| `microsoft-teams` | `list_user_joined_teams` | Get User Teams | 1 |
| `microsoft-teams` | `get_team` | Get Team Details | 1 |
| `microsoft-teams` | `create_user` | Create User | 1 |
| `microsoft-teams` | `archive_team` | Archive Team | 1 |
| `microsoft-teams` | `get_meeting` | Get Meeting Details | 1 |
| `microsoft-teams` | `clone_team` | Clone Team | 1 |
| `microsoft-teams` | `update_user` | Update User Details | 1 |
| `microsoft-teams` | `get_replies_to_channel_message` | Get Replies to Channel Message | 1 |
| `microsoft-teams` | `create_channel` | Create Channel | 1 |
| `microsoft-teams` | `delete_group` | Delete Group | 1 |
| `microsoft-teams` | `messages_mention` | Tag User in Message | 1 |
| `microsoft-teams` | `reply_messages` | Reply Message | 1 |
| `microsoft-teams` | `create_meeting` | Create Meeting | 1 |
| `microsoft-teams` | `get_chat_messages` | Get Chat Messages | 1 |
| `microsoft-teams` | `add_member` | Add Group Member | 1 |
| `microsoft-teams` | `update_team` | Update Team Details | 1 |
| `microsoft-teams` | `get_group_member` | Get Group Member | 1 |
| `microsoft-teams` | `delete_meeting` | Delete Meeting | 1 |
| `microsoft-teams` | `get_groups` | Get Groups | 1 |
| `microsoft-teams` | `update_meeting` | Update Meeting Details | 1 |
| `microsoft-teams` | `remove_group_member` | Remove Group Member | 1 |
| `microsoft-teams` | `create_team` | Create Team | 1 |
| `microsoft-teams` | `create_group` | Create Group | 1 |
| `microsoft-teams` | `get_users` | Get User Details | 1 |
| `microsoft-teams` | `send_chat` | Send Direct Message | 1 |
| `microsoft-teams` | `delete_user` | Delete User | 1 |
| `microsoft-teams` | `get_channel_messages` | Get Channel Messages | 1 |
| `microsoft-teams` | `list_users` | Get All Users | 1 |
| `microsoft-teams` | `get_group_owner` | Get Group Owner | 1 |
| `microsoft-teams` | `add_owner` | Add Group Owner | 1 |
| `microsoft-winrm` | `execute_command` | Run Command | 2 |
| `microsoft-winrm` | `upload_file` | Upload File To Endpoint | 1 |
| `microsoft-winrm` | `execute_ps_command` | Run Powershell Command | 1 |
| `microsoft-winrm` | `execute_script` | Run Script | 1 |
| `microsoft-winrm` | `execute_ps_script` | Run Inline Powershell Script | 1 |
| `microsoft-winrm` | `get_file` | Get File | 1 |
| `mitre-attack` | `get_mitre_data` | Get MITRE Data | 3 |
| `mysql` | `run_query` | Run Query | 5 |
| `mysql` | `list_columns` | List Columns | 1 |
| `mysql` | `list_tables` | List Tables | 1 |
| `nist-nvd` | `get_specific_cve_details` | Get Specific CVE ID Details | 3 |
| `nist-nvd` | `cve_search` | Advance CVE Search | 1 |
| `nist-nvd` | `cve_search_by_keywords` | CVE Search by Keywords | 1 |
| `nist-nvd` | `cpe_search` | CPE Search | 1 |
| `nist-nvd` | `get_cve_change_history` | Get CVE Change History | 1 |
| `openai` | `get_vector_store` | Get Vector Store Details | 2 |
| `openai` | `get_run_step` | Get Run Step Details | 2 |
| `openai` | `get_file` | Get File Details | 2 |
| `openai` | `get_thread` | Get Thread Details | 2 |
| `openai` | `create_vector_store` | Create Vector Store | 1 |
| `openai` | `get_usage` | Get Tokens Usage | 1 |
| `openai` | `chat_conversation` | Converse With OpenAI | 1 |
| `openai` | `get_run` | Get Run Details | 1 |
| `openai` | `count_tokens` | Get Token Count | 1 |
| `openai` | `create_translation` | Create Translation | 1 |
| `openai` | `update_assistant` | Update Assistant | 1 |
| `openai` | `delete_thread_message` | Delete Thread Message | 1 |
| `openai` | `get_thread_message` | Get Thread Message Details | 1 |
| `openai` | `update_thread_message` | Update Thread Message | 1 |
| `openai` | `create_speech` | Create Speech | 1 |
| `openai` | `upload_file` | Upload File | 1 |
| `openai` | `create_thread_and_run` | Create Thread and Run | 1 |
| `openai` | `create_transcription` | Create Transcription | 1 |
| `openai` | `create_thread_message` | Create Thread Message | 1 |
| `openai` | `create_thread` | Create Thread | 1 |
| `openai` | `create_conversation` | Create Conversation | 1 |
| `openai` | `get_vector_store_file_batch` | Get Vector Store File Batch | 1 |
| `openai` | `submit_tool_outputs_to_run` | Submit Tool Outputs To Run | 1 |
| `openai` | `cancel_vector_store_file_batch` | Cancel Vector Store File Batch | 1 |
| `openai` | `create_vector_store_file` | Create Vector Store File | 1 |
| `openai` | `update_thread` | Update Thread | 1 |
| `openai` | `get_assistant` | Get Assistant Details | 1 |
| `openai` | `list_models` | List Available Models | 1 |
| `openai` | `delete_thread` | Delete Thread | 1 |
| `openai` | `create_assistant` | Create Assistant | 1 |
| `openai` | `list_thread_messages` | List Thread Messages | 1 |
| `openai` | `chat_completions` | Ask a Question | 1 |
| `openai` | `delete_file` | Delete File | 1 |
| `openai` | `update_run` | Update Run | 1 |
| `openai` | `list_assistants` | List Assistants | 1 |
| `openai` | `create_vector_store_file_batch` | Create Vector Store File Batch | 1 |
| `openai` | `create_run` | Create Run | 1 |
| `openai` | `list_run_steps` | List Run Steps | 1 |
| `openai` | `create_response` | Create Response | 1 |
| `openai` | `list_runs` | List Runs | 1 |
| `openai` | `cancel_run` | Cancel Run | 1 |
| `openai` | `delete_assistant` | Delete Assistant | 1 |
| `openai` | `list_files` | List Files | 1 |
| `phishing-classifier` | `predict` | Predict | 2 |
| `phishing-classifier` | `train` | Train | 1 |
| `phishing-classifier` | `get_training_results` | Get Training Results | 1 |
| `qradar` | `query_qradar` | Make an Ariel Query to QRadar | 3 |
| `qradar` | `get_offenses` | Get Offenses from QRadar | 3 |
| `qradar` | `get_source_ip` | Get Source IP Addresses | 2 |
| `qradar` | `get_destination_ip` | Get Destination IP Addresses | 2 |
| `qradar` | `get_events_related_to_offense` | Get Events Related to an Offense | 1 |
| `qradar` | `get_closing_reasons` | Get Offense Closing Reasons | 1 |
| `qradar` | `get_cases` | Get Cases | 1 |
| `qradar` | `add_table_element` | Add or Update Table Element | 1 |
| `qradar` | `get_reference_tables` | Get Reference Tables | 1 |
| `qradar` | `get_notes` | Get Offense Notes | 1 |
| `qradar` | `close_offense` | Close Offense | 1 |
| `qradar` | `add_notes` | Create Note | 1 |
| `qradar` | `get_table_elements` | Get Table Elements | 1 |
| `qradar` | `create_case` | Create Case | 1 |
| `qradar` | `invoke_api` | Invoke QRadar REST API | 1 |
| `qradar` | `update_asset` | Update Asset | 1 |
| `qradar` | `get_offense_type` | Get Offense Types | 1 |
| `qradar` | `handle_reference_set_value` | Manipulate Reference Set Content | 1 |
| `qradar` | `get_assets` | Get Assets | 1 |
| `qradar` | `delete_table_element` | Delete Table Element | 1 |
| `qradar` | `delete_reference_table` | Delete or Purge Reference Table | 1 |
| `qradar` | `get_assets_properties` | Get Assets Properties | 1 |
| `qualys` | `list_host` | Get Scanned Host List | 1 |
| `screenshot` | `screenshot_url` | Screenshot URL | 2 |
| `screenshot` | `screenshot_eml_or_msg_file` | Screenshot EML OR MSG File Content | 1 |
| `screenshot` | `screenshot_mail` | Screenshot Email Content | 1 |
| `servicenow` | `create_incident` | Create Incident | 2 |
| `servicenow` | `get_assignment_group` | Get Assignment Group | 1 |
| `servicenow` | `get_location` | Get Location | 1 |
| `servicenow` | `get_users` | Get Users | 1 |
| `slacalculator` | `calculateSLA` | Calculate SLA | 1 |
| `slacalculator` | `calculate_elapsed_time` | Calculate Elapsed SLA Time | 1 |
| `slack` | `send_message` | Send Message | 4 |
| `slack` | `upload_file` | Upload File | 2 |
| `slack` | `rename_channel` | Rename Channel | 1 |
| `slack` | `create_channel` | Create Channel | 1 |
| `slack` | `search_channel` | Search Channel | 1 |
| `slack` | `get_channel_info` | Get Channel Information | 1 |
| `slack` | `close_channel` | Close Channel | 1 |
| `slack` | `invite_user_to_channel` | Invite User To Channel | 1 |
| `slack` | `list_users` | Get Users List | 1 |
| `slack` | `create_group` | Create Group | 1 |
| `slack` | `list_channels` | Get Channels List | 1 |
| `slack` | `get_message_history` | Get Message History | 1 |
| `slack` | `get_user` | Get User Information | 1 |
| `smtp` | `send_email_new` | Send Email; Send Email (Advanced) | 14 |
| `smtp` | `send_richtext_email` | Send Rich Text Email | 1 |
| `smtp` | `send_email` | Send Email | 1 |
| `splunk` | `get_results` | Get Results for a Search | 4 |
| `splunk` | `invoke_search` | Invoke Search | 4 |
| `ssh` | `run_remote_command` | Execute remote command | 4 |
| `symantec-cloudsoc` | `get_logs` | Get Event Logs | 1 |
| `symantec-dlp` | `get_incident_details` | Get Incident Details | 1 |
| `symantec-dlp` | `get_incidents_ids` | Get Incidents IDs | 1 |
| `tenable-io` | `get_vuln_details` | Get Vulnerability Information | 2 |
| `tenable-io` | `get_asset_export_status` | Get Asset Export Status | 2 |
| `tenable-io` | `download_asset_export_chunk` | Download Asset Export Chunk | 2 |
| `tenable-io` | `get_scan_assets` | List Scan's Assets | 2 |
| `tenable-io` | `get_vuln_export_status` | Get Vulnerability Export Status | 2 |
| `tenable-io` | `submit_asset_export_job` | Submit Asset Export Job | 2 |
| `tenable-io` | `get_scans` | List Scans | 2 |
| `tenable-io` | `download_vuln_export_chunk` | Download Vulnerability Export Chunk | 2 |
| `tenable-io` | `submit_vuln_export_job` | Submit Vulnerability Export Job | 2 |
| `tenable-io` | `get_asset_vulnerabilities` | List Asset's Vulnerabilities | 2 |
| `tenable-io` | `cancel_vuln_export_job` | Cancel Vulnerability Export Job | 1 |
| `tenable-io` | `get_host_details` | Get Host Details | 1 |
| `tenable-io` | `get_scan_history` | Get Scan History | 1 |
| `tenable-io` | `list_vuln_export_jobs` | List Vulnerability Export Jobs | 1 |
| `tenable-io` | `get_plugin_details` | Get Plugin Information | 1 |
| `tenable-io` | `list_asset_export_jobs` | List Asset Export Jobs | 1 |
| `tenable-io` | `trigger_scan` | Trigger Scan | 1 |
| `tenable-io` | `cancel_asset_export_job` | Cancel Asset Export Job | 1 |
| `time-series-chart-utilities` | `format_data_set_output_with_fieldgrouped` | Format Data Set Output with Field-Grouped | 2 |
| `time-series-chart-utilities` | `assemble_query_time_windows` | Assemble Query Time Windows | 2 |
| `time-series-chart-utilities` | `combine_query_results_into_data_columns` | Combine Query Results into Data Columns | 2 |
| `time-series-chart-utilities` | `flatten_data_sets_and_groups` | Flatten Data Sets and Groups | 2 |
| `toronto_weather` | `get_weather` | Get Weather | 1 |
| `trend-micro-vision-one` | `add_to_exception_list` | Add to Exception List | 2 |
| `trend-micro-vision-one` | `add_to_block_list` | Add to Block List | 1 |
| `trend-micro-vision-one` | `get_list_alerts` | Get Alert Lists | 1 |
| `trend-micro-vision-one` | `get_detection_data` | Get Detection Data | 1 |
| `trend-micro-vision-one` | `remove_from_suspicious_object_list` | Remove from Suspicious Object List | 1 |
| `trend-micro-vision-one` | `add_to_suspicious_object_list` | Add to Suspicious Object List | 1 |
| `trend-micro-vision-one` | `get_endpoint_details` | Get Endpoint Details | 1 |
| `trend-micro-vision-one` | `restore_endpoint` | Restore endpoints | 1 |
| `trend-micro-vision-one` | `get_alert_details` | Get Alert Details | 1 |
| `trend-micro-vision-one` | `quarantine_email_message` | Quarantine Email Message | 1 |
| `trend-micro-vision-one` | `terminates_process` | Terminates Process | 1 |
| `trend-micro-vision-one` | `isolate_endpoint` | Isolate Endpoints | 1 |
| `trend-micro-vision-one` | `delete_email_message` | Delete Email Message | 1 |
| `trend-micro-vision-one` | `collect_file` | Collect File | 1 |
| `trend-micro-vision-one` | `remove_from_block_list` | Remove from Block List | 1 |
| `trend-micro-vision-one` | `get_task_details` | Get Task Details | 1 |
| `urlscan-io` | `submit_url` | Submit URL | 2 |
| `urlscan-io` | `custom_search` | Custom Search | 1 |
| `urlscan-io` | `search_hash` | Search Hash | 1 |
| `urlscan-io` | `search_domain` | Search Domain | 1 |
| `urlscan-io` | `search_ip` | Search IP | 1 |
| `urlscan-io` | `get_report` | Get Report | 1 |
| `virustotal` | `query_ip` | Get IP Reputation | 7 |
| `virustotal` | `analysis_file` | Get Analysis Details | 6 |
| `virustotal` | `file_reputation` | Get File Reputation | 5 |
| `virustotal` | `query_domain` | Get Domain Reputation | 2 |
| `virustotal` | `query_url` | Get URL Reputation | 2 |
| `virustotal` | `get_widget_html_content` | Get Widget HTML Content | 2 |
| `virustotal` | `upload_sample` | Submit File | 2 |
| `virustotal` | `ip_re_analyze` | Reanalyze IP | 1 |
| `virustotal` | `url_re_analyze` | Reanalyze URL | 1 |
| `virustotal` | `scan_url` | Submit URL for scanning | 1 |
| `virustotal` | `get_widget_rendering_url` | Get Widget Rendering URL | 1 |
| `virustotal` | `file_re_analyze` | Reanalyze File | 1 |
| `virustotal` | `domain_re_analyze` | Reanalyze Domain | 1 |
| `virustotal` | `custom_endpoint` | Custom API Endpoint | 1 |
| `wazuh-siem` | `get_alerts_by_DSL_search` | DSL Search; Execute DSL Search | 2 |
| `wazuh-siem` | `get_all_alerts_in_last_x_minutes` | Get All Alerts in Last X Minutes | 1 |
| `wazuh-siem` | `get_alerts_by_lucene_search` | Execute Lucene Search | 1 |
| `wazuh-siem` | `get_alert_by_id` | Get Alert Details | 1 |
| `whois-freaks` | `ssl_certificates` | Get SSL Certificates | 1 |
| `whois-freaks` | `dns_lookup` | Get DNS Lookup | 1 |
| `whois-freaks` | `whois_lookup` | Get Whois Lookup | 1 |
| `whois-rdap` | `whois_ip` | Whois IP | 2 |
| `whois-xml-api` | `reverse_whois_search` | Get Reverse WHOIS Search | 1 |
| `whois-xml-api` | `dns_lookup` | Get DNS Lookup | 1 |
| `whois-xml-api` | `ssl_certificates` | Get SSL Certificates | 1 |
| `whois-xml-api` | `reverse_dns_search` | Get Reverse DNS Search | 1 |
| `whois-xml-api` | `whois_search` | Get WHOIS Search | 1 |
| `whois-xml-api` | `brand_monitor` | Brand Monitor | 1 |
| `whois-xml-api` | `whois_history_search` | Get WHOIS History Search | 1 |
| `whois-xml-api` | `domain_subdomain_discovery` | Domain or Subdomain Discovery | 1 |
| `xforce` | `get_dns_record` | Get DNS Record | 2 |
| `xforce` | `get_ip_reputation` | Get IP Reputation | 2 |
| `xforce` | `get_ip_behaviour` | Get IP Behaviour | 2 |
| `xforce` | `get_file_reputation_using_filehash` | Get File Reputation | 2 |
| `xforce` | `get_vulnerability_from_xfid` | Get Vulnerability from XFID | 1 |
| `xforce` | `get_url_behaviour` | Get URL Behaviour | 1 |
| `xforce` | `get_vulnerability` | Get Vulnerability | 1 |
| `xforce` | `search_signature_by_pamid` | Search Signature by PAMID | 1 |
| `xforce` | `get_vulnerability_from_stdcode` | Get Vulnerability from STDCODE | 1 |
| `xforce` | `search_signature` | Search Signature | 1 |
| `xforce` | `get_ip_report` | Get IP Report | 1 |
| `xforce` | `get_relative_malware` | Get Relative Malware | 1 |
| `xforce` | `search_signature_by_xpu` | Search Signature by XPU | 1 |
| `xforce` | `get_url_report` | Get URL Report | 1 |
| `xforce` | `get_ip_registrant` | Get IP Registrant | 1 |

### 2.2 Connectors grouped, most common ops

- **`cyops_utilities`** (244 calls): `make_cyops_request`×71, `no_op`×66, `updatemacro`×30, `format_richtext`×28, `json_to_html`×13
- **`gitlab`** (72 calls): `create_issue_comment`×4, `list_project_merge_requests`×4, `clone_repository`×3, `merge_merge_request`×2, `create_repository_branch`×2
- **`fortinet-fortimanager`** (69 calls): `get_incidents`×3, `get_incident_events`×2, `update_policy_package`×1, `create_ldap_server`×1, `update_custom_service`×1
- **`github`** (68 calls): `list_pull_request`×3, `create_repository`×2, `get_web_url`×2, `update_clone_repository`×2, `list_repository_collaborator`×2
- **`crowd-strike-falcon`** (63 calls): `alert_search`×3, `get_detection_details`×3, `detection_search`×3, `get_alert_details`×3, `process_details`×1
- **`fortinet-fortisiem`** (56 calls): `run_report`×5, `search_events`×5, `get_incident_details`×3, `get_incidents`×2, `get_device_info`×2
- **`fortigate-firewall`** (51 calls): `block_ip`×6, `quarantine_host`×2, `update_policy`×2, `block_url`×2, `get_system_events`×1
- **`openai`** (47 calls): `get_vector_store`×2, `get_run_step`×2, `get_file`×2, `get_thread`×2, `create_vector_store`×1
- **`fortinet-fortianalyzer`** (45 calls): `get_alerts_for_multiple_adoms`×3, `get_reports`×2, `get_device_info`×2, `count_alerts_for_multiple_adoms`×2, `get_schedules`×2
- **`fortinet-fortirecon-easm`** (43 calls): `get_subdomains`×2, `get_issues_discovered`×2, `update_archived_issue`×1, `update_leaked_credential_status`×1, `get_asset_asns`×1
- **`fortinet-fortiguard-threat-intelligence`** (40 calls): `threat_intel_search`×2, `threat_activities_statistics_by_country`×2, `ingest_feeds`×2, `threat_activities_statistics`×2, `threat_activities_statistics_by_industry`×2
- **`fortinet-fortirecon-aci`** (39 calls): `get_intel_reports`×4, `get_intel_iocs`×2, `get_ransomware_victims`×1, `get_ransomware_group_info`×1, `get_vulnerability_intelligence_vulnerable_vendors`×1
- **`microsoft-teams`** (38 calls): `get_users_all_messages`×2, `send_message`×2, `get_channel`×2, `unarchive_team`×1, `remove_group_owner`×1
- **`aws-commands`** (34 calls): `authorize_ingress`×1, `attach_volume`×1, `detach_volume`×1, `launch_instance`×1, `describe_instance`×1
- **`fortinet-fortiedr`** (33 calls): `get_event_list`×2, `isolate_collector`×2, `update_ipset`×1, `remediate_device`×1, `update_collector_installer`×1
- **`virustotal`** (33 calls): `query_ip`×7, `analysis_file`×6, `file_reputation`×5, `query_domain`×2, `query_url`×2
- **`aws`** (32 calls): `detach_volume`×1, `detach_instance_from_autoscaling_group`×1, `attach_instance_to_auto_scaling_group`×1, `reboot_instance`×1, `stop_instance`×1
- **`fortinet-fortindr-cloud`** (29 calls): `get_detections`×2, `get_detection_rules`×2, `get_detection_events`×2, `get_detection_rule_indicators`×1, `retrieve_annotation_for_entities`×1
- **`qradar`** (28 calls): `query_qradar`×3, `get_offenses`×3, `get_source_ip`×2, `get_destination_ip`×2, `get_events_related_to_offense`×1
- **`tenable-io`** (28 calls): `get_vuln_details`×2, `get_asset_export_status`×2, `download_asset_export_chunk`×2, `get_scan_assets`×2, `get_vuln_export_status`×2
- **`fortinet-fortisandbox`** (27 calls): `get_scan_result_job`×4, `get_submission_job_list`×4, `submit_urlfile`×3, `submit_file`×2, `get_file_verdict`×2
- **`darktrace`** (24 calls): `execute_api_request`×1, `get_incidents`×1, `get_enums`×1, `search_query`×1, `get_models`×1
- **`activedirectory`** (24 calls): `get_specific_object_details`×8, `disable_user_account`×4, `global_search`×4, `get_all_object_details`×2, `advanced_search`×2
- **`fortinet-fortirecon-brand-protection`** (23 calls): `get_code_repos`×1, `update_code_repo_status`×1, `get_social_media_threats`×1, `get_rogue_apps`×1, `update_social_media_threat_status`×1
- **`fortinet-fortidlp`** (21 calls): `get_incidents_list`×4, `get_users_list`×1, `add_labels_to_agents`×1, `get_label_details`×1, `update_incidents_by_id`×1
- **`xforce`** (19 calls): `get_dns_record`×2, `get_ip_reputation`×2, `get_ip_behaviour`×2, `get_file_reputation_using_filehash`×2, `get_vulnerability_from_xfid`×1
- **`trend-micro-vision-one`** (17 calls): `add_to_exception_list`×2, `add_to_block_list`×1, `get_list_alerts`×1, `get_detection_data`×1, `remove_from_suspicious_object_list`×1
- **`slack`** (17 calls): `send_message`×4, `upload_file`×2, `rename_channel`×1, `create_channel`×1, `search_channel`×1
- **`fortinet-fortiauthenticator`** (17 calls): `get_users`×2, `get_ldap_user_list`×2, `get_schema`×2, `get_ldap_user`×2, `update_ldapuser_status`×2
- **`csv-data-management`** (16 calls): `extract_data_from_csv`×10, `merge_two_csv_and_extract_data`×2, `join_two_csv_and_extract_data`×2, `concat_two_csv_and_extract_data`×1, `convert_json_to_csv_file`×1
- **`smtp`** (16 calls): `send_email_new`×14, `send_richtext_email`×1, `send_email`×1
- **`microsoft-graph-mail`** (16 calls): `search_emails`×2, `delete_email`×1, `add_email_category`×1, `copy_email`×1, `get_folders`×1
- **`fortinet-forticlient-ems`** (13 calls): `delete_custom_tag`×1, `get_zero_trust_rule_sets`×1, `get_zero_trust_tag_by_id`×1, `remove_custom_tag`×1, `get_endpoints`×1
- **`fortinet-forticnapp`** (13 calls): `search_alerts`×3, `add_comment_to_alert`×1, `close_alert`×1, `send_custom_request`×1, `get_alert_details`×1
- **`fortinet-fortiguard-outbreak`** (12 calls): `get_outbreak_alert_threat_actor_details_by_id`×1, `get_outbreak_alert_details_by_slug_name`×1, `list_threat_actors`×1, `list_outbreak_alert_details`×1, `bulk_ingest_outbreak_alert_iocs`×1
- **`fortisoar-soc-simulator`** (11 calls): `create_simulated_alert`×4, `malicious_file_indicator`×3, `bad_url`×3, `replace_variables`×1
- **`cisa-advisory`** (9 calls): `get_advisory`×5, `get_known_exploited_vulnerability_cves`×1, `get_advisory_by_product`×1, `get_advisory_by_year`×1, `get_advisory_by_vendor`×1
- **`fortinet-fortideceptor`** (9 calls): `decoy_stop`×1, `decoy_start`×1, `get_attack_events`×1, `decoy_deploy`×1, `decoy_delete`×1
- **`exchange`** (9 calls): `send_email`×7, `delete_email`×1, `run_query`×1
- **`whois-xml-api`** (8 calls): `reverse_whois_search`×1, `dns_lookup`×1, `ssl_certificates`×1, `reverse_dns_search`×1, `whois_search`×1
- **`time-series-chart-utilities`** (8 calls): `format_data_set_output_with_fieldgrouped`×2, `assemble_query_time_windows`×2, `combine_query_results_into_data_columns`×2, `flatten_data_sets_and_groups`×2
- **`splunk`** (8 calls): `get_results`×4, `invoke_search`×4
- **`file-content-extraction`** (7 calls): `extract_text`×4, `get_backend_config`×1, `create_xslx_file_from_json_data`×1, `extract_indicators_from_file`×1
- **`urlscan-io`** (7 calls): `submit_url`×2, `custom_search`×1, `search_hash`×1, `search_domain`×1, `search_ip`×1
- **`microsoft-winrm`** (7 calls): `execute_command`×2, `upload_file`×1, `execute_ps_command`×1, `execute_script`×1, `execute_ps_script`×1
- **`nist-nvd`** (7 calls): `get_specific_cve_details`×3, `cve_search`×1, `cve_search_by_keywords`×1, `cpe_search`×1, `get_cve_change_history`×1
- **`mysql`** (7 calls): `run_query`×5, `list_columns`×1, `list_tables`×1
- **`ip-quality-score`** (6 calls): `get_url_reputation`×2, `get_email_reputation`×2, `get_ip_reputation`×2
- **`fortinet-fortimanager-json-rpc`** (6 calls): `json_rpc_get`×1, `json_rpc_set`×1, `json_rpc_add`×1, `json_rpc_freeform`×1, `json_rpc_delete`×1
- **`malsilo`** (6 calls): `get_ipv4_feed`×2, `get_domain_feed`×2, `get_url_feed`×2
- **`fortinet-fortipam`** (5 calls): `update_user`×1, `execute_an_api_request`×1, `get_all_users`×1, `delete_user`×1, `get_user_details`×1
- **`axios-assyst`** (5 calls): `close_ticket`×1, `update_ticket`×1, `get_ticket_details`×1, `search_tickets`×1, `create_ticket`×1
- **`wazuh-siem`** (5 calls): `get_alerts_by_DSL_search`×2, `get_all_alerts_in_last_x_minutes`×1, `get_alerts_by_lucene_search`×1, `get_alert_by_id`×1
- **`servicenow`** (5 calls): `create_incident`×2, `get_assignment_group`×1, `get_location`×1, `get_users`×1
- **`fuzzy-search`** (4 calls): `filter_json_by_key_value`×3, `search_keyword_in_text`×1
- **`phishing-classifier`** (4 calls): `predict`×2, `train`×1, `get_training_results`×1
- **`cyops-system-monitoring`** (4 calls): `cpu_percent`×1, `disk_utilization`×1, `service_status`×1, `virtual_memory`×1
- **`screenshot`** (4 calls): `screenshot_url`×2, `screenshot_eml_or_msg_file`×1, `screenshot_mail`×1
- **`fortinet-fortiguard-ioc`** (4 calls): `get_selected_ioc_fields`×1, `get_visiting_countries`×1, `get_risk_distribution`×1, `execute_an_api_request`×1
- **`code-snippet`** (4 calls): `python_inline_code_editor`×4
- **`cicd-utils`** (4 calls): `import_fortisoar_template`×2, `review_import_fortisoar_template`×1, `export_fortisoar_template`×1
- **`ssh`** (4 calls): `run_remote_command`×4
- **`whois-freaks`** (3 calls): `ssl_certificates`×1, `dns_lookup`×1, `whois_lookup`×1
- **`fortinet-fortiai`** (3 calls): `submit_file`×1, `get_file_verdict_results`×1, `get_events`×1
- **`fortinet-fortiai-proxy`** (3 calls): `create_responses`×1, `chat_completion`×1, `get_token_balance_info`×1
- **`mitre-attack`** (3 calls): `get_mitre_data`×3
- **`fortisoar-ml-engine`** (3 calls): `train`×1, `predict`×1, `similar`×1
- **`cisco-catalyst`** (3 calls): `get_version`×1, `configure_vlan`×1, `get_config`×1
- **`exploit-prediction-scoring-system`** (3 calls): `get_epss_score_by_cve_id`×2, `get_epss_score`×1
- **`fortinet-web-filter-lookup`** (2 calls): `url_review`×2
- **`axonius`** (2 calls): `get_user_assets`×1, `get_device_assets`×1
- **`whois-rdap`** (2 calls): `whois_ip`×2
- **`slacalculator`** (2 calls): `calculateSLA`×1, `calculate_elapsed_time`×1
- **`dns`** (2 calls): `lookup_ip`×1, `lookup_domain`×1
- **`cyops-schedule-report`** (2 calls): `schedule_report_manual`×2
- **`ipstack`** (2 calls): `ip_locate`×2
- **`carbonblack-response`** (2 calls): `get_process_list`×1, `terminate_process`×1
- **`symantec-dlp`** (2 calls): `get_incident_details`×1, `get_incidents_ids`×1
- **`icanhazdadjoke`** (1 calls): `get_joke`×1
- **`toronto_weather`** (1 calls): `get_weather`×1
- **`imap`** (1 calls): `fetch_email_new`×1
- **`symantec-cloudsoc`** (1 calls): `get_logs`×1
- **`fortinet-fortimail`** (1 calls): `block_sender_address`×1
- **`alienvault-otx`** (1 calls): `get_file_reputation`×1
- **`qualys`** (1 calls): `list_host`×1

## 3. Trigger Types / Start Step Patterns

Start steps found: 1367 workflows with identifiable trigger step.

### 3.1 Trigger kind counts

| stepType UUID | Kind | Count |
|---|---|---|
| `f414d039-bb0d-4e59-9c39-a8f1e880b18a` | Manual button | 753 |
| `ea155646-3821-4542-9702-b246da430a8d` | On Create | 12 |
| `9300bf69-5063-486d-b3a6-47eb9da24872` | Field/status-change | 16 |
| `b348f017-9a94-471f-87f8-ce88b6a7ad62` | Referenced | 583 |
| `df26c7a2-4166-4ca5-91e5-548e24c01b5f` | REST API inbound | 3 |

### 3.2 Manual button (`f414d039-bb0d-4e59-9c39-a8f1e880b18a`) — 753 occurrences

Argument keys present (freq):

- `resources`: 753
- `inputVariables`: 753
- `step_variables`: 753
- `route`: 752
- `singleRecordExecution`: 750
- `noRecordExecution`: 745
- `executeButtonText`: 669
- `title`: 657
- `displayConditions`: 179
- `showToasterMessage`: 92
- `__triggerLimit`: 89
- `triggerOnSource`: 89
- `triggerOnReplicate`: 89
- `_promptexpanded`: 17
- `message`: 3
- `name`: 1
- `config`: 1
- `params`: 1
- `version`: 1
- `connector`: 1
- `operation`: 1
- `operationTitle`: 1

`step_variables.input` shapes observed:
- 445× input keys = ('records',)
- 305× input keys = ('params', 'records')
- 3× input keys = ('<none-or-other>',)

Example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "route": "f064f467-e02d-4a18-b2fd-7f03344ed00a",
    "title": "WhoisFreaks: Get SSL Certificates",
    "resources": [
      "alerts"
    ],
    "inputVariables": [],
    "step_variables": {
      "input": {
        "records": "{{vars.input.records[0]}}"
      }
    },
    "executeButtonText": "Execute",
    "noRecordExecution": true,
    "singleRecordExecution": false
  },
  "status": null,
  "top": "20",
  "left": "20",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "9520fe49-ea1d-48a6-9840-c2c5d5231ea1"
}
```
Second example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "route": "d9a0bbe1-2d94-4884-832d-2ac5f47c5c35",
    "title": "WhoisFreaks: Get DNS Lookup",
    "resources": [
      "alerts"
    ],
    "inputVariables": [],
    "step_variables": {
      "input": {
        "records": "{{vars.input.records[0]}}"
      }
    },
    "executeButtonText": "Execute",
    "noRecordExecution": true,
    "singleRecordExecution": false
  },
  "status": null,
  "top": "20",
  "left": "20",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "528d2c92-eebb-4930-9484-c0c46685965a"
}
```

### 3.2 On Create (`ea155646-3821-4542-9702-b246da430a8d`) — 12 occurrences

Argument keys present (freq):

- `resource`: 12
- `resources`: 12
- `step_variables`: 12
- `fieldbasedtrigger`: 12
- `__triggerLimit`: 1
- `triggerOnSource`: 1
- `triggerOnReplicate`: 1

`step_variables.input` shapes observed:
- 12× input keys = ('params', 'records')

Example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "resource": "threat_intel_reports",
    "resources": [
      "threat_intel_reports"
    ],
    "__triggerLimit": true,
    "step_variables": {
      "input": {
        "params": [],
        "records": [
          "{{vars.input.records[0]}}"
        ]
      }
    },
    "triggerOnSource": true,
    "fieldbasedtrigger": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": [
        {
          "type": "primitive",
          "field": "source",
          "value": "FortiRecon ACI Report",
          "operator": "eq",
          "_operator": "eq"
        }
      ]
    },
    "triggerOnReplicate": false
  },
  "status": null,
  "top": "30",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "c07f0c3d-2209-4f68-b6dd-3aae607b3476"
}
```
Second example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "resource": "alerts",
    "resources": [
      "alerts"
    ],
    "step_variables": {
      "input": {
        "params": {
          "file_iri": "{{ vars.file_iri }}",
          "alert_iri": "{{ vars.alert_iri }}"
        },
        "records": [
          "{{vars.input.records[0]}}"
        ]
      }
    },
    "fieldbasedtrigger": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": [
        {
          "type": "object",
          "field": "type",
          "value": "/api/3/picklists/<UUID>",
          "_value": {
            "display": "Suspicious Email",
            "itemValue": "Suspicious Email"
          },
          "operator": "eq"
        },
        {
          "type": "primitive",
          "field": "fileEmail",
          "value": "false",
          "operator": "isnull",
          "_operator": "isnull"
        }
      ]
    }
  },
  "status": null,
  "top": "30",
  "left": "300",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "df1be2cd-d2ea-429b-b6be-0eaf1a8bb51e"
}
```

### 3.2 Field/status-change (`9300bf69-5063-486d-b3a6-47eb9da24872`) — 16 occurrences

Argument keys present (freq):

- `resource`: 16
- `resources`: 16
- `step_variables`: 16
- `fieldbasedtrigger`: 16
- `__triggerLimit`: 3
- `triggerOnSource`: 3
- `triggerOnReplicate`: 3

`step_variables.input` shapes observed:
- 16× input keys = ('params', 'records')

Example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "resource": "threat_intel_reports",
    "resources": [
      "threat_intel_reports"
    ],
    "__triggerLimit": true,
    "step_variables": {
      "input": {
        "params": [],
        "records": [
          "{{vars.input.records[0]}}"
        ]
      }
    },
    "triggerOnSource": true,
    "fieldbasedtrigger": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": [
        {
          "type": "object",
          "field": "adversary",
          "value": "",
          "_value": {
            "@id": "",
            "display": "",
            "itemValue": ""
          },
          "operator": "changed"
        },
        {
          "type": "primitive",
          "field": "source",
          "value": "FortiRecon ACI Report",
          "operator": "eq",
          "_operator": "eq"
        }
      ]
    },
    "triggerOnReplicate": false
  },
  "status": null,
  "top": "20",
  "left": "120",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "75ea0139-8e70-4d29-8a1b-89d5351f4767"
}
```
Second example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "resource": "asset_change_activities",
    "resources": [
      "asset_change_activities"
    ],
    "step_variables": {
      "input": {
        "params": [],
        "records": [
          "{{vars.input.records[0]}}"
        ]
      }
    },
    "fieldbasedtrigger": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": [
        {
          "type": "object",
          "field": "status",
          "value": "",
          "_value": {
            "@id": "",
            "display": "",
            "itemValue": ""
          },
          "operator": "changed"
        },
        {
          "type": "object",
          "field": "status",
          "value": "/api/3/picklists/<UUID>",
          "_value": {
            "@id": "/api/3/picklists/<UUID>",
            "itemValue": "Closed"
          },
          "operator": "eq"
        }
      ]
    }
  },
  "status": null,
  "top": "30",
  "left": "475",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "f6e602b6-109f-4bd8-bf3f-28ce08117592"
}
```

### 3.2 Referenced (`b348f017-9a94-471f-87f8-ce88b6a7ad62`) — 583 occurrences

Argument keys present (freq):

- `step_variables`: 583
- `__triggerLimit`: 53
- `triggerOnSource`: 53
- `triggerOnReplicate`: 53
- `message`: 1

`step_variables.input` shapes observed:
- 467× input keys = ('params',)
- 107× input keys = ('records',)
- 9× input keys = ('<none-or-other>',)

Example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "step_variables": {
      "input": {
        "params": []
      }
    }
  },
  "status": null,
  "top": "20",
  "left": "20",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "45ee16ab-627d-4b88-8611-cb094843b858"
}
```
Second example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "step_variables": {
      "input": {
        "params": []
      }
    }
  },
  "status": null,
  "top": "20",
  "left": "20",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "74d1aee7-41bb-4685-b379-c9bb6ebf5f2e"
}
```

### 3.2 REST API inbound (`df26c7a2-4166-4ca5-91e5-548e24c01b5f`) — 3 occurrences

Argument keys present (freq):

- `route`: 3
- `authentication_methods`: 3
- `step_variables`: 2
- `__triggerLimit`: 1
- `triggerOnSource`: 1
- `triggerOnReplicate`: 1

`step_variables.input` shapes observed:
- 2× input keys = ('params',)
- 1× input keys = ('<none-or-other>',)

Example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "route": "qradar",
    "authentication_methods": [
      ""
    ]
  },
  "status": null,
  "top": "53",
  "left": "234",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "5cc52ab8-80ad-49b0-9dad-4987bd043068"
}
```
Second example (redacted):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "route": "fetch_emails_imap",
    "step_variables": {
      "input": {
        "params": {
          "api_body": "{{vars.request.data}}"
        }
      },
      "fileIndicatorType": "{{(\"IndicatorType\" | picklist(\"File\"))[\"@id\"]}}"
    },
    "authentication_methods": [
      ""
    ]
  },
  "status": null,
  "top": "53",
  "left": "60",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "ff54e698-3d97-4fd8-bbbc-891de63f7436"
}
```

### 3.3 Manual button `inputVariables` — full object shapes

Sampled 6 workflows with non-empty inputVariables.

Field keys on each inputVariable item (freq):
- `name`: 9
- `type`: 9
- `label`: 9
- `tooltip`: 9
- `dataType`: 9
- `formType`: 9
- `required`: 9
- `_expanded`: 9
- `useRecordFieldDefault`: 9
- `defaultValue`: 8
- `_previousName`: 6
- `title`: 5
- `usable`: 5
- `collection`: 5
- `searchable`: 5
- `templateUrl`: 5
- `lengthConstraint`: 5
- `allowedGridColumn`: 5
- `mmdUpdate`: 4
- `allowedEncryption`: 4
- `dataSource`: 3
- `visibilityQuery`: 3
- `jinjaExpressionView`: 3
- `_addVisibilityConditions`: 3
- `displayTemplate`: 2
- `bulkAction`: 1
- `inversedField`: 1
- `ownsRelationship`: 1
- `options`: 1
- `playbookField`: 1
- `moduleField`: 1

`type` values: {'picklists': 1, 'array': 1, 'string': 5, 'scenario': 1, 'boolean': 1}

Example inputVariables (redacted):
- _Sample.json_, workflow "MITRE ATT&CK > Fetch Latest Data", step "Start":
```json
[
  {
    "name": "matricesToPull",
    "type": "picklists",
    "label": "Matrices To Pull",
    "title": "Multiselect Picklist",
    "usable": true,
    "tooltip": "",
    "dataType": "multiselectpicklist",
    "formType": "multiselectpicklist",
    "required": false,
    "_expanded": true,
    "mmdUpdate": true,
    "bulkAction": [],
    "collection": true,
    "dataSource": {
      "model": "picklists",
      "query": {
        "sort": [
          {
            "field": "orderIndex",
            "direction": "ASC"
          }
        ],
        "logic": "AND",
        "filters": [
          {
            "field": "listName__name",
            "value": "Mitre ATT&CK Matrics",
            "operator": "eq"
          }
        ]
      },
      "displayConditions": {
        "1eca922e-85ff-46a7-af26-cafa7c334883": {
          "conditions": null,
          "visibility": "visible"
        },
        "6bf383dc-f042-4bf5-8ba6-0dedcdf0aa87": {
          "conditions": null,
          "visibility": "visible"
        },
        "e617e1bd-070b-4218-8e31-9e54e3f64c81": {
          "conditions": null,
          "visibility": "visible"
        }
      }
    },
    "searchable": false,
    "temp
```
- _Sample.json_, workflow "Get User's all Chat Messages", step "Start":
```json
[
  {
    "name": "getMessageBy",
    "type": "array",
    "label": "Get Message by",
    "title": "Dynamic List",
    "usable": true,
    "options": [
      "User Principal Name",
      "User ID"
    ],
    "tooltip": "",
    "dataType": "dynamicList",
    "formType": "dynamicList",
    "required": true,
    "_expanded": true,
    "mmdUpdate": true,
    "collection": false,
    "searchable": false,
    "templateUrl": "app/components/form/fields/dynamicList.html",
    "defaultValue": "User ID",
    "_previousName": "getMessageBy",
    "playbookField": true,
    "visibilityQuery": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": []
    },
    "lengthConstraint": true,
    "allowedGridColumn": false,
    "jinjaExpressionView": true,
    "useRecordFieldDefault": false,
    "_addVisibilityConditions": true
  },
  {
    "name": "userID",
    "type": "string",
    "label": "User ID",
    "tooltip": "Specify the ID of the User for which you want to retrieve all chat messages",
    "dataType": "text",
    "formType": "text",
    "required": true,
    "_expanded": true,
    "defaultValue": null,
    "_previousName": "",
    "visibilityQuery": {
      "sort": [],
```
- _UseCase.json_, workflow "Email (Manual Attach) - File to Alert (Suspicious Email)", step "Start":
```json
[
  {
    "name": "emailFile",
    "type": "string",
    "label": "Email File",
    "tooltip": "Upload email file, either *.eml or *.msg extension",
    "dataType": "text",
    "formType": "text",
    "required": true,
    "_expanded": true,
    "moduleField": "fileEmail",
    "_previousName": "",
    "useRecordFieldDefault": true
  }
]
```

### 3.4 REST API inbound trigger — `route` and `authentication_methods`

- _Sample.json_ "API - Push Offense From QRadar": route=`qradar`, auth=['']
- _Sample.json_ "IMAP > Ingest": route=`fetch_emails_imap`, auth=['']
- _UseCase.json_ "FortiRecon - Domain Threat": route=`deferred/Domain-Threat`, auth=['Basic']


## 4. Workflow Object Field Survey

Sampled 30 workflows. Fields present (with type distribution and sample values):

| Field | Present in N/30 | Type distribution | Sample values |
|---|---|---|---|
| `@type` | 30 | str:30 | Workflow | Workflow | Workflow |
| `triggerLimit` | 30 | null:30 | None | None | None |
| `name` | 30 | str:30 | Get SSL Certificates | Create Response | Search Code |
| `aliasName` | 30 | null:30 | None | None | None |
| `tag` | 30 | str:19, null:11 | #WhoisFreaks | #OpenAI | #GitHub |
| `description` | 30 | str:30 | Obtains a domain name's Secure Sockets Layer (SSL) | Replaces the deprecated 4-step Assistants API flow | Searches for specified query. |
| `isActive` | 30 | bool:30 | False | False | False |
| `debug` | 30 | bool:30 | False | False | False |
| `singleRecordExecution` | 30 | bool:30 | False | False | False |
| `remoteExecutableFlag` | 30 | bool:30 | False | False | False |
| `parameters` | 30 | list[0]:26, list[1]:2, list[2]:1, list[4]:1 | <list[0]> | <list[0]> | <list[0]> |
| `synchronous` | 30 | bool:30 | False | False | False |
| `lastModifyDate` | 30 | num:22, null:8 | None | 1777291089 | 1755774328 |
| `collection` | 30 | str:30 | /api/3/workflow_collections/01f8b143-e188-4e29-a99 | /api/3/workflow_collections/033c380b-3d36-4289-b05 | /api/3/workflow_collections/040f8b1d-88f2-436e-9ef |
| `versions` | 30 | list[0]:30 | <list[0]> | <list[0]> | <list[0]> |
| `triggerStep` | 30 | str:30 | /api/3/workflow_steps/9520fe49-ea1d-48a6-9840-c2c5 | /api/3/workflow_steps/305f8f33-b9e6-472c-87af-369d | /api/3/workflow_steps/85dd58e4-c2a2-4d94-b053-dca8 |
| `priority` | 30 | null:18, str:12 | None | None | None |
| `playbookOrigin` | 30 | str:30 | /api/3/picklists/15c1e8c9-22bf-4e66-8fbb-0a502d4a4 | /api/3/picklists/15c1e8c9-22bf-4e66-8fbb-0a502d4a4 | /api/3/picklists/15c1e8c9-22bf-4e66-8fbb-0a502d4a4 |
| `isEditable` | 30 | bool:30 | True | True | True |
| `uuid` | 30 | str:30 | ccdf20ac-2fc5-480f-8f32-969854ef192a | f3b8525e-9dd7-49d4-8e90-80df0e82c501 | 75dd6c6c-6204-444a-a3e9-fef4320660a7 |
| `id` | 30 | num:30 | 2967 | 6277 | 4194 |
| `owners` | 30 | list[0]:30 | <list[0]> | <list[0]> | <list[0]> |
| `isPrivate` | 30 | bool:30 | False | False | False |
| `deletedAt` | 30 | null:30 | None | None | None |
| `importedBy` | 30 | list[0]:26, list[1] of dict:4 | <list[0]> | <list[0]> | <list[0]> |
| `recordTags` | 30 | list[2]:23, list[1]:3, list[3]:3, list[5]:1 | <list[2]> | <list[2]> | <list[1]> |

### 4.1 Always-present fields (in all 30 sampled)

`@type`, `aliasName`, `collection`, `debug`, `deletedAt`, `description`, `id`, `importedBy`, `isActive`, `isEditable`, `isPrivate`, `lastModifyDate`, `name`, `owners`, `parameters`, `playbookOrigin`, `priority`, `recordTags`, `remoteExecutableFlag`, `singleRecordExecution`, `synchronous`, `tag`, `triggerLimit`, `triggerStep`, `uuid`, `versions`

### 4.2 Sometimes-absent fields


### 4.3 `priority` picklist values observed

- `2b563c61-ae2c-41c0-a85a-c9709585e3f2`: 462

### 4.4 `playbookOrigin` picklist values observed

- `15c1e8c9-22bf-4e66-8fbb-0a502d4a4a3f`: 1305
- `b6d710a9-a8ec-41ec-8817-fe9fa062fcdd`: 62

### 4.5 Ownership / collaboration / misc fields (sampled counts across ALL workflows)

- `isPrivate`: present in 1367/1367; value types: {'bool': 1367}
- `owners`: present in 1367/1367; value types: {'list': 1367}
- `isCollaborative`: present in 0/1367; value types: {}
- `waitForCompletion`: present in 0/1367; value types: {}
- `runAsUser`: present in 0/1367; value types: {}
- `ownership`: present in 0/1367; value types: {}
- `triggeredBy`: present in 0/1367; value types: {}
- `tags`: present in 0/1367; value types: {}
- `category`: present in 0/1367; value types: {}
- `aliasName`: present in 1367/1367; value types: {'NoneType:None': 1367}
- `tag`: present in 1367/1367; value types: {'str': 925, 'NoneType:None': 442}
- `remoteExecutableFlag`: present in 1367/1367; value types: {'bool': 1367}
- `synchronous`: present in 1367/1367; value types: {'bool': 1367}
- `singleRecordExecution`: present in 1367/1367; value types: {'bool': 1367}
- `debug`: present in 1367/1367; value types: {'bool': 1367}
- `isActive`: present in 1367/1367; value types: {'bool': 1367}
- `isEditable`: present in 1367/1367; value types: {'bool': 1367}
- `triggerLimit`: present in 1367/1367; value types: {'NoneType:None': 1367}
- `lastModifyDate`: present in 1367/1367; value types: {'NoneType:None': 418, 'int': 949}
- `playbookOrigin`: present in 1367/1367; value types: {'str': 1367}
- `id`: present in 1367/1367; value types: {'int': 1367}
- `importedBy`: present in 1367/1367; value types: {'list': 1367}
- `recordTags`: present in 1367/1367; value types: {'list': 1367}

## 5. Step Argument Patterns per Step Type

### 5.x `0bfed618-0316-11e7-93ae-92361f002671` — Connector external (1326 occurrences)

Argument keys (from sample): `name`(3), `config`(3), `params`(3), `version`(3), `connector`(3), `operation`(3), `operationTitle`(3), `step_variables`(3)
step_variables keys: `output_data`(3)

Example 1 — step "Get SSL Certificates" (workflow "Get SSL Certificates", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Get SSL Certificates",
  "description": null,
  "arguments": {
    "name": "WhoisFreaks",
    "config": "''",
    "params": {
      "chain": false,
      "SSLRaw": false
    },
    "version": "1.0.0",
    "connector": "whois-freaks",
    "operation": "ssl_certificates",
    "operationTitle": "Get SSL Certificates",
    "step_variables": {
      "output_data": "{{vars.result}}"
    }
  },
  "status": null,
  "top": "120",
  "left": "188",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "b1787d5e-0bf3-4f93-b793-51df55a32e72"
}
```
Example 2 — step "Get DNS Lookup" (workflow "Get DNS Lookup", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Get DNS Lookup",
  "description": null,
  "arguments": {
    "name": "WhoisFreaks",
    "config": "''",
    "params": {
      "type": "all"
    },
    "version": "1.0.0",
    "connector": "whois-freaks",
    "operation": "dns_lookup",
    "operationTitle": "Get DNS Lookup",
    "step_variables": {
      "output_data": "{{vars.result}}"
    }
  },
  "status": null,
  "top": "120",
  "left": "188",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "a3a587dc-c440-4e33-8472-4ff0c46393ca"
}
```
Example 3 — step "Get Whois Lookup" (workflow "Get Whois Lookup", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Get Whois Lookup",
  "description": null,
  "arguments": {
    "name": "WhoisFreaks",
    "config": "''",
    "params": [],
    "version": "1.0.0",
    "connector": "whois-freaks",
    "operation": "whois_lookup",
    "operationTitle": "Get Whois Lookup",
    "step_variables": {
      "output_data": "{{vars.result}}"
    }
  },
  "status": null,
  "top": "120",
  "left": "188",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "2fbf1419-72af-4901-a458-c76b262e41b0"
}
```

### 5.x `f414d039-bb0d-4e59-9c39-a8f1e880b18a` — Manual button (Start) (753 occurrences)

Argument keys (from sample): `route`(3), `title`(3), `resources`(3), `inputVariables`(3), `step_variables`(3), `executeButtonText`(3), `noRecordExecution`(3), `singleRecordExecution`(3)
step_variables keys: `input`(3)

Example 1 — step "Start" (workflow "Get SSL Certificates", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "route": "f064f467-e02d-4a18-b2fd-7f03344ed00a",
    "title": "WhoisFreaks: Get SSL Certificates",
    "resources": [
      "alerts"
    ],
    "inputVariables": [],
    "step_variables": {
      "input": {
        "records": "{{vars.input.records[0]}}"
      }
    },
    "executeButtonText": "Execute",
    "noRecordExecution": true,
    "singleRecordExecution": false
  },
  "status": null,
  "top": "20",
  "left": "20",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "9520fe49-ea1d-48a6-9840-c2c5d5231ea1"
}
```

### 5.x `b348f017-9a94-471f-87f8-ce88b6a7ad62` — b348f017-9a94-471f-87f8-ce88b6a7ad62 (583 occurrences)

Argument keys (from sample): `step_variables`(3)
step_variables keys: `input`(3)

Example 1 — step "Start" (workflow "Create Vector Store", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Start",
  "description": null,
  "arguments": {
    "step_variables": {
      "input": {
        "params": []
      }
    }
  },
  "status": null,
  "top": "20",
  "left": "20",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "45ee16ab-627d-4b88-8611-cb094843b858"
}
```

### 5.x `04d0cf46-b6a8-42c4-8683-60a7eaa69e8f` — Set Variable (543 occurrences)

Argument keys (from sample): `data`(3)

Example 1 — step "Set Result" (workflow "GitHub - List Pull Request", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Set Result",
  "description": null,
  "arguments": {
    "data": "{% if vars.input.params['list_pr_params']['pull_number'] %}{% set reviewers = vars.result.requested_reviewers | default([]) %}{% set reviewer_names = reviewers | map(attribute='login') | list %}{% set _ = vars.result.update({\"reviewer_names\": reviewer_names}) %}{% else %}{% for pr in vars.result %}{% set reviewers = pr.requested_reviewers | default([]) %}{% set reviewer_names = reviewers | map(attribute='login') | list %}{% set _ = pr.update({\"reviewer_names\": reviewer_names}) %}{% endfor %}\n{% endif %}{{ vars.result }}"
  },
  "status": null,
  "top": "300",
  "left": "120",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "584a4b09-0b14-4aef-8014-8dc6febf10d6"
}
```
Example 2 — step "Return Result" (workflow "GitHub - Get Commit Comparison", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Return Result",
  "description": null,
  "arguments": {
    "data": "{% set result = vars.steps.Get_Commit_Comparison.data %}{% set _ = result.update({\"web_url\": vars.web_url }) %}{{result}}"
  },
  "status": null,
  "top": "300",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "f2825893-376c-4a02-aa15-3cdd3cfb8f48"
}
```
Example 3 — step "Save Result" (workflow "GitHub - Fetch Release", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Save Result",
  "description": null,
  "arguments": {
    "data": "{% if vars.steps.Fetch_Release.data | length > 0 %}{{(vars.steps.Fetch_Release.data | json_query(\"[?name=='\"+(vars.input.params[\"fetch_release_params\"][\"release_name\"])+\"']\"))[0]}}{% endif %}"
  },
  "status": null,
  "top": "300",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "15caa26f-f91d-431d-9ee6-197df4c2dd1a"
}
```

### 5.x `2597053c-e718-44b4-8394-4d40fe26d357` — Create Record (314 occurrences)

Argument keys (from sample): `resource`(3), `operation`(3), `collection`(3), `__recommend`(3), `fieldOperation`(3), `step_variables`(3), `_showJson`(2), `for_each`(1)

Example 1 — step "Create Record" (workflow "MITRE ATT&CK > Create", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Create Record",
  "description": null,
  "arguments": {
    "resource": {
      "url": "{{vars.sourcedata[\"external_references\"][0][\"url\"]}}",
      "name": "{{vars.sourcedata[\"name\"]}}",
      "created": "{{vars.sourcedata[\"created\"]}}",
      "mitreId": "<System Mapping. Do not modify>",
      "version": "{{vars.sourcedata[\"x_mitre_version\"]}}",
      "__replace": "",
      "description": "{{vars.sourcedata[\"description\"]}}",
      "lastModified": "{{vars.sourcedata[\"modified\"]}}"
    },
    "_showJson": false,
    "operation": "Overwrite",
    "collection": "/api/3/mitre_groups",
    "__recommend": [],
    "fieldOperation": {
      "recordTags": "Overwrite"
    },
    "step_variables": []
  },
  "status": null,
  "top": "120",
  "left": "320",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "499bfc91-b9f9-47ba-8ea5-03ccf9867e0a"
}
```
Example 2 — step "Create Threat Intel Feed" (workflow "FortiSOAR Threat Intel Feeds Using Threat Intel Report > Create", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Create Threat Intel Feed",
  "description": null,
  "arguments": {
    "for_each": {
      "item": "{{vars.input.params['report_iocs']}}",
      "__bulk": true,
      "parallel": false,
      "condition": "",
      "batch_size": 100
    },
    "resource": {
      "value": "{{vars.item.name}}",
      "__link": {
        "recordTags": "{{vars.tags}}",
        "threatIntelReports": "[\"{{vars.steps.Create_Record['@id']}}\"]"
      },
      "source": "FortiRecon ACI Report",
      "sourceId": "{{vars.report_details.report_id}}",
      "__replace": "true",
      "expiresOn": "{{ arrow.now().int_timestamp + (vars.input.params['expiry'] | int) * 24 * 60 * 60 }}",
      "confidence": "{{vars.input.params.confidence}}",
      "reputation": "{{vars.input.params.reputation | resolveRange(vars.reputation_map)}}",
      "sourceData": "{{vars.item}}",
      "typeOfFeed": "{{vars.item.type | resolveRange(vars.threat_intel_feed_type_map)}}",
      "description": "<p>{{vars.report_details.title}}</p>",
      "patternType": "STIX",
      "patternVersion": "2.1"
    },
    "_showJson": false,
    "operation": "Append",
    "collection": "/api/3/upsert/threat_intel_feeds",
    "__recommend": [],
    "fieldOperation": {
      "recordTags": "Append",
      "threatTypes": "Overwrite",
      "killChainPhases": "Overwrite"
    },
    "step_variables": []
  },
  "status": null,
  "top": "705",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "df5c23a3-c0c7-4fec-a8af-b49bea961002"
}
```

### 5.x `0109f35d-090b-4a2b-bd8a-94cbc3508562` — Connector cyops_utilities (237 occurrences)

Argument keys (from sample): `params`(3), `version`(3), `connector`(3), `operation`(3), `operationTitle`(3), `step_variables`(3), `ignore_errors`(2)

Example 1 — step "Compute Category" (workflow "URL / Domain > Fortinet Web Filter Lookup > Enrichment", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Compute Category",
  "description": null,
  "arguments": {
    "params": {
      "value": "<table class=\"no-border\">\n    <tr>\n        <th colspan=\"1\" class=\"no-background padding-0\">\n            <div class=\"font-size-11 ng-binding padding-bottom-sm\">\n                <h4 style=\"color: orange;\"\n                    class=\"body-default-bgcolor margin-bottom-0 padding-bottom-md padding-left-md padding-top-md text-align-left\">\n                    Fortinet Web Filter Lookup Detection Summary</h4>\n            </div>\n        </th>\n    </tr>\n    <tr class=\"solid-border\">\n        <td>\n            <div small class=\"control-label\">Category</div>\n            <div class=\"card-container-body margin-left-0\" style=\"width: auto;\">\n                    <div class=\"body-default-bgcolor card-number padding-left-md\"\n                    style=\"border-left: 5px solid {{vars.input.params.style_colors.Malicious}};padding: 11px;font-size: 18px !important;\">{{vars.catagory.Category}}</div>\n            </div>\n        </td>\n    </tr>\n</table>"
    },
    "version": "3.2.1",
    "connector": "cyops_utilities",
    "operation": "format_richtext",
    "ignore_errors": false,
    "operationTitle": "Utils: Format as RichText",
    "step_variables": []
  },
  "status": null,
  "top": "570",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "50b86919-c277-4d8c-8890-44f1a822cf29"
}
```
Example 2 — step "No Operation" (workflow "URL / Domain > Fortinet Web Filter Lookup > Enrichment", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "No Operation",
  "description": null,
  "arguments": {
    "params": [],
    "version": "3.2.1",
    "connector": "cyops_utilities",
    "operation": "no_op",
    "operationTitle": "Utils: No Operation",
    "step_variables": []
  },
  "status": null,
  "top": "435",
  "left": "475",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "469ace6c-a414-4967-873d-6e88c51bd10d"
}
```
Example 3 — step "Compute Url Scan Summary" (workflow "URL > URLScan.io > Enrichment", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Compute Url Scan Summary",
  "description": null,
  "arguments": {
    "params": {
      "value": "<table class=\"no-border\">\n    <tr>\n        <th colspan=\"1\" class=\"no-background padding-0\">\n            <div class=\"font-size-11 ng-binding padding-bottom-sm\">\n                <h4 style=\"color: orange;\"\n                    class=\"body-default-bgcolor margin-bottom-0 padding-bottom-md padding-left-md padding-top-md text-align-left\">\n                    URL Scan Summary</h4>\n            </div>\n        </th>\n    </tr>\n    <tr class=\"solid-border\">\n        <td style=\"vertical-align: top;\">\n            <div><a title=\"Click Link\" href=\"{{vars.screenshot}}\" target=\"_blank\" rel=\"noopener noreferrer\"><img\n                        src=\"{{vars.screenshot}}\" alt=\"Screenshot URL\" width=\"200\" height=\"100\"></a></div>\n        </td>\n    </tr>\n</table>"
    },
    "version": "3.2.1",
    "connector": "cyops_utilities",
    "operation": "format_richtext",
    "ignore_errors": false,
    "operationTitle": "Utils: Format as RichText",
    "step_variables": []
  },
  "status": null,
  "top": "840",
  "left": "475",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "dd4471c7-ffbd-4e12-8745-3436bd60b27b"
}
```

### 5.x `74932bdc-b8b6-4d24-88c4-1a4dfbc524f3` — Reference a Playbook (231 occurrences)

Argument keys (from sample): `arguments`(3), `apply_async`(3), `step_variables`(3), `workflowReference`(3), `pass_parent_env`(2), `pass_input_record`(2), `do_until`(1), `for_each`(1)

Example 1 — step "Validate Slack Input Form" (workflow "Validate Slack Input From", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Validate Slack Input Form",
  "description": null,
  "arguments": {
    "do_until": {
      "delay": 5,
      "retries": 5,
      "condition": "{{vars.steps.Validate_Slack_Input_Form.validation == 1}}"
    },
    "arguments": [],
    "apply_async": false,
    "step_variables": [],
    "pass_parent_env": true,
    "pass_input_record": false,
    "workflowReference": "<WORKFLOW-IRI>"
  },
  "status": null,
  "top": "200",
  "left": "220",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "d1230d7d-5fc6-48e6-900f-455347646791"
}
```
Example 2 — step "Fetch" (workflow "MITRE ATT&CK > Ingest", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Fetch",
  "description": null,
  "arguments": {
    "arguments": [],
    "apply_async": false,
    "step_variables": [],
    "workflowReference": "<WORKFLOW-IRI>"
  },
  "status": null,
  "top": "140",
  "left": "240",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "e1ccd864-e151-44ca-b60e-4ff52980ba2b"
}
```
Example 3 — step "Create Threat Intel Record" (workflow "FortiRecon ACI Threat Intel Report > Fetch", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Create Threat Intel Record",
  "description": null,
  "arguments": {
    "for_each": {
      "item": "{{vars.steps.Get_Report_IOCs}}",
      "parallel": false,
      "condition": ""
    },
    "arguments": {
      "tlp": "",
      "expiry": "{{vars.expiry}}",
      "confidence": "{{vars.confidence}}",
      "reputation": "{{vars.reputation}}",
      "report_iocs": "{{vars.item.report_iocs}}",
      "report_details": "{{vars.item.report_details}}"
    },
    "apply_async": false,
    "step_variables": [],
    "pass_parent_env": false,
    "pass_input_record": true,
    "workflowReference": "<WORKFLOW-IRI>"
  },
  "status": null,
  "top": "1380",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "184eceeb-82c8-4489-b387-a59b2d611c85"
}
```

### 5.x `b593663d-7d13-40ce-a3a3-96dece928722` — Update Record (210 occurrences)

Argument keys (from sample): `resource`(3), `operation`(3), `collection`(3), `collectionType`(3), `fieldOperation`(3), `step_variables`(3), `__recommend`(2), `_showJson`(2)

Example 1 — step "Update Correlated Records" (workflow "Map Adversary to MITRE Groups/Techniques/Softwares", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Update Correlated Records",
  "description": null,
  "arguments": {
    "resource": {
      "__link": {
        "relatedMalware": "{{vars.software}}",
        "relatedThreatActors": "{{vars.groups_iri}}",
        "relatedATTCKTechniques": "{{vars.techniques}}"
      }
    },
    "operation": "Append",
    "collection": "{{vars.input.records[0]['@id']}}",
    "__recommend": [],
    "collectionType": "/api/3/threat_intel_reports",
    "fieldOperation": {
      "recordTags": "Append"
    },
    "step_variables": []
  },
  "status": null,
  "top": "570",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "3320d283-2210-49f4-b60d-2bcc2c13c0ae"
}
```
Example 2 — step "Update Alert" (workflow "IBM QRadar > Post Create Alert > Fetch Events", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Update Alert",
  "description": null,
  "arguments": {
    "resource": {
      "sourcedata": "{{vars.offense_details | toJSON }}"
    },
    "_showJson": false,
    "operation": "Overwrite",
    "collection": "{{vars.input.params.alertRecord['@id']}}",
    "__recommend": [],
    "collectionType": "/api/3/alerts",
    "fieldOperation": {
      "recordTags": "Append"
    },
    "step_variables": []
  },
  "status": null,
  "top": "353",
  "left": "840",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "0a5d9a2b-f044-4d65-9f28-4e21fb136aba"
}
```
Example 3 — step "Update Record" (workflow ">> FortiSIEM > Fetch Associated events for Incident", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Update Record",
  "description": null,
  "arguments": {
    "resource": {
      "sourcedata": "{{vars.incident_details | toJSON }}"
    },
    "_showJson": false,
    "operation": "Overwrite",
    "collection": "{{vars.incidentdata['@id']}}",
    "collectionType": "/api/3/alerts",
    "fieldOperation": {
      "recordTags": "Overwrite"
    },
    "step_variables": []
  },
  "status": null,
  "top": "420",
  "left": "720",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "1e1ba681-20b6-44c8-987d-06c5873d33ce"
}
```

### 5.x `12254cf5-5db7-4b1a-8cb1-3af081924b28` — Condition (188 occurrences)

Argument keys (from sample): `conditions`(3), `step_variables`(1)

Example 1 — step "Is Reputation Found" (workflow "URL / Domain > Fortinet Web Filter Lookup > Enrichment", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Is Reputation Found",
  "description": null,
  "arguments": {
    "conditions": [
      {
        "option": "Yes",
        "step_iri": "/api/3/workflow_steps/<UUID>",
        "condition": "{{ vars.foundFortinetWebFilterReputation or vars.useMockOutput }}",
        "step_name": "Get Category"
      },
      {
        "option": "No",
        "default": true,
        "step_iri": "/api/3/workflow_steps/<UUID>",
        "step_name": "No Operation"
      }
    ]
  },
  "status": null,
  "top": "300",
  "left": "300",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "70b820bd-d006-4809-8571-54168c26c559"
}
```
Example 2 — step "Validate required parameters" (workflow "Send Slack Input Form to Slack User", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Validate required parameters",
  "description": null,
  "arguments": {
    "conditions": [
      {
        "option": "Required parameters not provided",
        "step_iri": "/api/3/workflow_steps/<UUID>",
        "condition": "{{ vars.input_values.input1 == None }}",
        "step_name": "Set Result Not Ok"
      },
      {
        "option": "Validation successful",
        "default": true,
        "step_iri": "/api/3/workflow_steps/<UUID>",
        "step_name": "Set Result Ok"
      }
    ],
    "step_variables": []
  },
  "status": null,
  "top": "360",
  "left": "620",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "99fb4a30-7aa5-4350-ad54-5716b666db1d"
}
```

### 5.x `b593663d-7d13-40ce-a3a3-96dece928770` — Find Records (124 occurrences)

Argument keys (from sample): `query`(3), `module`(3), `step_variables`(3), `checkboxFields`(2)
step_variables keys: `resultRecordscount`(1)

Example 1 — step "Find Existing Description" (workflow "URL > FortiSandbox > Enrichment", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Find Existing Description",
  "description": null,
  "arguments": {
    "query": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": [
        {
          "type": "primitive",
          "field": "id",
          "value": "{{vars.input.records[0].id}}",
          "operator": "eq",
          "_operator": "eq"
        }
      ],
      "__selectFields": [
        "description"
      ]
    },
    "module": "indicators?$limit=30",
    "checkboxFields": true,
    "step_variables": []
  },
  "status": null,
  "top": "1515",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "721cd616-9c45-47aa-9986-cbb0ea0e806f"
}
```
Example 2 — step "Retrieve Existing Records" (workflow "> FortiEDR > Create and Link Asset", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Retrieve Existing Records",
  "description": null,
  "arguments": {
    "query": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": [
        {
          "logic": "AND",
          "filters": [
            {
              "type": "primitive",
              "field": "hostname",
              "value": "false",
              "operator": "isnull",
              "_operator": "isnull"
            },
            {
              "type": "primitive",
              "field": "hostname",
              "value": "{{vars.input.params.assetHostname | default('NULL', true)}}",
              "operator": "eq",
              "_operator": "eq"
            }
          ]
        },
        {
          "logic": "AND",
          "filters": [
            {
              "type": "primitive",
              "field": "ip",
              "value": "false",
              "operator": "isnull",
              "_operator": "isnull"
            },
            {
              "type": "primitive",
              "field": "ip",
              "value": "{{vars.input.params.assetIP | default('NULL', true) }}",
              "operator": "eq",
              "_operator": "eq"
            }
          ]
        }
      ]
    },
    "module": "assets?$limit=1",
    "step_variables": {
      "resultRecordscount": "{{vars.result | length}}"
    }
  },
  "status": null,
  "top": "165",
  "left": "300",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "2da5b6a9-c0b5-46ea-bb4e-9f1e9b702aba"
}
```

### 5.x `fc04082a-d7dc-4299-96fb-6837b1baa0fe` — fc04082a-d7dc-4299-96fb-6837b1baa0fe (61 occurrences)

Argument keys (from sample): `type`(3), `input`(3), `record`(3), `agent_id`(3), `owner_detail`(3), `isRecordLinked`(3), `step_variables`(3), `response_mapping`(3), `email_notification`(3), `inline_channel_list`(3), `external_channel_list`(3), `unauthenticated_input`(3), `inputExternalUser`(2), `inputInternalUsers`(2), `resources`(2), `is_approval`(1), `customEmailExternal`(1), `customEmailInternal`(1), `external_email_subject`(1), `internal_email_subject`(1), `custom_email_body_internal`(1), `internal_email_attachments`(1)

Example 1 — step "Sample Input From" (workflow "Send Slack Input Form to Slack User", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Sample Input From",
  "description": null,
  "arguments": {
    "type": "InputBased",
    "input": {
      "schema": {
        "title": "Sample Input Form",
        "description": "Please Provide Inputs",
        "inputVariables": [
          {
            "name": "input1",
            "type": "string",
            "label": "Input1",
            "title": "JSON",
            "usable": true,
            "tooltip": "",
            "dataType": "text",
            "formType": "text",
            "required": true,
            "_expanded": true,
            "mmdUpdate": true,
            "collection": false,
            "searchable": false,
            "templateUrl": "app/components/form/fields/json.html",
            "defaultValue": null,
            "_previousName": "input",
            "playbookField": true,
            "lengthConstraint": false,
            "allowedGridColumn": false,
            "jinjaExpressionView": true,
            "useRecordFieldDefault": false
          },
          {
            "name": "input2",
            "type": "string",
            "label": "Input2",
            "tooltip": "",
            "dataType": "text",
            "formType": "text",
            "required": false,
            "_expanded": true,
            "defaultValue": null,
            "_previousName": "input1",
            "jinjaExpressionView": true,
            "useRecordFieldDefault": false
          },
          {
            "name": "slackConfiguration",
            "type": "object",
            "label": "Slack Configuration",
            "title": "JSON",
            "usable": true,
            "tooltip": "",
            "dataType": "object",
            "formType": "object",
            "required": false,
            "_expanded": true,
            "mmdUpdate": true,
            "collection": false,
            "searchable": false,
            "templateUrl": "app/components/form/fields/json.html",
            "defaultValue": "{\n  \"require_confirmation_on_submission\": true,\n  \"playbook_resume_error_message\": \"Custom error message when resume playbook get failed\",\n  \"input_submitted_successfully_message\": \"Custom message when input form submitted successfully\",\n  \"message_for_button\": {\n    \"Yes\": {\n      \"input_submitted_successfully_message\": \"Custom message to show user when user click on Yes button and submit input form successfully\",\n      \"confirmation_message\": \"custom confirmation message f
```
Example 2 — step "Send Manual Input Form to Microsoft Teams" (workflow "Send Bot Message/Input Form", _Sample.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Send Manual Input Form to Microsoft Teams",
  "description": null,
  "arguments": {
    "type": "InputBased",
    "input": {
      "schema": {
        "title": "Do you Approve this request?",
        "description": "Please provide approval for this request.",
        "inputVariables": [
          {
            "name": "comment",
            "type": "string",
            "label": "Comment",
            "tooltip": "",
            "dataType": "text",
            "formType": "text",
            "required": false,
            "_expanded": true,
            "defaultValue": null,
            "_previousName": "comm",
            "jinjaExpressionView": true,
            "useRecordFieldDefault": false
          }
        ]
      }
    },
    "record": "",
    "agent_id": null,
    "resources": "alerts",
    "owner_detail": {
      "isAssigned": false,
      "emailRecipients": "",
      "externalRecipients": "{{vars.conversation_id}}"
    },
    "isRecordLinked": false,
    "step_variables": [],
    "response_mapping": {
      "options": [
        {
          "option": "Approve",
          "primary": true,
          "step_iri": "/api/3/workflow_steps/<UUID>"
        },
        {
          "option": "Reject",
          "primary": true,
          "step_iri": "/api/3/workflow_steps/<UUID>"
        }
      ],
      "duplicateOption": false
    },
    "inputExternalUser": false,
    "email_notification": {
      "enabled": false,
      "smtpParameters": []
    },
    "inputInternalUsers": true,
    "inline_channel_list": [
      "/api/3/picklists/<UUID>"
    ],
    "external_channel_list": [],
    "unauthenticated_input": true
  },
  "status": null,
  "top": "300",
  "left": "300",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "7e2d3ee2-b12d-455e-8aad-4039372543fb"
}
```
Example 3 — step "Assignee And Approver Name" (workflow "Add Cyber Asset", _UseCase.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Assignee And Approver Name",
  "description": null,
  "arguments": {
    "type": "InputBased",
    "input": {
      "schema": {
        "title": "Specify Assignee And Approver For Tasks",
        "description": "<h4>Following Tasks will be created based on the Asset Change Type Activity. Please assign suitable users for each task. The users will get notifications and the tasks will be assigned accordingly. </h4>\n<h5 ><span style=\"color: red\">Note:</span> New tasks get created once the previous task is completed. </h5>\n\n<hr>\n",
        "inputVariables": [
          {
            "name": "identifySecurityControl",
            "type": "people",
            "label": "Assignee For Task: Identify Security Control",
            "title": "Lookup (One to Many or One to One)",
            "usable": true,
            "tooltip": "Identify Impacted CIP-005 & CIP-007 Security Control.",
            "dataType": "lookup",
            "formType": "lookup",
            "required": true,
            "_expanded": false,
            "mmdUpdate": true,
            "collection": false,
            "dataSource": {
              "model": "people"
            },
            "searchable": false,
            "templateUrl": "app/components/form/fields/typeahead.html",
            "_nameTouched": true,
            "defaultValue": {
              "id": 3,
              "@id": "/api/3/people/<UUID>",
              "type": null,
              "uuid": "3451141c-bac6-467c-8d72-85e0fab569ce",
              "@type": "Person",
              "email": "admin@example.com",
              "roles": [
                "/api/3/roles/<UUID>",
                "/api/3/roles/<UUID>",
                "/api/3/roles/<UUID>"
              ],
              "tasks": [],
              "teams": [
                "/api/3/teams/<UUID>"
              ],
              "title": "Admin",
              "alerts": [],
              "avatar": null,
              "shifts": [],
              "userId": "d4f98222-a822-4dbd-849b-f5a91907a104",
              "display": "CS Admin",
              "@context": "/api/3/contexts/Person",
              "comments": [],
              "csActive": true,
              "lastname": "Admin",
              "phoneFax": null,
              "userType": null,
              "@settings": {
                "user": {
                  "view": {
                    "theme": "steel",
                    "details": {
                      "tasks": {
           
```

### 5.x `dc6ac63d-c5a5-472f-9eb4-6b18473a98b8` — dc6ac63d-c5a5-472f-9eb4-6b18473a98b8 (47 occurrences)

Argument keys (from sample): `message`(3), `resource`(3), `collection`(3), `step_variables`(3)

Example 1 — step "Approver Approval To Implement" (workflow "Add Cyber Asset", _UseCase.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Approver Approval To Implement",
  "description": null,
  "arguments": {
    "message": {
      "tags": [],
      "type": "/api/3/picklists/<UUID>",
      "tenant": "",
      "content": "<p>Added task <a href=\"/modules/tasks/{{vars.steps.Approver_Approval_To_Implement.uuid}}\" target=\"_blank\" rel=\"noopener\">{{vars.steps.Approver_Approval_To_Implement.name}}</a> to <strong>'Approver Approval To Implement'</strong></p>",
      "records": "{{vars.input.records[0]['@id']}}",
      "parentstepid": "/api/3/workflow_steps/<UUID>"
    },
    "resource": {
      "name": "Approver Approval To Implement - {{vars.input.records[0].title}}",
      "dueBy": "{{vars.input.records[0].dueDate}}",
      "assets": "{{vars.assetIRI}}",
      "status": "/api/3/picklists/<UUID>",
      "priority": "/api/3/picklists/<UUID>",
      "recordTags": [
        "/api/3/tags/AssetChangeActivity"
      ],
      "description": "Approval to proceed with the implementation.",
      "assignedOnDate": "{{arrow.utcnow().int_timestamp}}",
      "assignedToPerson": "{{vars.steps.Assignee_And_Approver_Name.input.approverApprovalToImplement}}",
      "assetChangeActivities": "{{vars.input.records[0]['@id']}}"
    },
    "collection": "tasks",
    "step_variables": []
  },
  "status": null,
  "top": "1515",
  "left": "568",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "a203fe02-2ea7-4ace-85d3-680ee2de15b1"
}
```
Example 2 — step "Assignee Approval To Implement" (workflow "Add Cyber Asset", _UseCase.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Assignee Approval To Implement",
  "description": null,
  "arguments": {
    "message": {
      "tags": [],
      "type": "/api/3/picklists/<UUID>",
      "tenant": "",
      "content": "<p>Added task <a href=\"/modules/tasks/{{vars.steps.Assignee_Approval_To_Implement.uuid}}\" target=\"_blank\" rel=\"noopener\">{{vars.steps.Assignee_Approval_To_Implement.name}}</a> to <strong>'Assignee Approval To Implement'</strong></p>",
      "records": "{{vars.input.records[0]['@id']}}",
      "parentstepid": "/api/3/workflow_steps/<UUID>"
    },
    "resource": {
      "name": "Assignee Approval To Implement - {{vars.input.records[0].title}}",
      "dueBy": "{{vars.input.records[0].dueDate}}",
      "assets": "{{vars.assetIRI}}",
      "status": "/api/3/picklists/<UUID>",
      "priority": "/api/3/picklists/<UUID>",
      "recordTags": [
        "/api/3/tags/AssetChangeActivity"
      ],
      "description": "Approval to proceed with the implementation.",
      "assignedOnDate": "{{arrow.utcnow().int_timestamp}}",
      "assignedToPerson": "{{vars.steps.Assignee_And_Approver_Name.input.assigneeApprovalToImplement}}",
      "assetChangeActivities": "{{vars.input.records[0]['@id']}}"
    },
    "collection": "tasks",
    "step_variables": []
  },
  "status": null,
  "top": "1110",
  "left": "475",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "890ce319-249e-477b-9523-1de9ca1c30f7"
}
```
Example 3 — step "Identify Security Control" (workflow "Add Cyber Asset", _UseCase.json_):
```json
{
  "@type": "WorkflowStep",
  "name": "Identify Security Control",
  "description": null,
  "arguments": {
    "message": {
      "tags": [],
      "type": "/api/3/picklists/<UUID>",
      "tenant": "",
      "content": "<p>Added task <a href=\"/modules/tasks/{{vars.steps.Identify_Security_Control.uuid}}\" rel=\"noopener\" target=\"_blank\" >{{vars.steps.Identify_Security_Control.name}}</a> to <strong>'Identify Security Control'</strong></p>",
      "records": "{{vars.input.records[0]['@id']}}"
    },
    "resource": {
      "name": "Identify Security Control - {{vars.input.records[0].title}}",
      "dueBy": "{{vars.input.records[0].dueDate}}",
      "assets": "{{vars.assetIRI}}",
      "status": "/api/3/picklists/<UUID>",
      "priority": "/api/3/picklists/<UUID>",
      "recordTags": [
        "/api/3/tags/AssetChangeActivity"
      ],
      "description": "Identify Impacted CIP 005 - CIP 007 Security Control.",
      "assignedOnDate": "{{arrow.utcnow().int_timestamp}}",
      "assignedToPerson": "{{vars.steps.Assignee_And_Approver_Name.input.identifySecurityControl}}",
      "assetChangeActivities": "{{vars.input.records[0]['@id']}}"
    },
    "collection": "tasks",
    "step_variables": []
  },
  "status": null,
  "top": "570",
  "left": "475",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "5c0f5211-e831-4154-b953-80b9ef18f195"
}
```

## 6. Routing & Conditions

### 6.1 Condition step `conditions` array — structure

Sampled 40 Condition steps.

Top-level Condition argument keys: `conditions`(40), `step_variables`(12)

Branch item keys: `step_iri`(82), `option`(72), `step_name`(68), `condition`(48), `default`(34)

Branches per Condition step: {2: 39, 4: 1}

Branches with `default` key: {False: 48, True: 34}

### 6.2 Real `condition` Jinja expressions (from `conditions[].condition`)

- `{{ vars.foundFortinetWebFilterReputation or vars.useMockOutput }}`
- `{{ vars.input_values.input1 == None }}`
- `{{ vars.foundUrlScanReputation or vars.useMockOutput }}`
- `{{ vars.request.env_setup == true }}`
- `{{ vars.steps.Get_Whois_Information.status == "Success" or vars.useMockOutput }}`
- `{{ vars.is_reputation_found }}`
- `{{ vars.is_reputation_found or vars.useMockOutput }}`
- `{{ vars.steps.IOC_Search.data.data | length > 0 }}`
- `{{ ("Success" in vars.steps.Get_IP_Reputation.data.message and vars.steps.Get_IP_Reputation.status == "Success") or vars.useMockOutput }}`
- `{{ vars.steps.Get_Email_Reputation.status == "Success" or vars.useMockOutput }}`
- `{{ ("Success" in vars.steps.Get_URL_Reputation.data.message and vars.steps.Get_URL_Reputation.status == "Success") or vars.useMockOutput }}`
- `{{ vars.steps.Get_IP_Reputation.status == "Success" or vars.useMockOutput }}`
- `{{ (vars.steps.Get_File_Reputation.data is mapping and vars.steps.Get_File_Reputation.status == "Success") or vars.useMockOutput }}`
- `{{ vars.steps.Get_QRadar_Macros.data['hydra:totalItems'] == 0 }}`
- `{{ vars.fetch_mode == 'By Updates In Last X Minutes' }}`
- `{{ vars.fetch_mode == 'By Sample Incident ID' }}`
- `{{ vars.inactive_service_list | length > 0 }}`
- `{{ (vars.steps.CPU_Utilization.data | int ) >= ( vars.cpu_threshold | int) }}`
- `{{ true }}`
- `{{ vars.steps.Virtual_Memory.data.svem.percent >= ( vars.virtual_memory_threshold | int ) }}`

(showing 20 distinct condition expressions)

### 6.3 Full Condition step example (redacted)

Workflow "URL / Domain > Fortinet Web Filter Lookup > Enrichment":
```json
{
  "@type": "WorkflowStep",
  "name": "Is Reputation Found",
  "description": null,
  "arguments": {
    "conditions": [
      {
        "option": "Yes",
        "step_iri": "/api/3/workflow_steps/<UUID>",
        "condition": "{{ vars.foundFortinetWebFilterReputation or vars.useMockOutput }}",
        "step_name": "Get Category"
      },
      {
        "option": "No",
        "default": true,
        "step_iri": "/api/3/workflow_steps/<UUID>",
        "step_name": "No Operation"
      }
    ]
  },
  "status": null,
  "top": "300",
  "left": "300",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "70b820bd-d006-4809-8571-54168c26c559"
}
```

### 6.4 Parallel branches / Join patterns

Steps whose name contains "join": 2 found in sample.
- _Sample.json_ "Read two CSV and join into single data set" "Join CSV" stepType=...92361f002671
- _UseCase.json_ "Read artefacts and ingest from CSV" "Join IP and URL CSV File and Create Dataset" stepType=...92361f002671

Out-degree distribution of routes (fan-out): {1: 2928, 2: 228, 3: 14, 4: 2}

There is **no dedicated Join stepType UUID**. Joining is achieved via a step that is the convergence target of multiple routes (fan-in), typically a Set Variable or a Condition step.

In-degree distribution of routes (fan-in / convergence): {1: 3241, 2: 68, 3: 10, 4: 4, 5: 1, 6: 1}

### 6.5 For-Each loop routing

Sampled 20 for_each steps.

`for_each` object keys: `item`(20), `condition`(20), `parallel`(18), `__bulk`(9), `batch_size`(4)

Example for_each step:
```json
{
  "@type": "WorkflowStep",
  "name": "Create Threat Intel Feed",
  "description": null,
  "arguments": {
    "for_each": {
      "item": "{{vars.input.params['report_iocs']}}",
      "__bulk": true,
      "parallel": false,
      "condition": "",
      "batch_size": 100
    },
    "resource": {
      "value": "{{vars.item.name}}",
      "__link": {
        "recordTags": "{{vars.tags}}",
        "threatIntelReports": "[\"{{vars.steps.Create_Record['@id']}}\"]"
      },
      "source": "FortiRecon ACI Report",
      "sourceId": "{{vars.report_details.report_id}}",
      "__replace": "true",
      "expiresOn": "{{ arrow.now().int_timestamp + (vars.input.params['expiry'] | int) * 24 * 60 * 60 }}",
      "confidence": "{{vars.input.params.confidence}}",
      "reputation": "{{vars.input.params.reputation | resolveRange(vars.reputation_map)}}",
      "sourceData": "{{vars.item}}",
      "typeOfFeed": "{{vars.item.type | resolveRange(vars.threat_intel_feed_type_map)}}",
      "description": "<p>{{vars.report_details.title}}</p>",
      "patternType": "STIX",
      "patternVersion": "2.1"
    },
    "_showJson": false,
    "operation": "Append",
    "collection": "/api/3/upsert/threat_intel_feeds",
    "__recommend": [],
    "fieldOperation": {
      "recordTags": "Append",
      "threatTypes": "Overwrite",
      "killChainPhases": "Overwrite"
    },
    "step_variables": []
  },
  "status": null,
  "top": "705",
  "left": "125",
  "stepType": "/api/3/workflow_step_types/<UUID>",
  "group": null,
  "uuid": "df5c23a3-c0c7-4fec-a8af-b49bea961002"
}
```

How for_each routes back: the for_each step itself has ONE outgoing route to the loop body. The loop body's final step routes back to the for_each step (forming the loop), OR routes forward to a "post-loop" step. The convergence is implicit — no special join step type. The for_each `item` var is iterated; after completion the single outgoing route continues.

## 7. Groups (WorkflowGroup)

Sampled 9 group objects.

Group keys (freq): `@type`(9), `name`(9), `description`(9), `type`(9), `isCollapsed`(9), `hasTriggerStep`(9), `hideInLogs`(9), `metadata`(9), `reusable`(9), `top`(9), `left`(9), `height`(9), `width`(9), `uuid`(9), `recordTags`(9)

`type` values: {'note': 6, 'block': 3}

Common field values:
- `color`: {None: 9}
- `isCollapsed`: {False: 9}
- `hasTriggerStep`: {False: 9}
- `hideInLogs`: {False: 8, True: 1}
- `reusable`: {False: 9}
- `top`: {'str': 9}
- `left`: {'str': 9}
- `width`: {'str': 9}
- `height`: {'str': 9}

Groups that reference another group (nested/sub-groups): 0

Example group objects (redacted):
- NOTE "Indicators Malicious" (workflow "Phishing Incident Management - Incident Response"):
```json
{
  "@type": "WorkflowGroup",
  "name": "Indicators Malicious",
  "description": "If Indicator has Malicious Reputation",
  "type": "note",
  "isCollapsed": false,
  "hasTriggerStep": false,
  "hideInLogs": false,
  "metadata": [],
  "reusable": false,
  "top": "80",
  "left": "760",
  "height": "0",
  "width": "300",
  "uuid": "5f7533d5-428d-4541-8ecc-caf3861820f1",
  "recordTags": []
}
```
- NOTE "Description" (workflow "01 - Phishing Alert-  Enrichment and Investigation"):
```json
{
  "@type": "WorkflowGroup",
  "name": "Description",
  "description": "Wrapper playbook to call the auto enrichment playbook",
  "type": "note",
  "isCollapsed": false,
  "hasTriggerStep": false,
  "hideInLogs": false,
  "metadata": [],
  "reusable": false,
  "top": "140",
  "left": "400",
  "height": "0",
  "width": "300",
  "uuid": "940b47cb-7306-4a2f-932f-a10d28409436",
  "recordTags": []
}
```
- NOTE "Check if Mail is Malicious" (workflow "Phishing Alert - Auto Enrichment"):
```json
{
  "@type": "WorkflowGroup",
  "name": "Check if Mail is Malicious",
  "description": "If the indicator contains 'Malicious' or 'Suspicious':\n  Mail is Malicious\nelse:\n  Mail is not Malicious",
  "type": "note",
  "isCollapsed": false,
  "hasTriggerStep": false,
  "hideInLogs": false,
  "metadata": [],
  "reusable": false,
  "top": "220",
  "left": "2240",
  "height": "124",
  "width": "371",
  "uuid": "fdf7b829-6bd3-4293-9ae9-6537a4d30c76",
  "recordTags": []
}
```
- BLOCK "Extracts Email Data To Alert" (workflow "Phishing Alert - Auto Enrichment"):
```json
{
  "@type": "WorkflowGroup",
  "name": "Extracts Email Data To Alert",
  "description": "",
  "type": "block",
  "isCollapsed": false,
  "hasTriggerStep": false,
  "hideInLogs": false,
  "metadata": [],
  "reusable": false,
  "top": "440",
  "left": "120",
  "height": "343",
  "width": "400",
  "uuid": "42474493-eaf1-4c3e-af1b-e93a29421810",
  "recordTags": []
}
```
- BLOCK "Update the Alert Severity & Status" (workflow "Phishing Alert - Auto Enrichment"):
```json
{
  "@type": "WorkflowGroup",
  "name": "Update the Alert Severity & Status",
  "description": "",
  "type": "block",
  "isCollapsed": false,
  "hasTriggerStep": false,
  "hideInLogs": false,
  "metadata": [],
  "reusable": false,
  "top": "780",
  "left": "2220",
  "height": "345",
  "width": "374",
  "uuid": "be5a0deb-419c-42f5-831c-dc3c22d99658",
  "recordTags": []
}
```
- BLOCK "Wait for All Indicators to be Enriched" (workflow "Phishing Alert - Auto Enrichment"):
```json
{
  "@type": "WorkflowGroup",
  "name": "Wait for All Indicators to be Enriched",
  "description": "",
  "type": "block",
  "isCollapsed": false,
  "hasTriggerStep": false,
  "hideInLogs": false,
  "metadata": [],
  "reusable": false,
  "top": "320",
  "left": "1120",
  "height": "217",
  "width": "310",
  "uuid": "2b9171f2-a424-4df8-b9e1-76f788c980cb",
  "recordTags": []
}
```

## 8. Jinja Patterns Observed in Production

Total distinct Jinja expressions harvested: 4551

### 8.1 By category

- **REST request**: 46 distinct
- **arrow date**: 33 distinct
- **filter**: 127 distinct
- **fromIRI filter**: 18 distinct
- **loop item**: 472 distinct
- **other**: 1355 distinct
- **picklist filter**: 170 distinct
- **previous step output**: 1191 distinct
- **result**: 121 distinct
- **statement block**: 534 distinct
- **trigger input**: 484 distinct

### 8.2 Top Jinja expressions (production patterns)

| Expression | Count | Category |
|---|---|---|
| `{% endif %}` | 599 | statement |
| `{{vars.input.records[0]}}` | 499 | trigger input |
| `{{vars.input.records}}` | 397 | trigger input |
| `{{vars.input.records[0]['@id']}}` | 370 | trigger input |
| `{% else %}` | 317 | statement |
| `{{vars.result}}` | 295 | other |
| `{%endif%}` | 142 | statement |
| `{% endfor %}` | 127 | statement |
| `{{vars.indicator_value}}` | 117 | other |
| `{{vars.input.records[0].title}}` | 103 | trigger input |
| `{{vars.mydomain}}` | 100 | other |
| `{{arrow.utcnow().int_timestamp}}` | 79 | other |
| `{{vars.input.records[0].tenant['@id']}}` | 77 | trigger input |
| `{{vars.item}}` | 74 | loop item |
| `{{vars.input.params['connector_config_id']}}` | 71 | trigger param |
| `{{None}}` | 65 | other |
| `{{globalVars.Demo_mode}}` | 59 | other |
| `{%else%}` | 58 | statement |
| `{{vars.assetIRI}}` | 54 | other |
| `{{vars.input.records[0].uuid}}` | 53 | trigger input |
| `{{vars.steps.Get_Correlated_Asset[0].assets \| json_query('[*]["@id"][]')}}` | 52 | step output |
| `{{vars.repo_name}}` | 50 | other |
| `{%endfor%}` | 48 | statement |
| `{{vars.input.records[0].dueDate}}` | 46 | trigger input |
| `{{ vars.input.records[0]["@id"] }}` | 43 | trigger input |
| `{{ firstname }}` | 39 | other |
| `{{ lastname }}` | 39 | other |
| `{{vars.org_name}}` | 37 | other |
| `{{vars.input.records[0].id}}` | 36 | trigger input |
| `{{vars.input.params.style_colors.Malicious}}` | 35 | trigger param |
| `{{vars.steps.Check_Source_Control_Connector_Configuration['config_id']}}` | 32 | step output |
| `{{vars.result.data}}` | 31 | other |
| `{{vars.steps.Find_Related_Task[0]['@id']}}` | 30 | step output |
| `{{vars.input.params.parameters.username}}` | 30 | trigger param |
| `{{vars.cicd_config.organizationName}}` | 29 | other |
| `{{vars.cicd_config.contentRepoName}}` | 29 | other |
| `{% set _ = config_params.update(prod_config) %}` | 28 | statement |
| `{{vars.input.records[0].sourceIp}}` | 27 | trigger input |
| `{{vars.last_pull_time}}` | 24 | other |
| `{{vars.source_ip}}` | 24 | other |
| `{{vars.item['@id']}}` | 22 | loop item |
| `{{vars.input.params['repo_name']}}` | 22 | trigger param |
| `{{globalVars.cicd_env}}` | 22 | other |
| `{{vars.input.records[0].userName}}` | 21 | trigger input |
| `{{globalVars.Current_Date}}` | 20 | other |
| `{{globalVars.Action_Icon}}` | 20 | other |
| `{{vars.input.params.style_colors.Good}}` | 19 | trigger param |
| `{{vars.input.params.style_colors['No Reputation Available']}}` | 19 | trigger param |
| `{{"No Reputation Available"}}` | 19 | other |
| `{{vars.request.record['@id']}}` | 19 | REST |

### 8.3 REST request — examples

- `{{vars.request.record['@id']}}` ×19
- `{{ vars.request.env_setup == true }}` ×8
- `{{vars.request.data.records}}` ×5
- `{{vars.request.selectedRepository}}` ×5
- `{{vars.request.env_setup}}` ×3
- `{{vars.request.record.title}}` ×3
- `{%if vars.request.env_setup %}` ×2
- `{{vars.request.data}}` ×2
- `{{vars.request.headers.tz}}` ×2
- `{{vars.request.record.commitStatus}}` ×2
- `{% if vars.request.selectedRepository == "Production Settings" %}` ×2
- `{% set alert_id = vars.request.data.records[0]['@id'] %}` ×2
- `{{vars.request.data["matricesToPull"]}}` ×1
- `{{ vars.request.data.Offense_ID }}` ×1
- `{{not(vars.request.env_setup)}}` ×1

### 8.3 arrow date — examples

- `{{arrow.get(vars.responseDueDate).int_timestamp}}` ×7
- `{{arrow.get().replace(second=0, microsecond=0) }}` ×4
- `{{arrow.get((arrow.utcnow().int_timestamp  \| int \| abs)).format('YYYYMMDDHHmm')}}` ×3
- `{{arrow.get(arrow.utcnow().shift(minutes=-vars.Pull_Sample_Events_in_Past_X_Minutes).int_timestamp).strftime('%Y-%m-%dT%H:%M:%S.%fZ')}}` ×2
- `{{arrow.get(arrow.utcnow().int_timestamp).strftime('%Y-%m-%dT%H:%M:%S.%fZ')}}` ×2
- `{{arrow.get(arrow.utcnow().shift(days=+vars.dueDays)).int_timestamp}}` ×2
- `{{arrow.get(vars.data['incident_data']["incidentLastSeen"]).to("UTC").format("YYYY-MM-DD HH:mm:ss ZZ")}}` ×2
- `{{arrow.get(vars.advisoryList \| json_query('[*]["release_date"][]') \| unique \| max).int_timestamp}}` ×2
- `{{arrow.get(vars.since).to("UTC").format("YYYY-MM-DDTHH:mm:ssZ")}}` ×1
- `{{ arrow.get(vars.report_details.published_ts).int_timestamp }}` ×1
- `{{ arrow.get(vars.report_details.information_date, 'YYYY-MM-DD').int_timestamp }}` ×1
- `{{ ( arrow.get(vars.curr_timestamp).shift(minutes=-vars.time_diff_min).int_timestamp) * 1000}}` ×1
- `{{arrow.get( arrow.utcnow().int_timestamp).strftime('%Y-%m-%dT%H:%M:%S.%fZ')}}` ×1
- `{{arrow.get( arrow.utcnow().timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')}}` ×1
- `{{arrow.get(arrow.utcnow().shift(minutes=-vars.last_x_minute).timestamp).strftime('%Y-%m-%dT%H:%M:%SZ')}}` ×1

### 8.3 filter — examples

- `{{vars.alerts \| length > 0 and vars.create_announcement is true}}` ×4
- `{{vars.advisoryList \| length > 0}}` ×4
- `{{ vars.cicd_config \| length == 0 }}` ×3
- `{% if vars.cat_summary \| length > 0 %}` ×2
- `{{ vars.msgAttachments \| length == 0 and vars.emlAttachments \| length == 0 }}` ×2
- `{% if (vars.categories \| length > 0) %}` ×2
- `{% if vars.SPF_Record \| length == 0 -%}` ×2
- `{% if vars.Not_Permitted_IPs_for_SPF_Fail \| length != 0 -%}` ×2
- `{% elif vars.Not_Permitted_IPs_for_SPF_SoftFail \| length != 0 -%}` ×2
- `{% if vars.foundList \| length != 0 %}` ×2
- `{{vars.cicd_config.env_config \| length == 1 and vars.cicd_config.env_config[0].itemValue == "Production"}}` ×2
- `{{ vars.demoRecordIRIs != None and vars.demoRecordIRIs \| length > 0 and vars.demoRecordIRIs \| type_debug == 'list' }}` ×2
- `{{vars.relatedRecordsIRIs \| length > 0}}` ×2
- `{{ (vars.demoRecordIRIs \| length > 0) and (vars.demoRecordIRIs \| type_debug == 'list') }}` ×2
- `{{ vars.email_recipient \| length > 0 }}` ×2

### 8.3 fromIRI filter — examples

- `{{vars.currentUser \| fromIRI}}` ×2
- `{{(vars.assetIRI \| fromIRI).criticality.itemValue or None}}` ×1
- `{{(vars.currentUser \| fromIRI).firstname}}` ×1
- `{{(vars.currentUser \| fromIRI).lastname}}` ×1
- `{{("/api/3/people/3451141c-bac6-467c-8d72-85e0fab569ce" \| fromIRI).sourceControlUsername }}` ×1
- `{{ (vars.alert_data['@id']+'?$relationships=true') \| fromIRI }}` ×1
- `{{(vars.indicator_data["@id"] \| fromIRI).description}}` ×1
- `{% set kEVCveData = cve.isInKEVCatalog \| fromIRI %}` ×1
- `{{(item.kevAlertIRI \| fromIRI)['uuid']}}` ×1
- `{{(item.kevAlertIRI \| fromIRI).title}}` ×1
- `{{arrow.get((item.kevAlertIRI \| fromIRI)['createDate']).format("YYYY-MM-DD HH:mm:ss")}}` ×1
- `{{arrow.get((item.kevAlertIRI \| fromIRI)['responseDueDate']).format("YYYY-MM-DD HH-mm-ss")}}` ×1
- `{{(data \| fromIRI).name}}` ×1
- `{% set _ = data.append((asset['@id'] + "?$relationships=true") \| fromIRI) %}` ×1
- `{% set criticality = (item.criticality \| fromIRI) %}` ×1

### 8.3 loop item — examples

- `{{vars.item}}` ×74
- `{{vars.item['@id']}}` ×22
- `{{vars.item.value}}` ×13
- `{{vars.item \| toJSON}}` ×11
- `{{vars.item["@id"]}}` ×9
- `{{ vars.item.headers['message-id'] \| join }}` ×8
- `{{vars.item["headers"]["to"]}}` ×7
- `{{vars.item["headers"]["from"]}}` ×7
- `{% if vars.item.attachments \| json_query("[*].metadata.md5") \| join(',') %}` ×7
- `{{vars.item.attachments \| json_query("[*].metadata.md5") \| join(', ')}}` ×7
- `{% if vars.item.headers.from %}` ×7
- `{{vars.item["body"]["text"]}}` ×6
- `{{vars.item["headers"]["subject"]}}` ×6
- `{{vars.item.headers.subject}}` ×6
- `{{vars.item['id']}}` ×6

### 8.3 other — examples

- `{{vars.indicator_value}}` ×117
- `{{vars.mydomain}}` ×100
- `{{arrow.utcnow().int_timestamp}}` ×79
- `{{None}}` ×65
- `{{globalVars.Demo_mode}}` ×59
- `{{vars.assetIRI}}` ×54
- `{{vars.repo_name}}` ×50
- `{{ firstname }}` ×39
- `{{ lastname }}` ×39
- `{{vars.org_name}}` ×37
- `{{vars.cicd_config.organizationName}}` ×29
- `{{vars.cicd_config.contentRepoName}}` ×29
- `{{vars.last_pull_time}}` ×24
- `{{vars.source_ip}}` ×24
- `{{globalVars.cicd_env}}` ×22

### 8.3 picklist filter — examples

- `{{'Severity'\| picklist('Medium') }}` ×11
- `{{'Severity'\| picklist('High') }}` ×11
- `{{'Severity'\| picklist('Low') }}` ×10
- `{{'Severity'\| picklist('Critical') }}` ×9
- `{{'Severity'\| picklist('Minimal') }}` ×8
- `{{"AlertStatus"\| picklist("Open")}}` ×6
- `{{"Severity" \| picklist((["Minimal","Low","Medium","High","Critical"]\|random), "@id")}}` ×4
- `{{'IndicatorReputation' \| picklist('Good', 'uuid')}}` ×3
- `{{'IndicatorReputation' \| picklist('Suspicious', 'uuid')}}` ×3
- `{{'IndicatorReputation' \| picklist('Malicious', 'uuid')}}` ×3
- `{{'IndicatorReputation' \| picklist('No Reputation Available', 'uuid')}}` ×3
- `{{'IndicatorReputation' \| picklist('TBD', 'uuid')}}` ×3
- `{{'AlertStatus'\| picklist('Open') }}` ×3
- `{{'AlertStatus'\| picklist('Closed') }}` ×3
- `{{"AlertStatus"\| picklist("Closed")}}` ×3

### 8.3 previous step output — examples

- `{{vars.steps.Get_Correlated_Asset[0].assets \| json_query('[*]["@id"][]')}}` ×52
- `{{vars.steps.Check_Source_Control_Connector_Configuration['config_id']}}` ×32
- `{{vars.steps.Find_Related_Task[0]['@id']}}` ×30
- `{{vars.steps.Get_Details_of_Submitted_File.data.result.data.score}}` ×15
- `{{vars.steps.Get_Repositories_Detail.input.orgName}}` ×15
- `{% for item in vars.steps.Find_Source_Control_Settings %}` ×14
- `{{vars.steps.Get_Details_of_Submitted_File.data.result.data.rating}}` ×12
- `{{vars.steps.Get_Repositories_Detail.input.contentRepositoryName}}` ×12
- `{{vars.steps.Get_Repositories_Detail.input.productionSettingsRepositoryName}}` ×11
- `{{vars.steps.Get_Repositories_Detail.input.developmentSettingsRepositoryName}}` ×11
- `{{vars.steps.Create_KEV_Alerts['@id']}}` ×11
- `{{vars.steps.Get_KEV_Alerts[0].kEVAlerts[0]['@id']}}` ×10
- `{% elif vars.steps.Get_Details_of_Submitted_File.data.result.data.score in vars.suspicious_score %}` ×9
- `{% elif vars.steps.Get_Details_of_Submitted_File.data.result.data.score == vars.good_score %}` ×9
- `{{vars.steps.Clone_Repository.data.path}}` ×7

### 8.3 result — examples

- `{{vars.result}}` ×295
- `{{vars.result.data}}` ×31
- `{{vars.result \| length > 0}}` ×14
- `{{vars.recordIRI.append(vars.result['@id'])}}` ×12
- `{{vars.result['@id']}}` ×8
- `{{vars.result.data.resources}}` ×7
- `{{ vars.result.data }}` ×5
- `{{vars.result.data.attributes['total_votes']}}` ×5
- `{{vars.result.data.attributes['last_analysis_stats']}}` ×5
- `{{vars.result.data.entries}}` ×4
- `{{vars.alertList.append(vars.result['@id'])}}` ×4
- `{{vars.taskIRI.append(vars.result['@id'])}}` ×4
- `{{vars.result['sourceAsset']}}` ×4
- `{{vars.result['destinationAsset']}}` ×4
- `{{ vars.result }}` ×3

### 8.3 statement block — examples

- `{% endif %}` ×599
- `{% else %}` ×317
- `{%endif%}` ×142
- `{% endfor %}` ×127
- `{%else%}` ×58
- `{%endfor%}` ×48
- `{% set _ = config_params.update(prod_config) %}` ×28
- `{% set config_params = {} %}` ×14
- `{% set prod_config = {} %}` ×14
- `{% set dev_config = {} %}` ×14
- `{% if item.configurationParameters is not none %}` ×14
- `{% if item.environment.itemValue == 'Production' %}` ×14
- `{% set _ = prod_config.update(item.configurationParameters) %}` ×14
- `{% elif item.environment.itemValue == 'Development' %}` ×14
- `{% set _ = dev_config.update(item.configurationParameters) %}` ×14

### 8.3 trigger input — examples

- `{{vars.input.records[0]}}` ×499
- `{{vars.input.records}}` ×397
- `{{vars.input.records[0]['@id']}}` ×370
- `{{vars.input.records[0].title}}` ×103
- `{{vars.input.records[0].tenant['@id']}}` ×77
- `{{vars.input.params['connector_config_id']}}` ×71
- `{{vars.input.records[0].uuid}}` ×53
- `{{vars.input.records[0].dueDate}}` ×46
- `{{ vars.input.records[0]["@id"] }}` ×43
- `{{vars.input.records[0].id}}` ×36
- `{{vars.input.params.style_colors.Malicious}}` ×35
- `{{vars.input.params.parameters.username}}` ×30
- `{{vars.input.records[0].sourceIp}}` ×27
- `{{vars.input.params['repo_name']}}` ×22
- `{{vars.input.records[0].userName}}` ×21

## 9. Macros

### 9.1 Sample.json — 2 macros

Macro object keys: `name`(2), `value`(2), `default_value`(2)

Examples (redacted, base64 truncated):
```json
{
  "name": "Demo_mode",
  "value": "true",
  "default_value": "true"
}
```
```json
{
  "name": "Default_Email",
  "value": "noreply@example.com",
  "default_value": null
}
```

### 9.1 UseCase.json — 12 macros

Macro object keys: `name`(12), `value`(12), `default_value`(12)

Examples (redacted, base64 truncated):
```json
{
  "name": "Demo_mode",
  "value": "true",
  "default_value": "true"
}
```
```json
{
  "name": "Current_Date",
  "value": "{{arrow.utcnow().timestamp}}",
  "default_value": "{{arrow.utcnow().timestamp}}"
}
```
```json
{
  "name": "Action_Icon",
  "value": "<span style=\"background-color:red;color:black;border-radius: 4px;font-size:8mm;\">&#10159;<font style=\"font-size:18px;font-weight: bold;font-family: 'Georgia', monospace;\">Action</font></span>",
  "default_value": "<span style=\"background-color:red;color:black;border-radius: 4px;font-size:8mm;\">&#10159;<font style=\"font-size:18px;font-weight: bold;font-family: 'Georgia', monospace;\">Action</font></span>"
}
```
```json
{
  "name": "Hint_Icon",
  "value": "<span style=\"background-color:orange;color:black;border-radius: 4px;font-size:8mm;\">&#9788;<font style=\"font-size:18px;font-weight: bold;font-family: 'Georgia', monospace;\">Hint</font></span>",
  "default_value": "<span style=\"background-color:orange;color:black;border-radius: 4px;font-size:8mm;\">&#9788;<font style=\"font-size:18px;font-weight: bold;font-family: 'Georgia', monospace;\">Hint</font></span>"
}
```

**Purpose**: The `macros` array carries reusable shared step templates / prebuilt snippets (e.g. packaged connector-call templates or sub-playbook snippets) that can be inserted into multiple workflows. They are **collection-level metadata** referenced by UUID. The skill should mention that exports include a top-level `macros` array and that newly generated playbooks can set `"macros": []` (empty) — there is no need to author macros for a self-contained generated playbook.

## 10. Exported Tags / recordTags

### 10.1 Sample.json — 166 exported_tags

exported_tags item keys: 

First 5 examples (redacted):
```json
"Whois"
```
```json
"whois-freaks"
```
```json
"openai"
```
```json
"Openai"
```
```json
"OpenAI"
```

### 10.1 UseCase.json — 109 exported_tags

exported_tags item keys: 

First 5 examples (redacted):
```json
"IT OT"
```
```json
"Add Cyber Asset"
```
```json
"Asset Change Activity"
```
```json
"ManualTrigger"
```
```json
"Replace Cyber Asset"
```

### 10.2 Workflow `recordTags` (sample)

Workflow recordTags (top 30): `Fortinet`(486), `CICD`(85), `fortinet-fortimanager`(69), `GitHub`(67), `dataingestion`(58), `CrowdStrike`(57), `crowd-strike-falcon`(57), `Microsoft`(56), `ManualTrigger`(54), `IT OT`(50), `openai`(47), `OpenAI`(47), `fortinet-fortisiem`(46), `Gitlab`(44), `fortinet-fortianalyzer`(42), `fortinet-fortigate`(42), `gitlab`(42), `fortinet-fortirecon-easm`(41), `fortinet-fortirecon-aci`(41), `fortinet-fortiguard-threat-intelligence`(39), `Subroutine`(38), `microsoft-teams`(36), `fortinet-fortiedr`(36), `Aws`(34), `aws-commands`(34), `Referenced`(34), `AWS`(32), `AWS EC2`(32), `fortinet-fortindr-cloud`(30), `qradar`(27)

**Purpose**: `exported_tags` is the set of tag definitions (name + UUID + color) bundled with the export so the importer can recreate the tag picklist. `recordTags` on a Workflow/Collection is the list of tag strings applied to that record. When generating, set `recordTags: []` unless the user requests specific tags; the `exported_tags` top-level array can be `[]`.


## 11. Parameters & inputVariables

### 11.1 Workflow-level `parameters` array

Workflows with non-empty parameters: 169/1367

Top parameter names: `connector_config_id`(58), `indicator_value`(17), `style_colors`(16), `parameters`(8), `parent_object_IRI`(6), `device_ip_address`(5), `get_commit_params`(4), `fileIndicatorType`(4), `username`(4), `repo_name`(4), `confidence`(3), `eventlimit`(3), `overrideIfNoMatch`(3), `limit`(3), `alert_data`(3), `indicator_IRI`(3), `email`(3), `alertRecordIRI`(3), `assetIRI`(3), `automated`(3), `alert_iri`(3), `indicatorIRI`(3), `indicatorValue`(3), `create_repo_params`(2), `update_remote_repo_params`(2), `add_pr_review_params`(2), `push_changes_params`(2), `list_pr_params`(2), `get_repo_params`(2), `clone_repo_params`(2), `create_update_file_content_params`(2), `get_pr_params`(2), `update_issue_params`(2), `issue_contents`(2), `create_issue_params`(2), `issue_title`(2), `issue_content`(2), `list_repo_collaborator_params`(2), `fetch_release_params`(2), `add_issue_comment_params`(2)

Example parameters arrays:
- _Sample.json_ "GitHub - Create Repository": ["connector_config_id", "create_repo_params"]
- _Sample.json_ "GitHub - Get Server URL": ["connector_config_id"]
- _Sample.json_ "GitHub - Update Remote Repository": ["connector_config_id", "update_remote_repo_params"]
- _Sample.json_ "GitHub - Add Pull Request Review": ["connector_config_id", "add_pr_review_params"]
- _Sample.json_ "GitHub - Push Changes": ["connector_config_id", "push_changes_params"]
- _Sample.json_ "GitHub - List Pull Request": ["connector_config_id", "list_pr_params"]
- _Sample.json_ "GitHub - Get Commit": ["connector_config_id", "get_commit_params"]
- _Sample.json_ "GitHub - Get Repository": ["get_repo_params", "connector_config_id"]

### 11.2 Referenced-playbook `parameters` (the input contract)

Referenced-trigger workflows with parameters: found 155 (sampled).
- _Sample.json_ "GitHub - Create Repository": ["connector_config_id", "create_repo_params"]
- _Sample.json_ "GitHub - Get Server URL": ["connector_config_id"]
- _Sample.json_ "GitHub - Update Remote Repository": ["connector_config_id", "update_remote_repo_params"]
- _Sample.json_ "GitHub - Add Pull Request Review": ["connector_config_id", "add_pr_review_params"]
- _Sample.json_ "GitHub - Push Changes": ["connector_config_id", "push_changes_params"]

### 11.3 Manual-button `inputVariables` — full object shape

inputVariable item keys: `name`(9), `type`(9), `label`(9), `tooltip`(9), `dataType`(9), `formType`(9), `required`(9), `_expanded`(9), `useRecordFieldDefault`(9), `defaultValue`(8), `_previousName`(6), `title`(5), `usable`(5), `collection`(5), `searchable`(5), `templateUrl`(5), `lengthConstraint`(5), `allowedGridColumn`(5), `mmdUpdate`(4), `allowedEncryption`(4), `dataSource`(3), `visibilityQuery`(3), `jinjaExpressionView`(3), `_addVisibilityConditions`(3), `displayTemplate`(2), `bulkAction`(1), `inversedField`(1), `ownsRelationship`(1), `options`(1), `playbookField`(1), `moduleField`(1)

`type` values: {'picklists': 1, 'array': 1, 'string': 5, 'scenario': 1, 'boolean': 1}

`dataType` values: {'multiselectpicklist': 1, 'dynamicList': 1, 'text': 4, 'lookup': 1, 'file': 1, 'checkbox': 1}

`formType` values: {'multiselectpicklist': 1, 'dynamicList': 1, 'text': 4, 'lookup': 1, 'file': 1, 'checkbox': 1}

Full inputVariable examples (redacted):
- _Sample.json_ "MITRE ATT&CK > Fetch Latest Data" step "Start":
```json
[
  {
    "name": "matricesToPull",
    "type": "picklists",
    "label": "Matrices To Pull",
    "title": "Multiselect Picklist",
    "usable": true,
    "tooltip": "",
    "dataType": "multiselectpicklist",
    "formType": "multiselectpicklist",
    "required": false,
    "_expanded": true,
    "mmdUpdate": true,
    "bulkAction": [],
    "collection": true,
    "dataSource": {
      "model": "picklists",
      "query": {
        "sort": [
          {
            "field": "orderIndex",
            "direction": "ASC"
          }
        ],
        "logic": "AND",
        "filters": [
          {
            "field": "listName__name",
            "value": "Mitre ATT&CK Matrics",
            "operator": "eq"
          }
        ]
      },
      "displayConditions": {
        "1eca922e-85ff-46a7-af26-cafa7c334883": {
          "conditions": null,
          "visibility": "visible"
        },
        "6bf383dc-f042-4bf5-8ba6-0dedcdf0aa87": {
          "conditions": null,
          "visibility": "visible"
        },
        "e617e1bd-070b-4218-8e31-9e54e3f64c81": {
          "conditions": null,
          "visibility": "visible"
        }
      }
    },
    "searchable": false,
    "templateUrl": "app/components/form/fields/typeahead.multiselect.html",
    "defaultValue": [
      {
        "id": 287,
        "@id": "/api/3/picklists/<UUID>",
        "icon": null,
        "uuid": "1eca922e-85ff-46a7-af26-cafa7c334883",
        "@type": "Picklist",
        "color": null,
        "dis
```
- _Sample.json_ "Get User's all Chat Messages" step "Start":
```json
[
  {
    "name": "getMessageBy",
    "type": "array",
    "label": "Get Message by",
    "title": "Dynamic List",
    "usable": true,
    "options": [
      "User Principal Name",
      "User ID"
    ],
    "tooltip": "",
    "dataType": "dynamicList",
    "formType": "dynamicList",
    "required": true,
    "_expanded": true,
    "mmdUpdate": true,
    "collection": false,
    "searchable": false,
    "templateUrl": "app/components/form/fields/dynamicList.html",
    "defaultValue": "User ID",
    "_previousName": "getMessageBy",
    "playbookField": true,
    "visibilityQuery": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": []
    },
    "lengthConstraint": true,
    "allowedGridColumn": false,
    "jinjaExpressionView": true,
    "useRecordFieldDefault": false,
    "_addVisibilityConditions": true
  },
  {
    "name": "userID",
    "type": "string",
    "label": "User ID",
    "tooltip": "Specify the ID of the User for which you want to retrieve all chat messages",
    "dataType": "text",
    "formType": "text",
    "required": true,
    "_expanded": true,
    "defaultValue": null,
    "_previousName": "",
    "visibilityQuery": {
      "sort": [],
      "limit": 30,
      "logic": "AND",
      "filters": [
        {
          "type": "array",
          "field": "getMessageBy",
          "value": [
            "User ID"
          ],
          "module": "getMessageBy",
          "display": "",
          "operator": "in",
          "template": 
```
- _UseCase.json_ "Email (Manual Attach) - File to Alert (Suspicious Email)" step "Start":
```json
[
  {
    "name": "emailFile",
    "type": "string",
    "label": "Email File",
    "tooltip": "Upload email file, either *.eml or *.msg extension",
    "dataType": "text",
    "formType": "text",
    "required": true,
    "_expanded": true,
    "moduleField": "fileEmail",
    "_previousName": "",
    "useRecordFieldDefault": true
  }
]
```
- _UseCase.json_ "Run Selected Scenario" step "Start":
```json
[
  {
    "name": "scenario",
    "type": "scenario",
    "label": "Scenario",
    "title": "Lookup (One to Many or One to One)",
    "usable": true,
    "tooltip": "",
    "dataType": "lookup",
    "formType": "lookup",
    "required": true,
    "_expanded": true,
    "mmdUpdate": true,
    "collection": false,
    "dataSource": {
      "model": "scenario"
    },
    "searchable": false,
    "templateUrl": "app/components/form/fields/typeahead.html",
    "defaultValue": null,
    "displayTemplate": "%7B%7B%20title%20%7D%7D",
    "lengthConstraint": false,
    "allowedEncryption": false,
    "allowedGridColumn": true,
    "useRecordFieldDefault": false
  }
]
```
- _UseCase.json_ "Import Scenario" step "Start":
```json
[
  {
    "name": "jSONFile",
    "type": "string",
    "label": "JSON File",
    "title": "File Field",
    "usable": true,
    "tooltip": "Exported JSON file from Export playbook",
    "dataType": "file",
    "formType": "file",
    "required": false,
    "_expanded": true,
    "mmdUpdate": true,
    "collection": false,
    "dataSource": {
      "model": "files"
    },
    "searchable": false,
    "templateUrl": "app/components/form/fields/file.html",
    "defaultValue": null,
    "_previousName": "",
    "lengthConstraint": true,
    "allowedEncryption": false,
    "allowedGridColumn": true,
    "useRecordFieldDefault": false
  },
  {
    "name": "importRelationships",
    "type": "boolean",
    "label": "Import Relationships",
    "title": "Checkbox",
    "usable": true,
    "tooltip": "If checked, will only update the existing records with the relationships",
    "dataType": "checkbox",
    "formType": "checkbox",
    "required": false,
    "_expanded": false,
    "collection": false,
    "searchable": true,
    "templateUrl": "app/components/form/fields/checkbox.html",
    "defaultValue": null,
    "lengthConstraint": false,
    "allowedEncryption": false,
    "allowedGridColumn": true,
    "useRecordFieldDefault": false
  }
]
```


## 12. Misc / Non-obvious Findings

### 12.1 Collection `image` (base64 icon)

Collections with non-null image: 41
- _Sample.json_ "Sample - WhoisFreaks - 1.0.0": image starts with `data:png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAIAAAABc2X6...` (base64-encoded PNG/JPEG icon)
- _Sample.json_ "Sample - Fortinet Web Filter Lookup - 2.0.0": image starts with `data:png;base64,iVBORw0KGgoAAAANSUhEUgAAAFAAAABQCAIAAAABc2X6...` (base64-encoded PNG/JPEG icon)

**Finding**: Collections carry a base64-encoded icon in `image`. When generating, you can set `"image": null` (no icon) or embed a base64 PNG. The skill currently shows `"image": null` which is fine, but should note that real collections frequently have icons.

### 12.2 `versions` array content

Example first `versions` entry (redacted):
**Finding**: `versions` holds snapshot history (each entry is a full prior-state WorkflowVersion with its own `steps`/`routes`). For generation, `"versions": []` is correct and safe — the server creates the first version on import. Never replay version snapshots.

### 12.3 `aliasName` and `tag`

Non-null aliasName: 0/1367
Top aliasName values: {}

Non-null tag: 925/1367
Top tag values: {'#Fortinet FortiManager': 66, '#CrowdStrike Falcon': 55, '#OpenAI': 47, '#Fortinet FortiSIEM': 43, '#GitLab': 42, '#GitHub': 41, '#Fortinet FortiRecon EASM': 41, '#Fortinet FortiAnalyzer': 39, '#Fortinet FortiRecon ACI': 35, '#Microsoft-Teams': 33, '#AWS Commands': 33, '#Fortinet FortiGate': 33, '#AWS EC2': 32, '#Fortinet FortiEDR': 28, '#Fortinet FortiRecon Brand Protection': 23}

**Finding**: `tag` is a category hashtag like `"#Subroutine"`, `"#Connector"`, `"#Triage"`, `"#Investigation"` — used to group playbooks in the UI. `aliasName` is rarely used (mostly null).

### 12.4 `singleRecordExecution` / `synchronous` / `remoteExecutableFlag` patterns

- singleRecordExecution: True=0, False=1367
- synchronous: True=0, False=1367
- remoteExecutableFlag: True=0, False=1367

remoteExecutableFlag=True workflows: often the Referenced-trigger (sub-playbook) kind. Used so MSSP/parent can invoke remotely.

### 12.5 `debug` / `isActive` defaults

- debug: True=11, False=1356
- isActive: True=277, False=1090

### 12.6 `do_until` (retry/poll loop) on Reference-a-Playbook steps

Found 5 Reference-a-Playbook steps with `do_until`.
```json
{
  "delay": 5,
  "retries": 5,
  "condition": "{{vars.steps.Validate_Slack_Input_Form.validation == 1}}"
}
```

### 12.7 `mock_result` / `useMockOutput`

Steps with mock_result/useMockOutput: 207

### 12.8 Collection object fields

Collection keys: `@type`(96), `name`(96), `description`(96), `visible`(96), `image`(96), `uuid`(96), `id`(96), `deletedAt`(96), `importedBy`(96), `recordTags`(96), `workflows`(96)

### 12.9 `when` / `ignore_errors` / `for_each` prevalence per step type

| stepType | when | ignore_errors | for_each |
|---|---|---|---|
| `0109f35d-090b-4a2b-bd8a-94cbc3508562` | 32 | 8 | 16 |
| `0bfed618-0316-11e7-93ae-92361f002671` | 21 | 36 | 12 |
| `2597053c-e718-44b4-8394-4d40fe26d357` | 35 | 1 | 47 |
| `4c0019b2-055c-44d0-968c-678a0c2d762e` | 0 | 5 | 0 |
| `74932bdc-b8b6-4d24-88c4-1a4dfbc524f3` | 22 | 4 | 58 |
| `7b221880-716b-4726-a2ca-5e568d330b3e` | 1 | 0 | 9 |
| `b593663d-7d13-40ce-a3a3-96dece928722` | 26 | 1 | 30 |
| `b593663d-7d13-40ce-a3a3-96dece928770` | 1 | 0 | 1 |

### 12.10 `operationTitle` naming conventions

- `activedirectory` title prefixes: {'Get Specific Object Details': 8, 'Global Search': 4, 'Disable User Account': 3, 'Get All Objects Details': 2, 'Advanced Search': 2, 'Reset Password': 2, 'Disable User Account ': 1, 'Add Group Members': 1}
- `alienvault-otx` title prefixes: {'Get File Reputation': 1}
- `aws` title prefixes: {'Detach Volume To Instance': 1, 'Detach Instance From Auto Scaling Group': 1, 'Attach Instance To Auto Scaling Group': 1, 'Reboot Instance': 1, 'Stop Instance': 1, 'Revoke Ingress': 1, 'Deregister Instance from ELB': 1, 'Get Details for All Images': 1}
- `aws-commands` title prefixes: {'Authorize Ingress': 1, 'Attach Volume': 1, 'Detach Volume': 1, 'Launch Instance': 1, 'Get Instance Details': 1, 'Delete Volume': 1, 'Get AMIs Detail': 1, 'Get User Details': 1}
- `axios-assyst` title prefixes: {'Close Ticket': 1, 'Update Ticket': 1, 'Get Ticket Details': 1, 'Search Tickets': 1, 'Create Ticket': 1}
- `axonius` title prefixes: {'Get User Assets': 1, 'Get Device Assets': 1}
- `carbonblack-response` title prefixes: {'Get All Processes': 1, 'Terminate Process': 1}
- `cicd-utils` title prefixes: {'Import FortiSOAR Template': 2, 'Review & Import FortiSOAR Template': 1, 'Export FortiSOAR Template': 1}
- `cisa-advisory` title prefixes: {'Get Advisory': 5, 'Get Known Exploited Vulnerability CVEs': 1, 'Get Advisory By Product': 1, 'Get Advisory By Year': 1, 'Get Advisory By Vendor': 1}
- `cisco-catalyst` title prefixes: {'Get Version': 1, 'Configure VLAN': 1, 'Get Configuration': 1}
- `code-snippet` title prefixes: {'Execute Python Code': 4}
- `crowd-strike-falcon` title prefixes: {'Spotlight': 3, 'Alert Search': 3, 'Get Detection Details': 3, 'Detection Search': 3, 'Get Alert Details': 3, 'Get Process Details': 1, 'Get Quarantine Files Count': 1, 'Hunt File': 1}
- `csv-data-management` title prefixes: {'Extract Data from Single CSV': 10, 'Merge and Extract Data from two CSV': 2, 'Join and Extract Data from two CSV': 2, 'Concat and Extract Data from two CSV': 1, 'Convert JSON to CSV File': 1}
- `cyops-schedule-report` title prefixes: {'Generate Report From Report ID': 2}
- `cyops-system-monitoring` title prefixes: {'CPU Utilization': 1, 'Disk Utilization': 1, 'Service Status': 1, 'Virtual Memory Utilization': 1}
- `cyops_utilities` title prefixes: {'Utils': 118, 'FSR': 84, 'CyOPs': 23, 'File': 16, 'Email': 3}
- `darktrace` title prefixes: {'Execute an API Request': 1, 'Get Incidents': 1, 'Get Enums': 1, 'Search Query': 1, 'Get Models': 1, 'Get Entity Details': 1, 'Get Components': 1, 'Get Breach Details': 1}
- `dns` title prefixes: {'Lookup IP': 1, 'Lookup FQDN/Domain': 1}
- `exchange` title prefixes: {'Send Email': 7, 'Delete Email': 1, 'Search Email': 1}
- `exploit-prediction-scoring-system` title prefixes: {'Get EPSS Score By CVE ID': 2, 'Get EPSS Score': 1}
- `file-content-extraction` title prefixes: {'Extract Text': 4, 'Get Backend Config': 1, 'Create XSLX file as attachment from JSON Data': 1, 'Extract Artifacts Extended': 1}
- `fortigate-firewall` title prefixes: {'Block IP Address': 7, 'Quarantine Host': 2, 'Update Policy': 2, 'Block URL': 2, 'Get System Events': 1, 'Unquarantine Host': 1, 'Delete Policy': 1, 'Get Address Groups': 1}
- `fortinet-fortiai` title prefixes: {'Submit File': 1, 'Get File Verdict Result': 1, 'Get Events': 1}
- `fortinet-fortiai-proxy` title prefixes: {'Create Response': 1, 'Make a chat_completion API call': 1, 'Get Token Balance Information': 1}
- `fortinet-fortianalyzer` title prefixes: {'Get Event for Multiple ADOMs': 3, 'Get Reports': 2, 'Get Device Information': 2, 'Count Events for Multiple ADOMs': 2, 'List Schedules': 2, 'Start and fetch bulk device logs': 1, 'Get Events For Incident': 1, 'Get Log-File Content': 1}
- `fortinet-fortiauthenticator` title prefixes: {'Get LDAP User List': 2, 'Get Schema': 2, 'Get Specific LDAP User': 2, 'Update LDAP User Status': 2, 'Get Local Users': 1, 'Update Radius User Status': 1, 'Get Specific Radius User': 1, 'Create Local User': 1}
- `fortinet-forticlient-ems` title prefixes: {'Delete Custom Tag': 1, 'Get Zero Trust Rule Sets List': 1, 'Get Zero Trust Tag By ID': 1, 'Remove Custom Tag From Endpoint': 1, 'Get All Endpoints': 1, 'Create Custom Tag': 1, 'Add Custom Tag to Endpoint': 1, 'Delete Zero Trust Tag': 1}
- `fortinet-forticnapp` title prefixes: {'Search Alerts': 3, 'Add Comment to Alert': 1, 'Close Alert': 1, 'Execute an API Call': 1, 'Get Alerts Details': 1, 'Get Alert Entities': 1, 'Search Configuration': 1, 'Search Container Vulnerabilities': 1}
- `fortinet-fortideceptor` title prefixes: {'Stop Decoy': 1, 'Start Decoy': 1, 'Get Attack Events': 1, 'Deploy Decoy': 1, 'Delete Decoy': 1, 'Get Templates': 1, 'Get Deployment Networks': 1, 'Get Attack Incidents': 1}
- `fortinet-fortidlp` title prefixes: {'Get Incidents List': 4, 'Get Users List': 1, 'Add Labels to Agents': 1, 'Get Label Details': 1, 'Update Incidents': 1, 'Get User Details': 1, 'Get Pending In-Flight Actions List': 1, 'Agent Action Request': 1}
- `fortinet-fortiedr` title prefixes: {'Get Events': 2, 'Isolate Collector': 2, 'Update IPSet': 1, 'Remediate Device': 1, 'Update Collector Installer': 1, 'Get Event Count': 1, 'Get Agent Groups': 1, 'Get System Summary': 1}
- `fortinet-fortiguard-ioc` title prefixes: {'Get Selected IOC Fields': 1, 'Get Visiting Countries': 1, 'Get Risk Distribution': 1, 'Execute an API Request': 1}
- `fortinet-fortiguard-outbreak` title prefixes: {'Get Outbreak Alert Threat Actor Details by ID': 1, 'Get Outbreak Alert Details by Slug Name': 1, 'List Threat Actors': 1, 'List Outbreak Alert Details': 1, 'Bulk Ingest Outbreak Alert IOCs': 1, 'Get Outbreak Alert IOCs': 1, 'Get Outbreak Threat Heat Map Details': 1, 'Get Outbreak Threat Live Map Details': 1}
- `fortinet-fortiguard-threat-intelligence` title prefixes: {'Threat Intel Search': 2, 'Get Threat Activity Statistics By Country': 2, 'Fetch Threat Intel Feeds': 2, 'Get Threat Activity Statistics': 2, 'Get Threat Activity Statistics By Industry': 2, 'Get Threat Activity Statistics By Country and Industry': 2, 'IOC Search': 2, 'Get Industry List': 1}
- `fortinet-fortimail` title prefixes: {'Block Sender Address': 1}
- `fortinet-fortimanager` title prefixes: {'List Incident': 3, 'Get Events Related to Incident': 2, 'Update Policy Package': 1, 'Create LDAP Server': 1, 'Update Custom Service': 1, 'Delete Address Group': 1, 'Delete Policy Package': 1, 'Get Service Categories List': 1}
- `fortinet-fortimanager-json-rpc` title prefixes: {'JSON RPC Get': 1, 'JSON RPC Set': 1, 'JSON RPC Add': 1, 'JSON RPC Freeform': 1, 'JSON RPC Delete': 1, 'JSON RPC Exec': 1}
- `fortinet-fortindr-cloud` title prefixes: {'Get Detections List': 2, 'Get Detection Rules List': 2, 'Get Detection Events': 2, 'Get Detection Rule Indicators': 1, 'Retrieve Annotation for Entities': 1, 'Add or Replace Entities to Annotation': 1, 'Resolve Detection': 1, 'Get Telemetry Bandwidth': 1}
- `fortinet-fortipam` title prefixes: {'Update User': 1, 'Execute an API Request': 1, 'Get All Users': 1, 'Delete User': 1, 'Get User Details': 1}
- `fortinet-fortirecon-aci` title prefixes: {'Get Adversary Centric Intelligence ACI Reports': 4, 'Get Intel IOCs': 2, 'Get Ransomware Victims': 1, 'Get Ransomware Group Information': 1, 'Get Vulnerability Intelligence vulnerable vendors': 1, 'Update Stealers Leaked Status': 1, 'Get Vendor Watchlist': 1, 'Get Specific Adversary Centric Intelligence ACI Report': 1}
- `fortinet-fortirecon-brand-protection` title prefixes: {'Get Code Repositories': 1, 'Update Code Repo Status': 1, 'Get Social Media Threats': 1, 'Get Rogue Apps': 1, 'Update Social Media Threat Status': 1, 'Get Original Domains Statistics': 1, 'Get Rogue App By ID': 1, 'Get Takedown Requests': 1}
- `fortinet-fortirecon-easm` title prefixes: {'Get Subdomains': 2, 'Get Issues Discovered': 2, 'Mark Archived Issue as Active': 1, 'Update Leaked Credential Status': 1, 'Get Asset ASNs': 1, 'Get Group Details': 1, 'Update Archived Asset': 1, 'Get Scan Statistics': 1}
- `fortinet-fortisandbox` title prefixes: {'Get Job Verdict Detail': 4, 'Get Submission Job List': 4, 'Submit URL File': 2, 'Submit File': 2, 'Get File Verdict': 2, 'Get URL Rating': 1, 'Update Allow or Block List': 1, 'Get Scan Stats': 1}
- `fortinet-fortisiem` title prefixes: {'Run Advanced Search Query': 5, 'Search Events': 5, 'Get Incident Details': 3, 'List Incidents': 2, 'Get Device Information': 2, 'Get Events For Incident': 2, 'Get Watch List Entry': 1, 'Delete Watch List Entry': 1}
- `fortinet-web-filter-lookup` title prefixes: {'Check Category of Domain or URL': 2}
- `fortisoar-ml-engine` title prefixes: {'Train': 1, 'Predict': 1, 'Fetch similar record(s)': 1}
- `fortisoar-soc-simulator` title prefixes: {'Create Simulated Alert': 4, 'Create Malicious File Indicator': 3, 'Fetch Malicious URL': 3, 'Replace Variables': 1}
- `fuzzy-search` title prefixes: {'Filter JSON by Key Value': 3, 'Search Keyword In Text': 1}
- `github` title prefixes: {'List Pull Request': 3, 'Create Repository': 2, 'Get Server URL': 2, 'Update Remote Repository': 2, 'List Repository Collaborator': 2, 'Add Pull Request Review': 2, 'Push Changes': 2, 'Clone Repository': 2}
- `gitlab` title prefixes: {'Create Issue Comment': 4, 'List Repository Merge Requests': 4, 'Clone Repository': 3, 'Merge a Merge Request': 2, 'Create Repository Branch': 2, 'Create Repository': 2, 'Update Remote Repository': 2, 'Review Merge Request': 2}
- `icanhazdadjoke` title prefixes: {'Get Joke': 1}
- `imap` title prefixes: {'Fetch Email(s)': 1}
- `ip-quality-score` title prefixes: {'Get URL Reputation': 2, 'Get Email Reputation': 2, 'Get IP Reputation': 2}
- `ipstack` title prefixes: {'Geolocate IP': 2}
- `malsilo` title prefixes: {'Get IPv4 Feeds': 2, 'Get Domain Feeds': 2, 'Get URL Feeds': 2}
- `microsoft-graph-mail` title prefixes: {'Search Emails': 2, 'Delete Email': 1, 'Add Email Category': 1, 'Copy Email': 1, 'Get Folders': 1, 'Forward Email': 1, 'Execute an API Request': 1, 'Move Email': 1}
- `microsoft-teams` title prefixes: {"Get User's all Chat Messages": 2, 'Unarchive Team': 1, 'Remove Group Owner': 1, 'Get User Teams': 1, 'Get Team Details': 1, 'Create User': 1, 'Archive Team': 1, 'Get Meeting Details': 1}
- `microsoft-winrm` title prefixes: {'Run Command': 2, 'Upload File To Endpoint': 1, 'Run Powershell Command': 1, 'Run Script': 1, 'Run Inline Powershell Script': 1, 'Get File': 1}
- `mitre-attack` title prefixes: {'Get MITRE Data': 3}
- `mysql` title prefixes: {'Run Query': 5, 'List Columns': 1, 'List Tables': 1}
- `nist-nvd` title prefixes: {'Get Specific CVE ID Details': 3, 'Advance CVE Search': 1, 'CVE Search by Keywords': 1, 'CPE Search': 1, 'Get CVE Change History': 1}
- `openai` title prefixes: {'Get Vector Store Details': 2, 'Get Run Step Details': 2, 'Get File Details': 2, 'Get Thread Details': 2, 'Create Vector Store': 1, 'Get Tokens Usage': 1, 'Converse With OpenAI': 1, 'Get Run Details': 1}
- `phishing-classifier` title prefixes: {'Predict': 2, 'Train': 1, 'Get Training Results': 1}
- `qradar` title prefixes: {'Make an Ariel Query to QRadar': 3, 'Get Offenses from QRadar': 3, 'Get Source IP Addresses': 2, 'Get Destination IP Addresses': 2, 'Get Events Related to an Offense': 1, 'Get Offense Closing Reasons': 1, 'Get Cases': 1, 'Add or Update Table Element': 1}
- `qualys` title prefixes: {'Get Scanned Host List': 1}
- `screenshot` title prefixes: {'Screenshot URL': 2, 'Screenshot EML OR MSG File Content': 1, 'Screenshot Email Content': 1}
- `servicenow` title prefixes: {'Create Incident': 2, 'Get Assignment Group': 1, 'Get Location': 1, 'Get Users': 1}
- `slacalculator` title prefixes: {'Calculate SLA': 1, 'Calculate Elapsed SLA Time': 1}
- `slack` title prefixes: {'Send Message': 4, 'Upload File': 2, 'Rename Channel': 1, 'Create Channel': 1, 'Search Channel': 1, 'Get Channel Information': 1, 'Close Channel': 1, 'Invite User To Channel': 1}
- `smtp` title prefixes: {'Send Email': 9, 'Send Email (Advanced)': 6, 'Send Rich Text Email': 1}
- `splunk` title prefixes: {'Get Results for a Search': 4, 'Invoke Search': 4}
- `ssh` title prefixes: {'Execute remote command': 4}
- `symantec-cloudsoc` title prefixes: {'Get Event Logs': 1}
- `symantec-dlp` title prefixes: {'Get Incident Details': 1, 'Get Incidents IDs': 1}
- `tenable-io` title prefixes: {'Get Vulnerability Information': 2, 'Get Asset Export Status': 2, 'Download Asset Export Chunk': 2, "List Scan's Assets": 2, 'Get Vulnerability Export Status': 2, 'Submit Asset Export Job': 2, 'List Scans': 2, 'Download Vulnerability Export Chunk': 2}
- `time-series-chart-utilities` title prefixes: {'Format Data Set Output with Field-Grouped': 2, 'Assemble Query Time Windows': 2, 'Combine Query Results into Data Columns': 2, 'Flatten Data Sets and Groups': 2}
- `toronto_weather` title prefixes: {'Get Weather': 1}
- `trend-micro-vision-one` title prefixes: {'Add to Exception List': 2, 'Add to Block List': 1, 'Get Alert Lists': 1, 'Get Detection Data': 1, 'Remove from Suspicious Object List': 1, 'Add to Suspicious Object List': 1, 'Get Endpoint Details': 1, 'Restore endpoints': 1}
- `urlscan-io` title prefixes: {'Submit URL': 2, 'Custom Search': 1, 'Search Hash': 1, 'Search Domain': 1, 'Search IP': 1, 'Get Report': 1}
- `virustotal` title prefixes: {'Get IP Reputation': 7, 'Get Analysis Details': 6, 'Get File Reputation': 5, 'Get Domain Reputation': 2, 'Get URL Reputation': 2, 'Get Widget HTML Content': 2, 'Submit File': 2, 'Reanalyze IP': 1}
- `wazuh-siem` title prefixes: {'Get All Alerts in Last X Minutes': 1, 'Execute Lucene Search': 1, 'DSL Search': 1, 'Get Alert Details': 1, 'Execute DSL Search': 1}
- `whois-freaks` title prefixes: {'Get SSL Certificates': 1, 'Get DNS Lookup': 1, 'Get Whois Lookup': 1}
- `whois-rdap` title prefixes: {'Whois IP': 2}
- `whois-xml-api` title prefixes: {'Get Reverse WHOIS Search': 1, 'Get DNS Lookup': 1, 'Get SSL Certificates': 1, 'Get Reverse DNS Search': 1, 'Get WHOIS Search': 1, 'Brand Monitor': 1, 'Get WHOIS History Search': 1, 'Domain or Subdomain Discovery': 1}
- `xforce` title prefixes: {'Get DNS Record': 2, 'Get IP Reputation': 2, 'Get IP Behaviour': 2, 'Get File Reputation': 2, 'Get Vulnerability from XFID': 1, 'Get URL Behaviour': 1, 'Get Vulnerability': 1, 'Search Signature by PAMID': 1}

### 12.11 Connector `version` strings (per connector)

- `activedirectory`: {'2.2.0': 11, '2.1.1': 5, '2.2.1': 4, '2.0.0': 2, '2.4.0': 2}
- `alienvault-otx`: {'1.0.2': 1}
- `aws`: {'3.1.2': 31, '3.1.0': 1}
- `aws-commands`: {'1.1.0': 34}
- `axios-assyst`: {'1.0.0': 5}
- `axonius`: {'1.1.0': 2}
- `carbonblack-response`: {'2.0.1': 1, '2.0.0': 1}
- `cicd-utils`: {'1.1.0': 3, '1.2.0': 1}
- `cisa-advisory`: {'1.1.0': 5, '1.0.1': 4}
- `cisco-catalyst`: {'1.0.0': 3}
- `code-snippet`: {'2.0.0': 3, '2.0.3': 1}
- `crowd-strike-falcon`: {'3.1.0': 63}
- `csv-data-management`: {'1.3.0': 9, '1.2.0': 4, '1.0.0': 2, '1.1.0': 1}
- `cyops-schedule-report`: {'1.3.2': 1, '1.4.0': 1}
- `cyops-system-monitoring`: {'1.6.1': 4}
- `cyops_utilities`: {'3.2.1': 73, '3.2.3': 45, '3.2.6': 17, '3.7.0': 14, '3.2.4': 14}
- `darktrace`: {'1.4.0': 24}
- `dns`: {'1.0.0': 2}
- `exchange`: {'4.0.0': 6, '4.2.2': 1, '3.4.4': 1, '3.4.3': 1}
- `exploit-prediction-scoring-system`: {'1.0.0': 3}
- `file-content-extraction`: {'1.3.1': 4, '1.0.3': 3}
- `fortigate-firewall`: {'5.4.0': 42, '5.2.1': 5, '5.2.3': 3, '5.0.0': 1}
- `fortinet-fortiai`: {'1.3.0': 3}
- `fortinet-fortiai-proxy`: {'1.0.0': 3}
- `fortinet-fortianalyzer`: {'4.0.0': 45}
- `fortinet-fortiauthenticator`: {'1.0.0': 17}
- `fortinet-forticlient-ems`: {'1.2.0': 13}
- `fortinet-forticnapp`: {'1.1.0': 13}
- `fortinet-fortideceptor`: {'1.0.0': 9}
- `fortinet-fortidlp`: {'1.1.0': 21}
- `fortinet-fortiedr`: {'2.1.0': 32, '1.3.0': 1}
- `fortinet-fortiguard-ioc`: {'1.1.0': 4}
- `fortinet-fortiguard-outbreak`: {'3.0.0': 12}
- `fortinet-fortiguard-threat-intelligence`: {'4.1.0': 40}
- `fortinet-fortimail`: {'1.1.0': 1}
- `fortinet-fortimanager`: {'4.1.3': 69}
- `fortinet-fortimanager-json-rpc`: {'1.1.0': 6}
- `fortinet-fortindr-cloud`: {'1.2.0': 28, '1.0.0': 1}
- `fortinet-fortipam`: {'1.0.0': 5}
- `fortinet-fortirecon-aci`: {'2.1.2': 39}
- `fortinet-fortirecon-brand-protection`: {'2.1.0': 23}
- `fortinet-fortirecon-easm`: {'1.2.1': 41, '1.0.0': 2}
- `fortinet-fortisandbox`: {'2.1.0': 24, '1.0.4': 3}
- `fortinet-fortisiem`: {'6.0.0': 46, '5.0.1': 4, '4.5.0': 1, '5.0.2': 1, '4.1.0': 1}
- `fortinet-web-filter-lookup`: {'2.0.0': 2}
- `fortisoar-ml-engine`: {'1.0.0': 3}
- `fortisoar-soc-simulator`: {'1.0.8': 6, '2.0.0': 4, '1.0.0': 1}
- `fuzzy-search`: {'1.0.0': 4}
- `github`: {'2.1.0': 68}
- `gitlab`: {'2.1.0': 72}
- `icanhazdadjoke`: {'1.0.0': 1}
- `imap`: {'3.5.8': 1}
- `ip-quality-score`: {'1.0.1': 6}
- `ipstack`: {'1.0.1': 1, '1.0.0': 1}
- `malsilo`: {'2.0.1': 6}
- `microsoft-graph-mail`: {'1.4.0': 8, '1.0.1': 6, '1.1.0': 2}
- `microsoft-teams`: {'3.1.1': 36, '1.0.1': 2}
- `microsoft-winrm`: {'2.1.0': 6, '1.0.2': 1}
- `mitre-attack`: {'2.0.1': 2, '2.0.2': 1}
- `mysql`: {'1.0.0': 4, '1.0.1': 3}
- `nist-nvd`: {'1.0.2': 5, '1.0.1': 2}
- `openai`: {'4.0.0': 47}
- `phishing-classifier`: {'1.0.0': 4}
- `qradar`: {'1.6.2': 27, '1.5.1': 1}
- `qualys`: {'1.0.1': 1}
- `screenshot`: {'1.0.1': 3, '1.0.0': 1}
- `servicenow`: {'3.2.0': 5}
- `slacalculator`: {'2.1.0': 2}
- `slack`: {'3.3.0': 14, '3.0.0': 3}
- `smtp`: {'2.5.0': 7, '2.4.2': 5, '2.4.4': 3, '2.4.3': 1}
- `splunk`: {'1.4.0': 8}
- `ssh`: {'2.1.1': 4}
- `symantec-cloudsoc`: {'1.0.0': 1}
- `symantec-dlp`: {'2.2.0': 1, '2.1.0': 1}
- `tenable-io`: {'1.4.0': 28}
- `time-series-chart-utilities`: {'1.0.0': 8}
- `toronto_weather`: {'1.0.0': 1}
- `trend-micro-vision-one`: {'1.0.0': 17}
- `urlscan-io`: {'1.1.2': 7}
- `virustotal`: {'3.2.1': 26, '3.0.2': 5, '1.0.1': 2}
- `wazuh-siem`: {'1.0.0': 5}
- `whois-freaks`: {'1.0.0': 3}
- `whois-rdap`: {'1.0.2': 2}
- `whois-xml-api`: {'1.0.0': 8}
- `xforce`: {'1.0.2': 19}


## Recommendations for skill enhancement

Prioritized, concrete changes for the skill maintainer. Each references the finding section above.

### P0 — Accuracy (fix things the skill gets wrong or omits)

1. **Add the `versions: []` invariant** to the validation gotchas (§12.2). The skill should state: when generating, ALWAYS set `versions: []`; never embed historical snapshots. The server creates version 1 on import.
2. **Document that there is NO dedicated Join stepType** (§6.4). The current skill does not address how parallel branches converge. Explain: convergence = a target step with multiple incoming routes (fan-in). Any step type (Set Variable, Condition, End) can be a join target. Add a routing diagram example.
3. **Document for_each loop routing explicitly** (§6.5). The for_each step emits ONE outgoing route to the loop body; the body's last step routes either back to the for_each step (to continue iteration) or forward to a post-loop step. The skill should show a 3-step loop example (for_each → body → post-loop) with the correct routes.
4. **Add `do_until` retry pattern** to Reference-a-Playbook step docs (§12.6). Real exports use `do_until: {delay, retries, condition}` for polling sub-playbooks. The quickref mentions it but the schema doc lacks a concrete example.
5. **Confirm stepType UUID set is complete and stable** (§1.2, §1.3). All 21 documented UUIDs appear in real exports; NO new undocumented UUIDs were found in these 1367 workflows. The existing quickref is accurate — no additions needed for stepType coverage.

### P1 — Coverage (add what the skill does not mention at all)

6. **Add a Connector Operations catalog** (§2). Build a per-connector reference table in a new file `reference/connector-operations.md` listing every (connector, operation, operationTitle) triple observed, with counts. This is the single highest-value addition — it lets the skill pick the correct `operation`/`operationTitle`/`version` for a requested integration. Include the ~28 connectors and their operation menus. Especially expand cyops_utilities (40+ ops), fortigate-firewall, fortinet-fortimanager, fortinet-fortisiem, microsoft-graph-mail, slack, microsoft-teams, virustotal, crowdstrike-falcon, tenable-io, smtp, exchange, imap, ssh, mysql, aws-ec2.
7. **Document `version` strings per connector** (§12.11). The skill currently uses placeholder versions like "3.5.0". Provide a per-connector "known good version" table so generated playbooks import cleanly against a matching connector version.
8. **Add a Jinja patterns cookbook** (§8). Create `reference/jinja-cookbook.md` with the 50+ real expressions categorized (trigger input, step output, loop item, REST request, picklist filter, fromIRI, arrow date, statement blocks, list mutation via `vars.x.append`). The current skill lists ~12 patterns; production uses far richer expressions including `{% if %}` control flow inside `temporary_var`, `| tojson`, `| fromIRI`, `arrow.get(...).int_timestamp`, `| unique`, `| split`, `| join`, nested `vars.steps.X.data.0.output`.
9. **Document `macros` and `exported_tags` top-level arrays** (§9, §10). State: generated exports should include `"macros": []` and `"exported_tags": []` at top level; these are collection-bundle metadata, not needed for self-contained playbooks.
10. **Document the `image` base64 icon field on collections** (§12.1). Real collections ship a base64 PNG icon; `"image": null` is acceptable for generated playbooks but the field exists and should be in the collection schema.
11. **Document `tag` (hashtag) values** (§12.3). Real exports use `tag` values like `"#Subroutine"`, `"#Connector"`, `"#Triage"`, `"#Investigation"`, `"#Hunt"`. Add a picklist of common tags the user can choose from.

### P2 — Precision (sharpen existing docs)

12. **Add `when` / `ignore_errors` / `for_each` prevalence table per step type** (§12.9). The quickref says these are "common argument keys" but does not say WHICH step types actually use them. e.g. `for_each` appears on Set Variable, Create Record, Update Record, Bulk ingest, Connector calls — but NOT on Condition/Reference/Wait. `when` is most common on connector & email steps. `ignore_errors` is most common on email & REST steps.
13. **Add `operationTitle` naming convention** (§12.10). Titles follow `"Prefix: Operation"` (e.g. `"Utils: No Operation"`, `"FSR: Make FortiSOAR API Call"`, `"Exch: Get Email"`). Document the prefix-per-connector convention so generated titles look native.
14. **Add inputVariable full schema** (§11.3). The skill shows one datetime example. Document all observed `type`/`dataType`/`formType` combos and the `dataSource` (picklist-source) sub-object for picklist-type inputs. Show a string, integer, datetime, and picklist example.
15. **Document `priority` picklist values** (§4.3). Confirm `2b563c61-...` = Medium is by far the most common; add the other priority levels if discoverable.
16. **Document `singleRecordExecution`/`synchronous`/`remoteExecutableFlag` defaults by trigger kind** (§12.4). Manual buttons → singleRecordExecution=true; Referenced (sub-playbook) → remoteExecutableFlag often true; synchronous usually false except for referenced sub-playbooks that block the caller.
17. **Document `debug:false, isActive:true` as the safe defaults** (§12.5) — overwhelmingly the most common in production.
18. **Add a `parameters` contract examples section** (§11.1, §11.2). Show that referenced playbooks declare `parameters: ["name1","name2"]` and the caller passes them via `arguments: {"name1": "{{...}}"}. Top real parameter names observed include `alert_original`, `connector_config`, `my_user_original`, `file_iri`, `recipient_list`.

### P3 — Workflow generation templates

19. **Add a "manual button with input form" template** that includes a populated `inputVariables` array with a string field, a datetime field, and a picklist field (§3.3, §11.3). This is a very common real pattern the current templates under-cover.
20. **Add a "polling/retry sub-playbook" template** using Reference-a-Playbook + `do_until` (§12.6).
21. **Add a "for_each bulk create" template** showing Set-Variable loop → Create Record with `for_each.__bulk=true, batch_size=100` (§6.5).
22. **Add a "parallel fan-out → join" template** showing one source step routing to 2 branches that both converge on a single join-target step (§6.4).
