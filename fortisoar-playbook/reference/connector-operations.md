# FortiSOAR Connector Operations Catalog

Catalog of FortiSOAR connector operations, harvested from the official fortinet-fortisoar GitHub org (418 connector repos scanned, 379 with manifests, 3339 operations total).

The `operation` field is what goes in a playbook step's `operation`; `title` is the `operationTitle`; `parameters` define the `params` object.

Full parameter detail (descriptions, data types, default values, choices) lives in `OFFICIAL/_connector-manifests.json`. The table below is scannable; in the `parameters` column each entry is `name(title[, REQ])`.

- [Connectors on GitHub](#connectors-on-github)
- [Connectors NOT on GitHub (built-in)](#connectors-not-on-github-built-in)

## Connectors on GitHub

Alphabetical by connector slug.

### `abnormal-security`

version 1.0.1 — Abnormal Security helps to prevent email and email-like attacks, automate your security operations and reduce your total spend with one exte…

- GitHub: connector-abnormal-security
- Category: Email Security
- Operations: 20

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_threats` | Get Threats | investigation | ✓ | `filter`(Filter), `source`(Source), `sender`(Sender), `recipient`(Recipient), `subject`(Subject), `topic`(Topic), `attackType`(Attack Type), `attackVector`(Attack Vector), `attackStrategy`(Attack Strategy), `impersonatedParty`(Impersonated Party), `mock-data`(Mock Data), `pageSize`(Page Size), `pageNumber`(Page Number) |
| `get_threat_details` | Get Threat Details | investigation | ✓ | `threatId`(Threat ID, REQ), `mock-data`(Mock Data), `pageSize`(Page Size), `pageNumber`(Page Number) |
| `get_threat_links` | Get Threat Links | investigation | ✓ | `threatId`(Threat ID, REQ), `mock-data`(Mock Data) |
| `get_threat_attachments` | Get Threat Attachments | investigation | ✓ | `threatId`(Threat ID, REQ), `mock-data`(Mock Data) |
| `get_cases` | Get Cases | investigation | ✓ | `filter`(Filter), `mock-data`(Mock Data), `pageSize`(Page Size), `pageNumber`(Page Number) |
| `get_case_details` | Get Case Details | investigation | ✓ | `caseId`(Case ID, REQ), `mock-data`(Mock Data) |
| `get_message_details` | Get Message Details | investigation | ✓ | `messageId`(Message ID, REQ) |
| `get_abuse_campaigns` | Get Abuse Campaigns | investigation | ✓ | `filter`(Filter), `sender`(Sender), `recipient`(Recipient), `subject`(Subject), `reporter`(Reporter), `attackType`(Attack Type), `threatType`(Threat Type), `mock-data`(Mock Data), `pageSize`(Page Size), `pageNumber`(Page Number) |
| `get_abuse_campaign_details` | Get Abuse Campaign Details | investigation | ✓ | `campaignId`(Campaign ID, REQ), `mock-data`(Mock Data) |
| `get_employee_info` | Get Employee Information | investigation | ✓ | `emailAddress`(Email Address, REQ), `mock-data`(Mock Data) |
| `get_employee_identity_analysis` | Get Employee Identity Analysis | investigation | ✓ | `emailAddress`(Email Address, REQ), `mock-data`(Mock Data) |
| `get_employee_login_info` | Get Employee Login Information | investigation | ✓ | `emailAddress`(Email Address, REQ), `mock-data`(Mock Data) |
| `get_detection_reports` | Get Detection Reports | investigation | ✓ | `inquiry_type`(Inquiry Type, REQ), `start`(Start), `end`(End), `status`(Status) |
| `check_case_action_status` | Check Case Action Status | investigation | ✓ | `caseId`(Case ID, REQ), `actionId`(Action ID, REQ), `mock-data`(Mock Data) |
| `check_threat_action_status` | Check Threat Action Status | investigation | ✓ | `threatId`(Threat ID, REQ), `actionId`(Action ID, REQ), `mock-data`(Mock Data) |
| `download_data_from_threat_log` | Download Data from Threat Log | investigation | ✓ | `filter`(Filter), `source`(Source), `mock-data`(Mock Data) |
| `manage_threat` | Manage Threat | investigation | ✓ | `threatId`(Threat ID, REQ), `action`(Action, REQ), `mock-data`(Mock Data) |
| `manage_abnormal_case` | Manage Abnormal Case | investigation | ✓ | `caseId`(Case ID, REQ), `action`(Action, REQ), `mock-data`(Mock Data) |
| `get_case_analysis` | Get Case Analysis | investigation | ✓ | `caseId`(Case ID, REQ), `mock-data`(Mock Data) |
| `submit_false_positive_report` | Submit a Missed Attack or False Positive Report | investigation | ✓ | `report_data`(False Positive Report Data, REQ), `mock-data`(Mock Data) |

### `acronis`

version 1.0.0 — Acronis Cyber Protect Connect is a remote access solution to remotely manage workloads - quickly and easily. This connector facilitates auto…

- GitHub: connector-acronis
- Category: Attack surface management
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_alert` | Create an Alert | investigation | ✓ | `title`(Title), `type`(Type), `category`(Category), `tenant`(Tenant), `description`(Description), `other_fields`(Other Fields) |
| `get_alerts` | Get Alerts | investigation | ✓ | `alerts_id`(Alert ID), `limit`(Limit) |
| `get_alert_types` | Get Alert Types | investigation | ✓ | `os_type`(OS Type), `category`(Category), `order`(Order) |
| `delete_alert` | Delete an Alert | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `get_categories` | Get Categories | investigation | ✓ | — |

### `activedirectory`

version 2.4.0 — Active Directory (AD) is a directory service that Microsoft developed for Windows domain networks. You can directly query AD to retrieve inf…

- GitHub: connector-activedirectory
- Category: Directory Service
- Operations: 17

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `add_object` | Add Object | investigation | ✓ | `object_class`(Object Type, REQ), `custom_attributes`(Custom Attributes) |
| `get_all_object_details` | Get All Objects Details | investigation | ✓ | `search_object`(Object Type, REQ), `page_size`(Page Size), `size_limit`(Size Limit), `cookie`(Paged Cookie) |
| `get_specific_object_details` | Get Specific Object Details | investigation | ✓ | `search_object`(Object Type, REQ) |
| `update_object` | Update Object | investigation | ✓ | `object_class`(Object Type, REQ), `custom_attributes`(Custom Attributes) |
| `move_computer_ou` | Move Computer to Targeted Organization Unit(OU) | investigation | ✓ | `computer_dn`(Distinguished Name (DN), REQ), `computer_name`(Common Name, REQ), `target_dn`(Target Organization Unit (OU), REQ) |
| `delete_object` | Delete Object | investigation | ✓ | `object_class`(Object Type, REQ) |
| `add_group_members` | Add Group Members | investigation | ✓ | `group_dn`(Group DN, REQ), `object_class`(Object Type, REQ) |
| `remove_group_members` | Remove Group Members | investigation | ✓ | `group_dn`(Group DN, REQ), `object_class`(Object Type, REQ) |
| `advanced_search` | Advanced Search | investigation | ✓ | `query`(LDAP Query, REQ), `page_size`(Page Size), `size_limit`(Size Limit), `cookie`(Paged Cookie) |
| `global_search` | Global Search | investigation | ✓ | `search_object`(Object Type, REQ), `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Value, REQ), `page_size`(Page Size), `size_limit`(Size Limit), `cookie`(Paged Cookie) |
| `enable_user_account` | Enable User Account | remediation | ✓ | `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Value, REQ) |
| `disable_user_account` | Disable User Account | containment | ✓ | `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Value, REQ) |
| `move_user_ou` | Move User to Targeted Organization Unit(OU) | investigation | ✓ | `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Value, REQ), `destinationOU`(Destination OU, REQ) |
| `enable_computer` | Enable Computer | remediation | ✓ | `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Value, REQ) |
| `disable_computer` | Disable Computer | containment | ✓ | `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Value, REQ) |
| `reset_password` | Reset Password | containment | ✓ | `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Attributes Value, REQ), `new_password`(New Password, REQ) |
| `force_password_reset_next_logon` | Force password reset on next logon | containment | ✓ | `search_attr_name`(Attributes Type, REQ), `search_attr_value`(Attributes Value, REQ) |

### `agentic-ai-investigation-report`

version 1.0.0 — Creates AI-generated investigation report that helps streamline analysis and accelerate incident response

- GitHub: connector-agentic-ai-investigation-report
- Category: ['Compliance and Reporting']
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `generate_investigation_pdf` | Generate Investigation Report | utilities | ✓ | `investigationJSON`(Investigation JSON, REQ), `outputFileName`(Output File Name, REQ), `alertName`(Alert Name, REQ), `alertid`(Alert ID, REQ), `kbQuestions`(Knowledge Base - Questions, REQ) |

### `akamai`

version 1.0.0 — Akamai is an American content delivery network (CDN), cybersecurity, and cloud service company, providing web and Internet security services…

- GitHub: connector-akamai
- Category: Network Security
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_critical_events` | List Critical Events | investigation | ✓ | `contract`(Contract Name, REQ) |
| `list_events` | List Events | investigation | ✓ | `contract`(Contract Name, REQ) |
| `list_attack_reports` | List Attack Reports | investigation | ✓ | `start`(Start Time, REQ), `end`(End Time, REQ), `contract`(Contract Name, REQ) |
| `get_an_attack_report` | Get An Attack Report | investigation | ✓ | `attackId`(Attack ID, REQ), `contract`(Contract Name, REQ) |

### `akamai-waf`

version 1.0.2 — Akamai Web Application Firewall (WAF) is a cloud-based security solution designed to protect web applications from various cyber threats. It…

- GitHub: connector-akamai-waf
- Category: Firewall and Network Protection
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_network_list` | Create Network List | investigation | ✓ | `name`(Name, REQ), `type`(Type, REQ), `list`(List of Elements, REQ), `description`(Description), `contractId`(Contract ID), `groupId`(Group ID) |
| `get_network_list` | Get Network List | investigation | ✓ | `search`(Search), `listType`(List Type), `extended`(Extended), `includeElements`(Include Elements) |
| `get_network_by_id` | Get Network by ID | investigation | ✓ | `networkListId`(Network List ID, REQ), `extended`(Extended), `includeElements`(Include Elements) |
| `update_network_list` | Update Network List | investigation | ✓ | `networkListId`(Network List ID, REQ), `name`(Name, REQ), `type`(Type, REQ), `list`(List of Elements, REQ), `syncPoint`(Sync Point, REQ), `description`(Description), `extended`(Extended), `includeElements`(Include Elements) |
| `delete_network_by_id` | Delete Network by ID | investigation | ✓ | `networkListId`(Network List ID, REQ) |
| `append_elements_to_network_list` | Append Elements to Network List | investigation | ✓ | `networkListId`(Network List ID, REQ), `list`(List of Elements, REQ) |
| `delete_element_from_network_list` | Delete an Element from Network List | investigation | ✓ | `networkListId`(Network List ID, REQ), `element`(Element Value, REQ) |
| `activate_network_list` | Activate Network List | investigation | ✓ | `networkListId`(Network List ID, REQ), `environment`(Environment, REQ), `comments`(Comment), `notificationRecipients`(Notify Recipients), `siebelTicketId`(Siebel Ticket ID) |
| `get_activation_status_of_network_list` | Get Activation Status of Network List | investigation | ✓ | `networkListId`(Network List ID, REQ), `environment`(Environment, REQ) |

### `alienvault-usm-anywhere`

version 1.2.0 — AlienVault USM Anywhere Connector can be used to automate actions like get events, get event details, get alarm details, get alarms, get ala…

- GitHub: connector-alienvault-usm-anywhere
- Category: Threat Detection
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alarms` | Get Alarms | investigation | ✓ | `page`(Page), `size`(Size), `sort`(Sort), `sort_order`(Sort Order), `status`(Status), `suppressed`(Suppressed), `rule_intent`(Rule Intent), `rule_method`(Rule Method), `rule_strategy`(Rule Strategy), `priority_label`(Priority Label), `alarm_sensor_sources`(Alarm Sensor Sources), `timestamp_occured_gte`(After Time), `timestamp_occured_lte`(Before Time) |
| `get_alarm_details` | Get Alarm Details | investigation | ✓ | `alarmId`(Alarm IDs, REQ) |
| `get_alarm_labels` | Get Alarm Labels | investigation | ✓ | `alarmId`(Alarm ID, REQ) |
| `add_alarm_label` | Add Alarm Label | investigation | ✓ | `alarmId`(Alarm ID, REQ), `labelId`(Label ID, REQ) |
| `delete_alarm_label` | Delete Alarm Label | investigation | ✓ | `alarmId`(Alarm ID, REQ), `labelId`(Label ID, REQ) |
| `get_events` | Get Events | investigation | ✓ | `accountName`(Account Name), `page`(Page), `size`(Size), `sort`(Sort), `sort_order`(Sort Order), `suppressed`(Suppressed), `plugin`(Plugin), `eventName`(Event Name), `sourceName`(Source Name), `sensorUUID`(Sensor UUID), `sourceUsername`(Source Username), `timestamp_occured_gte`(After Time), `timestamp_occured_lte`(Before Time) |
| `get_event_details` | Get Event Details | investigation | ✓ | `eventId`(Event ID, REQ) |

### `alloy-itsm`

version 1.0.0 — Alloy ITSM is an IT Service Management (ITSM) solution designed to help organizations manage and streamline their IT services and operations…

- GitHub: connector-alloy-itsm
- Category: ['Ticket Management']
- Operations: 17

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_current_user_profile` | Get Current User Profile | investigation | ✓ | — |
| `get_objects` | Get Objects | investigation | ✓ | `object_class`(Object Class, REQ), `par_fields`(Fields), `par_search_text`(Search Text), `filters`(Filters), `sort_by`(Sort By), `par_limit`(Limit), `par_offset`(Offset) |
| `get_objects_advanced` | Get Objects Advanced Search | investigation | ✓ | `object_class`(Object Class, REQ), `fields`(Fields), `filters`(Filters), `searchText`(Search Text), `sort`(Sort), `limit`(Limit), `offset`(Offset) |
| `get_object_by_id` | Get Object By ID | investigation | ✓ | `oid`(Object Identifier (OID or ID), REQ) |
| `get_object_activities` | Get Object Activities | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `par_fields`(Activity Fields), `filters`(Filters), `sort_by`(Sort By), `par_limit`(Limit), `par_offset`(Offset) |
| `get_object_activities_advanced` | Advanced Search for Object Activities | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `fields`(Activity Fields), `filters`(Filters), `sort`(Sort), `limit`(Limit), `offset`(Offset) |
| `get_classification_values` | Get Classification Values | investigation | ✓ | `par_objectClass`(Object Class, REQ), `par_refField`(Reference Field, REQ), `filters`(Filters), `par_fields`(Fields), `sort_by`(Sort By), `par_limit`(Limit), `par_offset`(Offset) |
| `get_classification_values_advanced` | Advanced Search for Classification Values | investigation | ✓ | `objectClass`(Object Class, REQ), `refField`(Reference Field, REQ), `fields`(Fields), `filters`(Filters), `sort`(Sort), `limit`(Limit), `offset`(Offset) |
| `create_object` | Create Object | investigation | ✓ | `action_id`(Action ID, REQ), `summary`(Summary), `description`(Description), `category`(Category), `requester`(Requester), `urgency`(Urgency), `impact`(Impact), `fields`(Additional Fields) |
| `run_step_action` | Update Object | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `action_id`(Step Action ID, REQ), `summary`(Summary), `description`(Description), `category`(Category), `requester`(Requester), `urgency`(Urgency), `impact`(Impact), `fields`(Additional Fields) |
| `check_step_action_availability` | Check Step Action Availability | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `action_id`(Step Action ID, REQ) |
| `list_object_attachments` | List Object Attachments | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `par_fields`(Fields), `filters`(Filters), `sort_by`(Sort By), `par_limit`(Limit), `par_offset`(Offset) |
| `get_attachment_content` | Get Attachment Content | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `attachment_id`(Attachment ID, REQ) |
| `download_attachment` | Download Attachment | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `attachment_id`(Attachment ID, REQ), `attachment_name`(Attachment Name), `attachment_description`(Attachment Description), `skip_fortisoar_upload`(Skip FortiSOAR Upload) |
| `add_attachments` | Add Attachments | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `path`(File or Attachment IRI, REQ) |
| `remove_attachment` | Remove Attachment | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `attachment_id`(Attachment ID, REQ) |
| `update_attachment_description` | Update Attachment Description | investigation | ✓ | `oid`(Object Identifier (OID), REQ), `attachment_id`(Attachment ID, REQ), `description`(Description, REQ) |

### `alphamountain`

version 1.0.0 — alphaMountain Threat Response integrates investigations informed by reputation scores of target hosts, domains, and IP addresses. It fetches…

- GitHub: connector-alphamountain
- Category: Threat Detection
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_threat_score` | Get Threat Score | investigation | ✓ | `input_type`(Input Type, REQ) |
| `get_url_categories` | Get URL Categories | investigation | ✓ | `input_type`(Input Type, REQ) |
| `identify_impersonation_detection` | Get Likely Impersonated Domain for a URL | investigation | ✓ | `url`(URL, REQ), `limit`(Limit, REQ) |
| `get_domain_popularity` | Get Popularity of Domain | investigation | ✓ | `domain`(Domain, REQ) |

### `alphamountain-feed`

version 1.0.0 — The AlphaMountain feed connector facilitates seamless integration with AlphaMountain's data sources, providing access to real-time and histo…

- GitHub: connector-alphamountain-feed
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `start`(Start Date), `flags`(Flags), `risk_min`(Minimum Risk), `risk_min`(Maximum Risk), `include_categories`(Include Categories), `include_popularity`(Include Popularity), `limit`(Limit) |
| `get_available_category` | Get Available Categories | investigation | ✓ | — |

### `anomali-limo-threat-intel-feed`

version 2.0.0 — Anomali Limo is a preconfigured set of intelligence feeds that STAXX users can access immediately upon download, and which offers indicators…

- GitHub: connector-anomali-limo-threat-intel-feed
- Category: Threat Intelligence
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_api_root_information` | Get API Root Information | investigation | ✓ | — |
| `get_collections` | Get Collections | investigation | ✓ | `collectionID`(Collection ID) |
| `get_objects_by_collection_id` | Get Objects By Collection ID | investigation | ✓ | `collectionID`(Collection ID, REQ), `added_after`(Created After), `output_mode`(Process Response As), `offset`(Offset, REQ), `limit`(Limit) |
| `get_output_schema` | Get Output Schema | — | ✓ | — |
| `get_objects_by_object_id` | Get Object By Object ID | investigation | ✓ | `collectionID`(Collection ID, REQ), `objectID`(Object ID, REQ) |
| `get_manifest_by_collection_id` | Get Manifest By Collection ID | investigation | ✓ | `collectionID`(Collection ID, REQ), `added_after`(Added After) |

### `anyrun`

version 2.0.0 — ANY.RUN empowers SOC teams to cut MTTD/MTTR with fast verdicts using the Interactive Sandbox. With the ANY.RUN Cloud Sandbox connector for F…

- GitHub: connector-anyrun
- Category: Malware Analysis
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_user_limits` | Retrieve Account Usage Limits | investigation | ✓ | — |
| `get_user_history` | Retrieve Analysis History | investigation | ✓ | `team`(Team), `skip`(Skip), `limit`(Limit) |
| `detonate_file` | Analyze File in Sandbox | investigation | ✓ | `attachment_iri`(Attachment IRI, REQ), `operationSystem`(Operating System, REQ) |
| `detonate_url` | Analyze URL in Sandbox | investigation | ✓ | `obj_url`(URL, REQ), `operationSystem`(Operating System, REQ) |
| `get_analysis_verdict` | Retrieve Analysis Verdict | investigation | ✓ | `task_uuid`(Analysis ID, REQ) |
| `get_report` | Retrieve Analysis Report | investigation | ✓ | `task_uuid`(Analysis ID, REQ), `report_type`(Report Type) |
| `get_report_attachments` | Retrieve Report Attachments | investigation | ✓ | `task_uuid`(Analysis ID, REQ), `report_type`(Report Type) |
| `delete_analysis` | Delete Sandbox Analysis | investigation | ✓ | `task_uuid`(Analysis ID, REQ) |

### `anyrun-threat-intelligence-feeds`

version 1.0.0 — The ANY.RUN Threat Intelligence Feeds connector FortiSOAR users with continuously updated, high-fidelity IOCs (malicious IPs, domains, and U…

- GitHub: connector-anyrun-threat-intelligence-feeds
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `collectionType`(Collection type, REQ), `feedFetchDepth`(Feed Fetch Depth), `output_mode`(Process Response As) |

### `anyrun-threat-intelligence-lookup`

version 1.0.0 — ANY.RUN empowers SOC teams to cut MTTD/MTTR with fast IOC enrichment using the Threat Intelligence Lookup. With the ANY.RUN Threat Intellige…

- GitHub: connector-anyrun-threat-intelligence-lookup
- Category: ['Data Enrichment & Threat Intelligence']
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_intelligence` | Lookup IoC in Threat Intelligence | investigation | ✓ | `query`(Query, REQ), `lookup_depth`(Lookup Depth) |

### `anything-llm`

version 1.0.0 — This connector is providing automation actions for Anything LLM that supports using Retrieval Augmented Generation (RAG) with an LLM and use…

- GitHub: connector-anything-llm
- Category: ML Service
- Operations: 15

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_documents` | Get Documents List | investigation | ✓ | — |
| `get_document` | Get Document by Name | investigation | ✓ | `doc_name`(Document Name, REQ) |
| `get_workspace_list` | Get Workspace List | investigation | ✓ | — |
| `get_workspace` | Get Workspace by Slug | investigation | ✓ | `workspace_name`(Workspace Slug, REQ) |
| `add_workspace_embedding` | Add Workspace Embedding | investigation | ✓ | `workspace_name`(Workspace Slug, REQ), `folder_name`(Folder Name, REQ), `doc_name`(Document Name, REQ) |
| `upload_document` | Upload Document | investigation | ✓ | `file_type`(Filepath or Record IRI, REQ) |
| `upload_document_link` | Upload Document Link | investigation | ✓ | `web_link`(Web Link, REQ) |
| `upload_document_text` | Upload Document Text | investigation | ✓ | `plain_text`(Plain Text, REQ), `doc_title`(Document Title, REQ), `description`(Description, REQ), `author`(Author, REQ), `source`(Source, REQ) |
| `create_workspace` | Create Workspace | investigation | ✓ | `workspace_name`(Workspace Name, REQ) |
| `create_document_folder` | Create Folder in Documents | investigation | ✓ | `folder_name`(Folder Name, REQ) |
| `update_workspace_settings` | Update Workspace Settings | investigation | ✓ | `workspace_name`(Workspace Slug, REQ), `settings_data`(Workspace Settings, REQ) |
| `workspace_chat` | Workspace Chat | investigation | ✓ | `workspace_name`(Workspace Slug, REQ), `message`(Massage to send, REQ), `mode`(Mode, REQ) |
| `move_document` | Move Document | investigation | ✓ | `src_folder_name`(Source Folder Name, REQ), `dest_folder_name`(Destination Folder Name, REQ), `doc_name`(Document Name, REQ) |
| `delete_document` | Delete Document | investigation | ✓ | `folder_name`(Folder Name, REQ), `doc_name`(Document Name, REQ) |
| `delete_workspace_embedding` | Remove Workspace Embedding | investigation | ✓ | `workspace_name`(Workspace Slug, REQ), `folder_name`(Folder Name, REQ), `doc_name`(Document Name, REQ) |

### `apivoid`

version 2.0.0 — Apivoid connector provides several threat intelligence services ranging from IP/URL/Domain reputation to domain age and website screenshots

- GitHub: connector-apivoid
- Category: Threat Intelligence
- Operations: 12

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `domainbl` | Get Domain Reputation | investigation | ✓ | `req_value`(Domain Name, REQ) |
| `iprep` | Get IP Reputation | investigation | ✓ | `req_value`(IP Address, REQ) |
| `screenshot` | Get URL Screenshot | investigation | ✓ | `req_value`(URL, REQ) |
| `urlrep` | Get URL Reputation | investigation | ✓ | `req_value`(URL, REQ) |
| `domainage` | Get Domain Age | investigation | ✓ | `req_value`(Domain Name, REQ) |
| `sitetrust` | Get Domain Trustworthiness | investigation | ✓ | `req_value`(Domain Name, REQ) |
| `parkeddomain` | Get Domain Parked Status | investigation | ✓ | `req_value`(Domain Name, REQ) |
| `urlstatus` | Get URL Status | investigation | ✓ | `req_value`(URL, REQ) |
| `emailverify` | Get Email Reputation | investigation | ✓ | `req_value`(Email Address, REQ) |
| `dnspropagation` | Get DNS Propagation | investigation | ✓ | `req_value`(Domain Name, REQ), `dns_record_type`(Record Type, REQ) |
| `sslinfo` | Get SSL Info | investigation | ✓ | `req_value`(Domain Name, REQ) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `arbor-aed`

version 1.1.0 — Netscout Arbor Edge Defense (AED) secures the internet data center edge from threats against availability — specifically from application-la…

- GitHub: connector-arbor-aed
- Category: Network Security
- Operations: 26

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_countries` | Get Countries | investigation | ✓ | `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `create_inbound_protection_groups` | Create Inbound Protection Groups | investigation | ✓ | `name`(Protection Group Name, REQ), `prefixes`(IP Addresses or CIDRs, REQ), `serverType`(Protection Group Server Type, REQ), `description`(Description), `active`(Active), `protectionLevel`(Protection Level) |
| `get_inbound_protection_groups` | Get Inbound Protection Groups | investigation | ✓ | `pgid`(Protection Group Identifier), `name`(Protection Group Name), `description`(Description), `timeCreated`(Created Time), `active`(Active), `protectionLevel`(Protection Level), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `update_inbound_protection_groups` | Update Inbound Protection Groups | investigation | ✓ | `pgid`(Protection Group IDs, REQ), `active`(Active), `protectionLevel`(Protection Level) |
| `add_inbound_blacklist_countries` | Add Inbound Blacklist Countries | investigation | ✓ | `country`(Country Code, REQ), `cid_pgid`(Select CID or PGID), `annotation`(Annotation) |
| `get_inbound_blacklisted_countries` | Get Inbound Blacklisted Countries | investigation | ✓ | `country`(Country Code), `cid_pgid`(Select CID or PGID), `updateTime`(Update Time), `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `remove_inbound_blacklisted_countries` | Remove Inbound Blacklisted Countries | investigation | ✓ | `country`(Country, REQ), `cid_pgid`(Select CID or PGID) |
| `add_inbound_blacklist_domains` | Add Inbound Blacklist Domains | investigation | ✓ | `domain`(Domain, REQ), `cid_pgid`(Select CID or PGID), `annotation`(Annotation) |
| `get_inbound_blacklisted_domains` | Get Inbound Blacklisted Domains | investigation | ✓ | `domain`(Domain), `cid_pgid`(Select CID or PGID), `updateTime`(Update Time), `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `remove_inbound_blacklisted_domains` | Remove Inbound Blacklisted Domains | investigation | ✓ | `domain`(Domain, REQ), `cid_pgid`(Select CID or PGID) |
| `add_inbound_blacklist_hosts` | Add Inbound Blacklist Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID), `annotation`(Annotation) |
| `get_inbound_blacklisted_hosts` | Get Inbound Blacklisted Hosts | investigation | ✓ | `hostAddress`(Host Address), `cid_pgid`(Select CID or PGID), `updateTime`(Update Time), `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `remove_inbound_blacklisted_hosts` | Remove Inbound Blacklisted Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID) |
| `add_inbound_whitelisted_hosts` | Add Inbound Whitelisted Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID), `annotation`(Annotation) |
| `get_inbound_whitelisted_hosts` | Get Inbound Whitelisted Hosts | investigation | ✓ | `hostAddress`(Host Address), `cid_pgid`(Select CID or PGID), `updateTime`(Update Time), `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `remove_inbound_whitelisted_hosts` | Remove Inbound Whitelisted Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID) |
| `add_inbound_blacklist_urls` | Add Inbound Blacklist URLs | investigation | ✓ | `url`(URL, REQ), `cid_pgid`(Select CID or PGID), `annotation`(Annotation) |
| `get_inbound_blacklisted_urls` | Get Inbound Blacklisted URLs | investigation | ✓ | `url`(URL), `cid_pgid`(Select CID or PGID), `updateTime`(Update Time), `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `remove_inbound_blacklisted_urls` | Remove Inbound Blacklisted URLs | investigation | ✓ | `url`(URL, REQ), `cid_pgid`(Select CID or PGID) |
| `add_outbound_blacklist_hosts` | Add Outbound Blacklist Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID), `annotation`(Annotation) |
| `get_outbound_blacklisted_hosts` | Get Outbound Blacklisted Hosts | investigation | ✓ | `hostAddress`(Host Address), `updateTime`(Update Time), `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `remove_outbound_blacklisted_hosts` | Remove Outbound Blacklisted Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID) |
| `add_outbound_whitelisted_hosts` | Add Outbound Whitelist Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID), `annotation`(Annotation) |
| `get_outbound_whitelisted_hosts` | Get Outbound Whitelisted Hosts | investigation | ✓ | `hostAddress`(Host Address), `updateTime`(Update Time), `q`(Queue), `select`(Response Fields), `sort_param`(Sort), `direction`(Direction), `page`(Page Number), `perPage`(Records Per Page), `other_fields`(Other Fields) |
| `remove_outbound_whitelisted_hosts` | Remove Outbound Whitelisted Hosts | investigation | ✓ | `hostAddress`(Host Address, REQ), `cid_pgid`(Select CID or PGID) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `arcanna-ai`

version 1.2.0 — Arcanna.ai is a platform for delivering decision intelligence. It augments Security Operation Center analysts in dealing with incoming threa…

- GitHub: connector-arcanna-ai
- Category: Threat Intelligence
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_arcanna_response` | Get Decision on Event | investigation | ✓ | `jobId`(Job ID, REQ), `eventId`(Event ID, REQ), `retryCount`(Retry Count, REQ), `waitTime`(Wait Time, REQ) |
| `trigger_training` | Trigger Job Training | utilities | ✓ | `jobId`(Job ID, REQ), `username`(Username) |
| `get_decision_set` | Get Job Decision Set | investigation | ✓ | `jobId`(Job ID, REQ) |
| `export_event` | Get Event | investigation | ✓ | `jobId`(Job ID, REQ), `eventId`(Event ID, REQ) |
| `send_feedback` | Send Feedback | investigation | ✓ | `jobId`(Job ID, REQ), `eventId`(Event ID, REQ), `feedback`(Feedback, REQ), `user`(Username) |
| `get_jobs` | Get Jobs | utilities | ✓ | — |
| `send_to_arcanna` | Send Event | investigation | ✓ | `jobId`(Job ID, REQ), `body`(Body, REQ), `caseId`(Case ID) |
| `get_job_by_name` | Get Job By Name | utilities | ✗ | `jobName`(Job Name, REQ) |
| `start_job` | Start Job | utilities | ✗ | `jobId`(Job ID, REQ), `username`(Username) |
| `stop_job` | Stop Job | utilities | ✗ | `jobId`(Job ID, REQ), `username`(Username) |

### `argo-cd`

version 1.0.1 — Argo CD (short for Argo Continuous Delivery) is a declarative, GitOps continuous delivery tool for Kubernetes. It allows you to manage and d…

- GitHub: connector-argo-cd
- Category: DevOps and Digital Operations
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_application` | Create Application | investigation | ✓ | `name`(Application Name, REQ), `source`(Source, REQ), `destination`(Destination, REQ), `metadata`(Metadata), `spec`(Specifications), `operation`(Operation), `additional_properties`(Additional Properties) |
| `get_applications` | Get Applications | investigation | ✓ | `name`(Application Name), `projects`(Projects), `additional_properties`(Additional Properties) |
| `get_application_by_name` | Get Application by Name | investigation | ✓ | `name`(Application Name, REQ) |
| `update_application` | Update Application | investigation | ✓ | `name`(Application Name, REQ), `source`(Source, REQ), `destination`(Destination, REQ), `metadata`(Metadata), `spec`(Specifications), `operation`(Operation), `additional_properties`(Additional Properties) |
| `delete_application` | Delete Application | investigation | ✓ | `name`(Application Name, REQ) |
| `get_clusters` | Get Clusters | investigation | ✓ | `server`(Server), `name`(Cluster Name) |
| `send_custom_request` | Execute an API Call | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `arkime`

version 1.0.0 — Arkime is an open-source, large-scale, full packet capture (FPC) and indexing system. It's designed for security professionals to store and …

- GitHub: connector-arkime
- Category: Network Security
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_connections` | Get All Connections | investigation | ✓ | `srcField`(Source Field), `dstField`(Destination Field), `baselineDate`(Baseline Date), `baselineVis`(Baseline Visible), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_connections_csv` | Get All Connections CSV | investigation | ✓ | `srcField`(Source Field), `dstField`(Destination Field), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_pcap_files` | Get All PCAP Files | investigation | ✓ | `length`(Limit), `start`(Offset) |
| `get_all_sessions` | Get All Sessions | investigation | ✓ | `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_sessions_csv` | Get All Sessions CSV | investigation | ✓ | `ids`(Session IDs), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_sessions_pcap` | Get All Sessions PCAP | investigation | ✓ | `ids`(Session IDs), `segments`(Segments), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_spi_graph` | Get All SPI Graph | investigation | ✓ | `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_spi_view` | Get All SPI View | investigation | ✓ | `spi`(SPI), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_fields` | Get All Fields | investigation | ✓ | `array`(Array) |
| `get_all_unique_fields` | Get All Unique Fields | investigation | ✓ | `counts`(Counts), `exp`(Expression Field), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `get_all_multiple_unique_fields` | Get All Multiple Unique Fields | investigation | ✓ | `counts`(Counts), `exp`(Expression Field), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `add_tags_to_sessions` | Add Tags to Sessions | investigation | ✓ | `ids`(Sessions IDs), `tags`(Tags), `segments`(Segments), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `remove_tags_from_sessions` | Remove Tags from Sessions | investigation | ✓ | `ids`(Sessions IDs), `tags`(Tags), `segments`(Segments), `date`(Relative Time (Hours Ago)), `expression`(Search Expression), `view`(Arkime View), `facets`(Include Aggregations), `startTime`(Start DateTime), `stopTime`(Stop DateTime), `order`(Sort Order), `fields`(Fields to Return), `bounding`(Time Bounding), `length`(Limit), `start`(Offset) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `armis`

version 1.1.0 — Armis connector protects from cyber threats created by the onslaught of unmanaged IoT devices. This connector facilitates operations to get …

- GitHub: connector-armis
- Category: OT & IoT Security
- Operations: 12

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alerts List | investigation | ✓ | `alert_id`(Alert ID), `start_time`(Start Time), `risk_level`(Risk Level), `status`(Status), `alert_type`(Alert Type), `site`(Sites), `records`(Number of Records to Return, REQ) |
| `get_alerts_by_asq` | Get Alerts By Armis Standard Query | investigation | ✓ | `query_string`(Armis Standard Query), `records`(Number of Records to Return, REQ) |
| `update_alert_status` | Update Alert Status | investigation | ✓ | `alert_id`(Alert ID, REQ), `status`(Status, REQ) |
| `get_devices` | Get Devices List | investigation | ✓ | `device_name`(Device Name), `device_id`(Device ID), `mac_address`(MAC Address), `ip_address`(IP Address), `device_type`(Device Type), `risk_level`(Risk Level), `site`(Sites), `time_frame`(Time Frame), `records`(Number of Records to Return, REQ) |
| `get_devices_by_asq` | Get Devices By Armis Standard Query | investigation | ✓ | `query_string`(Armis Standard Query), `records`(Number of Records to Return, REQ) |
| `update_device` | Update Device | investigation | ✓ | `device_id`(Device ID, REQ), `attributes`(Attributes, REQ) |
| `add_device_tags` | Add Device Tag | investigation | ✓ | `device_id`(Device ID, REQ), `tags`(Tags, REQ) |
| `remove_device_tags` | Remove Device Tag | investigation | ✓ | `device_id`(Device ID, REQ), `tags`(Tags, REQ) |
| `get_policies` | Get Policies List | investigation | ✓ | `records`(Number of Records to Return, REQ) |
| `update_policy` | Update Policy | investigation | ✓ | `policy_id`(Policy ID, REQ), `attributes`(Attributes, REQ) |
| `get_reports` | Get Reports List | investigation | ✓ | — |
| `get_vulnerability_matches` | Get Vulnerability Matches | investigation | ✓ | `input_type`(Input Type, REQ), `ids`(Device IDs / Vulnerability IDs, REQ), `records`(Number of Records to Return, REQ) |

### `aruba-clearpass`

version 1.2.0 — Aruba ClearPass is a policy management platform that enables businesses to effortlessly onboard new devices, grant varying access levels, an…

- GitHub: connector-aruba-clearpass
- Category: Network Security
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_guests` | Get List of Guests | investigation | ✓ | — |
| `get_guest_details` | Get Guest Details | investigation | ✓ | `guest_id`(Guest ID, REQ) |
| `list_endpoints` | List Endpoint | investigation | ✓ | — |
| `get_endpoint_details` | Get Endpoint Detail | investigation | ✓ | `endpoint_id`(Endpoint ID, REQ) |
| `update_endpoint_status` | Update Endpoint Status | investigation | ✓ | `endpoint_id`(Endpoint ID, REQ), `endpoint_status`(Endpoint Status, REQ), `description`(Description) |
| `list_sessions` | List Sessions | investigation | ✓ | `filter`(Filter) |
| `terminate_session` | Terminate Sessions | investigation | ✓ | `session_id`(Session ID, REQ) |
| `disable_device` | Disable Device | remediation | ✓ | `mac_address`(MAC Address) |
| `session_coa_mac` | Send Session COA by MAC | remediation | ✓ | `mac_address`(MAC Address), `coa_profile`(COA Profile) |
| `get_device_profile` | Get Device Profile | investigation | ✓ | `mac_or_ip`(MAC Address /IP Address) |
| `get_endpoint_details_by_macaddress` | Get Endpoint Details by MAC Address | investigation | ✗ | `mac_address`(MAC Address, REQ) |
| `block_endpoint` | Block Endpoint | containment | ✗ | `mac_adress`(MAC Address, REQ) |
| `execute_api_request` | Execute an API Request | investigation | ✓ | `endpoint`(Endpoint, REQ), `method`(Method, REQ), `query_params`(Query Parameters), `payload`(Payload) |

### `atlassian-confluence-cloud`

version 1.0.0 — Atlassian Confluence is a collaborative workspace where teams create, organize, and share project documents, ideas, and knowledge in one cen…

- GitHub: connector-atlassian-confluence-cloud
- Category: Utilities
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_space` | Create Space | investigation | ✓ | `name`(Name, REQ), `alias`(Alias), `key`(Key), `representation`(Representation), `value`(Value), `roleAssignments`(Role Assignments), `copySpaceAccessConfiguration`(Copy Space Access Configuration), `createPrivateSpace`(Create Private Space), `templateKey`(Template Key) |
| `get_spaces` | Get Spaces | investigation | ✓ | `ids`(Space IDs), `keys`(Space Keys), `type`(Type), `status`(Status), `labels`(Labels), `favorited-by`(Favorited By), `not-favorited-by`(Not Favorited By), `sort`(Sort), `description-format`(Description Format), `include-icon`(Include Icon), `limit`(Limit) |
| `get_specific_space_details` | Get Specific Spaces Details | investigation | ✓ | `id`(Space ID), `description-format`(Description Format), `include-icon`(Include Icon), `include-operations`(Include Operations), `include-properties`(Include Properties), `include-permissions`(Include Permissions), `include-role-assignments`(Include Role Assignments), `include-labels`(Include Labels) |
| `create_custom_content` | Create Custom Content | investigation | ✓ | `type`(Content Type, REQ), `title`(Title, REQ), `representation`(Representation, REQ), `value`(Body, REQ), `status`(Status), `spaceId`(Space ID), `pageId`(Page ID), `blogPostId`(Blog Post ID), `customContentId`(Custom Content ID) |
| `get_specific_custom_content` | Get Specific Custom Content | investigation | ✓ | `id`(Custom Content ID, REQ), `version`(Version), `body-format`(Body Format), `include-labels`(Include Labels), `include-properties`(Include Properties), `include-operations`(Include Operations), `include-version`(Include Version), `include-collaborators`(Include Collaborators) |
| `get_custom_contents` | Get Custom Contents | investigation | ✓ | `type`(Custom Content Type, REQ), `id`(Custom Content IDs), `space-id`(Space ID), `body-format`(Body Format), `sort`(Sort), `cursor`(Cursor), `limit`(Limit) |
| `update_custom_content` | Update Custom Content | investigation | ✓ | `id `(Custom Content ID), `type`(Custom Content Type, REQ), `title`(Title), `status`(Status), `representation`(Representation, REQ), `value`(Body, REQ), `number`(Version Number), `message`(Version Message), `spaceId`(Space ID), `pageId`(Page ID), `blogPostId`(Blog Post ID), `customContentId`(Custom Content ID) |
| `delete_custom_content` | Delete Custom Content | investigation | ✓ | `id`(Custom Content ID, REQ), `purge`(Purge) |
| `create_footer_comment` | Create Footer Comment | investigation | ✓ | `blogPostId`(Blog Post ID), `pageId`(Page ID), `parentCommentId`(Parent Comment ID), `attachmentId`(Attachment ID), `customContentId`(Custom Content ID), `representation`(Representation, REQ), `value`(Body, REQ) |
| `get_groups` | Get Groups | investigation | ✓ | `start`(Offset), `limit`(Limit), `accessType`(Access Type) |
| `get_users` | Get Users | investigation | ✓ | `accountId`(Account IDs, REQ), `expand`(Expand) |
| `get_audit_records` | Get Audit Records | investigation | ✓ | `startDate`(Start Date), `endDate`(End Date), `searchString`(Search String), `start`(Offset), `limit`(Limit) |
| `get_attachments` | Get Attachments | investigation | ✓ | `sort`(Sort), `cursor`(Cursor), `status`(Status), `mediaType`(Media Type), `filename`(File Name), `limit`(Limit) |

### `atlassian-confluence-server`

version 1.0.0 — Atlassian Confluence is a team workspace where knowledge and collaboration meet. Create, collaborate, and organize all your work in one plac…

- GitHub: connector-atlassian-confluence-server
- Category: IT Service Management
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_spaces_list` | Get Spaces List | investigation | ✓ | `type`(Type), `status`(Status), `limit`(Limit) |
| `create_space` | Create Space | investigation | ✓ | `key`(Key, REQ), `name`(Name, REQ), `description`(Description, REQ) |
| `get_content_list` | Get Content List | investigation | ✓ | `spaceKey`(Space Key, REQ), `title`(Page Title, REQ), `expand`(Properties to Expand), `limit`(Limit) |
| `create_content` | Create Content | investigation | ✓ | `type`(Content Type, REQ), `space`(Space Key, REQ), `title`(Title, REQ), `body`(Body, REQ) |
| `update_content` | Update Content | investigation | ✓ | `contentId`(Content ID, REQ), `version`(Version Number, REQ), `type`(Content Type, REQ), `space`(Space Key), `title`(Title), `body`(Body) |
| `delete_content` | Delete Content | investigation | ✓ | `contentId`(Content ID, REQ) |
| `get_content_list_using_cql` | Get Content List Using CQL | investigation | ✓ | `cql`(CQL, REQ), `cqlcontext`(CQL Context), `expand`(Properties to Expand), `limit`(Limit) |

### `atlassian-iam`

version 1.0.0 — Integrate with Atlassian's services to execute CRUD operations for employee lifecycle processes.

- GitHub: connector-atlassian-iam
- Category: Data Enrichment and Threat Intelligence
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_user` | Create User | investigation | ✓ | `userName`(Username), `emails`(Email Address), `title`(Title), `department`(Department), `organization`(Organization), `active`(Active), `custom_filter`(Custom Filter) |
| `get_users` | Get Users | investigation | ✓ | — |
| `update_user` | Update User | investigation | ✓ | `userId`(User ID, REQ), `userName`(Username), `emails`(Email Address), `title`(Title), `department`(Department), `organization`(Organization), `custom_filter`(Custom Filter) |
| `deactivate_user` | Deactivate User | investigation | ✓ | `userId`(User ID, REQ) |

### `atlassian-status-page`

version 1.0.0 — This connector enables automated operations such as creating incidents, retrieving incident lists, managing active maintenances, and more.

- GitHub: connector-atlassian-status-page
- Category: Monitoring
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_incident` | Create Incident | investigation | ✓ | `page_id`(Page ID, REQ), `name`(Name, REQ), `status`(Status), `impact_override`(Impact Override), `body`(Comment), `deliver_notifications`(Deliver Notifications), `components`(Components), `component_ids`(Component IDs), `metadata`(Meta Data), `additional_fields`(Additional Fields) |
| `get_incident` | Get Incident | investigation | ✓ | `page_id`(Page ID, REQ), `incident_id`(Incident ID, REQ) |
| `update_incident` | Update Incident | investigation | ✓ | `page_id`(Page ID, REQ), `incident_id`(Incident ID, REQ), `name`(Name), `status`(Status), `impact_override`(Impact Override), `body`(Comment), `deliver_notifications`(Deliver Notifications), `components`(Components), `component_ids`(Component IDs), `metadata`(Meta Data), `additional_fields`(Additional Fields) |
| `delete_incident` | Delete Incident | investigation | ✓ | `page_id`(Page ID, REQ), `incident_id`(Incident ID, REQ) |
| `get_list_status_pages` | Get Status Pages | investigation | ✓ | — |
| `get_list_incidents` | Get Incident List | investigation | ✓ | `page_id`(Page ID, REQ), `q`(Query), `limit`(Limit), `page`(Offset) |
| `get_active_maintenance` | Get Active Maintenance Incidents | investigation | ✓ | `page_id`(Page ID, REQ), `per_page`(Limit), `page`(Offset) |
| `get_upcoming_incidents` | Get Upcoming Incidents | investigation | ✓ | `page_id`(Page ID, REQ), `per_page`(Limit), `page`(Offset) |
| `get_scheduled_incidents` | Get Scheduled Incidents | investigation | ✓ | `page_id`(Page ID, REQ), `per_page`(Limit), `page`(Offset) |
| `get_unresolved_incidents` | Get Unresolved Incidents | investigation | ✓ | `page_id`(Page ID, REQ), `per_page`(Limit), `page`(Offset) |
| `execute_api_request` | Execute an API Request | utilities | ✓ | `endpoint`(Endpoint, REQ), `method`(Method, REQ), `query_params`(Query Parameters), `payload`(Request Body/Payload) |

### `aws-access-analyzer`

version 1.1.0 — AWS Access Analyzer helps you identify the resources in your organization and accounts, such as Amazon S3 buckets or IAM roles, shared with …

- GitHub: connector-aws-access-analyzer
- Category: Identity and Access Management
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_analyzers` | List Analyzers | investigation | ✓ | `assume_role`(Assume a Role), `type`(Analyzer Type, REQ), `size`(Max Result Size, REQ), `next_token`(Next Page Token) |
| `get_analyzers` | Get analyzer details | investigation | ✓ | `assume_role`(Assume a Role), `analyzer_name`(Analyzer Name, REQ) |
| `list_analyzed_resources` | List of Analyzed Resources | investigation | ✓ | `assume_role`(Assume a Role), `analyzer_arn`(Analyzer ARN, REQ), `resource_type`(Resource Type), `size`(Max Result Size), `next_token`(Next Page Token) |
| `get_analyzed_resources` | Details of an Analyzed Resources | investigation | ✓ | `assume_role`(Assume a Role), `analyzer_arn`(Analyzer ARN, REQ), `resource_arn`(Resource ARN, REQ) |
| `list_findings` | List of Findings | investigation | ✓ | `assume_role`(Assume a Role), `analyzer_arn`(Analyzer ARN, REQ), `size`(Max Result Size), `filter`(Filter Query), `sort`(Sort Parameter), `next_token`(Next Page Token) |
| `get_findings` | Get Finding Details | investigation | ✓ | `assume_role`(Assume a Role), `analyzer_arn`(Analyzer ARN, REQ), `id`(ID, REQ) |
| `start_resource_scan` | Start Resource Scan | investigation | ✓ | `assume_role`(Assume a Role), `analyzer_arn`(Analyzer ARN, REQ), `resource_arn`(Resource ARN, REQ) |
| `update_findings` | Update Findings Status | investigation | ✓ | `assume_role`(Assume a Role), `analyzer_arn`(Analyzer ARN, REQ), `update_by`(Update By, REQ), `status`(Status, REQ), `client_token`(Client Token) |

### `aws-cloudwatch-log`

version 1.0.0 — AWS CloudWatch Log helps you monitor, store, and access your system, application, and custom log files. This connector facilitates the autom…

- GitHub: connector-aws-cloudwatch-log
- Category: Monitoring
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_log_group` | Create Log Group | miscellaneous | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ), `kmsKeyId`(KMS Key ARN), `tags`(Tags) |
| `create_log_stream` | Create Log Stream | miscellaneous | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ), `logStreamName`(Log Stream Name, REQ) |
| `get_list_log_groups` | Get Log Groups List | investigation | ✓ | `assume_role`(Assume a Role), `logGroupNamePrefix`(Log Group Name Prefix), `nextToken`(Next Page Token), `limit`(Limit) |
| `get_list_log_streams` | Get Log Streams List | investigation | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ), `orderBy`(Order By), `nextToken`(Next Page Token), `limit`(Limit) |
| `get_log_events` | Get Log Events | investigation | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ), `logStreamName`(Log Stream Name, REQ), `startTime`(Start Time), `endTime`(End Time), `nextToken`(Next Page Token), `limit`(Limit), `startFromHead`(Oldest Logs First) |
| `delete_log_group` | Delete Log Group | miscellaneous | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ) |
| `delete_log_stream` | Delete Log Stream | miscellaneous | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ), `logStreamName`(Log Stream Name, REQ) |
| `update_log_retention_policy` | Update Log Retention Policy | miscellaneous | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ), `retentionInDays`(Retention Period, REQ) |
| `revert_log_retention_policy` | Revert Log Retention Policy | miscellaneous | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ) |
| `upload_log_event` | Upload Log Event | miscellaneous | ✓ | `assume_role`(Assume a Role), `logGroupName`(Log Group Name, REQ), `logStreamName`(Log Stream Name, REQ), `timestamp`(Timestamp, REQ), `message`(Message, REQ), `sequenceToken`(Sequence Token) |
| `run_log_insight_query` | Run Log Insight Query | investigation | ✓ | `assume_role`(Assume a Role), `logGroupNames`(Log Group Names, REQ), `startTime`(Start Time, REQ), `endTime`(End Time, REQ), `queryString`(Query String, REQ), `limit`(Limit) |
| `get_log_insight_query_result` | Get Log Insight Query Result | investigation | ✓ | `assume_role`(Assume a Role), `queryId`(Log Insight Query ID, REQ) |
| `stop_log_insight_query` | Stop Log Insight Query | miscellaneous | ✓ | `assume_role`(Assume a Role), `queryId`(Log Insight Query ID, REQ) |

### `aws-commands`

version 1.1.0 — AWS Commands are used to run AWS native commands for AWS resources configurations directly from FortiSOAR.

- GitHub: connector-aws-commands
- Category: IT Services
- Operations: 34

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `generic_command` | Execute AWS Command | investigation | ✓ | `command`(Command, REQ), `optional_parameters`(Parameters) |
| `get_details_for_all_images` | Get AMIs Detail | investigation | ✓ | `assume_role`(Assume a Role), `image_ids`(Image IDs), `executable_users`(Executable Users), `owners`(Owners), `filters`(Filters) |
| `launch_instance` | Launch Instance | miscellaneous | ✓ | `assume_role`(Assume a Role), `image_id`(Image ID, REQ), `instance_type`(Instance Type, REQ), `maxcount`(Instance MaxCount, REQ), `mincount`(Instance MinCount, REQ), `subnetid`(SubNet ID), `device_name`(Device Name, REQ), `delete_on_termination`(Instance Delete on Termination, REQ), `security_groups_list`(Security Group IDs), `purpose`(Purpose For Launch Instance), `customer_name`(Customer Name), `terminate_by_date`(Terminate by Date) |
| `describe_instance` | Get Instance Details | investigation | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ) |
| `start_instance` | Start Instance | miscellaneous | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ), `description`(Purpose) |
| `stop_instance` | Stop Instance | miscellaneous | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ) |
| `reboot_instance` | Reboot Instance | miscellaneous | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ) |
| `add_tag_to_instance` | Add Instance Tag | miscellaneous | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ), `tag_key`(Tag Key, REQ), `tag_value`(Value, REQ) |
| `register_instance_to_elb` | Register Instance To ELB | miscellaneous | ✓ | `assume_role`(Assume a Role), `elb_name`(ELB Name, REQ), `instance_id`(Instance ID, REQ) |
| `deregister_instance_from_elb` | Deregister Instance from ELB | miscellaneous | ✓ | `assume_role`(Assume a Role), `elb_name`(ELB Name, REQ), `instance_id`(Instance ID, REQ) |
| `attach_instance_to_auto_scaling_group` | Attach Instance To Auto Scaling Group | miscellaneous | ✓ | `assume_role`(Assume a Role), `autoscaling_group_name`(Auto Scaling Group Name, REQ), `instance_id`(Instance IDs (In CSV or List Format), REQ) |
| `detach_instance_from_autoscaling_group` | Detach Instance From Auto Scaling Group | miscellaneous | ✓ | `assume_role`(Assume a Role), `autoscaling_group_name`(Auto Scaling Group Name (In CSV or List Format), REQ), `instance_id`(Instance IDs, REQ) |
| `instance_api_termination` | Instance API Termination  | — | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ), `operation`(Select Action, REQ) |
| `terminate_instance` | Terminate Instance | miscellaneous | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ) |
| `attach_volume` | Attach Volume | miscellaneous | ✓ | `assume_role`(Assume a Role), `volume_id`(Volume Id, REQ), `device_name`(Device Name, REQ), `instance_id`(Instance Id, REQ) |
| `snapshot_volume` | Capture Volume Snapshot | miscellaneous | ✓ | `assume_role`(Assume a Role), `volume_id`(Volume ID, REQ), `description`(Volume Description, REQ) |
| `detach_volume` | Detach Volume | remediation | ✓ | `assume_role`(Assume a Role), `volume_id`(Volume Id, REQ), `device_name`(Device Name, REQ), `instance_id`(Instance ID, REQ), `force`(Force To Detach, REQ) |
| `delete_volume` | Delete Volume | remediation | ✓ | `assume_role`(Assume a Role), `volume_id`(Volume ID, REQ) |
| `create_network_acl` | Create Network ACL | containment | ✓ | `assume_role`(Assume a Role), `vpc_id`(VPC ID, REQ) |
| `add_network_acl_rule` | Add Network ACL Rule | containment | ✓ | `assume_role`(Assume a Role), `network_acl_id`(Network ACL ID, REQ), `egress_rule`(Egress Rule, REQ), `ip_address`(IP Address, REQ), `rule_action`(Rule Action, REQ), `rule_number`(Rule Number, REQ) |
| `describe_network_acls` | Get Details of Network ACLs | investigation | ✓ | `assume_role`(Assume a Role), `network_acl_ids`(Network ACL IDs), `filters`(Filters) |
| `delete_network_acl_rule` | Delete Network ACL Rule | containment | ✓ | `assume_role`(Assume a Role), `network_acl_id`(Network ACL ID, REQ), `egress_rule`(Egress Rule, REQ), `rule_number`(Rule Number, REQ) |
| `delete_network_acl` | Delete Network ACL | containment | ✓ | `assume_role`(Assume a Role), `network_acl_id`(Network ACL ID, REQ) |
| `describe_user` | Get User Details | investigation | ✓ | `assume_role`(Assume a Role), `username`(Username, REQ) |
| `create_security_group` | Create Security Groups | containment | ✓ | `assume_role`(Assume a Role), `group_name`(Group Name, REQ), `description`(Description, REQ) |
| `get_security_groups` | Get Security Groups | investigation | ✓ | `assume_role`(Assume a Role) |
| `get_details_of_security_group` | Get Details of Security Group | investigation | ✓ | `assume_role`(Assume a Role), `security_group_id`(Security Group ID, REQ) |
| `add_security_group_to_instance` | Add Security Group To Instance | containment | ✓ | `assume_role`(Assume a Role), `instance_id`(Instance ID, REQ), `group_list`(Security Group Name or ID (In CSV or List Format), REQ) |
| `delete_security_group` | Delete Security Groups | remediation | ✓ | `assume_role`(Assume a Role), `security_group_id`(Security Group ID, REQ) |
| `authorize_ingress` | Authorize Ingress | containment | ✓ | `assume_role`(Assume a Role), `security_group_id`(Security Group ID, REQ), `ip_permissions`(IP Permissions, REQ) |
| `authorize_egress` | Authorize Egress | containment | ✓ | `assume_role`(Assume a Role), `security_group_id`(Security Group ID, REQ), `ip_permissions`(IP Permissions, REQ) |
| `revoke_egress` | Revoke Egress | containment | ✓ | `assume_role`(Assume a Role), `security_group_id`(Security Group ID, REQ), `ip_permissions`(IP Permissions, REQ) |
| `revoke_ingress` | Revoke Ingress | containment | ✓ | `assume_role`(Assume a Role), `security_group_id`(Security Group ID, REQ), `ip_permissions`(IP Permissions, REQ) |
| `revoke_all_active_sessions` | Revoke All Active Sessions | remediation | ✓ | `roleName`(Role Name, REQ) |

### `aws-dynamodb`

version 1.0.0 — AWS DynamoDB is a fully managed NoSQL database service that provides fast and predictable performance with seamless scalability. This connec…

- GitHub: connector-aws-dynamodb
- Category: Database
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_table` | Create Table | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ), `partitionKeyName`(Partition Key Name, REQ), `partitionKeyDataType`(Partition Key Data Type, REQ), `sortKey`(Sort Key (Optional)), `billingMode`(Billing Mode, REQ) |
| `delete_table` | Delete Table | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ) |
| `update_table` | Update Table | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ), `updateOperation`(Operation, REQ) |
| `get_table_list` | Get Table List | utilities | ✓ | `assume_role`(Assume a Role) |
| `get_table_details` | Get Table Details | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ) |
| `create_or_update_table_item` | Create or Update Table Item | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ), `partitionKeyName`(Partition Key Name, REQ), `partitionKeyDataType`(Partition Key Data Type, REQ), `partitionKeyValue`(Partition Key Value, REQ), `sortKey`(Sort Key (Optional)), `additionalAttributes`(Additional Attributes) |
| `delete_item` | Delete Table Item | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ), `partitionKeyName`(Partition Key Name, REQ), `partitionKeyDataType`(Partition Key Data Type, REQ), `partitionKeyValue`(Partition Key Value, REQ), `sortKey`(Sort Key) |
| `search_item` | Search Table Item | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ), `partitionKeyName`(Partition Key Name, REQ), `partitionKeyDataType`(Partition Key Data Type, REQ), `partitionKeyValue`(Partition Key Value, REQ), `sortKey`(Sort Key) |
| `list_table_items` | Get Table Items List | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ), `Select`(Select Attributes), `Limit`(Page Size) |
| `create_global_table` | Create Global Table | utilities | ✓ | `assume_role`(Assume a Role), `globalTableName`(Global Table Name, REQ), `regionName`(Region Name, REQ) |
| `get_global_table_details` | Get Global Table Details | utilities | ✓ | `assume_role`(Assume a Role), `globalTableName`(Global Table Name, REQ) |
| `get_global_table_list` | Get Global Table List | utilities | ✓ | `assume_role`(Assume a Role) |
| `create_backup` | Create Table Backup | utilities | ✓ | `assume_role`(Assume a Role), `TableName`(Table Name, REQ), `BackupName`(Backup Name, REQ) |
| `get_table_backup_details` | Get Table Backup Details | utilities | ✓ | `assume_role`(Assume a Role), `BackupArn`(Backup ARN, REQ) |
| `get_table_backup_list` | Get Table Backup List | utilities | ✓ | `assume_role`(Assume a Role) |
| `delete_table_backup` | Delete Table Backup | utilities | ✓ | `assume_role`(Assume a Role), `BackupArn`(Backup ARN, REQ) |

### `aws-feed`

version 1.0.0 — Amazon Web Services (AWS) publishes its current IP address ranges in JSON format. This connector facilitates automated operations to fetch t…

- GitHub: connector-aws-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `last_pull_time`(Modified After) |

### `aws-network-firewall`

version 1.0.0 — AWS Network Firewall is a managed service that makes it easy to deploy essential network protections for all of your Amazon Virtual Private …

- GitHub: connector-aws-network-firewall
- Category: AWS Service
- Operations: 20

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_associate_firewall_policy` | Get Associate Firewall Policy | investigation | ✓ | `assume_role`(Assume a Role), `FirewallPolicyArn`(Firewall Policy ARN, REQ), `FirewallArn`(Firewall ARN), `FirewallName`(Firewall Name), `UpdateToken`(Update Token) |
| `get_associate_subnets` | Get Associate Subnets | investigation | ✓ | `assume_role`(Assume a Role), `subnet_ids`(Subnet IDs, REQ), `FirewallArn`(Firewall ARN), `FirewallName`(Firewall Name), `UpdateToken`(Update Token) |
| `get_list_firewall_policies` | Get List Firewall Policies | investigation | ✓ | `assume_role`(Assume a Role), `MaxResults`(Limit), `NextToken`(Next Token) |
| `get_list_firewalls` | Get List Firewalls | investigation | ✓ | `assume_role`(Assume a Role), `MaxResults`(Limit), `NextToken`(Next Token), `VpcIds`(VPC IDs) |
| `get_list_rule_groups` | Get List Rule Groups | investigation | ✓ | `assume_role`(Assume a Role), `MaxResults`(Limit), `NextToken`(Next Token), `Scope`(Scope) |
| `get_list_tag_for_resource` | Get List Tag For Resource | investigation | ✓ | `assume_role`(Assume a Role), `ResourceArn`(Resource ARN, REQ), `MaxResults`(Limit), `NextToken`(Next Token) |
| `create_firewall` | Create Firewall | investigation | ✓ | `assume_role`(Assume a Role), `FirewallName`(Firewall Name, REQ), `FirewallPolicyArn`(Firewall Policy ARN, REQ), `Description`(Description), `DeleteProtection`(Delete Protection), `FirewallPolicyChangeProtection`(Firewall Policy Change Protection), `SubnetChangeProtection`(Subnet Change Protection), `SubnetMappings`(SubnetIDs, REQ), `VpcId`(VPC ID, REQ), `Tags`(Tags) |
| `create_firewall_policy` | Create Firewall Policy | miscellaneous | ✓ | `assume_role`(Assume a Role), `FirewallPolicyName`(Firewall Policy Name, REQ), `firewall_policy_json`(Firewall Policy, REQ), `Description`(Description), `Tags`(Tags) |
| `create_rule_group` | Create Rule Group | miscellaneous | ✓ | `assume_role`(Assume a Role), `rule_group_name`(Rule Group Name, REQ), `setting_type`(Setting Type, REQ), `type`(Type, REQ), `capacity`(Capacity, REQ), `description`(Description), `tags`(Tags) |
| `describe_firewall` | Describe Firewall | investigation | ✓ | `assume_role`(Assume a Role), `FirewallArn`(Firewall ARN), `FirewallName`(Firewall Name) |
| `describe_firewall_policy` | Describe Firewall Policy | investigation | ✓ | `assume_role`(Assume a Role), `FirewallPolicyArn`(Firewall Policy ARN), `FirewallPolicyName`(Firewall Policy Name) |
| `describe_logging_configuration` | Describe Logging Configuration | investigation | ✓ | `assume_role`(Assume a Role), `FirewallArn`(Firewall ARN), `FirewallName`(Firewall Name) |
| `describe_resource_policy` | Describe Resource Policy | investigation | ✓ | `assume_role`(Assume a Role), `ResourceArn`(Resource ARN, REQ) |
| `describe_rule_group` | Describe Rule Group | investigation | ✓ | `assume_role`(Assume a Role), `RuleGroupName`(Rule Group Name), `RuleGroupArn`(Rule Group ARN), `Type`(Type) |
| `delete_firewall` | Delete Firewall | miscellaneous | ✓ | `assume_role`(Assume a Role), `FirewallArn`(Amazon Resource Name (ARN)), `FirewallName`(Firewall Name) |
| `delete_firewall_policy` | Delete Firewall Policy | miscellaneous | ✓ | `assume_role`(Assume a Role), `FirewallPolicyArn`(Firewall Policy ARN), `FirewallPolicyName`(Firewall Policy Name) |
| `delete_resource_policy` | Delete Resource Policy | miscellaneous | ✓ | `assume_role`(Assume a Role), `ResourceArn`(Resource ARN, REQ) |
| `delete_rule_group` | Delete Rule Group | miscellaneous | ✓ | `assume_role`(Assume a Role), `RuleGroupArn`(Rule Group ARN), `RuleGroupName`(Rule Group Name), `Type`(Type) |
| `disassociate_subnets` | Disassociate Subnets | investigation | ✓ | `assume_role`(Assume a Role), `SubnetIds`(Subnet IDs, REQ), `FirewallArn`(Firewall ARN), `FirewallName`(Firewall Name), `UpdateToken`(Update Token) |
| `tag_resource` | Tag Resource | investigation | ✓ | `assume_role`(Assume a Role), `ResourceArn`(Resource ARN, REQ), `Tags`(Tags, REQ), `NextToken`(Next Token) |

### `aws-sagemaker`

version 1.1.0 — AWS SageMaker helps data scientists and developers to prepare, build, train, and deploy high-quality machine learning (ML) models quickly by…

- GitHub: connector-aws-sagemaker
- Category: AWS Service
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_actions` | Get Actions | investigation | ✓ | `assume_role`(Assume a Role), `SourceUri`(Source URI), `ActionType`(Action Type), `CreatedAfter`(Created After), `CreatedBefore`(Created Before), `SortBy`(Sort By), `SortOrder`(Sort Order), `NextToken`(Next Token), `MaxResults`(Max Results) |
| `get_algorithms` | Get Algorithms | investigation | ✓ | `assume_role`(Assume a Role), `CreationTimeAfter`(Creation Time After), `CreationTimeBefore`(Creation Time Before), `NameContains`(Name Contains), `SortBy`(Sort By), `SortOrder`(Sort Order), `MaxResults`(Max Results), `NextToken`(Next Token) |
| `get_apps` | Get Applications | investigation | ✓ | `assume_role`(Assume a Role), `MaxResults`(Max Results), `SortOrder`(Sort Order), `SortBy`(Sort By), `DomainIdEquals`(Domain ID Equals), `UserProfileNameEquals`(User Profile Name Equals), `NextToken`(Next Token) |
| `get_artifacts` | Get Artifacts | investigation | ✓ | `assume_role`(Assume a Role), `SourceUri`(Source URI), `ArtifactType`(Artifact Type), `CreatedAfter`(Created After), `CreatedBefore`(Created Before), `SortBy`(Sort By), `SortOrder`(Sort Order), `NextToken`(Next Token), `MaxResults`(Max Results) |

### `aws-waf`

version 1.0.0 — AWS WAF is a web application firewall that lets you monitor and manage web requests that are forwarded to protected AWS resources.

- GitHub: connector-aws-waf
- Category: DevOps
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_ip_set` | Create IP Set | investigation | ✓ | `Name`(Name, REQ), `IPAddressVersion`(IP Address Version, REQ), `Addresses`(IP Addresses), `Description`(Description), `Tags`(Tags) |
| `update_ip_set` | Update IP Set | investigation | ✓ | `Name`(Name, REQ), `Id`(ID, REQ), `LockToken`(Lock Token, REQ), `AddressesToAdd`(IP Addresses To Add), `AddressesToRemove`(IP Addresses To Remove), `Description`(Description) |
| `list_ip_set` | List IP Set | investigation | ✓ | `Limit`(Limit), `NextMarker`(Next Marker) |
| `get_ip_set` | Get IP Set | investigation | ✓ | `Name`(Name, REQ), `Id`(ID, REQ) |
| `delete_ip_set` | Delete IP Set | investigation | ✓ | `Name`(Name, REQ), `Id`(ID, REQ), `LockToken`(Lock Token, REQ) |

### `aws-waf-classic`

version 1.0.0 — AWS WAF Classic is a web application firewall that lets you monitor and manage web requests that are forwarded to protected AWS resources.

- GitHub: connector-aws-waf-classic
- Category: DevOps
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_ip_set` | Create IP Set | investigation | ✓ | `Name`(Name, REQ), `ChangeToken`(Change Token, REQ) |
| `update_ip_set` | Update IP Set | investigation | ✓ | `IPSetId`(IP Set ID, REQ), `ChangeToken`(Change Token, REQ), `Updates`(IP Addresses, REQ) |
| `list_ip_set` | List IP Sets | investigation | ✓ | `Limit`(Limit), `NextMarker`(Next Marker) |
| `get_ip_set` | Get IP Set | investigation | ✓ | `IPSetId`(IP Set ID, REQ) |
| `delete_ip_set` | Delete IP Set | investigation | ✓ | `ChangeToken`(Change Token, REQ), `IPSetId`(IP Set ID, REQ) |
| `get_change_token` | Get Change Token | investigation | ✓ | — |

### `azure-active-directory`

version 2.2.1 — Microsoft Entra ID, formerly known as Azure Active Directory (Azure AD), is a cloud-based identity and access management (IAM) service that …

- GitHub: connector-azure-active-directory
- Category: Identity and Access Management
- Operations: 24

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_user_membership` | Get User Membership | enrichment | ✓ | `user_id`(User ID, REQ), `membership_type`(Membership Type, REQ) |
| `get_people` | Get People | enrichment | ✓ | `user_id`(User ID, REQ), `$filter`(Filter Query), `$select`(Select Query), `$top`(Number Of Records To Fetch), `$skip`(Offset) |
| `get_managers` | Get Managers | enrichment | ✓ | `user_id`(User ID, REQ) |
| `revoke_sign_in_sessions` | Revoke SignIn Sessions | response | ✓ | `user_id`(User ID, REQ) |
| `list_direct_reports` | List Direct Reports | investigation | ✓ | `user_id`(User ID, REQ) |
| `list_devices` | List Devices | investigation | ✓ | `$filter`(Filter Query), `$select`(Select Query), `$top`(Number Of Records To Fetch), `get_all_pages`(Get All Pages), `$skipToken`(Skip Token) |
| `get_registered_owners` | List Registered Owners | investigation | ✓ | `device_id`(Device ID, REQ) |
| `get_registered_users` | List Registered Users | investigation | ✓ | `device_id`(Device ID, REQ) |
| `list_user_owned_devices` | List User Owned Devices | enrichment | ✓ | `user_id`(User ID, REQ) |
| `list_user_owned_objects` | List User Owned Objects | enrichment | ✓ | `user_id`(User ID, REQ) |
| `list_groups` | List Groups | investigation  | ✓ | `$filter`(Filter Query), `$select`(Select Query), `$top`(Number Of Groups To Fetch), `get_all_pages`(Get All Pages), `$skipToken`(Skip Token) |
| `list_group_members` | List Group Members | investigation  | ✓ | `id`(Group ID, REQ), `$filter`(Filter Query), `$select`(Select Query), `$top`(Number Of Group Members To Fetch), `get_all_pages`(Get All Pages), `$skipToken`(Skip Token) |
| `get_group_details` | Get Group Details | investigation  | ✓ | `id`(Group ID, REQ) |
| `remove_member` | Remove Member | investigation  | ✓ | `id`(Group ID, REQ), `dir_object_id`(User ID, REQ) |
| `add_member` | Add Member | investigation  | ✓ | `id`(Group ID, REQ), `dir_object_id`(User ID, REQ) |
| `list_sign_ins` | List SignIns Events | investigation  | ✓ | `$filter`(Filter Query), `$top`(Number of Events to Fetch), `get_all_pages`(Get All Pages), `$skipToken`(Skip Token) |
| `list_users` | List Users | investigation  | ✓ | `$filter`(Filter Query), `$select`(Select Query), `$top`(Number Of Users To Fetch), `get_all_pages`(Get All Pages), `$skipToken`(Skip Token) |
| `get_user_details` | Get User Details | investigation | ✓ | `based_on`(Based On, REQ), `additional_info`(Provide Additional Details) |
| `add_user` | Add User | investigation | ✓ | `displayName`(Display Name, REQ), `mailNickname`(Mail Nick Name, REQ), `userPrincipalName`(User Principal Name, REQ), `password`(Password, REQ), `force_change`(Force Change Password Next Login), `accountEnabled`(Account Enabled), `additional_fields`(Additional Fields) |
| `enable_user` | Enable User | containment | ✓ | `based_on`(Based On, REQ) |
| `disable_user` | Disable User | containment | ✓ | `based_on`(Based On, REQ) |
| `delete_user` | Delete User | investigation | ✓ | `based_on`(Based On, REQ) |
| `reset_password` | Reset Password | containment | ✓ | `based_on`(Based On, REQ), `password`(Password, REQ), `force_change`(Force Change Password Next Login) |
| `rest_api_call` | Generic REST API Call | investigation | ✓ | `endpoint`(API Endpoint, REQ), `method`(HTTP method), `params`(Query params), `body`(Request Payload) |

### `azure-blob-storage`

version 1.1.0 — Azure Blob Storage is Microsoft's object storage solution for the cloud. Blob Storage is optimized for storing massive amounts of unstructur…

- GitHub: connector-azure-blob-storage
- Category: IT Services
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_blob` | List Blobs | investigation | ✓ | `container_name`(Container Name) |
| `create_blob` | Create Blob | investigation | ✓ | `container_name`(Container Name), `blob_name`(Blob Name, REQ), `input`(Type, REQ), `timeout`(Timeout) |
| `get_blob` | Get Blob | investigation | ✓ | `container_name`(Container Name), `blob_name`(Blob Name, REQ) |
| `copy_blob` | Copy Blob | investigation | ✓ | `source_container_name`(Source Container Name, REQ), `blob_name`(Blob Name, REQ), `destination_container_name`(Destination Container Name, REQ) |
| `delete_blob` | Delete Blob | investigation | ✓ | `container_name`(Container Name), `blob_name`(Blob Name, REQ) |
| `abort_copy_blob` | Abort Copy Blob | investigation | ✓ | `container_name`(Container Name), `blob_name`(Blob Name, REQ), `copy_id`(Copy Blob ID, REQ) |
| `get_blob_properties` | Get Blob Properties | investigation | ✓ | `container_name`(Container Name), `blob_name`(Blob Name, REQ) |
| `get_blob_metadata` | Get Blob Metadata | investigation | ✓ | `container_name`(Container Name), `blob_name`(Blob Name, REQ) |
| `get_blob_tags` | Get Blob Tags | investigation | ✓ | `container_name`(Container Name), `blob_name`(Blob Name, REQ) |

### `azure-commands`

version 1.0.1 — Azure Commands are used to run Azure native commands for Azure resources configurations directly from FortiSOAR.

- GitHub: connector-azure-commands
- Category: Asset Management
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `generic_command` | Execute Azure Command | investigation | ✓ | `command`(Command, REQ), `optional_parameters`(Parameters) |
| `list_vm` | Get Virtual Machines List | investigation | ✓ | `resource_group`(Resource Group), `optional_parameters`(Optional Parameters) |
| `get_vm` | Get Virtual Machine | investigation | ✓ | `input`(Filter by, REQ), `optional_parameters`(Optional Parameters) |
| `delete_vm` | Delete Virtual Machine | investigation | ✓ | `input`(Filter by, REQ), `optional_parameters`(Optional Parameters) |
| `list_resource` | Get Resources List | investigation | ✓ | `location`(Location), `optional_parameters`(Optional Parameters) |
| `get_resource` | Get Resource | investigation | ✓ | `input`(Filter by, REQ), `optional_parameters`(Optional Parameters) |
| `delete_resource` | Delete Resource | investigation | ✓ | `input`(Filter by, REQ), `optional_parameters`(Optional Parameters) |
| `list_webapp` | Get Webapp List | investigation | ✓ | `resource_group`(Resource Group), `optional_parameters`(Optional Parameters) |
| `list_ssh_keys` | Get SSH Keys List | investigation | ✓ | `resource_group`(Resource Group), `optional_parameters`(Optional Parameters) |
| `list_storage_fs_directory` | Get Storage FS Directory List | investigation | ✓ | `file_system`(Container Name, REQ), `optional_parameters`(Optional Parameters) |

### `azure-cosmos-db`

version 1.0.0 — Azure Cosmos DB is a globally distributed, multi-model database service offered by Microsoft. It is designed to provide high availability, s…

- GitHub: connector-azure-cosmos-db
- Category: Database
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `insert_document` | Insert Document | investigation | ✓ | `document_details`(Document Details, REQ), `collection_name`(Container Name, REQ), `database_name`(Database Name) |
| `query_document` | Query Document | investigation | ✓ | `query`(Azure Cosmos Query, REQ), `collection_name`(Container Name, REQ), `database_name`(Database Name) |
| `update_document` | Update Document | investigation | ✓ | `doc_id`(Document ID, REQ), `document_details`(Document Details, REQ), `collection_name`(Container Name, REQ), `database_name`(Database Name) |
| `delete_document` | Delete Document | investigation | ✓ | `doc_id`(Document ID, REQ), `partition_key`(Partition Value, REQ), `collection_name`(Container Name, REQ), `database_name`(Database Name) |
| `get_collections` | Get Containers | investigation | ✓ | `database_name`(Database Name) |
| `get_database_properties` | Get Database Properties | investigation | ✓ | `database_name`(Database Name) |

### `azure-devops`

version 2.0.0 — Azure DevOps is a cloud-based service for managing software development projects. The Azure DevOps FortiSOAR connector integrates with Azure…

- GitHub: connector-azure-devops
- Category: Source Code Management
- Operations: 30

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_pipelines` | Get Pipeline List | investigation | ✓ | `project`(Project Name, REQ), `field`(Sort Field), `order`(Sort Order), `continuationToken`(Continuation Token), `$top`(Limit) |
| `list_pipeline_runs` | Get Pipeline Run List | investigation | ✓ | `project`(Project Name, REQ), `pipelineId`(Pipeline ID, REQ) |
| `get_pipeline_run` | Get Pipeline Run Details | investigation | ✓ | `project`(Project Name, REQ), `pipelineId`(Pipeline ID, REQ), `runId`(Run ID, REQ) |
| `list_projects` | Get Project List | investigation | ✓ | `stateFilter`(State), `continuationToken`(Continuation Token), `$skip`(Offset), `$top`(Limit) |
| `list_repositories` | Get Repository List | investigation | ✓ | `project`(Project Name, REQ), `includeHidden`(Include Hidden Repositories), `includeAllUrls`(Include All URLs), `includeLinks`(Include Reference Links) |
| `list_branches` | Get Branch List | investigation | ✓ | `project`(Project Name, REQ), `repository`(Repository, REQ), `filterContains`(Branch Name Filter (Contains)), `filter`(Branch Name Filter (Starts With)), `includeMyBranches`(Include My Branches), `includeStatuses`(Include Statuses), `includeLinks`(Include Links), `latestStatusesOnly`(Latest Statuses Only), `peelTags`(Peel Tags), `continuationToken`(Continuation Token), `$top`(Limit) |
| `get_commit` | Get Commit Details | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `commitId`(Commit ID, REQ), `changeCount`(Change Count) |
| `list_pull_requests` | Get Pull Request List | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `searchCriteria.status`(Status), `searchCriteria`(Search Criteria), `$skip`(Offset), `$top`(Limit) |
| `get_pull_requests_by_id` | Get Pull Request Details | investigation | ✓ | `project`(Project Name, REQ), `pullRequestId`(Pull Request ID, REQ) |
| `create_pull_request` | Create Pull Request | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `title`(Pull Request Title, REQ), `sourceRefName`(Source Branch Name, REQ), `targetRefName`(Target Branch Name, REQ), `description`(Pull Request Description), `reviewers`(Reviewers), `supportsIterations`(Supports Iterations), `additional_input`(Additional Inputs) |
| `update_pull_request` | Update Pull Request | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `pullRequestId`(Pull Request ID, REQ), `title`(Pull Request Title), `description`(Pull Request Description), `status`(Pull Request Status), `targetRefName`(Target Branch Name), `additional_input`(Additional Inputs) |
| `list_pull_request_reviewers` | Get Pull Request Reviewer List | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `pullRequestId`(Pull Request ID, REQ) |
| `add_pull_request_reviewer` | Add Pull Request Reviewer | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `pullRequestId`(Pull Request ID, REQ), `reviewerId`(Reviewer, REQ), `isRequired`(Required Reviewer) |
| `list_pull_request_commits` | Get Pull Request Commit List | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `pullRequestId`(Pull Request ID, REQ), `$top`(Limit), `continuationToken`(Continuation Token) |
| `list_commits` | Get Commit List | investigation | ✓ | `project`(Project Name, REQ), `repositoryId`(Repository, REQ), `type`(Search Options) |
| `run_pipeline` | Run Pipeline | investigation | ✓ | `project`(Project Name, REQ), `pipelineId`(Pipeline ID, REQ), `stagesToSkip`(Stages to Skip), `pipelineVersion`(Pipeline Version), `previewRun`(Preview Run), `resources`(Resources) |
| `create_repository` | Create Repository | investigation | ✓ | `project`(Project ID, REQ), `repository`(Repository Name, REQ), `parentRepository`(Parent Repository ID), `sourceRef`(Source Ref) |
| `update_repository` | Update Repository | investigation | ✓ | `repositoryId`(Repository ID, REQ), `name`(Repository Name), `defaultBranch`(Default Branch), `isDisabled`(Disable Repository) |
| `push_repository` | Push Changes | investigation | ✓ | `project`(Project, REQ), `repositoryId`(Repository ID, REQ), `branch`(Branch Name, REQ), `previousCommitSha`(Previous Commit ID, REQ), `commit_message`(Commit Message, REQ), `clone_path`(Cloned Repository Path, REQ) |
| `create_branch` | Create Branch | investigation | ✓ | `project`(Project, REQ), `repositoryId`(Repository ID, REQ), `branch`(Branch Name, REQ), `commit_message`(Commit Message, REQ), `previousCommitSha`(Previous Commit ID) |
| `delete_branch` | Delete Branch | investigation | ✓ | `project`(Project, REQ), `repositoryId`(Repository, REQ), `branch`(Branch Name, REQ), `previousCommitSha`(Previous Commit ID, REQ) |
| `create_pull_request_comment` | Create Pull Request Comment | investigation | ✓ | `repositoryId`(Repository ID, REQ), `pullRequestId`(Pull Request ID, REQ), `content`(Content, REQ), `threadId`(Thread ID), `parentCommentId`(Parent Comment ID) |
| `list_pull_request_comment` | Get Pull Request Comment List | investigation | ✓ | `repositoryId`(Repository ID, REQ), `pullRequestId`(Pull Request ID, REQ), `threadId`(Thread ID) |
| `list_users` | Get User List | investigation | ✓ | `scopeDescriptor`(Scope), `continuationToken`(Continuation Token), `subjectTypes`(Subject Subtypes) |
| `get_file_from_repository` | Get File | investigation | ✓ | `repositoryId`(Repository, REQ), `versionDescriptor.version`(Branch Name, REQ), `path`(File Path, REQ), `includeContent`(Include Content), `includeContentMetadata`(Include Content Metadata) |
| `create_merge_request` | Create Merge Request | investigation | ✓ | `project`(Project, REQ), `repositoryNameOrId`(Repository, REQ), `parents`(Parent Commit ID, REQ), `comment`(Comment, REQ) |
| `create_new_file_in_repository` | Create File | investigation | ✓ | `project`(Project, REQ), `repo_name`(Repository, REQ), `branch`(Branch Name, REQ), `previousCommitSha`(Previous Commit ID, REQ), `file_path`(File Path, REQ), `content`(Content, REQ), `commit_message`(Commit Message, REQ) |
| `update_file_in_repository` | Update File | investigation | ✓ | `project`(Project, REQ), `repo_name`(Repository, REQ), `branch`(Branch Name, REQ), `previousCommitSha`(Previous Commit ID, REQ), `file_path`(File Path, REQ), `content`(Content, REQ), `operation`(Operation, REQ), `commit_message`(Commit Message, REQ) |
| `delete_existing_file_in_repository` | Delete File | investigation | ✓ | `project`(Project, REQ), `repo_name`(Repository, REQ), `branch`(Branch Name, REQ), `previousCommitSha`(Previous Commit ID, REQ), `file_path`(File Path, REQ), `commit_message`(Commit Message, REQ) |
| `execute_an_api_request` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `azure-front-door-waf`

version 1.0.0 — Azure Front Door Service enables you to define, manage, and monitor the global routing for your web traffic by optimizing for best performan…

- GitHub: connector-azure-front-door-waf
- Category: Firewall and Network Protection
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_or_update_policy` | Create or Update Policy | investigation | ✓ | `policyName`(Policy Name, REQ), `location`(Location, REQ), `customRules`(Custom Rules), `managedRules`(Managed Rules), `policySettings`(Policy Settings), `sku`(Sku), `tags`(Tags) |
| `get_policy_details` | Get Policy Details | investigation | ✓ | `policyName`(Policy Name, REQ) |
| `get_policies_list` | Get Policies List | investigation | ✓ | — |
| `delete_policy` | Delete Policy | investigation | ✓ | `policyName`(Policy Name, REQ) |
| `block_ip` | Block IP | containment | ✓ | `policyName`(Policy Name, REQ), `location`(Location, REQ), `rule_name`(Rule Name, REQ), `rule_priority`(Rule Priority, REQ), `ip_address`(IP Address, REQ), `sku`(Sku) |
| `unblock_ip` | Unblock IP | remediation | ✓ | `policyName`(Policy Name, REQ), `rule_name`(Rule Name, REQ), `ip_address`(IP Address, REQ) |

### `azure-key-vault`

version 2.0.0 — Azure Key Vault is a cloud based key management and security service that enables in securing cryptographic keys, password and other secret …

- GitHub: connector-azure-key-vault
- Category: Identity and Access Management
- Operations: 18

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_key_vault` | List Key Vaults | investigation | ✓ | `skip_token`(Skip Token), `size`(Size) |
| `get_key_vault` | Get Key Vault | investigation | ✓ | `vault_name`(Vault Name, REQ), `resource_group_name`(Resource Group Name, REQ) |
| `delete_key_vault` | Delete Key Vault | investigation | ✓ | `vault_name`(Vault Name, REQ), `resource_group_name`(Resource Group Name, REQ) |
| `update_vault_access_policy` | Update Vault's Access Policies | investigation | ✓ | `vault_name`(Vault Name, REQ), `resource_group_name`(Resource Group Name, REQ), `operation_kind`(Operation, REQ), `accessPolicies`(Policies, REQ) |
| `list_keys` | Get All Keys | investigation | ✓ | `vault_name`(Vault Name, REQ), `skip_token`(Skip Token), `size`(Size) |
| `get_key` | Get Key Details | investigation | ✓ | `vault_name`(Vault Name, REQ), `key_name`(Key Name, REQ), `key-version`(Key Version) |
| `delete_key` | Delete Key | investigation | ✓ | `vault_name`(Vault Name, REQ), `key_name`(Key Name, REQ) |
| `list_secret` | Get All Secrets | investigation | ✓ | `vault_name`(Vault Name, REQ), `size`(Size), `skip_token`(Skip Token) |
| `get_secret` | Get Secret Details | investigation | ✓ | `vault_name`(Vault Name, REQ), `secret_name`(Secret Name, REQ), `secret_version`(Secret Version) |
| `delete_secret` | Delete Secret | investigation | ✓ | `vault_name`(Vault Name, REQ), `secret_name`(Secret Name, REQ) |
| `list_certificate` | Get All Certificates | investigation | ✓ | `vault_name`(Vault Name, REQ), `includePending`(Include Pending), `skip_token`(Skip Token), `size`(Size) |
| `get_certificate` | Get Certificate Details | investigation | ✓ | `vault_name`(Vault Name, REQ), `certificate_name`(Certificate Name, REQ), `certificate-version`(Certificate Version) |
| `delete_certificate` | Delete Certificate | investigation | ✓ | `vault_name`(Vault Name, REQ), `certificate_name`(Certificate Name, REQ) |
| `get_certificate_policy` | Get Certificate Policy | investigation | ✓ | `vault_name`(Vault Name, REQ), `certificate_name`(Certificate Name, REQ) |
| `get_versions` | Get Versions | investigation | ✓ | `vault_name`(Vault Name, REQ), `object`(Object Name, REQ), `skip_token`(Skip Token), `size`(Size) |
| `get_credentials` | Get Credentials | investigation | ✓ | — |
| `get_credentials_details` | Get Credentials Details | investigation | ✓ | `secret_id`(Secret Name, REQ) |
| `get_credential` | Get Credential | investigation | ✓ | `secret_id`(Secret Name, REQ) |

### `azure-kubernetes-services`

version 1.0.0 — Deploy and manage containerized applications with a fully managed Kubernetes. This connector facilitates the automated operations related to…

- GitHub: connector-azure-kubernetes-services
- Category: IT Services
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_managed_cluster` | Create Managed Cluster | investigation | ✓ | `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `resourceName`(Resource Name, REQ), `location`(Resource Location, REQ), `additional_fields`(Additional Fields) |
| `get_managed_clusters_list` | Get Managed Clusters List | investigation  | ✓ | `subscriptionId`(Workspace Subscription ID, REQ) |
| `get_managed_cluster` | Get Managed Cluster | investigation | ✓ | `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `resourceName`(Resource Name, REQ) |
| `update_managed_cluster` | Update Managed Cluster | investigation | ✓ | `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `resourceName`(Resource Name, REQ), `location`(Resource Location, REQ), `additional_fields`(Additional Fields) |
| `delete_managed_cluster` | Delete Managed Cluster | investigation | ✓ | `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `resourceName`(Resource Name, REQ) |
| `managed_cluster_actions` | Managed Cluster Actions | investigation | ✓ | `action`(Action to Process the cluster, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `resourceName`(Resource Name, REQ) |
| `run_command` | Run Command | investigation | ✓ | `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `resourceName`(Resource Name, REQ), `command`(Command, REQ), `additional_fields`(Additional Fields) |
| `get_command_details` | Get Command Details | investigation | ✓ | `commandId`(Command ID, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `resourceName`(Resource Name, REQ) |

### `azure-log-analytics`

version 2.0.1 — Log Analytics is a tool in the Azure portal that's used to edit and run log queries against data in the Azure Monitor Logs store. This conne…

- GitHub: connector-azure-log-analytics
- Category: Analytics and SIEM
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `execute_query` | Execute Query | investigation  | ✓ | `workspace_id`(Workspace ID, REQ), `query`(Query, REQ), `timespan`(TimeSpan), `workspace_name`(Workspace Name) |
| `create_saved_searches` | Create Saved Searches | investigation | ✓ | `savedSearchId`(Saved Search ID, REQ), `workspace_name`(Workspace Name, REQ), `category`(Category, REQ), `displayName`(Display Name, REQ), `query`(Query, REQ), `etag`(ETag), `additional_fields`(Additional Fields) |
| `list_saved_searches` | List Saved Searches | investigation  | ✓ | `workspace_name`(Workspace Name, REQ) |
| `get_saved_searches` | Get Saved Searches | investigation | ✓ | `savedSearchId`(Saved Search ID, REQ), `workspace_name`(Workspace Name, REQ) |
| `update_saved_searches` | Update Saved Searches | investigation | ✓ | `savedSearchId`(Saved Search ID, REQ), `workspace_name`(Workspace Name, REQ), `category`(Category, REQ), `displayName`(Display Name, REQ), `query`(Query, REQ), `additional_fields`(Additional Fields) |
| `delete_saved_search` | Delete Saved Search | investigation | ✓ | `savedSearchId`(Saved Search ID, REQ), `workspace_name`(Workspace Name, REQ) |

### `azure-resource-health`

version 1.0.0 — Azure Resource Health helps you diagnose and get support for service problems that affect your Azure resources, it reports on the current an…

- GitHub: connector-azure-resource-health
- Category: IT Service Management
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_availability_status` | Get Availability Status | investigation | ✓ | `subscription_id`(Subscription ID, REQ), `resource_group_name`(Resource Group Name, REQ), `resource_provider_name`(Resource Provider Name, REQ), `resource_type`(Resource Type, REQ), `resource_name`(Resource Name, REQ), `filter`(Filter) |
| `get_availability_status_list` | Get Availability Transitions List | investigation | ✓ | `subscription_id`(Subscription ID, REQ), `resource_group_name`(Resource Group Name, REQ), `resource_provider_name`(Resource Provider Name, REQ), `resource_type`(Resource Type, REQ), `resource_name`(Resource Name, REQ), `filter`(Filter) |
| `get_availability_status_by_resource_group` | Get Current Availability Status by Resource Group | investigation | ✓ | `subscription_id`(Subscription ID, REQ), `resource_group_name`(Resource Group Name, REQ), `filter`(Filter) |
| `get_availability_status_by_subscription_id` | Get Current Availability Status by Subscription ID | investigation | ✓ | `subscription_id`(Subscription ID, REQ), `filter`(Filter) |
| `get_event_list_for_resource` | Get Event List for Resource | investigation | ✓ | `subscription_id`(Subscription ID, REQ), `resource_group_name`(Resource Group Name, REQ), `resource_provider_name`(Resource Provider Name, REQ), `resource_type`(Resource Type, REQ), `resource_name`(Resource Name, REQ), `filter`(Filter) |
| `get_event_list_for_subscription_id` | Get Event List for Subscription ID | investigation | ✓ | `subscription_id`(Subscription ID, REQ), `query_start_time`(Query Start Time), `filter`(Filter) |
| `get_event_list_for_tenant_id` | Get Event List for Tenant ID | investigation | ✓ | `query_start_time`(Query Start Time), `filter`(Filter) |

### `azure-storage`

version 1.0.0 — Deploy and manage storage accounts and blob services. This connector facilitates the automated operations related to storage account, blob s…

- GitHub: connector-azure-storage
- Category: IT Services
- Operations: 12

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_storage_accounts` | List Storage Accounts | investigation  | ✓ | `subscriptionId`(Workspace Subscription ID, REQ) |
| `get_storage_account` | Get Storage Account | investigation | ✓ | `accountName`(Account Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ) |
| `update_storage_account` | Update Storage Account | investigation | ✓ | `accountName`(Account Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `additional_fields`(Additional Fields) |
| `delete_storage_account` | Delete Storage Account | investigation | ✓ | `accountName`(Account Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ) |
| `list_blob_services` | List Blob Services | investigation  | ✓ | `accountName`(Account Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ) |
| `get_blob_service_properties` | Get Blob Service Properties | investigation | ✓ | `accountName`(Account Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ) |
| `set_blob_service_properties` | Set Blob Service Properties | investigation | ✓ | `accountName`(Account Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `additional_fields`(Additional Fields) |
| `create_blob_container` | Create Blob Container | investigation | ✓ | `accountName`(Account Name, REQ), `containerName`(Container Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `additional_fields`(Additional Fields) |
| `list_blob_containers` | List Blob Containers | investigation  | ✓ | `accountName`(Account Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `$filter`(Search Query), `$include`(Include), `$maxpagesize`(Page Size) |
| `get_blob_container` | Get Blob Container | investigation | ✓ | `accountName`(Account Name, REQ), `containerName`(Container Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ) |
| `update_blob_container` | Update Blob Container | investigation | ✓ | `accountName`(Account Name, REQ), `containerName`(Container Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ), `additional_fields`(Additional Fields) |
| `delete_blob_container` | Delete Blob Container | investigation | ✓ | `accountName`(Account Name, REQ), `containerName`(Container Name, REQ), `resourceGroupName`(Workspace Resource Group, REQ), `subscriptionId`(Workspace Subscription ID, REQ) |

### `azure-storage-table`

version 1.0.0 — Azure Table storage is a service that stores non-relational structured data (also known as structured NoSQL data) in the cloud, providing a …

- GitHub: connector-azure-storage-table
- Category: IT Services
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_table` | Create Table | investigation | ✗ | `table_name`(Table Name, REQ) |
| `insert_entity_table` | Insert Entity Into Table | investigation | ✗ | `table_name`(Table Name, REQ), `partition_key`(Partition Key, REQ), `row_key`(Row Key, REQ), `entity_fields`(Entity Fields , REQ) |
| `query_table` | Query Table | investigation | ✓ | `query_filter`(Query Filter), `records_limit`(Records Limit) |
| `query_entity_table` | Query Entity Into Table | investigation | ✓ | `table_name`(Table Name, REQ), `partition_key`(Partition Key), `row_key`(Row Key), `query_filter`(Query Filter), `property_names`(Property Names) |
| `update_entity_table` | Update Entity Into Table | investigation | ✓ | `table_name`(Table Name, REQ), `partition_key`(Partition Key, REQ), `row_key`(Row Key, REQ), `entity_fields`(Entity Fields , REQ) |
| `delete_entity_table` | Delete Entity Into Table | investigation | ✓ | `table_name`(Table Name, REQ), `partition_key`(Partition Key, REQ), `row_key`(Row Key, REQ) |
| `delete_table` | Delete Table | investigation | ✓ | `table_name`(Table Name, REQ) |

### `azure-web-application-firewall`

version 1.1.0 — The Azure WAF (Web Application Firewall) integration provides centralized protection of your web applications from common exploits and vulne…

- GitHub: connector-azure-web-application-firewall
- Category: Firewall and Network Protection
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_or_update_policy` | Create Or Update Policy | investigation | ✓ | `policy_name`(Policy Name, REQ), `managedRules`(Managed Rules, REQ), `location`(Resource Location, REQ), `id`(Resource ID), `tags`(Tags), `customRules`(Custom Rules), `policySettings`(Policy Settings) |
| `delete_policy` | Delete Policy | investigation | ✓ | `policy_name`(Policy Name, REQ) |
| `get_policy` | Get Policy | investigation | ✓ | `policy_name`(Policy Name, REQ) |
| `list_policies` | Get Policy List | investigation | ✓ | `option`(Option, REQ) |

### `bambenek-feed`

version 1.0.0 — Bambenek Consulting is an IT consulting firm focused on cybersecurity and cybercrime. This connector facilitates automated operations relate…

- GitHub: connector-bambenek-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `high_confidence`(High-Confidence Families Only, REQ), `output_mode`(Process Response As), `create_pb_params`(Create Playbook Parameters) |

### `barracuda-reputation-block-list`

version 1.0.0 — Barracuda Reputation System is a real-time database of IP addresses that have a poor reputation for sending valid emails. Barracuda Central …

- GitHub: connector-barracuda-reputation-block-list
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `iplookup`(Lookup IPv4 Or IPv6, REQ) |

### `beyondtrust-privileged-remote-access`

version 1.0.0 — BeyondTrust Privileged Remote Access controls, manages, and audits privileged accounts and credentials. This enables just-in-time, zero trus…

- GitHub: connector-beyondtrust-privileged-remote-access
- Category: Identity and Access Management
- Operations: 18

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_accounts_in_vault` | Get Account List From Vault | investigation | ✓ | `name`(Account Name), `include_personal`(Include Personal), `type`(Account Type), `account_group_id`(Account Group ID), `current_page`(Page), `per_page`(Size) |
| `create_account_in_vault` | Create Account in Vault | investigation | ✓ | `name`(Account Name, REQ), `username`(Username, REQ), `type`(Account Type, REQ), `description`(Description), `account_group_id`(Account Group ID) |
| `delete_account_in_vault` | Delete Account From Vault | investigation | ✓ | `account_id`(Account ID, REQ) |
| `checkin_or_checkout_private_key_or_password` | Checkin or Checkout Credentials From Vault | investigation | ✓ | `operation`(Operation, REQ), `account_id`(Account ID, REQ) |
| `get_all_vault_account_policies` | Get Vault Account Policy List | investigation | ✓ | `name`(Policy Name), `code_name`(Policy Code Name), `current_page`(Page), `per_page`(Size) |
| `get_all_vault_account_groups` | Get Vault Account Group List | investigation | ✓ | `name`(Group Name), `current_page`(Page), `per_page`(Size) |
| `get_all_users` | Get User List | investigation | ✓ | `username`(Username), `email_address`(Email ID), `security_provider_id`(Security Provider ID), `current_page`(Page), `per_page`(Size) |
| `get_all_vault_endpoints` | Get Vault Endpoint List | investigation | ✓ | `name`(Endpoint Name), `hostname`(Host Name), `domain_name`(Domain Name), `description`(Description), `current_page`(Page), `per_page`(Size) |
| `get_all_vendor_groups` | Get Vendor Group List | investigation | ✓ | `name`(Vendor Group Name), `current_page`(Page), `per_page`(Size) |
| `create_vendor_group` | Create Vendor Group | investigation | ✓ | `name`(Vendor Group Name, REQ), `default_policy`(Policy ID, REQ), `administrator_id`(Administrator ID, REQ), `account_expiration`(Accounts Expire After), `user_added_notification_enabled`(Notify the PRA User when a user is added), `user_expired_notification_enabled`(Notify the PRA User when a user has expired), `user_approval_enabled`(Require PRA User approval to activate users), `network_restrictions`(Network Address Allow List) |
| `get_vendor_group_by_id` | Get Vendor Group Details | investigation | ✓ | `group_id`(Vendor Group ID, REQ) |
| `update_vendor_group` | Update Vendor Group | investigation | ✓ | `group_id`(Vendor Group ID, REQ), `name`(Vendor Group Name), `default_policy`(Policy ID), `account_expiration`(Accounts Expire After), `user_added_notification_enabled`(Notify the PRA User when a user is added), `user_expired_notification_enabled`(Notify the PRA User when a user has expired), `user_approval_enabled`(Require PRA User approval to activate users), `administrator_id`(Administrator ID), `network_restrictions`(Network Address Allow List) |
| `delete_vendor_group` | Delete Vendor Group | investigation | ✓ | `group_id`(Vendor Group ID, REQ) |
| `get_all_users_in_vendor_groups` | Get User List in Vendor Group | investigation | ✓ | `group_id`(Vendor Group ID, REQ), `current_page`(Page), `per_page`(Size) |
| `create_user_in_vendor_group` | Create User in Vendor Group | investigation | ✓ | `group_id`(Vendor Group ID, REQ), `username`(Username, REQ), `public_display_name`(Display Name, REQ), `password`(Password, REQ), `email_address`(Email Address, REQ), `password_never_expire`(Password Never Expire), `password_reset_next_login`(Must Reset Password at Next Login), `account_disabled`(Account Disabled), `preferred_email_language`(Preferred Email Language) |
| `get_user_in_vendor_groups` | Get User Details in Vendor Group | investigation | ✓ | `group_id`(Vendor Group ID, REQ), `user_id`(User ID, REQ) |
| `remove_user_from_vendor_groups` | Remove User from Vendor Group | investigation | ✓ | `group_id`(Vendor Group ID, REQ), `user_id`(User ID, REQ) |
| `get_all_group_policies` | Get Group Policy List | investigation | ✓ | `name`(Policy Name), `current_page`(Page), `per_page`(Size) |

### `binaryedge`

version 1.0.0 — Binaryedge helps to automatically scan the entire public internet, create real-time threat intelligence feeds or security reports that show …

- GitHub: connector-binaryedge
- Category: Threat Intelligence
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_host_details` | Get Host Details | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_ip_risk_score_details` | Get IP Risk Score Details | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_list_of_affect_cve_details` | Get CVEs List | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_subdomain_details` | Get Subdomain Details | investigation | ✗ | `domain`(Domain, REQ) |
| `get_dns_details` | Get DNS Details | investigation | ✗ | `domain`(Domain, REQ) |

### `bitbucket`

version 1.0.0 — Bitbucket is a comprehensive platform designed to streamline the software development process. It encompasses all aspects of the development…

- GitHub: connector-bitbucket
- Category: Source Code Management
- Operations: 19

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_repository` | Create Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `name`(Repository Name, REQ), `display_name`(Repository Display Name, REQ), `links`(Links) |
| `delete_repository` | Delete Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ) |
| `get_file_from_repository` | Get File Details | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `at`(Branch Name, REQ), `file_path`(File Name, REQ), `size`(Size) |
| `create_update_file_contents` | Create or Update File Contents | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `file_path`(File Name, REQ), `branch`(Branch Name, REQ), `content`(Content Information, REQ), `message`(Commit Message, REQ), `sourceBranch`(Source Branch), `sourceCommitId`(Source Commit ID) |
| `update_user_repository_permission` | Update User Repository Permission | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `name`(Usernames, REQ), `permission`(REPOSITORY Permissions, REQ) |
| `get_users_with_repository_permission` | Get Member List of Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `filter`(Filter), `start`(Page), `limit`(Per Page) |
| `find_repository_branches` | Get Repository Branch List | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `filterText`(Filter Text), `boostMatches`(Boost Matches to Top), `details`(Retrieve Metadata), `order`(Sort Order), `start`(Page), `limit`(Per Page) |
| `create_repository_branch` | Create Repository Branch | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `name`(Branch Name, REQ), `startPoint`(Reference Branch, REQ) |
| `delete_repository_branch` | Delete Repository Branch | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `name`(Branch, REQ), `endPoint`(End Point), `dryRun`(Dry Run) |
| `list_pull_request` | Get Pull Request List | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `pull_number`(Pull Number), `filterText`(Filter Text), `state`(State), `direction`(Direction), `withAttributes`(With Attributes), `withProperties`(With Properties), `draft`(Draft), `order`(Sort Order), `start`(Page), `limit`(Per Page) |
| `merge_pull_request` | Merge Pull Request | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `pullRequestId`(Pull Request ID, REQ), `message`(Merge Commit Message), `strategyId`(Strategy), `version`(Version), `autoSubject`(Auto Subject), `autoMerge`(Auto Merge) |
| `create_pull_request` | Create Pull Request | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `fromRef`(Head Repository, REQ), `toRef`(Base Branch, REQ), `title`(Title, REQ), `description`(Description), `reviewers`(Reviewers), `draft`(Draft), `additional_fields`(Additional Fields) |
| `create_pull_request_comment` | Create Pull Request Comment | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `id`(Pull Request ID, REQ), `text`(Description, REQ), `severity`(Severity), `state`(State), `other_fields`(Other Fields) |
| `list_tags` | Get Tag List | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `filterText`(Filter Text), `orderBy`(Order By), `start`(Page), `limit`(Per Page) |
| `create_tag` | Create Tag | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `name`(Tag Name, REQ), `startPoint`(Target Branch, REQ), `message`(Tag Message), `type`(Type), `force`(Overwrite) |
| `get_web_url` | Get Server URL | investigation | ✓ | — |
| `list_pull_requests_comments` | Get Pull Request Comments | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `id`(Pull Request ID, REQ), `fromId`(From ID), `fromType`(From Type), `start`(Page), `limit`(Per Page) |
| `clone_repository` | Clone Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo_name`(Repository Name, REQ), `branch_name`(Branch Name, REQ), `clone_zip`(Clone As ZIP) |
| `update_clone_repository` | Update Remote Repository | investigation | ✓ | `file_iri`(FortiSOAR File IRI, REQ), `clone_path`(Cloned Repository Path, REQ) |

### `bitcoin-abuse-db`

version 1.0.0 — BitcoinAbuse.com is a public database of bitcoin addresses used by scammers, hackers, and criminals. This connector lets you tracking bitcoi…

- GitHub: connector-bitcoin-abuse-db
- Category: Vulnerability and Risk Management
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_lookup_abuse_types` | Get Lookup Abuse Types | investigation | ✗ | — |
| `get_lookup_distinct_reports` | Get Lookup Distinct Reports | investigation | ✗ | `page`(Page), `reverse`(Reverse) |
| `check_given_address` | Check Address | investigation | ✗ | `address`(Address, REQ) |
| `get_all_reports` | Get Complete Download | investigation | ✗ | `time_period`(Time Period, REQ) |

### `bitdefender`

version 1.0.0 — Bitdefender Endpoint Detection and Response (EDR) is a security solution designed to detect, investigate, and respond to advanced cyber thre…

- GitHub: connector-bitdefender
- Category: Endpoint Security
- Operations: 22

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_computers_quarantine_items_list` | Get Computers Quarantine List | investigation | ✓ | `endpointId`(Endpoint ID), `page`(Page), `perPage`(Per Page), `filters`(Filter) |
| `get_exchange_quarantine_items_list` | Get Exchange Quarantine List | investigation | ✓ | `endpointId`(Endpoint ID), `page`(Page), `perPage`(Per Page), `filters`(Filter) |
| `get_accounts_list` | Get Accounts List | investigation | ✓ | `page`(Page), `perPage`(Per Page) |
| `get_policies_list` | Get Policies List | investigation | ✓ | `page`(Page), `perPage`(Per Page) |
| `add_to_blocklist` | Add to Blocklist | Security | ✓ | `type`(Type, REQ), `hash`(Hash, REQ), `sourceinfo`(Source Info) |
| `get_block_list_items` | Get Block List Items | Security | ✓ | `page`(Page, REQ), `perPage`(Per Page, REQ) |
| `remove_from_blocklist` | Remove from BlockList | Security | ✓ | `hashItemId`(Hash Item ID, REQ) |
| `create_isolate_endpointtask` | Create Isolate Endpoint Task | Security | ✓ | `endpointId`(Endpoint ID, REQ) |
| `createRestoreEndpointFromIsolationTask` | Create Restore Endpoint from Isolation | Security | ✓ | `endpointId`(Endpoint ID, REQ) |
| `get_custom_rule_list` | Get Custom Rules List | Security | ✓ | `page`(Page, REQ), `perPage`(Per Page, REQ), `companyId`(Company Id, REQ), `type`(Type, REQ) |
| `delete_custom_rule` | Delete Custom Rule | Security | ✓ | `ruleId`(Rule Id, REQ), `type`(Type, REQ) |
| `update_incident_note` | Update Incident Note | Security | ✓ | `incident_id`(Incident Id, REQ), `type`(Type, REQ), `note`(Note, REQ) |
| `change_incident_status` | Change Incident Status | Security | ✓ | `incident_id`(Incident Id, REQ), `type`(Type, REQ), `status`(Status, REQ) |
| `get_endpoints_list` | Get Endpoints List | Security | ✓ | `isManaged`(Is Managed), `page`(Page), `perPage`(Per Page) |
| `get_managed_endpoints_details` | Get Managed Endpoints Details | Security | ✓ | `endpointId`(Endpoint ID, REQ) |
| `move_endpoints` | Move Endpoints | Security | ✓ | `endpointId`(Endpoint ID, REQ), `groupId`(Group ID, REQ) |
| `set_endpoint_label` | Set Endpoint Label | Security | ✓ | `endpointId`(Endpoint ID, REQ), `label`(Label, REQ) |
| `create_scan_task` | Create Scan Task | Security | ✓ | `targetIds`(Target IDs, REQ), `type`(Type, REQ), `name`(Scan Name), `returnAllTaskIds`(Return All TaskIds) |
| `create_scan_task_by_mac` | Create Scan Task By Mac Address | Security | ✓ | `macAddresses`(Mac Addresses, REQ), `type`(Type, REQ), `name`(Scan Name), `returnAllTaskIds`(Return All TaskIds) |
| `get_scan_tasks_list` | Get Scan Task List | Security | ✓ | `status`(Status), `page`(Page), `perPage`(Per Page) |
| `get_scan_tasks_status` | Get Scan Task Status | Security | ✓ | `taskId`(Task ID) |
| `create_add_file_to_quarantine_task` | Create Add File To Quarantine Task | Security | ✓ | `endpointIds`(Endpoint ID), `filePath`(File Path) |

### `bitsight`

version 1.0.0 — Bitsight is a global cyber risk management leader transforming how companies manage exposure, performance, and risk for themselves and their…

- GitHub: connector-bitsight
- Category: Attack Surface Management
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alerts | investigation | ✓ | `alert_date_gte`(Start Date), `alert_date_lte`(End Date), `alert_type`(Alert Category), `company_guid`(Company GUID), `expand`(Include Details), `folder_guid`(Folder GUID), `severity`(Severity), `limit`(Limit), `offset`(Offset) |
| `get_companies_with_exposed_credentials` | Get Companies With Exposed Credentials | investigation | ✓ | `date_added_gte`(Start Date), `date_added_lte`(End Date), `limit`(Limit), `offset`(Offset) |
| `get_credentials_leaks` | Get Credentials Leaks Affecting Your Portfolio | investigation | ✓ | `limit`(Limit), `offset`(Offset) |
| `get_threat_evidence` | Get Threat Evidence | investigation | ✓ | `company_guid`(Company GUID, REQ), `threat_guid`(Threat GUID, REQ), `last_seen_date_gte`(Last Seen Start Date), `last_seen_date_lte`(Last Seen End Date), `detection_type`(Detection Type), `evidence_certainty`(Evidence Certainty), `exposure_detection`(Exposure Detection), `force_masked`(Force Masked), `limit`(Limit), `offset`(Offset) |
| `get_portfolio_threats` | Get Portfolio Threats | investigation | ✓ | `company_guid`(Company GUID), `category_slug`(Category Slug), `currently_exposed_count_lte`(Maximum Number of Exposed Entities), `currently_exposed_count_gte`(Minimum Number of Exposed Entities), `last_seen_date_gte`(Last Seen Start Date), `last_seen_date_lte`(Last Seen End Date), `expand`(Expand), `folder`(Folder), `impacts_group`(Impact Group), `severity_level`(Severity Level), `sort`(Sort), `threat_guid`(Threat GUID), `tier`(Tier), `limit`(Limit), `offset`(Offset) |
| `get_cataloged_threats` | Get Cataloged Threats | investigation | ✓ | `category`(Category), `support_started_date_gte`(Support Start Date), `support_started_date_lte`(Support End Date), `guid`(GUID), `name`(Name), `severity_level`(Severity Level), `sort`(Sort), `limit`(Limit), `offset`(Offset) |
| `get_threat_statistics` | Get Threat Statistics | investigation | ✓ | `folder`(Folder), `scope`(Scope), `tier`(Tier) |
| `get_threat_impact` | Get Threat Impact | investigation | ✓ | `threat_guid`(Threat GUID, REQ), `last_seen_date_gte`(Last Seen Start Date), `last_seen_date_lte`(Last Seen End Date), `evidence_certainty`(Evidence Certainty), `expand`(Expand), `exposure_detection`(Exposure Detection), `folder`(Folder), `sort`(Sort), `sub_threats_count_gte`(Minimum Sub Threats Count), `sub_threats_count_lte`(Maximum Sub Threats Count), `tier`(Tier), `limit`(Limit), `offset`(Offset) |
| `get_assets` | Get Assets | investigation | ✓ | `company_guid`(Company GUID, REQ), `asset`(Asset Name), `combined_overrides.importance`(Asset Importance), `expand`(Expand), `findings.total_count_gte`(Minimum Asset Count), `findings.total_count_lte`(Maximum Asset Count), `hosted_by_isnull`(Hosted By), `importance_categories`(Importance Categories), `importance_overrides`(Importance Overrides), `ip_address`(IP Address), `is_ip`(Check If IP), `origin_subsidiary_isnull`(Origin Subsidiary), `overrides_isnull`(Calculated or User-Assigned), `tags_contains`(Tags), `limit`(Limit), `offset`(Offset), `attack_surface_analytics`(Attack Surface Analytics) |
| `get_assets_risk_matrix` | Get Asset Risk Matrix | investigation | ✓ | `company_guid`(Company GUID, REQ) |

### `blocklist_de-feed`

version 1.0.0 — Blocklist.de is a free and voluntary service provided by a Fraud/Abuse-specialist, whose servers are often attacked via SSH-, Mail-Login-, F…

- GitHub: connector-blocklist_de-feed
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `time`(Added After), `service`(Service Type), `output_mode`(Process Response As) |
| `get_ips_by_service` | Fetch All Blocklist IPs | investigation | ✓ | `service`(Service Type, REQ), `output_mode`(Process Response As) |

### `blueliv-threatcompass`

version 1.0.0 — Blueliv ThreatCompass systematically looks for information about companies,products, people, brands, logos, assets, technology and other inf…

- GitHub: connector-blueliv-threatcompass
- Category: Vulnerability Management
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_resource_list` | Get Resource List | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `to`(To), `since`(Since), `page`(Page), `maxRows`(Limit), `other_fields`(Other Fields) |
| `get_resource_by_id` | Get Resource by ID | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `resource_id`(Resource ID, REQ), `other_fields`(Other Fields) |
| `update_resource_status` | Update Resource Status | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `module_type`(Module Type, REQ), `resource_id`(Resource ID, REQ), `status`(Status, REQ), `other_fields`(Other Fields) |
| `update_resource_label` | Update Resource Label | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `module_type`(Module Type, REQ), `resources`(Resource ID, REQ), `label`(Label ID, REQ), `other_fields`(Other Fields) |
| `update_resource_read_status` | Update Resource Read Status | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `module_type`(Module Type, REQ), `resources`(Resource ID, REQ), `read`(Read Status, REQ), `other_fields`(Other Fields) |
| `update_resource_rating` | Update Resource Rating | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `module_type`(Module Type, REQ), `resources`(Resource ID, REQ), `rate`(Rating, REQ), `other_fields`(Other Fields) |
| `update_resource_fav` | Update Resource FAV | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `module_type`(Module Type, REQ), `resources`(Resource ID, REQ), `status`(FAV Status, REQ), `other_fields`(Other Fields) |
| `update_resource_tlp` | Update Resource TLP | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `module_type`(Module Type, REQ), `resource_id`(Resource ID, REQ), `tlp_status`(TLP Status, REQ), `other_fields`(Other Fields) |
| `get_module_labels` | Get Module Labels | investigation | ✓ | `org_id`(Organization ID, REQ), `module_id`(Module ID, REQ), `module_type`(Module Type, REQ), `other_fields`(Other Fields) |

### `bmc-discovery`

version 1.0.0 — BMC Discovery is a data center discovery solution that automatically discovers data center inventory, configuration and relationship data, a…

- GitHub: connector-bmc-discovery
- Category: Endpoint Security
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_query` | Run Search | investigation | ✓ | `query`(Filter Query, REQ), `delete`(Result Deleted), `offset`(Offset), `results_id`(Results ID), `limit`(Limit) |

### `botvrij-misp-osint-feed`

version 1.0.0 — Botvrij.eu MISP OSINT Feed Integration.<br/><br/>This connector has a dependency on the <a href="/content-hub/all-content/?contentType=solut…

- GitHub: connector-botvrij-misp-osint-feed
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_collections` | Get Collections | investigation | ✗ | `modified_after`(Modified After) |
| `get_objects_by_collection_id` | Get Objects By Collection ID | investigation | ✓ | `collectionID`(Collection ID, REQ), `modified_after`(Modified After) |

### `brute-force-blocker-feed`

version 1.1.0 — BruteForceBlocker Feed it's main purpose is to block SSH bruteforce attacks via firewall.This connector facilitates automated operations rel…

- GitHub: connector-brute-force-blocker-feed
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `last_pull_time`(Last Pull Time) |
| `download_indicators` | Download Indicators | investigation | ✓ | `last_pull_time`(Last Pull Time) |

### `censys`

version 2.0.0 — Censys is a search engine that focuses on providing comprehensive information about devices and systems connected to the Internet. It is spe…

- GitHub: connector-censys
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_host_details` | Get Host Details Using IP Address | investigation | ✓ | `ip`(IP Address, REQ), `at_time`(Since Date) |
| `search_hosts` | Search Hosts | investigation | ✓ | `q`(Censys Search Query, REQ), `per_page`(Max Hits), `virtual_hosts`(Virtual Hosts), `cursor`(Cursor), `fields`(Fields) |
| `lookup_certificate` | Lookup Certificate | investigation | ✓ | `fingerprint`(SHA-256 Fingerprint, REQ) |

### `chatsonic`

version 1.0.0 — This integration supports Writesonic's Chatsonic generative AI. A powerful language model with real time data

- GitHub: connector-chatsonic
- Category: Miscellaneous
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `chat_completions` | Ask a Question | miscellaneous | ✓ | `param@input_text`(Message, REQ), `param@google_enabled`(Enable Google Search), `param@language`(Language) |
| `chat_conversation` | Converse With Chatsonic | miscellaneous | ✓ | `param@input_text`(Message, REQ), `param@history_data`(Messages, REQ), `param@google_enabled`(Enable Google Search), `param@language`(Language) |

### `check-host`

version 1.0.0 — Check host offers various network-related tools and services. It also provides tools for checking the availability and response time of a we…

- GitHub: connector-check-host
- Category: Networking
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `ping_check` | Ping Check | investigation | ✗ | `host`(Host, REQ), `max_nodes`(Max Nodes, REQ) |
| `http_check` | HTTP Check | investigation | ✗ | `host`(Host, REQ), `max_nodes`(Max Nodes, REQ) |
| `tcp_connection_check` | TCP Connection Check | investigation | ✗ | `host`(Host, REQ), `max_nodes`(Max Nodes, REQ) |
| `dns_address_check` | DNS Address Check | investigation | ✗ | `host`(Host, REQ), `max_nodes`(Max Nodes, REQ) |
| `check_result_by_request_id` | Check Result By Request ID | investigation | ✗ | `request_id`(Request ID, REQ) |

### `check-phish`

version 1.0.0 — Check Phish is free scanner to detect phishing & fraudulent sites in real-time. This connector facilitates automated interactions, such as r…

- GitHub: connector-check-phish
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_url_info` | Get URL Information | investigation | ✓ | `url`(URL, REQ), `scanType`(Scan Type, REQ), `insights`(Insights, REQ) |

### `checkpoint-firewall`

version 2.2.0 — Check Point Firewall that can use for block/unblock IP, Application, URL

- GitHub: connector-checkpoint-firewall
- Category: Firewall and Network Protection
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `check_policies` | Validate Configuration Policies | investigation | ✓ | — |
| `get_list_of_applications` | Get Applications Detail | investigation | ✓ | `start_index`(Start Index, REQ), `limit`(Number of Results (Range: 1 To 500), REQ) |
| `block_ip` | Block IP Address | containment | ✓ | `ip_address_list`(IP Address (In CSV or List Format), REQ) |
| `block_applications` | Block Applications | containment | ✓ | `app_list`(Application Names (In CSV or List Format), REQ) |
| `block_urls` | Block URLs | containment | ✓ | `url_list`(URLs (In CSV or List Format), REQ) |
| `unblock_ip` | Unblock IP Address | remediation | ✓ | `ip_address_list`(IP Address (In CSV or List Format), REQ) |
| `unblock_urls` | Unblock URLs | remediation | ✓ | `url_list`(URLs (In CSV or List Format), REQ) |
| `unblock_applications` | Unblock Applications | remediation | ✓ | `app_list`(Application Names (In CSV or List Format), REQ) |
| `get_blocked_urls` | Get Blocked URLs | investigation | ✓ | — |
| `get_blocked_ip_addresses` | Get Blocked IP Addresses | investigation | ✓ | — |
| `get_blocked_application_names` | Get Blocked Application Names | investigation | ✓ | — |
| `show_sessions` | Get Sessions | investigation | ✓ | — |
| `get_session` | Get Session | investigation | ✓ | `session_id`(Session UID, REQ) |
| `discard_session` | Terminate Session | remediation | ✓ | `session_uid`(Session UID, REQ) |

### `checkpoint-management-console`

version 1.0.0 — CheckPoint Management Console helps you to configure and view the security policy and objects in a Security Management Server or Multi Domai…

- GitHub: connector-checkpoint-management-console
- Category: Firewall and Network Protection
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `add_host` | Create Host | investigation | ✓ | `name`(Name, REQ), `ip-address`(IP Address), `ipv4-address`(IPv4 Address), `ipv6-address`(IPv6 Address), `interfaces`(Interfaces), `nat-settings`(NAT Settings), `tags`(Tags), `host-servers`(Host Servers), `set-if-exists`(Set If Exists), `color`(Color), `comments`(Comments), `details-level`(Details Level), `groups`(Groups), `ignore-warnings`(Ignore Warnings), `ignore-errors`(Ignore Errors) |
| `update_host` | Update Host | investigation | ✓ | `params_type`(Based On, REQ), `interfaces`(Interfaces), `ip-address`(IP Address), `ipv4-address`(IPv4 Address), `ipv6-address`(IPv6 Address), `nat-settings`(NAT Settings), `new-name`(New Name), `tags`(Tags), `host-servers`(Host Servers), `color`(Color), `comments`(Comments), `details-level`(Details Level), `groups`(Groups), `ignore-warnings`(Ignore Warnings), `ignore-errors`(Ignore Errors) |
| `get_hosts_list` | Get Hosts List | investigation | ✓ | `filter`(Filter), `limit`(Limit), `offset`(Offset), `order`(Order), `show-membership`(Show Membership), `details-level`(Details Level) |
| `get_host_details` | Get Host Details | investigation | ✓ | `params_type`(Based On, REQ) |
| `delete_host` | Delete Host | investigation | ✓ | `params_type`(Based On, REQ) |

### `cicd-utils`

version 1.2.0 — CICD Utils provides out of the box actions for CICD solution pack

- GitHub: connector-cicd-utils
- Category: Utilities
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `unzip_export_template` | Unzip Export Template | utilities | ✓ | `filepath`(Filepath, REQ) |
| `split_export_templates` | Split Export Template | utilities | ✓ | `prod_content_filepath`(Prod Content Filepath, REQ), `prod_content_json`(Prod Content JSON, REQ), `prod_settings_filepath`(Prod Settings Filepath, REQ), `prod_settings_json`(Prod Settings JSON, REQ), `dev_settings_filepath`(Dev Settings Filepath, REQ), `dev_settings_json`(Dev Settings JSON, REQ), `unzip_filepath`(Unzip Export Template Filepath, REQ), `zip_filename`(Split Zip Export Template Filename, REQ) |
| `export_fortisoar_template` | Export FortiSOAR Template | utilities | ✓ | `export_template_name`(Export Template Name, REQ), `export_file_name`(Export File Name, REQ), `ignore_keys`(Ignore Keys) |
| `import_fortisoar_template` | Import FortiSOAR Template | utilities | ✓ | `filename`(File Name, REQ), `file_path`(File Path, REQ) |
| `review_import_fortisoar_template` | Review & Import FortiSOAR Template | utilities | ✓ | `filename`(File Name, REQ), `file_path`(File Path, REQ) |

### `cins-army-feed`

version 1.0.0 — CINS Army List is a subset of the CINS Active Threat Intelligence ruleset provided to our Sentinel IPS customers, and consists of IP address…

- GitHub: connector-cins-army-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `output_mode`(Process Response As) |

### `circl-cve-search`

version 1.0.0 — This app searches publicly known information from security vulnerabilities in software and hardware along with their corresponding exposures…

- GitHub: connector-circl-cve-search
- Category: Vulnerability and Risk Management
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_per_id` | Get CVE Details | investigation | ✓ | `cve-id`(CVE ID, REQ) |
| `browse_vendors` | Get Vendors | investigation | ✓ | — |
| `browse_products` | Get Products | investigation | ✓ | `vendor`(Vendor, REQ) |
| `search_per_product` | Search Specific Product | investigation | ✓ | `vendor`(Vendor, REQ), `product`(Product, REQ) |
| `last_updated_cves` | Get Last Updated CVEs | investigation | ✓ | — |
| `current_cve_dbinfo` | Get CVE DB Info | investigation | ✓ | — |

### `circleci`

version 1.0.0 — CircleCI is the continuous integration & delivery platform that helps the development teams to release code rapidly and automate the build, …

- GitHub: connector-circleci
- Category: DevOps and Digital Operations
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_workflows_list` | Get Workflows List | investigation | ✓ | `vc_type`(Version Control System Type), `organization`(Organization Name), `project`(Project Name), `page-token`(Page Token), `branch_name`(Fetch Data From, REQ), `reporting-window`(Reporting Window) |
| `get_artifacts_list` | Get Artifacts List | investigation | ✓ | `job-number`(Job Number, REQ), `vc_type`(Version Control System Type), `organization`(Organization Name), `project`(Project Name) |
| `get_workflow_jobs_list` | Get Workflow Jobs List | investigation | ✓ | `id`(Workflow ID, REQ) |
| `get_workflow_last_runs` | Get Workflow Last Runs | investigation | ✓ | `workflow-name`(Workflow Name, REQ), `vc_type`(Version Control System Type), `organization`(Organization Name), `project`(Project Name), `page-token`(Page Token), `branch_name`(Fetch Data From, REQ), `start-date`(Start Date), `end-date`(End Date) |
| `trigger_workflow` | Trigger Workflow | investigation | ✓ | `vc_type`(Version Control System Type), `organization`(Organization Name), `project`(Project Name), `parameters`(Parameters) |

### `cisa-advisory`

version 1.1.0 — CISA Advisory connector fetches the Advisory and Known Exploited Vulnerability (KEV) CVE published by CISA.

- GitHub: connector-cisa-advisory
- Category: Utilities
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_advisory` | Get Advisory | investigation | ✓ | `advisory_type`(Advisory Type, REQ), `date_filter`(Date Filter) |
| `get_advisory_by_year` | Get Advisory By Year | investigation | ✓ | `advisory_type`(Advisory Type, REQ) |
| `get_advisory_by_vendor` | Get Advisory By Vendor | investigation | ✓ | `advisory_type`(Advisory Type, REQ), `vendor`(Vendor, REQ), `similarityThreshold`(Similarity Threshold, REQ) |
| `get_advisory_by_product` | Get Advisory By Product | investigation | ✓ | `advisory_type`(Advisory Type, REQ), `vendor`(Vendor, REQ), `product`(Product, REQ), `version`(Version), `vendorSimilarityThreshold`(Vendor Similarity Threshold, REQ), `productSimilarityThreshold`(Product Similarity Threshold, REQ) |
| `get_known_exploited_vulnerability_cves` | Get Known Exploited Vulnerability CVEs | investigation | ✓ | — |

### `cisco-asa`

version 2.0.2 — Cisco ASA connector that you can use to Get Version of the device, Block and Unblock IP Address, List and Terminate Sessions etc.

- GitHub: connector-cisco-asa
- Category: Firewall
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_version` | Get Version | investigation | ✓ | — |
| `block_ip` | Block IP | containment | ✓ | `dest`(Destination IP Address, REQ), `src`(Source IP Address, REQ), `direction`(Rule Direction, REQ), `access_list`(Access List Name, REQ), `interface`(Interface Name to Apply the Rule on, REQ) |
| `unblock_ip` | Unblock IP | remediation | ✓ | `dest`(Destination IP Address, REQ), `src`(Source IP Address, REQ), `direction`(Rule direction, REQ), `access_list`(Access List Name, REQ), `interface`(Interface Name to Apply the Rule on, REQ) |
| `list_sessions` | List Sessions | investigation | ✓ | — |
| `terminate_sessions` | Terminate Sessions | Remediation | ✓ | `username`(Username, REQ) |
| `get_network_group` | Get Network Group | investigation | ✓ | `group_name`(Network Group Name, REQ) |
| `update_group` | Update Network Group | containment | ✓ | `group_name`(Network Group Name, REQ), `method`(Method, REQ), `ip`(IP Address, REQ) |
| `run_custom_commands` | Run Custom Commands | containment | ✓ | `custom_commands`(Commands, REQ) |

### `cisco-esa-rest`

version 1.0.0 — The Cisco Email Security Virtual Appliance significantly lowers the cost of deploying email security, especially in highly distributed netwo…

- GitHub: connector-cisco-esa-rest
- Category: Email Security
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_quarantine_messages` | Search Quarantine Messages | investigation | ✓ | `startDate`(Start Datetime), `endDate`(End Datetime), `quarantineType`(Quarantine Type), `orderBy`(Order By), `orderDir`(Sort), `offset`(Offset), `limit`(Limit), `envelopeRecipientFilterOperator`(Recipient Filter Operator), `envelopeRecipientFilterValue`(Recipient Filter Value), `filterOperator`(Filter Operator), `filterValue`(Filter Value) |
| `get_quarantine_message` | Get Quarantine Message By ID | investigation | ✓ | `mid`(Message ID, REQ), `quarantineType`(Quarantine Type) |
| `release_quarantine_message` | Release Quarantine Messages | investigation | ✓ | `mids`(Message ID, REQ), `action`(Action), `quarantineType`(Quarantine Type) |
| `delete_quarantine_message` | Delete Quarantine Messages | investigation | ✓ | `mids`(Message ID, REQ), `quarantineType`(Quarantine Type) |
| `search_safelist_or_blocklist_entries` | Search Safelist or Blocklist Entries | investigation | ✓ | `safelist_or_blocklist`(Safelist or Blocklist, REQ), `action`(Action), `quarantineType`(Quarantine Type), `viewBy`(View By), `orderBy`(Order By), `offset`(Offset), `limit`(Limit), `orderDir`(Sort), `search`(Search) |
| `edit_safelist_or_blocklist_entries` | Edit Safelist or Blocklist Entries | investigation | ✓ | `safelist_or_blocklist`(Safelist or Blocklist, REQ), `action`(Action, REQ), `quarantineType`(Quarantine Type), `viewBy`(View By), `recipientAddresses`(Recipient Addresses), `recipientList`(Recipient List), `senderAddresses`(Sender Addresses), `senderList`(Sender List) |
| `delete_safelist_or_blocklist_entries` | Delete Safelist or Blocklist Entries | investigation | ✓ | `safelist_or_blocklist`(Safelist or Blocklist, REQ), `quarantineType`(Quarantine Type), `recipientList`(Recipient List), `senderList`(Sender List), `viewBy`(View By) |
| `get_message_dlp_details` | Get Message DLP Details | investigation | ✓ | `startDate`(Start Datetime, REQ), `endDate`(End Datetime, REQ), `serialNumber`(Serial Number), `mid`(Message ID), `icid`(Injection Connection ID) |
| `get_message_amp_details` | Get Message AMP Details | investigation | ✓ | `startDate`(Start Datetime, REQ), `endDate`(End Datetime, REQ), `serialNumber`(Serial Number), `mid`(Message ID), `icid`(Injection Connection ID) |
| `get_message_url_details` | Get Message URL Details | investigation | ✓ | `startDate`(Start Datetime, REQ), `endDate`(End Datetime, REQ), `serialNumber`(Serial Number), `mid`(Message ID), `icid`(Injection Connection ID) |
| `get_report` | Get Report | investigation | ✓ | `reportType`(Report Type, REQ), `startDate`(Start Datetime, REQ), `endDate`(End Datetime, REQ), `device_type`(Device Type, REQ), `query_type`(Query Type), `orderBy`(Order By), `orderDir`(Sort), `offset`(Offset), `limit`(Limit), `top`(Data Retrieval), `filterValue`(Filter Value), `filterBy`(Filter By), `filterOperator`(Filter Operator), `device_group_name`(Device Group Name), `device_name`(Device Name) |

### `cisco-ise`

version 2.1.1 — Cisco ISE connector provides actions like, list all active sessions, quarantine IP/Mac address, un-quarantine IP/Mac address etc.

- GitHub: connector-cisco-ise
- Category: Network Access Control
- Operations: 21

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_active_sessions` | List All Active Sessions | investigation | ✓ | — |
| `get_internal_user_details` | Get Internal User Details | investigation | ✓ | `userid`(User ID, REQ) |
| `list_internal_users` | List Internal Users | investigation | ✓ | `filter.name`(User Name), `filter.firstName`(First Name), `filter.lastName`(Last Name), `filter.email`(Email Address), `size`(Size), `page`(Page) |
| `disable_internal_user` | Disable Internal User | containment | ✓ | `filter.name`(Username, REQ) |
| `enable_internal_user` | Enable Internal User | containment | ✓ | `filter.name`(Username, REQ) |
| `list_guest_users` | List Guest Users | investigation | ✓ | `filter.name`(User Name), `filter.firstName`(First Name), `filter.lastName`(Last Name), `filter.emailAddress`(Email Address), `filter.sponsorUserName`(Sponsor Username), `filter.company`(Company), `filter.phoneNumber`(Phone Number), `size`(Size), `page`(Page) |
| `get_guest_user_details` | Get Guest User Details | investigation | ✓ | `userid`(User ID, REQ) |
| `suspend_guest_user` | Suspend Guest User | containment | ✓ | `filter.name`(Guest Username, REQ) |
| `reinstate_guest_user` | Reinstate Guest User | containment | ✓ | `filter.name`(Guest Username, REQ) |
| `quarantine_ip` | EPS: Quarantine IP Address | containment | ✓ | `target_ipaddr`(Target IP Address, REQ) |
| `quarantine_mac` | EPS: Quarantine MAC Address | containment | ✓ | `target_mac`(Target MAC Address, REQ) |
| `unquarantine_ip` | EPS: Un-Quarantine IP Address | containment | ✓ | `target_ipaddr`(Target IP Address, REQ) |
| `unquarantine_mac` | EPS: Un-Quarantine MAC Address | containment | ✓ | `target_mac`(Target MAC Address, REQ) |
| `end_session` | End a Target MAC Address Session | miscellaneous | ✓ | `target_mac`(Target MAC Address, REQ) |
| `log_system_off` | MAC Address Logout | miscellaneous | ✓ | `target_mac`(Target MAC Address, REQ), `target_server`(Target Server Address, REQ) |
| `get_ise_endpoint` | Get Endpoints | investigation | ✓ | `get_endpoint_by`(Get Endpoint By), `size`(Size), `page`(Page) |
| `get_anc_endpoint` | Get ANC Endpoint | investigation | ✓ | `id`(ANC Endpoint ID), `size`(Size), `page`(Page) |
| `create_anc_policy` | Create ANC Policy | containment | ✓ | `name`(ANC Policy Name, REQ), `actions`(Action, REQ) |
| `get_anc_policy` | Get ANC Policy | investigation | ✓ | `get_policy_by`(Get Policy By), `size`(Size), `page`(Page) |
| `assign_policy` | Assign ANC Policy | containment | ✓ | `policyName`(ANC Policy Name, REQ), `apply_to`(Apply To, REQ) |
| `revoke_policy` | Revoke ANC Policy | remediation | ✓ | `policyName`(ANC Policy Name, REQ), `revoke_from`(Revoke From, REQ) |

### `cisco-meraki-mx-l3`

version 1.0.0 — Cisco Meraki MX L3 Firewall gives administrators complete control over the users, content, and applications on their network. This connector…

- GitHub: connector-cisco-meraki-mx-l3
- Category: Firewall
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_network_appliance_firewall_rules` | Get Network Appliance Firewall L3 Firewall Rules | investigation | ✓ | `networkId`(Network ID, REQ) |
| `update_network_appliance_firewall_rules` | Update Network Appliance Firewall L3 Firewall Rules | investigation | ✓ | `networkId`(Network ID, REQ), `policy`(Policy, REQ), `protocol`(Protocol, REQ), `srcCidr`(Source IP Address(es), REQ), `destCidr`(Destination IP Address(es), REQ), `srcPort`(Source Port(s)), `destPort`(Destination Port(s)), `comment`(Comment), `syslogEnabled`(Syslog Enabled) |

### `cisco-talos-feed`

version 1.0.0 — Cisco Talos Reputation Center provides access to expansive threat data and related information. This connector facilitates automated operati…

- GitHub: connector-cisco-talos-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `output_mode`(Process Response As) |

### `cisco-talos-threat-intelligence`

version 1.0.0 — Talos Threat Intelligence connector enables seamless integration with Cisco Talos Threat Intelligence using CIsco SecureX APIs to retrieve r…

- GitHub: connector-cisco-talos-threat-intelligence
- Category: Threat Intelligence
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✗ | `domain`(Domain, REQ) |
| `get_url_reputation` | Get URL Reputation | investigation | ✗ | `url`(URL, REQ) |
| `get_file_hash_reputation` | Get File Hash Reputation | investigation | ✗ | `file_hash`(File Hash, REQ) |

### `cisco-umbrella-enforcement`

version 3.0.1 — Cisco Umbrella is a cloud security platform that provides the first line of defense against threats on the internet wherever users go. Cisco…

- GitHub: connector-cisco-umbrella-enforcement
- Category: Network Security
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `add_destination` | Add Destinations to Destination List | investigation | ✓ | `listId`(Destination List ID, REQ), `destinations`(Destinations, REQ), `comment`(Comment) |
| `get_destination_lists` | Get All Destination List | investigation | ✓ | — |
| `list_destinations` | Get Destinations in Destination List | investigation | ✓ | `listId`(Destination List ID, REQ), `page`(Page Number), `limit`(Limit) |
| `delete_destinations_from_list` | Delete Destinations from Destination List | investigation | ✓ | `listId`(Destination List ID, REQ), `id`(Destinations ID, REQ) |

### `claroty`

version 1.1.0 — Claroty CTD is a robust solution that delivers comprehensive cybersecurity controls for industrial environments. This connector provides aut…

- GitHub: connector-claroty
- Category: OT & IoT Security
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_assets` | Get Assets | investigation | ✓ | `asset_type__in`(Asset Type), `protocol__exact`(Protocol), `criticality__exact`(Asset Criticality), `timestamp__gte`(Start Time), `timestamp__lte`(End Time), `filters`(Other Filters), `per_page`(Limit), `page`(Page), `format`(Format) |
| `get_asset_details` | Get Asset Details | investigation | ✓ | `resource_id`(Resource ID, REQ) |
| `get_alerts` | Get Alerts | investigation | ✓ | `resolution__exact`(Status), `category__exact`(Category), `severity__exact`(Alert Severity), `timestamp__gte`(Start Time), `timestamp__lte`(End Time), `filters`(Other Filters), `per_page`(Limit), `page`(Page) |
| `get_alert_details` | Get Alert Details | investigation | ✓ | `resource_id`(Resource ID, REQ) |
| `get_tasks` | Get Tasks | investigation | ✓ | `name__icontains`(Name Contains (Case-Sensitive)), `site_id__exact`(Site ID), `per_page`(Limit), `page`(Page), `sort`(Sort By), `sort_order`(Sort Order) |
| `get_queries` | Get Queries | investigation | ✓ | `name__icontains`(Name Contains(case-sensitive)), `site_id__exact`(Site ID), `sort`(Sort By), `sort_order`(Sort Order), `per_page`(Limit), `page`(Page) |
| `get_insights` | Get Insights | investigation | ✓ | `format`(Format, REQ), `sort`(Sort By, REQ), `sort_order`(Sort Order), `ghost__exact`(Host Exact), `special_hint__exact`(Special Hint Exact), `insight_status__exact`(Insight Status Exact), `site_id__exact`(Site ID), `per_page`(Limit), `page`(Page) |
| `get_events` | Get Events | investigation | ✓ | `site_id`(Site ID), `id__exact`(Resource ID), `alert_id__exact`(Alert Resource ID), `timestamp__gte`(Start Time), `timestamp__lte`(End Time), `description__contains`(Description), `description__icontains`(Description (case-sensitive)), `type__exact`(Type), `status__exact`(Status), `sort`(Sort By), `sort_order`(Sort Order), `per_page`(Limit), `page`(Page) |
| `get_insight_details` | Get Insight Details | investigation | ✓ | `insight_name`(Insight Name, REQ), `format`(Format), `ghost__exact`(Host Exact), `special_hint__exact`(Special Hint Exact), `insight_status__exact`(Insight Status Exact), `site_id__exact`(Site ID), `per_page`(Limit), `page`(Page) |
| `get_asset_risks_and_vulnerabilities` | Get Asset Risks And Vulnerabilities | investigation | ✓ | `resource_id`(Asset Resource Id, REQ) |

### `claroty-xdome`

version 1.0.0 — Claroty xDome is a modular, SaaS-powered industrial cybersecurity platform that scales to protect your environment and fulfill your goals as…

- GitHub: connector-claroty-xdome
- Category: OT & IoT Security
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alerts | investigation | ✓ | `fields`(Fields, REQ), `before_detected_time`(Before Detected Time), `after_detected_time`(After Detected Time), `before_updated_time`(Before Updated Time), `after_updated_time`(After Updated Time), `id`(IDs), `category`(Category), `filter_by`(Filter By), `sort_by`(Sort By), `offset`(Offset), `limit`(Limit), `all_alerts`(Fetch all Alerts) |
| `get_devices` | Get Devices | investigation | ✓ | `fields`(Fields, REQ), `device_type`(Device Type), `mac_oui_list`(MAC OUI), `model`(Model), `software_or_firmware_version`(Software/Firmware Version), `device_category`(Device Category), `device_subcategory`(Device Sub-Category), `purdue_level`(Purdue Level), `known_vulnerabilities`(Vulnerabilities), `risk_score`(Risk Score), `filter_by`(Filter By), `sort_by`(Sort By), `offset`(Offset), `limit`(Limit) |
| `get_ot_events` | Get OT Activity Events | investigation | ✓ | `fields`(Fields, REQ), `event_id`(OT Event ID), `event_type`(OT Event Type), `dest_asset_id`(Destination Asset ID), `source_asset_id`(Source Asset ID), `filter_by`(Filter By), `sort_by`(Sort By), `offset`(Offset), `limit`(Limit) |
| `get_vulnerabilities` | Get Vulnerabilities | investigation | ✓ | `fields`(Fields, REQ), `id`(Vulnerability ID), `name`(Vulnerability name), `vulnerability_type`(Vulnerability Type), `cve_ids`(CVE ID), `cvss_v3_score`(CVSS V3 Score), `filter_by`(Filter By), `sort_by`(Sort By), `offset`(Offset), `limit`(Limit) |
| `execute_generic_claroty_api` | Execute Generic Claroty API | investigation | ✓ | `endpoint`(Endpoint, REQ), `parameters`(Parameters, REQ) |

### `clicksend`

version 2.0.0 — ClickSend is a cloud-based service that lets you send and receive SMS, Email, Voice, Fax, and Letters worldwide.

- GitHub: connector-clicksend
- Category: Communication and Coordination
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `send_message` | Send Message | investigation | ✓ | `body`(Message, REQ), `send_to`(To, REQ), `from`(From), `schedule`(Schedule), `custom_string`(Custom String), `country`(Country), `from_email`(Email) |
| `get_contact_list` | Get Contact List | investigation | ✓ | `page`(Page), `limit`(Limit) |
| `send_voice_message` | Send Voice Message | investigation | ✓ | `body`(Message, REQ), `voice`(Voice, REQ), `send_to`(To, REQ), `schedule`(Schedule), `custom_string`(Custom String), `country`(Country), `lang`(Language), `require_input`(Require Input), `machine_detection`(Machine Detection) |

### `cloudflare`

version 1.0.0 — Cloudflare helps to automatically scan the entire public internet, including DDoS protection, web application firewall, bot management, encr…

- GitHub: connector-cloudflare
- Category: Threat Intelligence
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_firewall_rules` | Get Firewall Rules | investigation | ✗ | — |
| `get_firewall_rule_set` | Get Firewall Rule Sets | investigation | ✗ | — |
| `get_rule_id_by_rule_name` | Get Rule ID By Rule Name | investigation | ✗ | `ruleset_name`(Ruleset Name, REQ) |
| `block_ip` | Block IP | containment | ✗ | `ruleset_id`(Ruleset ID, REQ), `ip_address`(IP Address, REQ), `description`(Description, REQ) |
| `unblock_ip` | Unblock IP | remediation | ✗ | `ip_address`(IP Address, REQ) |

### `cloudflare-waf`

version 1.0.0 — Cloudflare Web Application Firewall (WAF) integration allows customers to manage firewall rules, filters, and IP Lists. It also allows to re…

- GitHub: connector-cloudflare-waf
- Category: Firewall and Network Protection
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_firewall_rule` | Create Firewall Rule | investigation | ✗ | `description`(Description, REQ), `action`(Action), `products`(Products), `paused`(Paused), `priority`(Priority), `ref`(Reference Tag), `filter_id`(Filter ID), `filter_expression`(Filter Expression) |
| `update_firewall_rule` | Update Firewall Rule | investigation | ✗ | `id`(Rule ID, REQ), `description`(Description), `action`(Action), `products`(Products), `paused`(Paused), `priority`(Priority), `ref`(Reference Tag), `filter_id`(Filter ID) |
| `list_firewall_rules` | List Firewall Rules | investigation | ✗ | `action`(Action), `description`(Description), `id`(Rule ID), `paused`(Paused), `page`(Page Number), `per_page`(Record Per Page) |
| `delete_firewall_rule` | Delete Firewall Rule | investigation | ✗ | `id`(Rule ID, REQ) |
| `create_filter` | Create Filter | investigation | ✗ | `zone_id`(Zone ID), `description`(Description), `expression`(Expression), `ref`(Reference ID), `paused`(Paused) |
| `list_filters` | List Filters | investigation | ✗ | `id`(Filter ID), `description`(Description), `expression`(Expression), `ref`(Reference ID), `page`(Page Number), `per_page`(Per Page) |
| `update_filter` | Update Filter | investigation | ✗ | `id`(Filter ID, REQ), `zone_id`(Zone ID), `description`(Description), `expression`(Expression), `ref`(Reference ID), `paused`(Paused) |
| `delete_filter` | Delete Filter | investigation | ✗ | `id`(Filter ID, REQ) |
| `list_zones` | List Zones | investigation | ✗ | `match`(Match), `name`(Name), `account_name`(Account Name), `order`(Order), `status`(Status), `direction`(Direction), `page`(Page Number), `per_page`(Per Page) |
| `get_ip_lists` | Get IP Lists | investigation | ✗ | `page`(Page Number), `per_page`(Per Page) |
| `create_ip_list` | Create IP List | investigation | ✗ | `name`(Name, REQ), `description`(Description) |
| `delete_ip_list` | Delete IP List | investigation | ✗ | `list_id`(List ID, REQ) |
| `create_ip_items_list` | Create IP Items List | investigation | ✗ | `list_id`(List ID, REQ), `ip_address`(IP Address, REQ) |
| `get_ip_list_item` | Get IP List Items | investigation | ✗ | `list_id`(List ID, REQ), `page`(Page Number), `per_page`(Record Per Page) |
| `update_ip_list_item` | Update IP List Items | investigation | ✗ | `list_id`(List ID, REQ), `ip_address`(IP Address, REQ) |
| `delete_ip_list_item` | Delete IP List Items | investigation | ✗ | `list_id`(List ID, REQ), `items_id`(Item ID, REQ) |

### `cofense-vision`

version 1.0.0 — Cofense Vision is a security solution designed to help organizations quickly detect, locate, and quarantine phishing emails across all emplo…

- GitHub: connector-cofense-vision
- Category: Email Security
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_email` | Search Email | investigation | ✓ | `emailSubject`(Email Subject, REQ), `senderEmailAddress`(Sender Email Address, REQ) |
| `quarantine_email` | Quarantine Email | investigation | ✓ | `recipientAddress`(Recipient Address, REQ), `internetMessageId`(Internet Message ID, REQ) |

### `commvault`

version 1.0.0 — Commvault is an Intelligent Data Services platform which helps you close the business integrity gap, keeping your data available and ready f…

- GitHub: connector-commvault
- Category: Network Security
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_of_alerts` | Get Alerts List | investigation | ✓ | — |
| `alert_details` | Get Alert Details | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `list_of_users` | Get Users List | investigation | ✓ | `level`(Level) |
| `update_user` | Update User Details | investigation | ✓ | `user_id`(User ID, REQ), `description`(Description), `associatedUserGroupsOperationType`(Associated User Groups Operation Type), `agePasswordDays`(Age Password Days), `password`(Password), `email`(Email), `fullName`(Full Name), `enableUser`(Enable User), `userGroupNames`(User Group Names), `userName`(Username) |

### `coralogix`

version 1.0.0 — Coralogix is a modern log analytics platform that provides real-time insights and monitoring for your log data. It offers advanced indexing,…

- GitHub: connector-coralogix
- Category: Logging
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_archived_logs` | Search Archived Logs | investigation | ✓ | `query`(Query), `start_date`(Start Date), `end_date`(End Date), `metadata`(Metadata) |

### `criminal-ip`

version 1.0.0 — Criminal IP provides cyber threat intelligence search engine through which you can scan IP, domain, urls.

- GitHub: connector-criminal-ip
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_url_reputation` | Get URL Reputation | investigation | ✓ | `query`(URL, REQ) |
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `query`(IP, REQ) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `query`(Domain, REQ) |

### `crowdsec-cyber-threat-intelligence`

version 1.0.0 — CrowdSec Cyber Threat Intelligence & Service APIs provide a unified, real-time threat intelligence and automation platform that enables orga…

- GitHub: connector-crowdsec-cyber-threat-intelligence
- Category: ['Threat Intelligence']
- Operations: 26

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `search_ip_reputation` | Search IP Reputation | investigation | ✓ | `query`(Query, REQ), `since`(Since), `page`(Page), `limit`(Limit) |
| `batch_get_ip_reputation` | Batch Get IP Reputation | investigation | ✓ | `ips`(IP Addresses, REQ) |
| `get_malevolent_ips` | Get Fire IPs | investigation | ✓ | `page`(Page), `limit`(Limit), `since`(Since) |
| `list_blocklists` | List All Blocklists | investigation | ✓ | — |
| `create_blocklist` | Create New Blocklist | containment | ✓ | `name`(Blocklist Name, REQ), `description`(Description) |
| `update_blocklist` | Update Blocklist | containment | ✓ | `blocklist_id`(Blocklist ID, REQ), `label`(Label, REQ), `description`(Description, REQ), `references`(References, REQ), `tags`(Tags, REQ), `from_cti_query`(CTI Query, REQ), `since`(Since Period, REQ) |
| `add_ips_to_blocklist` | Add IPs to Blocklist | containment | ✓ | `blocklist_id`(Blocklist ID, REQ), `ips`(IP Addresses, REQ), `expiration`(Expiration Date, REQ) |
| `get_blocklist_ips` | Get Blocklist IPs | investigation | ✓ | `blocklist_id`(Blocklist ID, REQ) |
| `delete_ips_from_blocklist` | Delete IPs from Blocklist | containment | ✓ | `blocklist_id`(Blocklist ID, REQ), `ips`(IP Addresses, REQ) |
| `bulk_overwrite_blocklist_ips` | Bulk Overwrite Blocklist IPs | containment | ✓ | `blocklist_id`(Blocklist ID, REQ), `ips`(IP Addresses, REQ), `expiration`(Expiration Date, REQ) |
| `get_blocklist` | Get Specific Blocklist | investigation | ✓ | `blocklist_id`(Blocklist ID, REQ) |
| `delete_blocklist` | Delete Blocklist | containment | ✓ | `blocklist_id`(Blocklist ID, REQ) |
| `list_allowlists` | List All Allowlists | investigation | ✓ | — |
| `create_allowlist` | Create New Allowlist | remediation | ✓ | `name`(Allowlist Name, REQ), `description`(Description) |
| `get_allowlist_items` | Get Items in Allowlist | investigation | ✓ | `allowlist_id`(Allowlist ID, REQ) |
| `add_items_to_allowlist` | Add IPs to Allowlist | remediation | ✓ | `allowlist_id`(Allowlist ID, REQ), `items`(IP Addresses, REQ), `description`(Description), `expiration`(Expiration Date) |
| `get_specific_allowlist_item` | Get Specific Allowlist Item | investigation | ✓ | `allowlist_id`(Allowlist ID, REQ), `item_id`(Item ID, REQ) |
| `update_allowlist` | Update Allowlist | remediation | ✓ | `allowlist_id`(Allowlist ID, REQ), `name`(Name), `description`(Description) |
| `delete_allowlist_item` | Delete Item from Allowlist | remediation | ✓ | `allowlist_id`(Allowlist ID, REQ), `item_id`(Item ID, REQ) |
| `delete_allowlist` | Delete Allowlist | remediation | ✓ | `allowlist_id`(Allowlist ID, REQ), `force`(Force Delete) |
| `list_integrations` | List Integrations | investigation | ✓ | — |
| `create_integration` | Create Integration | remediation | ✓ | `name`(Name, REQ), `description`(Description), `entity_type`(Entity Type, REQ), `output_format`(Output Format, REQ) |
| `get_integration` | Get Integration | investigation | ✓ | `integration_id`(Integration ID, REQ) |
| `update_integration` | Update Integration | remediation | ✓ | `integration_id`(Integration ID, REQ), `name`(Name), `description`(Description), `output_format`(Output Format), `regenerate_credentials`(Regenerate Credentials) |
| `delete_integration` | Delete Integration | remediation | ✓ | `integration_id`(Integration ID, REQ) |

### `csv-data-management`

version 1.3.0 — CSV Data management can perform different operations on CSV files like read file, perform deduplication, merge two CSV files, join two CSV f…

- GitHub: connector-csv-data-management
- Category: —
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `extract_data_from_csv` | Extract Data from Single CSV | investigation | ✗ | `input`(Type, REQ), `value`(Reference ID, REQ), `columnNames`(Column Names), `deDupValuesOn`(Deduplicate Values on), `numberOfRowsToSkip`(Number of rows to skip), `filterInput`(Filter Dataset), `recordBatch`(Convert recordset into batch), `saveAsAttachment`(Save as attachment) |
| `merge_two_csv_and_extract_data` | Merge and Extract Data from two CSV | investigation | ✗ | `input`(Type, REQ), `file_one_value`(First File Reference ID, REQ), `file1_column_names`(First File Column Names), `numberOfRowsToSkipFirst`(Number of rows to skip from First File), `input`(Type, REQ), `file_two_value`(Second File Reference ID, REQ), `file2_column_names`(Second File Column Names), `numberOfRowsToSkipSecond`(Number of rows to skip from Second File), `mergeColumnNames`(Merge on Column, REQ), `deDupValuesOn`(Deduplicate Values on), `filterInput`(Filter Dataset), `recordBatch`(Convert recordset into batch), `saveAsAttachment`(Save as attachment) |
| `concat_two_csv_and_extract_data` | Concat and Extract Data from two CSV | investigation | ✗ | `input`(Type, REQ), `file_one_value`(First File Reference ID, REQ), `file1_column_names`(First File Column Names), `numberOfRowsToSkipFirst`(Number of rows to skip from First File), `input`(Type, REQ), `file_two_value`(Second File Reference ID, REQ), `file2_column_names`(Second File Column Names), `numberOfRowsToSkipSecond`(Number of rows to skip from Second File), `deDupValuesOn`(Deduplicate Values on), `filterInput`(Filter Dataset), `recordBatch`(Convert recordset into batch), `saveAsAttachment`(Save as attachment) |
| `join_two_csv_and_extract_data` | Join and Extract Data from two CSV | investigation | ✓ | `input`(Type, REQ), `file_one_value`(First File Reference ID, REQ), `file1_column_names`(First File Column Names), `numberOfRowsToSkipFirst`(Number of rows to skip from First File), `input`(Type, REQ), `file_two_value`(Second File Reference ID, REQ), `file2_column_names`(Second File Column Names), `numberOfRowsToSkipSecond`(Number of rows to skip from Second File), `deDupValuesOn`(Deduplicate Values on), `filterInput`(Filter Dataset), `recordBatch`(Convert recordset into batch), `saveAsAttachment`(Save as attachment) |
| `convert_json_to_csv_file` | Convert JSON to CSV File | investigation | ✗ | `input`(Input Type, REQ) |

### `csv-feed`

version 1.0.0 — CSV Feed can be used to fetch Threat Intel Feeds from a csv file from any Publicly hosted url or from FortiSOAR Attachment/File. <br/><br/>T…

- GitHub: connector-csv-feed
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_feeds_from_url` | Get Feeds from URL | investigation | ✓ | `col_name`(Column Name, REQ), `delimiter`(Delimiter), `n_rows`(Limit) |
| `get_feeds_from_attachment` | Get Feeds from Attachment | investigation | ✓ | `input`(Input Type, REQ), `value`(Reference ID, REQ), `process_response_as`(Process Response As, REQ), `col_name`(Column Name), `delimiter`(Delimiter), `n_rows`(Limit) |

### `ctm360-cyberblindspot`

version 1.0.0 — CyberBlindspot is CTM360's Digital Risk Protection platform which combines surface, deep, and dark web monitoring, including brand protectio…

- GitHub: connector-ctm360-cyberblindspot
- Category: Threat Intelligence
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_incidents` | Get Incidents | — | ✗ | `date_field`(Date Field), `date_from`(Date From), `date_to`(Date To) |
| `close_incident` | Close Incident | — | ✗ | `ticket_id`(Ticket ID, REQ) |
| `request_takedown` | Request Takedown | investigation | ✓ | `ticket_id`(Ticket ID, REQ) |
| `add_comment` | Add Comment | investigation | ✓ | `ticket_id`(Ticket Id, REQ), `comment`(Comment, REQ) |
| `get_malware_logs` | Get Malware Logs | investigation | ✓ | `date_from`(Date From, REQ), `date_to`(Date To, REQ), `size`(Page Size) |
| `get_breached_credentials` | Get Breached Credentials | investigation | ✓ | `date_from`(Date From, REQ), `date_to`(Date To, REQ), `size`(Page Size) |
| `get_card_leaks` | Get Card Leaks | investigation | ✓ | `date_from`(Date From, REQ), `date_to`(Date To, REQ), `size`(Page Size) |
| `get_domain_protection` | Get Domain Protection | investigation | ✓ | `date_from`(Date From, REQ), `date_to`(Date To, REQ), `type`(Incident Type, REQ), `risk_score_min`(Risk Score Min), `risk_score_max`(Risk Score Max), `finding_status`(Finding Status), `size`(Page Size) |

### `ctm360-cyna`

version 1.0.0 — This connector allows FortiSOAR to pull cyber news from the CTM360 platform to keep security teams informed of the latest threat intelligenc…

- GitHub: connector-ctm360-cyna
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_cyber_news` | Get Cyber News | — | ✗ | `search_after`(Search After), `fields`(Fields), `start_date`(Start Date), `end_date`(End Date), `size`(Size), `search_after`(Offset) |

### `ctm360-hackerview`

version 1.0.0 — HackerView is CTM360’s External Attack Surface Management platform, offering automated asset discovery, issue identification, security ratin…

- GitHub: connector-ctm360-hackerview
- Category: Threat Intelligence
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_issues` | Get Issues | — | ✗ | `first_seen`(First Seen, REQ) |
| `get_domains` | Get Domains | — | ✗ | — |
| `get_hosts` | Get Hosts | — | ✗ | — |
| `get_ip_addresses` | Get IP Addresses | — | ✗ | — |
| `get_resolved_issues` | Get Resolved Issues | — | ✗ | `from_date`(From Date), `to_date`(To Date) |

### `cuckoo`

version 1.1.0 — Cuckoo sandbox is an open source software for automating analysis of suspicious files. To do so it makes use of custom components that monit…

- GitHub: connector-cuckoo
- Category: Malware Analysis
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `submit_file` | Submit File | investigation | ✓ | `file`(File To Detonate, REQ) |
| `submit_url` | Submit URL | investigation | ✓ | `url`(URL To Detonate, REQ) |
| `get_report` | Get Report | investigation | ✓ | `taskid`(Task ID, REQ) |

### `cyberark-aim`

version 1.1.0 — CyberArk Application Identity Manager (AIM) is a key component in CyberArk's Privileged Access Security suite. It helps manage and secure cr…

- GitHub: connector-cyberark-aim
- Category: Vault
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_password` | Get Password | investigation | ✓ | `Folder`(Folder), `UserName`(Username), `Address`(Address), `PolicyID`(Policy ID), `additional_attributes`(Additional Properties) |
| `get_credentials` | Get Credentials | investigation | ✓ | — |
| `get_credentials_details` | Get Credentials Details | investigation | ✓ | `secret_id`(Secret ID, REQ) |
| `get_credential` | Get Credential | investigation | ✓ | `secret_id`(Secret ID, REQ), `attribute_name`(Attribute Name, REQ) |

### `cybereason`

version 1.0.0 — The Cybereason Defense Platform combines endpoint prevention, detection, and response all in one lightweight agent.

- GitHub: connector-cybereason
- Category: Endpoint Security
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_sensors` | Query Sensors | investigation | ✓ | `limit`(Limit), `offset`(Offset), `sortDirection`(Sort Direction), `filter.machineName`(Machine Name), `filter.guid`(Machine GUID), `filter.externalIpAddress`(External IP Address), `filter.internalIpAddress`(Internal IP Address), `filter.customTags`(Custom Tags), `filter.department`(Department), `raw_filters`(Custom Filters) |
| `get_malops` | Get Incidents | investigation | ✓ | `start_time`(Start Time), `end_time`(End Time) |
| `query_user` | Query User | investigation | ✓ | `filter.username`(Username) |
| `query_file` | Query File by its Hash | investigation | ✓ | `filter.filehash`(File Hash, REQ) |
| `query_process` | Get Process On Endpoint | remediation | ✓ | `filter.elementDisplayName`(Process Name), `filter.calculatedUser`(User), `filter.execedBy`(Executed By), `filter.ownerMachine`(Machine Owner), `filter.parentProcess`(Parent Process), `filter.hasOutgoingConnection`(Has Outgoing Connection), `filter.hasModuleFromTempEvidence`(From Temporary Folder), `raw_filters`(Custom Filters) |
| `isolate_sensor_by_pylum_id` | Isolate Malop Machine by Pylum ID | remediation | ✓ | `pylumIds`(Pylum ID(s), REQ) |
| `unisolate_sensor_by_pylum_id` | Un-Isolate Malop Machine by Pylum ID | remediation | ✓ | `pylumIds`(Pylum ID(s), REQ) |
| `isolate_sensor_by_ip` | Isolate Malop Machine by IP Address | remediation | ✓ | `ip_addresses`(Internal IP Address, REQ) |
| `unisolate_sensor_by_ip` | Un-Isolate Malop Machine by IP Address | remediation | ✓ | `ip_addresses`(Internal IP Address, REQ) |
| `kill_process` | Kill Process On Endpoint | remediation | ✓ | `process_guid`(Process GUID, REQ), `machine_guid`(Machine GUID, REQ) |
| `blacklist_file` | Blacklist File | remediation | ✓ | `keys`(File Hash, REQ), `remove`(Remove From List), `prevent`(Prevent Execution) |
| `whitelist_file` | Whitelist File | remediation | ✓ | `keys`(File Hash, REQ), `remove`(Remove From List) |
| `blacklist_ip_or_domain` | Blacklist IP or Domain | remediation | ✓ | `keys`(IPs or Domains, REQ), `remove`(Remove From List) |
| `whitelist_ip_or_domain` | Whitelist IP or Domain | remediation | ✓ | `keys`(IPs or Domains, REQ), `remove`(Remove From List) |

### `cybereason-threat-intel`

version 1.0.0 — Access the Cybereason global threat intelligence database on file hashes, IP addresses, and domains.

- GitHub: connector-cybereason-threat-intel
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `file_batch` | Get File Reputation | enrichment | ✓ | `keys`(File Hash, REQ) |
| `ip_batch` | Get IP Reputation | enrichment | ✓ | `keys`(IP Address, REQ) |
| `domain_batch` | Get Domain Reputation | enrichment | ✓ | `keys`(Domain Name, REQ) |

### `cyble-vision`

version 2.0.0 — Cyble Threat Intel that enables users to access and enrich Indicators of Compromise (IOCs) from Cyble's TAXII Feed service within their envi…

- GitHub: connector-cyble-vision
- Category: Threat Intelligence
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `ioc`(IOC), `type`(Indicator Type), `begin`(Start Time), `end`(End Time), `order`(Order By), `sortBy`(Sort By), `limit`(Limit) |
| `fetch_alerts` | Fetch Alerts | investigation | ✓ | `companyID`(Company ID, REQ), `begin`(Start Time), `end`(End Time), `severity`(Severity), `status`(Status), `service`(Service), `sortBy`(Order By), `limit`(Limit) |
| `list_advisories` | List Advisories | investigation | ✗ | `from`(From DateTime), `to`(To DateTime), `sortBy`(Sort By), `order`(Sort Order), `limit`(Limit), `page`(Page), `customTags`(Custom Tags), `countries`(Countries), `vulnerabilities`(Vulnerabilities) |
| `get_advisory_details` | Get Advisory Details | investigation | ✗ | `advisoryID`(Advisory ID, REQ) |
| `fetch_companies` | Fetch All Users for a Company | investigation | ✗ | — |
| `fetch_ip_details` | Fetch IP Details | investigation | ✗ | `companyId`(Company ID, REQ), `addressIP`(IP Address, REQ) |
| `add_comment_to_alert` | Add Comment to Alert | utilities | ✗ | `alertID`(Alert ID, REQ), `comment`(Comment) |
| `fetch_cve_details` | Fetch CVE Details | investigation | ✗ | `cve`(CVE ID, REQ) |

### `cymulate-asm`

version 1.0.0 — The Cymulate Exposure Management and Security Validation Platform provides the technology for exposure discovery, validation, and prioritiza…

- GitHub: connector-cymulate-asm
- Category: Attack Surface Management
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_internal_assessment` | Create Internal Assessment | investigation | ✓ | `name`(Assessment Name, REQ), `description`(Assessment Description, REQ), `address`(Agent Name, REQ), `agentUserName`(Profile Name, REQ), `selectedPlatforms`(Platforms, REQ), `crownJewels`(Crown Jewels, REQ), `scheduledFor`(Schedule For), `scheduleLoop`(Schedule Loop, REQ) |
| `get_assessment_list` | Get Assessment List | investigation | ✓ | `fromDate`(From Date), `toDate`(To Date) |
| `get_findings_list_for_latest_assessment` | Get Findings List For Latest Assessment | investigation | ✓ | — |
| `get_findings_list_by_assessment_id` | Get Findings List By Assessment ID | investigation | ✓ | `id`(Assessment ID, REQ) |
| `get_assets_list_for_latest_assessment` | Get Assets List For Latest Assessment | investigation | ✓ | — |
| `get_assets_list_by_assessment_id` | Get Assets List By Assessment ID | investigation | ✓ | `id`(Assessment ID, REQ) |
| `get_internal_assessment_list` | Get Internal Assessment List | investigation | ✓ | `skip`(Offset, REQ), `limit`(Limit, REQ) |
| `get_internal_assessment_by_id` | Get Internal Assessment By ID | investigation | ✓ | `id`(Assessment ID, REQ) |
| `delete_internal_assessment_by_id` | Delete Internal Assessment By ID | investigation | ✓ | `id`(Assessment ID, REQ) |

### `cymulate-endpoint-security`

version 1.0.0 — Cymulate’s Endpoint Security vector allows organizations to deploy and run simulations of full attack scenario’s e.g. ransomware or implemen…

- GitHub: connector-cymulate-endpoint-security
- Category: Endpoint Security
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_assessment` | Create Assessment | investigation | ✓ | `agentName`(Agent Name, REQ), `agentProfileName`(Agent Profile Name, REQ), `templateID`(Template ID, REQ), `worm_ipRange_exclude`(Worm IP Range to Exclude, REQ), `scheduleLoop`(Schedule Loop, REQ), `integrationsSelected`(Integrations to Select, REQ), `schedule`(Schedule) |
| `get_latest_report_results` | Get Latest Report Results | investigation | ✓ | `env`(Environment ID) |
| `get_latest_technical_report_results` | Get Latest Technical Report Results | investigation | ✓ | `skip`(Offset), `limit`(Limit), `env`(Environment ID) |
| `get_latest_siem_detection_results` | Get Latest SIEM Detection Results | investigation | ✓ | `env`(Environment ID) |
| `get_detection_results_by_payload_id` | Get Detection Results By Payload ID | investigation | ✓ | `id`(Payload ID, REQ) |
| `get_attack_navigator_results` | Get Attack Navigator Results | investigation | ✓ | `env`(Environment ID) |
| `get_attack_navigator_results_by_assessment_id` | Get Attack Navigator Results By Assessment ID | investigation | ✓ | `id`(Assessment ID, REQ) |
| `get_assessment_history` | Get Assessment History | investigation | ✓ | `fromDate`(From Date), `toDate`(To Date), `env`(Environment ID) |
| `get_technical_report_results_by_assessment_id` | Get Technical Report Results By Assessment ID | investigation | ✓ | `id`(Assessment ID, REQ), `skip`(Offset), `limit`(Limit) |
| `get_executive_report_results_by_assessment_id` | Get Executive Report Results By Assessment ID | investigation | ✓ | `id`(Assessment ID, REQ) |
| `get_template_list` | Get Template List | investigation | ✓ | — |
| `get_template_by_id` | Get Template By ID | investigation | ✓ | `id`(Template ID, REQ) |
| `get_assessment_status` | Get Assessment Status | investigation | ✓ | `id`(Assessment ID) |
| `stop_assessment` | Stop Assessment | investigation | ✓ | `env`(Environment ID) |

### `cymulate-full-kill-chain-campaign`

version 1.0.0 — Cymulate Continuous Automated Red Teaming (CART) validates security controls and responses against real-world cyber attacks to stress-test d…

- GitHub: connector-cymulate-full-kill-chain-campaign
- Category: Breach and Attack Simulation
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_campaign_report` | Get Campaign Report | investigation | ✓ | `env`(Environment ID) |
| `get_campaign_assessments_ids` | Get Campaign Assessments IDs | investigation | ✓ | `env`(Environment ID) |
| `get_technical_report_for_specific_assessment` | Get Technical Report for Specific Assessment | investigation | ✓ | `assessment_id`(Assessment ID, REQ) |
| `launch_campaign_assessment` | Launch Campaign Assessment | investigation | ✓ | `templateID`(Template ID, REQ), `schedule`(Schedule Time, REQ), `scheduleLoop`(Schedule Loop, REQ) |
| `stop_campaign_assessment` | Stop Campaign Assessment | investigation | ✓ | `env`(Environment ID, REQ) |
| `get_campaign_assessment_history` | Get Campaign Assessment History | investigation | ✓ | `env`(Environment ID), `fromDate`(From Date), `toDate`(To Date) |
| `get_specific_campaign_assessment_report` | Get Specific Campaign Assessment Report | investigation | ✓ | `id`(Assessment ID, REQ), `skip`(Index), `limit`(Limit) |
| `get_campaign_assessment_status` | Get Campaign Assessment Status | investigation | ✓ | `id`(Assessment ID) |
| `get_campaign_templates` | Get Campaign Templates | investigation | ✓ | — |

### `cymulate-phishing-awareness`

version 1.0.0 — Cymulate's Phishing Awareness campaigns evaluate employees' security awareness levels by simulating phishing attacks.

- GitHub: connector-cymulate-phishing-awareness
- Category: Security Posture Management
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_phishing_awareness_report` | Get Phishing Awareness Report | investigation | ✓ | `env`(Environment ID) |
| `get_phishing_awareness_assessment_id` | Get Phishing Awareness assessment IDs | investigation | ✓ | `env`(Environment ID) |
| `get_phishing_awareness_report_for_specific_assessment` | Get Phishing Awareness Report for Specific Assessment | investigation | ✓ | `id`(Assessment ID, REQ) |
| `get_phishing_awareness_assessment_history` | Get Phishing Awareness Assessment History | investigation | ✓ | `fromDate`(From Date), `toDate`(To Date), `env`(Environment ID) |
| `get_phishing_awareness_campaign_report_for_specific_assessment` | Get Phishing Awareness Campaign Report for Specific Assessment | investigation | ✓ | `id`(Assessment ID, REQ), `skip`(Offset), `limit`(Limit) |
| `create_phishing_awareness_contact_group` | Create Phishing Awareness Contact Group | investigation | ✓ | `groupName`(Group Name) |
| `get_phishing_awareness_contact_groups` | Get Phishing Awareness Contact Groups | investigation | ✓ | — |
| `get_phishing_awareness_contacts` | Get Phishing Awareness Contacts | investigation | ✓ | `groupId`(Group ID) |

### `cymulate-web-application-firewall`

version 1.0.0 — The Cymulate Web Application Firewall will validate the configuration, implementation, and efficacy, to ensure that the Web Application Fire…

- GitHub: connector-cymulate-web-application-firewall
- Category: Firewall and Network Protection
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_waf_report_results` | Get WAF Report Results | investigation | ✓ | `env`(Environment ID) |
| `get_waf_site_results` | Get WAF Site Results | investigation | ✓ | `env`(Environment ID) |
| `get_waf_payload_response` | Get WAF Payload Response | investigation | ✓ | `id`(Payload ID, REQ) |
| `get_technical_report_results` | Get Technical Report Results | investigation | ✓ | `SiteID`(Site ID, REQ), `skip`(Offset), `limit`(Limit) |
| `launch_waf_assessment` | Launch WAF Assessment | investigation | ✓ | `sites`(Sites, REQ), `templateID`(Template ID, REQ), `schedule`(Schedule), `scheduleLoop`(Schedule Loop, REQ) |
| `stop_waf_assessment` | Stop WAF Assessment | investigation | ✓ | `env`(Environment ID) |
| `get_waf_assessment_history` | Get WAF Assessment History | investigation | ✓ | `fromDate`(From Date), `toDate`(To Date), `env`(Environment ID) |
| `get_technical_report_results_by_id` | Get Technical Report Results By Assessment ID | investigation | ✓ | `id`(Assessment ID, REQ), `skip`(Offset), `limit`(Limit) |
| `get_executive_report_results_by_id` | Get Executive Report Results By Assessment ID | investigation | ✓ | `id`(Assessment ID, REQ) |
| `get_waf_site_ids` | Get WAF Site IDs | investigation | ✓ | — |
| `get_waf_sites` | Get WAF Sites | investigation | ✓ | — |
| `get_waf_templates` | Get WAF Templates | investigation | ✓ | — |
| `get_waf_template_by_id` | Get WAF Template By ID | investigation | ✓ | `id`(Template ID, REQ) |
| `get_waf_assessment_status` | Get WAF Assessment Status | investigation | ✓ | `id`(Assessment ID) |

### `cyolo`

version 1.0.0 — Cyolo helps enterprises provide their global workforce with convenient and secure access to applications, resources, workstations, servers, …

- GitHub: connector-cyolo
- Category: Identity and Access Management
- Operations: 18

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_users` | Get Users List | investigation | ✓ | — |
| `list_user_policies` | Get User Policies | investigation | ✓ | `id`(User ID, REQ) |
| `get_user_by_id_or_name` | Get User By ID Or Name | investigation | ✓ | `id`(User ID Or Name, REQ) |
| `delete_user_by_id_or_name` | Delete User By ID Or Name | investigation | ✓ | `id`(User ID Or Name, REQ) |
| `list_policies` | Get Policy List | investigation | ✓ | — |
| `get_policy_by_id_or_name` | Get Policy By ID Or Name | investigation | ✓ | `id`(Policy ID Or Name, REQ) |
| `list_simple_groups` | Get Simple Group List | investigation | ✓ | — |
| `list_dynamic_groups` | Get Dynamic Group List | investigation | ✓ | — |
| `list_constraints` | Get Constraints List | investigation | ✓ | — |
| `list_capabilities` | Get Capabilities List | investigation | ✓ | — |
| `list_mappings` | Get Mappings List | investigation | ✓ | — |
| `list_webhooks` | Get Webhooks List | investigation | ✓ | — |
| `list_device_posture_profiles` | Get Device Posture Profiles List | investigation | ✓ | — |
| `list_mapping_categories` | Get Mapping Categories List | investigation | ✓ | — |
| `list_certificates` | Get Certificates List | investigation | ✓ | — |
| `create_policy` | Create Policy | investigation | ✓ | `name`(Name, REQ), `enabled`(Enabled), `dynamic_groups`(Dynamic Groups), `simple_groups`(Simple Groups), `mappings`(Applications), `mapping_categories`(Application Categories), `supervisors`(Supervisors), `users`(Users), `webhooks`(Webhooks), `timed_access_status`(Enable Time Access), `start`(Start), `end`(End), `days`(Days), `trusted_certificates`(Trusted Certificates), `device_posture_profiles`(Device Posture Profiles), `capabilities`(Capabilities), `constraints`(Constraints) |
| `update_policy` | Update Policy | investigation | ✓ | `id`(Policy ID, REQ), `name`(Name), `enabled`(Enabled), `dynamic_groups`(Dynamic Groups), `simple_groups`(Simple Groups), `mappings`(Application), `mapping_categories`(Application Categories), `supervisors`(Supervisors), `users`(Users), `webhooks`(Webhooks), `timed_access_status`(Enable Time Access), `start`(Start), `end`(End), `days`(Days), `trusted_certificates`(Trusted Certificates), `device_posture_profiles`(Device Posture Profiles), `capabilities`(Capabilities), `constraints`(Constraints) |
| `delete_user_from_policy` | Delete User From Policy | investigation | ✓ | `id`(Policy ID, REQ), `users`(Users, REQ) |

### `cyren`

version 1.0.0 — Cyren is leading a revolution in internet security by utilizing extensive cloud intelligence to provide the fastest protection available. Th…

- GitHub: connector-cyren
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_url_lookup` | Get URL Lookup | investigation | ✓ | `input_type`(Input Type, REQ), `value`(Lookup URL, REQ) |

### `cyware-ctix`

version 2.0.0 — Allows user to search for URL, Domain and IP,Hash and CVE ID, chooses the matching element, and displays relevant details.

- GitHub: connector-cyware-ctix
- Category: Threat Intelligence
- Operations: 33

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_domain` | Search Domain | investigation | ✓ | `domain`(Domain, REQ), `page_size`(Page Size) |
| `search_ip` | Search IP | investigation | ✓ | `ip`(IP Address, REQ), `page_size`(Page Size) |
| `search_url` | Search URL | investigation | ✓ | `url`(URL, REQ), `page_size`(Page Size) |
| `search_hash` | Search Hash | investigation | ✓ | `hash`(Hash, REQ), `page_size`(Page Size) |
| `search_cve_id` | Search CVE ID | investigation | ✓ | `cve_id`(CVE ID, REQ), `page_size`(Page Size) |
| `get_supported_allowed_indicator_types_list` | Get Supported Allowed Indicator Types List | investigation | ✗ | `q`(Query String) |
| `bulk_lookup_and_create` | Bulk Lookup and Create (Deprecated) | investigation | ✗ | `ioc_values`(Indicator Values, REQ), `create`(Create Records), `enrichment`(Enrich Records), `metadata`(Metadata), `source`(Source), `collection`(Collection) |
| `create_intel_via_open_api` | Create Intel via Open API | investigation | ✗ | `title`(Title, REQ), `allSDOS`(All SDOS, REQ), `source`(Source), `collection`(Collection), `metadata`(Metadata) |
| `list_threat_data` | Get Threat Data | investigation | ✗ | `query`(Query, REQ), `page`(Page), `page_size`(Page Size), `page_limit`(Page Limit), `enrichment`(Enrichment), `sort`(Sort) |
| `bulk_add_relation` | Bulk Add Relation | investigation | ✗ | `object_ids`(Object Ids, REQ), `object_type`(Object Type, REQ), `data`(Data, REQ) |
| `bulk_deprecate_undeprecate_objects` | Bulk Deprecate/Undeprecate Objects | investigation | ✗ | `object_ids`(Object Ids, REQ), `object_type`(Object Type, REQ), `action_type`(Action Type, REQ) |
| `bulk_mark_unmark_false_positive` | Bulk Mark/Unmark False Positive | remediation | ✗ | `object_ids`(Object Ids, REQ), `object_type`(Object Type, REQ), `action_type`(Action Type, REQ) |
| `bulk_ioc_lookup_and_create_intel` | Bulk IOC Lookup and Create Intel | investigation | ✗ | `ioc_values`(Indicator Values, REQ), `source`(Source), `collection`(Collection), `metadata`(Metadata), `create`(Create Records), `enrichment`(Enrich Records) |
| `bulk_ioc_lookup_advanced` | Bulk IOC Lookup (Advanced) | investigation | ✗ | `object_type`(Object Type, REQ), `value`(Value, REQ), `objectID`(Object ID), `enrichment_data`(Enrichment Data), `relation_data`(Relation Data), `enrichment_tools`(Enrichment Tools), `fields`(Fields) |
| `list_threat_data_object_details` | Get Threat Data Object Details List | investigation | ✗ | `object_type`(Object Type, REQ), `objectID`(Object ID, REQ) |
| `threat_data_object_advanced_details` | Get Threat Data Object Additional Details | investigation | ✗ | `object_type`(Object Type, REQ), `object_id`(Object ID, REQ) |
| `list_relations_of_threat_data_object` | Get Relations List of Threat Data Object | investigation | ✗ | `objectID`(Object ID, REQ), `objectType`(Object Type, REQ), `sources`(Sources), `page`(Page), `page_size`(Page Size) |
| `create_threat_bulletin` | Create Threat Bulletin | investigation | ✗ | `title`(Title, REQ), `description`(Description), `status`(Status, REQ), `tlp`(Tlp), `server_collections`(Server Collections), `tags`(Tags), `attachments`(Attachments) |
| `update_threat_bulletin` | Update Threat Bulletin | investigation | ✗ | `threat_bulletin_id`(Threat Bulletin ID, REQ), `title`(Title, REQ), `description`(Description), `status`(Status, REQ), `server_collections`(Server Collections), `tags`(Tags) |
| `list_rules` | List Rules | investigation | ✗ | `page`(Page), `pageSize`(Page Size), `source`(Source), `createdByID`(Created By ID), `status`(Status), `lastActiveTo`(Last Active To), `lastActiveFrom`(Last Active From), `createdFrom`(Created From), `createdTo`(Created To), `isManualRun`(Is Manual Run) |
| `run_rule` | Run Rule | investigation | ✗ | `rule`(Rule, REQ), `startTime`(Start Time, REQ), `endTime`(End Time, REQ) |
| `enrichment_tools` | Get Enrichment Tool List | investigation | ✗ | `action_name`(Action Name, REQ), `component`(Component), `full_list`(Full List) |
| `get_enrichment_object_details` | Get Enrichment Object Details | investigation | ✗ | `object_type`(Object Type, REQ), `objectID`(Object ID, REQ), `toolID`(Tool ID, REQ) |
| `get_enriched_threat_data` | Get Enriched Threat Data | investigation | ✗ | `app_slug`(App Slug, REQ), `value`(Value, REQ), `action_slug`(Action Slug, REQ), `objectID`(Object ID, REQ), `object_type`(Object Type, REQ) |
| `add_note_to_threat_data_object` | Add Note to Threat Data Object | investigation | ✗ | `object_id`(Object Id, REQ), `text`(Text, REQ), `type`(Type, REQ), `meta_data`(Meta Data), `is_json`(Is Json, REQ) |
| `create_tag` | Create Tag | utilities | ✗ | `name`(Name, REQ), `colour_code`(Colour Code, REQ) |
| `delete_tag` | Delete Tag | utilities | ✗ | `tag_id`(Tag ID, REQ) |
| `list_allowed_indicators` | List Allowed Indicators | investigation | ✗ | `type`(Type), `page`(Page), `page_size`(Page Size), `created_by_id`(Created by Id), `modified_by_id`(Modified by Id), `created_from`(Created From), `created_to`(Created To), `last_active_from`(Last Active From), `last_active_to`(Last Active To), `sort`(Sort) |
| `delete_allowed_indicator` | Delete Allowed Indicator | containment | ✗ | `indicator_id`(Indicator Id, REQ) |
| `list_reports` | List Reports | — | ✗ | `type`(Type), `page`(Page), `page_size`(Page Size), `repeat_type`(Repeat Type), `shared_type`(Shared Type), `created_by`(Created By), `modified_by`(Modified By), `created_to`(Created To), `created_from`(Created From), `modified_from`(Modified From), `modified_to`(Modified To), `date_last_run_from`(Date Last Run From), `date_last_run_to`(Date Last Run To) |
| `create_report` | Create Report | utilities | ✗ | `name`(Name, REQ), `type`(Type), `basic_report_type`(Basic Report Type), `shared_type`(Shared Type, REQ), `saved_search`(Saved Search, REQ), `schedule`(Schedule, REQ), `file_types`(File Types, REQ), `columns`(Columns, REQ), `internal_recipients`(Internal Recipients), `query_key`(Query Key), `external_recipients`(External Recipients) |
| `run_report` | Run Report | remediation | ✗ | `report_id`(Report ID, REQ), `type`(Type, REQ), `start_time`(Start Time, REQ), `end_time`(End Time, REQ), `file_types`(File Types), `internal_recipients`(Internal Recipients), `external_recipients`(External Recipients) |
| `create_custom_attribute` | Create Custom Attribute | utilities | ✗ | `name`(Name, REQ), `description`(Description), `type`(Type, REQ), `choices`(Choices), `is_actionable`(Is Actionable), `status`(Status), `sdo_objects`(Sdo Objects) |

### `cyware-ctix-feed`

version 1.1.0 — An automated Threat Intelligence Platform (TIP) for ingestion, enrichment, analysis, prioritization, actioning, and bidirectional sharing of…

- GitHub: connector-cyware-ctix-feed
- Category: Threat Intelligence Exchange
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_save_result_set_data` | Get Save Result Set Data | investigation | ✓ | `label_name`(Label Name), `from_timestamp`(Start Datetime), `to_timestamp`(End Datetime), `page_size`(Limit, REQ), `page`(Offset, REQ) |
| `get_save_result_set_indicators` | Get Save Result Set Indicators | investigation | ✓ | `label_name`(Label Name), `from_timestamp`(Start Datetime), `to_timestamp`(End Datetime), `record_number`(Number of Records to Return, REQ) |
| `get_threat_data` | Get Threat Data | investigation | ✓ | `query`(CQL Query, REQ), `page`(Page Number), `page_size`(Page Size), `page_limit`(Limit), `enrichment`(Enrichment), `sort`(Sort), `fetch_all_records`(Fetch All Records) |

### `databricks`

version 1.0.1 — Query an Azure Databricks Cluster table in a catalog's schema (database). Uses Databricks SQL Connector for Python.

- GitHub: connector-databricks
- Category: Database
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `run_query` | Run Query | investigation | ✓ | `query_string`(Query String, REQ) |

### `datadog-siem-cloud`

version 1.0.0 — Datadog Cloud SIEM is a real time threat detection platform paired with rich observability context to achieve faster security outcomes.

- GitHub: connector-datadog-siem-cloud
- Category: Analytics and SIEM
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_incidents` | Get Incidents | investigation | ✓ | `include`(Include), `page_offset`(Offset), `page_size`(Limit) |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `search_incidents` | Search Incidents | investigation | ✓ | `created_after`(Start Datetime), `created_before`(End Datetime), `state`(State), `severity`(Severity), `customer_impacted`(Customer Impacted), `detection_method`(Detection Method), `sort`(Sort), `include`(Include), `offset`(Offset), `limit`(Limit), `fetch_all_incidents`(Fetch All Incidents) |
| `update_incident` | Update Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `customer_impact_end`(Customer Impact End Date), `customer_impact_scope`(Customer Impact Scope), `customer_impact_start`(Customer Impact Start Date), `customer_impacted`(Customer Impacted), `detected`(Detected Date), `state`(State), `severity`(Severity), `detection_method`(Detection Method), `root_cause`(Root Cause), `title`(Title), `summary`(Summary) |
| `search_events` | Search Events | investigation | ✓ | `from`(Start Datetime), `to`(End Datetime), `query`(Query), `time_difference`(Time Difference), `sort`(Sort), `cursor`(Cursor), `limit`(Limit) |
| `get_event_details` | Get Event Details | investigation | ✓ | `event_id`(Event ID, REQ) |
| `get_hosts` | Get Hosts | investigation | ✓ | `filter`(Filter), `sort_field`(Sort Field), `sort_dir`(Sort Order), `start`(Offset), `count`(Limit), `_from`(Start Datetime), `include_muted_hosts_data`(Include Muted Hosts Data), `include_hosts_metadata`(Include Hosts Metadata) |
| `get_attachments` | Get Attachments | investigation | ✓ | `incident_id`(Incident ID, REQ) |

### `dnstwist`

version 1.0.0 — DNSTwist is a python script used for detecting phishing attacks, typo squatters, and attack domains.

- GitHub: connector-dnstwist
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search` | Search Registered Domains | investigation | ✓ | `domain`(Domain, REQ) |

### `domain-analysis`

version 1.0.0 — Whois for IPs, Domains and ASNs in addition to DGA detection and domain popularity lookup

- GitHub: connector-domain-analysis
- Category: Enrichment
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `analyze_domain` | Analyze Domain | — | ✓ | `domain`(Domain Name, REQ) |
| `get_domain_popularity` | Get Domain Popularity | — | ✓ | `domain`(Domain Name, REQ), `list_date`(List Date) |
| `whois` | Whois | — | ✓ | `input_value`(Input Value, REQ) |
| `get_domain_report` | Get Domain Report | — | ✓ | `domain`(Domain Name, REQ) |

### `doppel`

version 1.1.0 — Doppel is a next-generation AI security company that specializes in protecting organizations from social engineering attacks, impersonation,…

- GitHub: connector-doppel
- Category: Threat Intelligence
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_alerts` | Get All Alerts | investigation | ✓ | `search_key`(Search Key), `queue_state`(Queue State), `product`(Product), `created_after`(Created After), `created_before`(Created Before), `last_activity_timestamp`(Last Activity Timestamp), `sort_type`(Sort Type), `sort_order`(Order By), `page`(Page Number), `tags`(Tags) |
| `get_alert_details` | Get Alert Details | investigation | ✓ | `id`(Alert ID), `entity`(Entity) |
| `update_alert` | Update Alert | investigation | ✓ | `id`(Alert ID), `entity`(Entity), `queue_state`(Queue State), `entity_state`(Entity State), `comment`(Comment), `tag_action`(Action on Tag), `tag_name`(Tag Name) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `dragos-sitestore`

version 1.0.0 — Dragos SiteStore is a key component of the Dragos Platform, designed to enhance cybersecurity for industrial control systems (ICS) and opera…

- GitHub: connector-dragos-sitestore
- Category: Asset Management
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_assets` | Get All Assets | investigation | ✓ | `createdAtAfter`(Created After), `createdAtBefore`(Created Before), `lastSeenAtAfter`(LastSeen After), `lastSeenAtBefore`(LastSeen Before), `is_deleted`(Include Deleted Assets), `overlaps_starttime`(Overlaps Address Start DateTime), `overlaps_endtime`(Overlaps Address End DateTime), `maskAddress_starttime`(Mask Address Start DateTime), `maskAddress_endtime`(Mask Address End DateTime), `sort_by`(Sort By), `order_by`(Order By), `pageSize`(Page Size), `pageNumber`(Page Number), `limitTotalCount`(Limit Total Count), `additional_fields`(Additional Parameters) |
| `get_notifications` | Get All Notifications | investigation | ✓ | `filter`(Filter), `createdAtAfter`(Created After), `state`(State), `sorts`(Sorts), `sortField`(Sort By), `sortDescending`(Order By), `resolveChildrenDepth`(Resolve Children Depth), `offset`(Offset), `pageSize`(Page Size), `pageNumber`(Page Number), `limitTotalCount`(Limit Total Count), `additional_fields`(Additional Parameters) |
| `get_notification_details` | Get Notifications Details | investigation | ✓ | `ids`(Notification IDs, REQ), `resolveChildrenDepth`(Resolve Children Depth), `includeConversations`(Include Conversations) |
| `get_stats_of_notification` | Get Statistics of Notification | investigation | ✓ | `groupBy`(Group By, REQ), `filter`(Filter) |
| `get_vulnerabilities` | Get All Vulnerabilities | investigation | ✓ | `sort_by`(Sort By), `order_by`(Order By), `pageSize`(Page Size), `pageNumber`(Page Number), `limitTotalCount`(Limit Total Count), `additional_fields`(Additional Parameters) |
| `get_vulnerability_detections` | Get All Vulnerability Detections | investigation | ✓ | `sort_by`(Sort By), `order_by`(Order By), `pageSize`(Page Size), `pageNumber`(Page Number), `limitTotalCount`(Limit Total Count), `additional_fields`(Additional Parameters) |
| `get_detections` | Get All Detections | investigation | ✓ | `includeFields`(Include Fields), `excludeFields`(Exclude Fields), `sort_by`(Sort By), `order_by`(Order By), `pageSize`(Page Size), `pageNumber`(Page Number), `limitTotalCount`(Limit Total Count), `additional_fields`(Additional Parameters) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `dragos-worldview-threat-intelligence`

version 1.1.0 — Dragos WorldView industrial threat intelligence provides actionable information and recommendations on threats to operations technology (OT)…

- GitHub: connector-dragos-worldview-threat-intelligence
- Category: Threat Intelligence
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_indicators` | Get All Indicators | investigation | ✓ | `value`(Indicator Value), `type`(Indicator Type), `updated_after`(Updated After), `serial`(Report Serial Numbers), `tags`(Tags), `record_number`(Number of Records to Return, REQ) |
| `get_all_indicators_in_stix2` | Get All Indicators In Stix2 | investigation | ✓ | `value`(Indicator Value), `type`(Indicator Type), `page_size`(Page Size), `page`(Page Number), `updated_after`(Updated After), `serial`(Report Serial Numbers), `tags`(Tags) |
| `get_all_reports` | Get All Reports | investigation | ✓ | `sort_by`(Sort By), `sort_order`(Sort Order), `page`(Page Number), `page_size`(Page Size), `updated_after`(Updated After), `serials`(Report Serial Numbers), `indicator`(Indicator) |
| `get_report_metadata` | Get Report Metadata | investigation | ✓ | `report_serial_number`(Report Serial Number, REQ) |
| `get_indicators_of_report` | Get Indicators Of Report | investigation | ✓ | `process_response_as`(Process Response As, REQ), `report_serial_number`(Report Serial Number, REQ) |
| `get_all_tags` | Get All Tags | investigation | ✓ | `page`(Page Number), `page_size`(Page Size), `tag_type`(Tag Type) |

### `ducont-sms`

version 1.0.0 — The WCF Restful Service - Push SMS supports single and bulk messages request with parameterized or customized message.

- GitHub: connector-ducont-sms
- Category: Communication and Coordination
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `push_sms` | Push SMS | investigation | ✓ | `recipients`(Recipient Mobile Numbers, REQ), `body`(Body, REQ), `sender_id`(Sender ID, REQ), `message_id`(Message ID, REQ), `priority`(Priority, REQ), `channel_id`(Channel ID), `template_id`(Template ID), `template_variables`(Template Variables), `validity_period`(Validity Period, REQ), `language_id`(Language ID, REQ), `confirm_delivery`(Confirm Delivery) |
| `push_sms_sub` | Push SMS SUB | investigation | ✓ | `recipients`(Recipient Mobile Numbers, REQ), `body`(Body, REQ), `channel_id`(Channel ID), `sender_id`(Sender ID, REQ), `message_id`(Message ID, REQ), `priority`(Priority, REQ), `template_id`(Template ID), `template_variables`(Template Variables), `validity_period`(Validity Period, REQ), `language_id`(Language ID, REQ), `confirm_delivery`(Confirm Delivery, REQ) |

### `eclecticiq`

version 1.2.0 — EclecticIQ is a global threat intelligence, hunting and response technology provider. This connector facilitates the automated operations li…

- GitHub: connector-eclecticiq
- Category: Threat Intelligence
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `observable`(IP Address, REQ), `is_parsed_response`(Parsed Response) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `observable`(Domain, REQ), `is_parsed_response`(Parsed Response) |
| `get_email_reputation` | Get Email Reputation | investigation | ✓ | `observable`(Email, REQ), `is_parsed_response`(Parsed Response) |
| `get_file_reputation` | Get Filename or Hash Reputation | investigation | ✓ | `observable`(Filename or Hash, REQ), `is_parsed_response`(Parsed Response) |
| `get_uri_reputation` | Get URL Reputation | investigation | ✓ | `observable`(URL, REQ), `is_parsed_response`(Parsed Response) |
| `query_entities` | Query Entities | investigation | ✓ | `query`(Search Observable), `entity_value`(Search Text into Entities Title), `entity_type`(Entity Type to Query, REQ), `size`(Number of Entities to Fetch), `from`(Fetch Entities From) |
| `create_sighting` | Create Sighting | investigation | ✓ | `sighting_title`(Sighting Title, REQ), `sighting_description`(Sighting Description), `observable_value`(Observable Value, REQ), `observable_type`(Observable type, REQ), `observable_maliciousness`(Observable maliciousness, REQ), `confidence_value`(Confidence value, REQ), `impact_value`(Impact value, REQ), `tags`(Sighting Tags, REQ) |

### `elastic-kibana`

version 1.0.0 — Elastic Kibana provides a powerful UI for interacting with the Elastic Stack. It enables users to search, visualize, and manage data from El…

- GitHub: connector-elastic-kibana
- Category: ['Analytics and SIEM']
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_data_views` | Get All Data Views | investigation | ✓ | — |
| `get_saved_queries` | Get Saved Queries | investigation | ✓ | — |
| `create_a_live_query` | Create Live Query | investigation | ✓ | `query`(Query, REQ), `agent_ids`(Agent IDs, REQ), `agent_platforms`(Agent Platforms, REQ), `agent_policy_ids`(Agent Policy IDs), `alert_ids`(Alert IDs), `case_ids`(Case IDs), `ecs_mapping`(ECS Mapping), `event_ids`(Event IDs), `metadata`(Metadata), `pack_id`(Pack ID) |
| `get_live_query_results` | Get Live Query Results | investigation | ✓ | `id`(Query ID, REQ), `actionId`(Query Action ID, REQ) |
| `search_cases` | Search cases | investigation | ✓ | `assignees`(Assignees), `category`(Category), `defaultSearchOperator`(Default Search Operator), `from_`(From DateTime), `to`(To DateTime), `owner`(Owner), `reporters`(Reporters), `search`(Search Query), `searchFields`(Search Fields), `severity`(Severity), `status`(Status), `tags`(Tags), `sortField`(Sort Field), `sortOrder`(Sort Order), `page`(Page Number), `perPage`(Page Size) |
| `get_case_information` | Get Case Information | investigation | ✓ | `caseId`(Case ID, REQ) |
| `add_and_remove_detection_alert_tags` | Add and Remove Detection Alert Tags | investigation | ✓ | `ids`(Alert IDs, REQ), `tags`(Tags, REQ) |
| `generic_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `api_endpoint`(Endpoint, REQ), `params`(Query Parameters), `json_data`(Request Payload) |
| `generic_action` | (Deprecation Warning) Generic Action | investigation | ✓ | `method`(HTTP Method, REQ), `apiendpoint`(Endpoint, REQ), `data`(Request Payload), `params`(Query Parameters) |

### `elastic-security`

version 1.0.0 — Elastic Security provides threat prevention, detection, and response capabilities built on the Elastic Stack. It unifies SIEM, endpoint secu…

- GitHub: connector-elastic-security
- Category: ['Analytics and SIEM']
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_the_cluster_health_status` | Get Cluster Health Status | investigation | ✓ | `index`(Index, REQ) |
| `get_eql_search_results` | Get EQL Search Results | investigation | ✓ | `index`(Index, REQ), `query`(Query, REQ) |
| `run_an_esql_query` | Run an ES\|QL Query | investigation | ✓ | `query`(Query, REQ), `format`(Format), `delimiter`(Delimiter), `drop_null_columns`(Remove Empty Columns), `allow_partial_results`(Allow Partial Results) |
| `generic_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `api_endpoint`(Endpoint, REQ), `params`(Query Parameters), `json_data`(Request Payload) |
| `get_status` | (Deprecation Warning) Get Status | investigation | ✓ | — |
| `eql_search_api` | (Deprecation Warning) EQL Search API | investigation | ✓ | `target`(Index, REQ), `data`(Query, REQ) |
| `esql_search_api` | (Deprecation Warning) ESQL Search API | investigation | ✓ | `data`(Query, REQ) |
| `generic_action` | (Deprecation Warning) Generic Action | investigation | ✓ | `method`(HTTP Method, REQ), `apiendpoint`(Endpoint, REQ), `data`(Request Payload), `params`(Query Parameters) |

### `eset-protect-enterprise`

version 1.0.0 — ESET Protect Enterprise extended detection and response (XDR) that delivers enterprise-grade visibility, threat hunting and response options…

- GitHub: connector-eset-protect-enterprise
- Category: Endpoint Security
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_executables` | Get Executables List | investigation | ✓ | `server_url`(Application Management URL, REQ), `executableUuid`(Executable UUID), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_device_tasks` | Get Device Tasks List | investigation | ✓ | `server_url`(Server URL, REQ), `task_uuid`(Task UUID), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_detections` | Get Detections List | investigation | ✓ | `server_url`(Incident Management URL, REQ), `detectionUuid`(Detection UUID), `deviceUuid`(Device UUID), `start_time`(Start Time), `end_time`(End Time), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_detection_groups` | Get Detection Groups List | investigation | ✓ | `server_url`(Incident Management URL, REQ), `detectionGroupUuid`(Detection Group UUID), `deviceUuid`(Device UUID), `start_time`(Start Time), `end_time`(End Time), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_device` | Get Device by UUID | investigation | ✓ | `server_url`(Server URL, REQ), `deviceUuid`(Device UUID, REQ) |
| `get_device_groups` | Get Device Groups List | investigation | ✓ | `server_url`(Server URL, REQ), `groupUuid`(Group UUID), `pageSize`(Page Size), `pageToken`(Page Token) |
| `create_device_tasks` | Create Device Task | containment | ✓ | `server_url`(Server URL, REQ), `task_payload`(Task Payload, REQ) |
| `isolate_computer_from_network` | Isolate Computer From Network | containment | ✓ | `server_url`(Server URL, REQ), `device_uuid`(Device UUID, REQ), `device_group_uuid`(Device Group UUID, REQ), `task_expire_time`(Task Expire Time in minutes, REQ), `task_display_name`(Task Display Name), `task_description`(Task Description) |
| `end_computer_isolation_from_network` | End Computer Isolation From Network | containment | ✓ | `server_url`(Server URL, REQ), `device_uuid`(Device UUID, REQ), `device_group_uuid`(Device Group UUID, REQ), `task_expire_time`(Task Expire Time in minutes, REQ), `task_display_name`(Task Display Name), `task_description`(Task Description) |
| `block_executables` | Block Executables | containment | ✓ | `server_url`(Application Management URL, REQ), `executableUuid`(Executable UUID), `json_data`(Request Body) |
| `unblock_executables` | Unblock Executables | remediation | ✓ | `server_url`(Application Management URL, REQ), `executableUuid`(Executable UUID), `json_data`(Request Body) |

### `everbridge`

version 1.0.0 — Everbridge that provides enterprise software applications that automate and accelerate organizations operational response to critical events…

- GitHub: connector-everbridge
- Category: OT & IoT Security
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_organizations_list` | Get Organizations List | investigation | ✓ | — |
| `get_incident_list` | Get Incident List | investigation | ✓ | `organizationId`(Organization ID, REQ), `dateType`(Date Type), `startTime`(Start Time), `endTime`(End Time), `incidentType`(Incident Type), `status`(Incident Status), `onlyOpen`(Only Open), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `organizationId`(Organization ID, REQ), `incidentId`(Incident ID, REQ) |
| `update_incident` | Update Incident | investigation | ✓ | `organizationId`(Organization ID, REQ), `incidentId`(Incident ID, REQ), `incidentAction`(Incident Action, REQ), `incidentStatus`(Incident Status), `incidentType`(Incident Type), `incidentMode`(Incident Mode), `name`(Incident Name), `closeBy`(Close By), `additional_fields`(Additional Fields) |
| `get_assets_list` | Get Assets List | investigation | ✓ | `organizationId`(Organization ID, REQ), `pageNumber`(Page Number) |
| `get_asset_details` | Get Asset Details | investigation | ✓ | `organizationId`(Organization ID, REQ), `id`(Asset/External ID, REQ) |
| `update_asset` | Update Asset | investigation | ✓ | `organizationId`(Organization ID, REQ), `id`(Asset ID, REQ), `autoGeoCoding`(Geo Coding), `name`(Name), `floorNo`(Floor No), `street`(Street), `city`(City), `state`(State), `country`(Country), `countryFullName`(Country Full Name), `postalCode`(Postal Code) |

### `excel-tools`

version 1.0.0 — Utility to manage excel files

- GitHub: connector-excel-tools
- Category: Utilities
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `read_sheet` | Read Sheet | — | ✓ | `file_iri`(File IRI, REQ), `sheet_name`(Sheet Name, REQ), `use_column_title`(Use Column Title) |
| `read_column_by_name` | Read Column By Name | — | ✓ | `file_iri`(File IRI, REQ), `sheet_name`(Sheet Name, REQ), `column_name`(Column Name, REQ) |
| `update_column` | Update Column | — | ✓ | `file_iri`(File IRI, REQ), `sheet_name`(Sheet Name, REQ), `select_column`(Select Column By, REQ) |
| `update_cell` | Update Cell | — | ✓ | `file_iri`(File IRI, REQ), `sheet_name`(Sheet Name, REQ), `cell_id`(Cell ID, REQ), `cell_value`(Value, REQ) |
| `list_sheets` | List Sheets | — | ✓ | `file_iri`(File IRI, REQ) |

### `exploit-prediction-scoring-system`

version 1.0.0 — The Exploit Prediction Scoring System (EPSS) is a framework used in cybersecurity to assess the likelihood of a vulnerability being exploite…

- GitHub: connector-exploit-prediction-scoring-system
- Category: Utilities
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_epss_score` | Get EPSS Score | investigation | ✓ | `scope`(Scope, REQ), `byDate`(By Date), `fields`(Fields), `limit`(Limit), `offset`(Offset), `sort`(Sort), `envelope`(Envelope), `pretty`(Pretty), `orderResult`(Order Result) |
| `get_epss_score_by_cve_id` | Get EPSS Score By CVE ID | investigation | ✓ | `scope`(Scope), `cve`(CVE ID, REQ), `byDate`(By Date), `fields`(Fields), `sort`(Sort), `envelope`(Envelope), `pretty`(Pretty), `orderResult`(Order Result) |

### `fastly-next-gen-waf`

version 1.0.0 — Fastly Next-Gen WAF offers advanced web application protection with automated security measures, real-time monitoring, and rapid incident re…

- GitHub: connector-fastly-next-gen-waf
- Category: Firewall and Network Protection
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_site_allow_list` | Get Site Allow List | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ) |
| `add_ip_to_allow_list` | Add IP Address to Allow List | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `source`(IP Address, REQ), `note`(Note), `expires`(Expiry Date) |
| `remove_ip_from_allow_list` | Remove IP Address from Allow List | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `id`(IP Address ID, REQ) |
| `get_site_block_list` | Get Site Block List | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ) |
| `add_ip_to_block_list` | Add IP Address to Block List | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `source`(IP Address, REQ), `note`(Note), `expires`(Expiry Date) |
| `remove_ip_from_block_list` | Remove IP Address from Block List | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `id`(IP Address ID, REQ) |
| `get_all_site_lists` | Get All Site Lists | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ) |
| `get_site_list_by_id` | Get Site List Details | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `id`(List ID, REQ) |
| `list_sites_in_corp` | List Sites in Corporation | investigation | ✓ | `corporation`(Corporation Name, REQ), `name`(Site Name), `agent_level`(Agent Level), `page`(Page), `limit`(Limit) |
| `list_corps` | List Corporations | investigation | ✓ | — |
| `list_alerts` | List Alerts | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ) |
| `get_alert_details` | Get Alert Details | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `id`(Alert ID, REQ) |
| `update_alert` | Update Alert | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `id`(Alert ID, REQ), `long_name`(Long Name), `tag_name`(Tag Name), `interval`(Interval), `threshold`(Threshold), `block_duration_seconds`(Block Duration Seconds), `enabled`(Enabled), `action`(Action) |
| `list_events` | List Events | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `status`(Status), `action`(Action), `ip`(IP), `tag`(Tag), `since_id`(Since ID), `max_id`(Max ID), `from`(Start Time), `until`(End Time), `sort`(Sort), `page`(Page), `limit`(Limit) |
| `get_event_details` | Get Event Details | investigation | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `id`(Event ID, REQ) |
| `expire_event_by_id` | Expire Event By ID | management | ✓ | `corporation`(Corporation Name, REQ), `site_name`(Site Name, REQ), `id`(Event ID, REQ) |

### `fidelis-edr`

version 1.1.0 — Fidelis Endpoint EDR detects endpoint activity in real time and retrospectively so you can accelerate your response and stop adversaries at …

- GitHub: connector-fidelis-edr
- Category: Endpoint Protection
- Operations: 21

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alerts | investigation | ✓ | `facetSearch`(Search String), `startDate`(Start Date), `endDate`(End Date), `skip`(Offset), `take`(Limit), `sort`(Sort Alerts) |
| `get_endpoints` | Get Endpoints | investigation | ✓ | `startIndex`(Offset, REQ), `count`(Limit, REQ), `sort`(Sort, REQ) |
| `get_endpoints_by_name` | Get Endpoint By Name | investigation | ✓ | `nameArray`(Endpoint Names, REQ) |
| `delete_endpoint` | Delete Endpoint | investigation | ✓ | `endpointID`(Endpoint ID, REQ) |
| `get_playbooks` | Get Playbooks | investigation | ✓ | `take`(Limit Playbooks, REQ) |
| `get_playbooks_scripts` | Get Playbooks And Scripts | investigation | ✓ | `filterType`(Type), `platformFilter`(OS Platform), `sort`(Sorting Order), `take`(Limit), `skip`(Offset) |
| `get_playbooks_detail` | Get Playbooks Details | investigation | ✓ | `id`(Playbook ID, REQ) |
| `get_api_info` | Get API version Information | investigation | ✓ | — |
| `get_script_packages` | Get Script Packages | investigation | ✓ | — |
| `get_script_packages_file` | Get Script Packages File | investigation | ✓ | `scriptID`(Script Package ID, REQ) |
| `get_script_packages_manifest` | Get Script Packages Manifest | investigation | ✓ | `scriptID`(Script Package ID, REQ) |
| `get_script_packages_metadata` | Get Script Packages Metadata | investigation | ✓ | `scriptID`(Script Package ID, REQ) |
| `get_script_packages_template` | Get Script Packages Template | investigation | ✓ | `scriptID`(Script Package ID, REQ) |
| `execute_script_package` | Execute Script Package | investigation | ✓ | `scriptPackageId`(Script Package ID, REQ), `timeoutInSeconds`(Timeout In Seconds, REQ), `hosts`(Hosts, REQ), `integrationOutputs`(Integration Outputs), `questions`(Questions) |
| `script_job_results` | Get Script Job Results | investigation | ✓ | `jobResultID`(Job Result ID, REQ) |
| `create_task` | Execute Task | investigation | ✓ | `packageId`(Package ID, REQ), `isplaybook`(IS Playbook Or Script, REQ), `endpoints`(Endpoint IDs, REQ) |
| `get_installed_software` | Get Installed Software | investigation | ✓ | `endpointID`(Endpoint ID, REQ), `facetSearch`(Search String), `skip`(Offset), `take`(Limit), `sort`(Sort) |
| `get_alert_responses` | Get Alert Responses | investigation | ✓ | `search`(Search), `offset`(Offset), `columns`(Columns), `limit`(Limit), `sort`(Sort) |
| `get_endpoints_by_search_query` | Get Endpoints By Search Query | investigation | ✓ | `startRange`(Start Range, REQ), `count`(Count, REQ), `search`(Search, REQ), `sort`(Sort, REQ), `accessType`(Access Type) |
| `get_job_status_by_job_id` | Get Job Status By Job ID | investigation | ✓ | `jobResultID`(Job Result ID, REQ) |
| `create_custom_task` | Create Custom Task | investigation | ✓ | `packageId`(Package ID, REQ), `isplaybook`(Is Playbook Or Script, REQ), `endpoints`(Endpoint IDs, REQ), `integration_output_format`(Integration Output Format, REQ), `script_id`(Script ID, REQ), `questions`(Questions, REQ), `json_questions`(Json Questions), `timeout_in_Seconds`(Timeout In Seconds, REQ), `queue_expiration_in_hours`(Queue Expiration In Hours) |

### `file-content-extraction`

version 1.3.1 — Utility to Extract Text, Artifacts and Metadata from almost any file. Internet connectivity is required for the connector to download depend…

- GitHub: connector-file-content-extraction
- Category: Utilities
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `extract_text` | Extract Text | investigation | ✓ | `file_iri`(File IRI/Path, REQ), `html_output_format`(Set Output Format to XHTML) |
| `extract_indicators` | Extract Artifacts | investigation | ✓ | `file_iri`(File IRI/Path, REQ) |
| `extract_indicators_from_file` | Extract Artifacts Extended | investigation | ✓ | `file_iri`(File IRI/Path, REQ) |
| `get_backend_config` | Get Backend Config | investigation | ✓ | `verbose_config`(Verbose) |
| `create_xslx_file_from_json_data` | Create XLSX File as Attachment From JSON Data | investigation | ✓ | `fileName`(File Name, REQ), `jsonData`(JSON Data, REQ), `xLSXFields`(XLSX Fields) |

### `fireeye-detection-on-demand`

version 1.0.1 — FireEye Detection On Demand is a threat detection service that uncovers harmful objects in the cloud. It delivers flexible file and content …

- GitHub: connector-fireeye-detection-on-demand
- Category: Forensics and Malware Analysis
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_hashes` | Get File Reputation | investigation | ✓ | `hash`(File Hash) |
| `submit_urls` | Submit URLs | investigation | ✓ | `urls`(URLs) |
| `submit_file` | Submit File | investigation | ✓ | `attachment_iri`(Attachment IRI, REQ), `password`(Password), `parameters`(Parameters), `file_extraction`(File Extraction), `memory_dump`(Memory Dump), `pcap`(PCAP) |
| `get_reports` | Get Report | investigation | ✓ | `report_id`(Report ID), `extended`(Extended) |
| `get_report_url` | Get Report URL | investigation | ✓ | `report_id`(Report ID), `report_id`(Expiry) |
| `get_artifacts` | Get Artifacts | investigation | ✓ | `report_id`(Report ID, REQ), `artifacts_type`(Type, REQ), `artifacts_uuid`(Artifact UUID, REQ) |

### `focsec`

version 1.0.0 — Focsec help to real-time threat intelligence API, powered by proprietary Artificial Intelligence algorithms,for detecting VPNs,Proxys,Bots, …

- GitHub: connector-focsec
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_details` | Get IP Details | investigation | ✗ | `ip_address`(IP Address, REQ) |

### `forcepoint-dlp`

version 1.0.0 — Forcepoint DLP used to prevent data leakage, ensure regulatory compliance, protect intellectual property, manage employee productivity, miti…

- GitHub: connector-forcepoint-dlp
- Category: Network Security
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_incidents_by_ids` | Get Incidents by IDs | investigation | ✗ | `type`(Type, REQ), `ids`(IDs, REQ) |
| `get_incidents_by_date_range` | Get Incidents by Date Range | investigation | ✗ | `type`(Type, REQ), `from_date`(From Date, REQ), `to_date`(To Date, REQ) |
| `get_incidents_by_action` | Get Incidents by Action | investigation | ✗ | `type`(Type, REQ), `from_date`(From Date, REQ), `to_date`(To Date, REQ), `action`(Action, REQ) |
| `get_incidents_by_severity` | Get Incidents by Severity | investigation | ✗ | `type`(Type, REQ), `from_date`(From Date, REQ), `to_date`(To Date, REQ), `severity`(Severity, REQ) |
| `get_incidents_by_status` | Get Incidents by Status | investigation | ✗ | `type`(Type, REQ), `from_date`(From Date, REQ), `to_date`(To Date, REQ), `status`(Status, REQ) |
| `get_incidents_by_policy_name` | Get Incidents by Policy Name | investigation | ✗ | `type`(Type, REQ), `from_date`(From Date, REQ), `to_date`(To Date, REQ), `policies`(Policies, REQ) |
| `get_list_of_incidents_by_filter` | Get List Of Incident By Filter | investigation | ✗ | `type`(Type, REQ), `sort_by`(Sort By), `from_date`(From Date, REQ), `to_date`(To Date, REQ), `detected_by`(Detected By), `analyzed_by`(Analyzed By), `event_id`(Event ID), `destination`(Destination), `policies`(Policies), `action`(Action), `source`(Source), `status`(Status), `severity`(Severity), `endpoint_type`(Endpoint Type), `channel`(Channel), `assigned_to`(Assigned To), `tag`(Tag) |
| `update_incident_status_by_incident_id_and_partition_index` | Update Incident Status By Incident ID And Partition Index | investigation | ✗ | `type`(Type, REQ), `action_type`(Action Type, REQ) |
| `update_incident_status_by_scan_partitions` | Update Incident Status By Scan Partitions | investigation | ✗ | `type`(Type, REQ), `action_type`(Action Type, REQ), `scan_partitions`(Scan Partitions, REQ) |
| `update_incident_status_by_event_ids` | Update Incident Status By Event IDs | investigation | ✗ | `type`(Type, REQ), `event_ids`(Event IDs, REQ), `action_type`(Action Type, REQ) |

### `forticloud-asset-management`

version 1.0.0 — Asset Management is an easy-to-use portal to register, organize and view all Fortinet products and services in FortiCloud. New products, lic…

- GitHub: connector-forticloud-asset-management
- Category: Asset Management
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_assets` | List Assets | investigation | ✓ | `filter`(Fetch Based On, REQ) |
| `register_product` | Register Product | investigation | ✓ | `serial_number`(Serial Number, REQ), `contract_number`(Contract Number), `description`(Description), `asset_group_ids`(Asset Group IDs), `replaced_serial_number`(Replaced Serial Number), `additional_info`(Additional Info), `cloud_key`(Cloud Key), `is_government`(Is Government) |
| `update_description` | Update Description | investigation | ✓ | `serial_number`(Serial Number, REQ), `description`(Description, REQ) |
| `product_details` | Get Product Details | investigation | ✓ | `serial_number`(Serial Number, REQ) |
| `update_location` | Update Location | investigation | ✓ | `serial_number`(Serial Number, REQ), `address`(Address, REQ), `city`(City, REQ), `stateOrProvince`(State/Province, REQ), `countryCode`(Country, REQ), `postalCode`(Postal Code, REQ), `company`(Company), `email`(Email), `phone`(Phone), `fax`(Fax) |
| `decommission_product` | Decommission Product | investigation | ✓ | `serial_numbers`(Serial Numbers, REQ) |
| `register_license` | Register License | investigation | ✓ | `license_registration_code`(License Registration Code, REQ), `serial_number`(Serial Number), `description`(Description), `additional_info`(Additional Info), `is_government`(Is Government) |
| `download_license` | Download License | investigation | ✓ | `serial_number`(Serial Number, REQ) |
| `generic_api_call` | Generic API Call | investigation | ✓ | `method`(Method, REQ), `endpoint`(Endpoint, REQ), `payload`(Payload) |
| `register_service` | Register Service | investigation | ✓ | `contract_number`(Contract Number, REQ), `description`(Description), `additional_info`(Additional Info), `is_government`(Is Government) |

### `fortinet-fortiauthenticator`

version 1.0.0 — FortiAuthenticator provides centralized authentication services for the Fortinet Security Fabric including single sign on services, certific…

- GitHub: connector-fortinet-fortiauthenticator
- Category: Authentication
- Operations: 12

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_schema` | Get Schema | investigation | ✓ | — |
| `create_local_user` | Create Local User | investigation | ✓ | `username`(Username, REQ), `password`(Password, REQ), `email`(Email, REQ), `first_name`(First Name, REQ), `last_name`(Last Name, REQ), `active`(Activate/Deactivate), `additional_fields`(Additional Fields) |
| `get_users` | Get Local User List | investigation | ✓ | `limit`(Limit), `offset`(Offset) |
| `get_local_user` | Get Specific Local User | investigation | ✓ | `output_mode`(Search User By, REQ) |
| `update_user_status` | Update Local User Status | investigation | ✓ | `userid`(User ID, REQ), `active`(Activate/Deactivate, REQ) |
| `get_ldap_user_list` | Get LDAP User List | investigation | ✓ | `limit`(Limit), `offset`(Offset) |
| `get_ldap_user` | Get Specific LDAP User | investigation | ✓ | `output_mode`(Search User By, REQ) |
| `update_ldapuser_status` | Update LDAP User Status | investigation | ✓ | `userid`(User ID, REQ), `active`(Activate/Deactivate, REQ) |
| `get_radius_user_list` | Get Radius User List | investigation | ✓ | `limit`(Limit), `offset`(Offset) |
| `get_radius_user` | Get Specific Radius User | investigation | ✓ | `output_mode`(Search User By, REQ) |
| `update_radiususer_status` | Update Radius User Status | investigation | ✓ | `userid`(User ID, REQ), `active`(Activate/Deactivate, REQ) |
| `get_userlockout_policy` | Get User Lockout Policy Info | investigation | ✓ | — |

### `fortinet-forticasb`

version 1.0.0 — FortiCASB (Cloud Access Security Broker) is Fortinet’s cloud-native CASB solution, designed for comprehensive visibility, compliance, data s…

- GitHub: connector-fortinet-forticasb
- Category: Cloud access security broker (CASB)
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_resource_url_map` | Get Resource URL Map | miscellaneous | ✓ | — |
| `search_alerts` | Search Alerts | investigation | ✓ | `service`(Service, REQ), `startTime`(Start Time), `endTime`(End Time), `user`(User), `policy`(Policy), `severity`(Severity), `status`(Status), `idList`(Alert IDs), `businessunitname`(Business Unit Name) |
| `get_file_summary` | Get File Summary | investigation | ✗ | — |
| `get_policies` | Get Policies | investigation | ✓ | — |
| `get_datapatterns` | Get Data Patterns | investigation | ✓ | — |
| `search_activity` | Search Activity | investigation | ✓ | `startTime`(Start Time), `endTime`(End Time), `service`(Service), `idList`(Activity IDs), `activity`(Activity Type), `ipList`(IP List) |

### `fortinet-forticnp`

version 2.0.0 — Fortinet FortiCNP integrates with APIs provided by cloud vendors including AWS, Azure, and Google Cloud Platform to monitor and track all se…

- GitHub: connector-fortinet-forticnp
- Category: Investigation
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_resource_map` | Get Resource Map | investigation | ✓ | — |
| `get_resource_list` | Get Resource List | investigation | ✓ | `filter`(Filter JSON, REQ), `skip`(Offset), `limit`(Limit), `orderBy`(Sort By), `orderDirection`(Sort Order) |
| `get_resource_details` | Get Resource Details | investigation | ✓ | `resourceid`(Resource ID, REQ) |
| `get_finding_list` | Get Finding List | investigation | ✓ | `objectId`(Resource ID, REQ), `startTime`(Start Time, REQ), `endTime`(End Time, REQ), `skip`(Offset), `limit`(Limit) |

### `fortinet-fortiddos`

version 1.0.0 — FortiDDoS Protection Solution defends enterprise data centers against DDoS attacks by leveraging an extensive collection of known DDoS metho…

- GitHub: connector-fortinet-fortiddos
- Category: Network Security
- Operations: 24

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_spp_settings` | Get Protection Profiles | investigation | ✓ | `spp`(SPP Name, REQ), `resource_name`(Resource Name, REQ) |
| `update_service_protection_profile_settings` | Update Protection Profiles Settings | remediation | ✓ | `spp`(SPP Name, REQ), `resource_name`(Resource Name, REQ), `parameter_name_val`(Resource Arguments, REQ) |
| `get_global_settings` | Get Global Settings | investigation | ✓ | — |
| `get_global_spp` | Get Global Service Protection Profiles | investigation | ✓ | `resource_name`(Resource Name, REQ) |
| `get_settings` | Get Settings | investigation | ✓ | `resource_name`(Resource Name, REQ) |
| `get_global_settings_address` | Get Global Settings Address | investigation | ✓ | `resource_name`(Resource Name, REQ) |
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | — |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | — |
| `get_proxy_ip` | Get Proxy IP | investigation | ✓ | — |
| `get_proxy_ip_policy` | Get Proxy IP Policy | investigation | ✓ | — |
| `get_do_not_track_policy` | Get Do Not Track Policy | investigation | ✓ | `resource_name`(Resource Name, REQ) |
| `get_global_acl` | Get Access Control List | investigation | ✓ | `resource_name`(Resource Name, REQ) |
| `get_bypass_mac` | Get Bypass MAC | investigation | ✓ | — |
| `get_system_settings` | Get System Settings | investigation | ✓ | `primary_resource_name`(Primary Resource Name, REQ) |
| `get_log_settings` | Get Log Settings | investigation | ✓ | `resource_name`(Resource Name, REQ) |
| `get_attack_information` | Get Attack Information | investigation | ✓ | `spp_name`(SPP, REQ), `subtype`(Subtype, REQ), `dir`(Direction), `period`(Period) |
| `add_distress_acl` | Add Distress ACL | remediation | ✓ | `mkey`(MKey, REQ), `acl-enable`(ACL Enable), `destination`(Destination, REQ), `destination-port`(Destination Port), `dscp`(DSCP), `fragment`(Fragment), `protocol`(Protocol), `source-ip`(Source IP), `source-port`(Source Port), `tcp-control-flag`(TCP Control Flag), `ttl`(TTL) |
| `delete_distress_acl` | Delete Distress ACL | remediation | ✓ | `name`(Distress ACL Name, REQ) |
| `add_service_protection_profile_policy` | Add Service Protection Profile Policy | remediation | ✓ | `spp`(SPP, REQ), `subnet-id`(Subnet ID, REQ), `mkey`(MKey Name, REQ), `ip-version`(IP Version, REQ), `alt-spp-enable`(Alternate SPP Enable, REQ), `comment`(Comment) |
| `get_service_protection_profile_policy` | Get Service Protection Profile Policy | investigation | ✓ | — |
| `delete_service_protection_profile_policy` | Delete Service Protection Profile Policy | remediation | ✓ | `policy_name`(SPP Policy Name, REQ) |
| `add_lq` | Add Legitimate DNS Query | remediation | ✓ | `query`(Query, REQ), `type`(Type, REQ), `class`(Class, REQ) |
| `delete_lq` | Delete Legitimate DNS Query | remediation | ✓ | `query`(Domain, REQ), `type`(Type, REQ), `class`(Class, REQ) |
| `generate_bgp_flowspec` | Generate BGP Flowspec | containment | ✓ | `vendor`(Vendor, REQ), `destination`(Destination, REQ), `threshold`(Threshold, REQ) |

### `fortinet-fortiflex`

version 1.0.0 — FortiFlex is a points-based program that empowers organizations to provision the Fortinet services and solutions, and offers the flexibility…

- GitHub: connector-fortinet-fortiflex
- Category: Asset Management
- Operations: 17

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_programs` | Get All Program List | investigation | ✓ | — |
| `create_configuration` | Create Configuration | investigation | ✓ | `programSerialNumber`(Program Serial Number, REQ), `name`(Configuration Name, REQ), `productTypeId`(Product Type, REQ), `accountId`(Account ID) |
| `get_configurations` | Get All Configuration List | investigation | ✓ | `programSerialNumber`(Program Serial Number, REQ), `accountId`(Account ID) |
| `enable_configuration` | Enable Configuration | investigation | ✓ | `id`(Configuration ID, REQ) |
| `disable_configuration` | Disable Configuration | investigation | ✓ | `id`(Configuration ID, REQ) |
| `update_configuration` | Update Configuration | investigation | ✓ | `id`(Configuration ID, REQ), `name`(Configuration Name, REQ), `productTypeId`(Product Type, REQ) |
| `create_vm_entitlements` | Create VM Entitlements | investigation | ✓ | `configId`(Configuration ID, REQ), `count`(Count, REQ), `folderPath`(Folder Path, REQ), `description`(Description), `endDate`(End DateTime) |
| `create_hardware_entitlements` | Create Hardware Entitlements | investigation | ✓ | `configId`(Configuration ID, REQ), `serialNumbers`(Serial Numbers, REQ), `endDate`(End DateTime) |
| `get_entitlements` | Get All Entitlement List | investigation | ✓ | `filter`(Fetch Based On, REQ) |
| `update_entitlements` | Update Entitlements | investigation | ✓ | `configId`(Configuration ID, REQ), `serialNumber`(Serial Number, REQ), `description`(Description, REQ), `endDate`(End DateTime, REQ) |
| `stop_entitlement` | Stop Entitlement | investigation | ✓ | `serialNumber`(Serial Number, REQ) |
| `reactivate_entitlement` | Reactivate Entitlement | investigation | ✓ | `serialNumber`(Serial Number, REQ) |
| `transfer_entitlement` | Transfer Entitlement | investigation | ✓ | `sourceAccountId`(Source Account ID, REQ), `sourceConfigId`(Source Config ID, REQ), `serialNumbers`(Serial Number, REQ), `targetAccountId`(Target Account ID, REQ), `targetConfigId`(Target Config ID) |
| `regenerate_token_for_vm` | Regenerate Token for VM | investigation | ✓ | `serialNumber`(Serial Number, REQ) |
| `get_point_usage_for_vm` | Get Point Usage for VM | investigation | ✓ | `filter`(Fetch Based On, REQ), `startDate`(Start DateTime, REQ), `endDate`(End DateTime, REQ) |
| `get_groups` | Get All Group List | investigation | ✓ | `accountId`(Account ID, REQ) |
| `get_group_next_token` | Get NextToken for Group | investigation | ✓ | `accountId`(Account ID, REQ), `configId`(Config ID), `folderPath`(Asset Folder Path) |

### `fortinet-fortiguard-threat-intel-feed`

version 1.0.0 — FortiSOAR Integration with Fortiguard Premium Services for ingesting the Threat Intel Feeds and Signature Lookup

- GitHub: connector-fortinet-fortiguard-threat-intel-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `ingest_feeds` | Fetch All Threat Intel Feeds Into FortiSOAR | investigation | ✓ | `cc`(Country Codes), `date`(Date), `modified_after`(Pull only if feed modified after), `create_pb_id`(Record Creation Playbook IRI) |

### `fortinet-fortimanager-json-rpc`

version 1.1.0 — The Fortinet FortiManager JSON RPC Connector is an advanced connector with freeform actions to use the JSON-RPC API directly. This connector…

- GitHub: connector-fortinet-fortimanager-json-rpc
- Category: Centralized Security Management
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `json_rpc_add` | JSON RPC Add | investigation | ✓ | `url`(URL, REQ), `data`(Data, REQ) |
| `json_rpc_set` | JSON RPC Set | investigation | ✓ | `url`(URL, REQ), `data`(Data, REQ) |
| `json_rpc_get` | JSON RPC Get | investigation | ✓ | `url`(URL, REQ), `data`(Data) |
| `json_rpc_execute` | JSON RPC Exec | investigation | ✓ | `url`(URL, REQ), `data`(Data, REQ), `track_task`(Track Task) |
| `json_rpc_delete` | JSON RPC Delete | investigation | ✓ | `url`(URL, REQ), `data`(Data, REQ) |
| `json_rpc_freeform` | JSON RPC Freeform | investigation | ✓ | `method`(Method, REQ), `data`(Data, REQ) |

### `fortinet-fortindr-cloud`

version 1.2.0 — Fortinet FortiNDR Cloud is a cloud-native network detection and response solution built for the rapid detection of threat activity, investig…

- GitHub: connector-fortinet-fortindr-cloud
- Category: Cloud Security
- Operations: 26

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_pcap_tasks` | Get PCAP Tasks | investigation | ✓ | `task_uuid`(Task UUID), `sensor_id`(Sensor ID), `created_start`(Created Start DateTime), `created_end`(Created End DateTime), `search_text`(Search Text), `has_files_only`(Include Hash Files), `page_size`(Page Size), `page_num`(Page Number) |
| `download_pcap_task_file` | Download PCAP Task File | investigation | ✓ | `task_uuid`(Task UUID, REQ), `file_name`(File Name) |
| `terminate_pcap_task` | Terminate PCAP Task | investigation | ✓ | `task_uuid`(Task UUID, REQ) |
| `delete_pcap_task` | Delete PCAP Task | investigation | ✓ | `task_uuid`(Task UUID, REQ) |
| `get_sensors` | Get Sensors List | investigation | ✓ | `sensor_id`(Sensor ID), `account_code`(Account Code), `include`(Include) |
| `get_telemetry_events` | Get Telemetry Events | investigation | ✓ | `sensor_id`(Sensor ID), `account_code`(Account Code), `interval`(Interval), `start_date`(Start DateTime), `end_date`(End DateTime), `event_type`(Event Type), `group_by`(Group By) |
| `get_telemetry_bandwidth` | Get Telemetry Bandwidth | investigation | ✓ | `account_code`(Account Code), `start_date`(Start DateTime), `end_date`(End DateTime), `interval`(Interval), `latest_each_month`(Latest Month), `sort_order`(Sort Order), `limit`(Limit), `offset`(Offset) |
| `get_telemetry_packetstats` | Get Telemetry Packetstats | investigation | ✓ | `sensor_id`(Sensor ID), `interval`(Interval), `start_date`(Start DateTime), `end_date`(End DateTime), `group_by`(Group By) |
| `get_entity_tracking` | Get Entity Tracking | investigation | ✓ | `entity_type`(Entity Type, REQ), `entity_value`(Entity Value, REQ), `start_time`(Start DateTime), `end_time`(End DateTime), `limit`(Limit), `offset`(Offset) |
| `get_entity_summary` | Get Entity Summary | investigation | ✓ | `entity`(IP/Domain, REQ) |
| `get_entity_pdns` | Get Passive DNS Details | investigation | ✓ | `entity`(IP/Domain, REQ), `record_type`(Record Type), `start_date`(Start DateTime), `end_date`(End DateTime), `limit`(Limit) |
| `get_detections` | Get Detections List | investigation | ✓ | `rule_uuid`(Rule UUID), `sensor_id`(Sensor ID), `status`(Status), `device_ip`(Device IP), `muted`(Muted), `muted_device`(Muted Device), `muted_rule`(Muted Rule), `include`(Include), `indicator_value`(Indicator Value), `created_start_date`(Created Start DateTime), `created_end_date`(Created End DateTime), `sort_by`(Sort By), `sort_order`(Sort Order), `limit`(Limit), `offset`(Offset) |
| `resolve_detection` | Resolve Detection | investigation | ✓ | `detection_uuid`(Detection UUID, REQ), `resolution`(Resolution, REQ), `resolution_comment`(Comment) |
| `get_devices_with_detection` | Get Devices with Detection | investigation | ✓ | `account_uuid`(Account UUID), `search`(Search), `muted`(Muted), `muted_device`(Muted Device), `muted_rule`(Muted Rule), `status`(Status), `sort_by`(Sort By), `sort_order`(Sort Order), `limit`(Limit), `offset`(Offset) |
| `get_detection_events` | Get Detection Events | investigation | ✓ | `detection_uuid`(Detection UUID, REQ), `limit`(Limit), `offset`(Offset) |
| `get_detection_rule_indicators` | Get Detection Rule Indicators | investigation | ✓ | `rule_uuid`(Rule UUID), `detection_muted`(Detection Muted), `detection_status`(Detection Status), `sort_by`(Sort By), `sort_order`(Sort Order), `limit`(Limit), `offset`(Offset) |
| `get_detection_rules` | Get Detection Rules List | investigation | ✓ | `rule_account_uuid`(Rule Account UUID), `search`(Search By), `has_detections`(Has Detection), `detection_device_ip`(Detection Device IP), `indicator_value`(Indicator Value), `severity`(Severity), `confidence`(Confidence), `category`(Category), `rule_account_muted`(Include Muted Rules), `enabled`(Enabled), `sort_by`(Sort By), `sort_order`(Sort Order), `limit`(Limit), `offset`(Offset) |
| `get_detection_rule_details` | Get Detection Rule Details | investigation | ✓ | `rule_uuid`(Rule UUID, REQ), `rule_account_uuid`(Rule Account UUID) |
| `get_detection_rule_events` | Get Detection Rule Events List | investigation | ✓ | `rule_uuid`(Rule UUID, REQ), `limit`(Limit), `offset`(Offset) |
| `add_annotation` | Add Annotation | investigation | ✓ | `annotations`(Annotations, REQ), `account_uuid`(Account UUID) |
| `retrieve_annotations` | Retrieve Annotations | investigation | ✓ | `account_uuid`(Account UUID), `value`(Annotation Value), `entity`(Entity), `entity_type`(Entity Type), `limit`(Limit), `offset`(Offset) |
| `modify_annotation` | Modify Annotation | investigation | ✓ | `annotation_uuid`(Annotation UUID, REQ), `annotation`(Annotation, REQ) |
| `delete_annotation` | Delete Annotation | investigation | ✓ | `annotation_uuid`(Annotation UUID, REQ) |
| `retrieve_annotation_for_entities` | Retrieve Annotation for Entities | investigation | ✓ | `entities`(Entities, REQ), `account_uuid`(Account UUID) |
| `add_or_replace_entities_to_annotation` | Add or Replace Entities to Annotation | investigation | ✓ | `annotation_uuid`(Annotation UUID, REQ), `entities`(Entities, REQ), `replace`(Replace) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `fortinet-fortiproxy`

version 1.0.1 — FortiProxy provides a secure web gateway, which protects against web attacks with URL filtering, visibility and control of encrypted web tra…

- GitHub: connector-fortinet-fortiproxy
- Category: Web Application
- Operations: 26

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_firewall_policy` | Create Firewall Policy | investigation | ✓ | `name`(Policy Name, REQ), `schedule`(Schedule Name, REQ), `type`(Policy Type), `srcaddr`(Source Address), `dstaddr`(Destination Address), `srcaddr6`(IPV6 Source Address), `dstaddr6`(IPV6 Destination Address), `policyid`(Policy ID), `policy_action`(Policy Action), `status`(Status), `vdom`(VDOM), `action`(Action), `nkey`(New Resource ID), `custom_attributes`(Custom Properties) |
| `get_firewall_policy` | Get Firewall Policy | investigation | ✓ | `datasource`(Data Source), `start`(Start), `count`(Count), `with_meta`(With Meta), `with_contents_hash`(Contents Hash), `skip`(Skip), `format`(Include Properties), `filter`(Filter), `key`(Key), `pattern`(Pattern), `scope`(Scope), `exclude-default-values`(Exclude Default Values), `meta_only`(Meta Only), `action`(Action), `vdom`(VDOM) |
| `get_firewall_policy_details` | Get Firewall Policy Details | investigation | ✓ | `policyid`(Policy ID, REQ), `datasource`(Data Source), `with_meta`(Include Meta Information), `skip`(Skip), `format`(Include Properties), `action`(Action), `vdom`(VDOM) |
| `update_firewall_policy` | Update Firewall Policy | investigation | ✓ | `policyid`(Policy ID, REQ), `name`(Policy Name), `schedule`(Schedule Name), `type`(Policy Type), `srcaddr`(Source Address), `dstaddr`(Destination Address), `srcaddr6`(IPV6 Source Address), `dstaddr6`(IPV6 Destination Address), `policy_action`(Policy Action), `status`(Status), `vdom`(VDOM), `action`(Action), `nkey`(New Resource ID), `before`(Before), `after`(After), `custom_attributes`(Custom Properties) |
| `delete_firewall_policy` | Delete Firewall Policy | investigation | ✓ | `policyid`(Policy ID, REQ), `vdom`(VDOM) |
| `create_firewall_address` | Create Firewall Address | investigation | ✓ | `name`(Address Name, REQ), `type`(Address Type), `interface`(Interface), `vdom`(VDOM), `action`(Action), `nkey`(New Resource ID), `custom_attributes`(Custom Properties) |
| `get_firewall_address` | Get Firewall Address | investigation | ✓ | `datasource`(Data Source), `start`(Start), `count`(Count), `with_meta`(Include Meta Information), `with_contents_hash`(Include Contents Hash), `skip`(Skip), `format`(Include Properties), `filter`(Filter), `key`(Filter on Property), `pattern`(Pattern), `scope`(Scope), `exclude-default-values`(Exclude Default Properties), `meta_only`(Meta Only), `action`(Action), `vdom`(VDOM) |
| `get_firewall_address_details` | Get Firewall Address Details | investigation | ✓ | `name`(Address Name, REQ), `datasource`(Data Source), `with_meta`(Meta Information), `skip`(Skip), `format`(Include Properties), `action`(Action), `vdom`(VDOM) |
| `update_firewall_address` | Update Firewall Address | investigation | ✓ | `name`(Address Name, REQ), `type`(Address Type), `interface`(Interface), `vdom`(VDOM), `action`(Action), `nkey`(New Resource ID), `before`(Before), `after`(After), `custom_attributes`(Custom Properties) |
| `delete_firewall_address` | Delete Firewall Address | investigation | ✓ | `name`(Address Name, REQ), `vdom`(VDOM) |
| `create_firewall_address_group` | Create Firewall Address Group | investigation | ✓ | `name`(Address Group Name, REQ), `member`(Member, REQ), `type`(Address Group Type), `comment`(Comment), `exclude`(Exclude Address), `color`(Color), `allow-routing`(Allow Routing), `fabric-object`(Security Fabric Object), `vdom`(VDOM), `action`(Action), `nkey`(New Resource ID), `custom_attributes`(Custom Properties) |
| `get_firewall_address_group` | Get Firewall Address Group | investigation | ✓ | `datasource`(Data Source), `start`(Start), `count`(Count), `with_meta`(Meta Information), `with_contents_hash`(Include Contents Hash), `skip`(Skip), `format`(Include Properties), `filter`(Filter), `key`(Filter on Property), `pattern`(Pattern), `scope`(Scope), `exclude-default-values`(Exclude Default Properties), `meta_only`(Meta Only), `action`(Action), `vdom`(VDOM) |
| `get_firewall_address_group_details` | Get Firewall Address Group Details | investigation | ✓ | `name`(Address Group Name, REQ), `datasource`(Data Source), `with_meta`(Meta Information), `skip`(Skip), `format`(Include Properties), `action`(Action), `vdom`(VDOM) |
| `update_firewall_address_group` | Update Firewall Address Group | investigation | ✓ | `name`(Address Group Name, REQ), `member`(Member), `comment`(Comment), `exclude`(Exclude Address), `color`(Color), `allow-routing`(Allow Routing), `fabric-object`(Security Fabric Object), `vdom`(VDOM), `action`(Action), `before`(Before), `after`(After), `custom_attributes`(Custom Properties) |
| `delete_firewall_address_group` | Delete Firewall Address Group | investigation | ✓ | `name`(Address Group Name, REQ), `vdom`(VDOM) |
| `create_firewall_service_group` | Create Firewall Service Group | investigation | ✓ | `name`(Address Group Name, REQ), `proxy`(Proxy), `member`(Member), `color`(Color), `comment`(Comment), `fabric-object`(Security Fabric Object), `vdom`(VDOM), `action`(Action), `nkey`(New Resource ID) |
| `get_firewall_service_group` | Get Firewall Service Group | investigation | ✓ | `datasource`(Data Source), `start`(Start), `count`(Count), `with_meta`(Meta Information), `with_contents_hash`(Include Contents Hash), `skip`(Skip), `format`(Include Properties), `filter`(Filter), `key`(Filter on Property), `pattern`(Pattern), `scope`(Scope), `exclude-default-values`(Exclude Default Properties), `meta_only`(Meta Only), `action`(Action), `vdom`(VDOM) |
| `get_firewall_service_group_details` | Get Firewall Service Group Details | investigation | ✓ | `name`(Address Group Name, REQ), `datasource`(Data Source), `with_meta`(Meta Information), `skip`(Skip), `format`(Include Properties), `action`(Action), `vdom`(VDOM) |
| `update_firewall_service_group` | Update Firewall Service Group | investigation | ✓ | `name`(Address Group Name, REQ), `member`(Member), `color`(Color), `comment`(Comment), `fabric-object`(Security Fabric Object), `vdom`(VDOM), `action`(Action), `before`(Before), `after`(After) |
| `delete_firewall_service_group` | Delete Firewall Service Group | investigation | ✓ | `name`(Address Group Name, REQ), `vdom`(VDOM) |
| `get_authenticated_firewall_users_list` | Get Authenticated Firewall Users List | investigation | ✓ | `start`(Start), `count`(Count), `ipv4`(Include IPV4 Users), `ipv6`(Include IPV6 Users) |
| `deauthenticate_firewall_users` | DeAuthenticate Firewall Users | investigation | ✓ | `user_type`(User Type, REQ), `id`(User ID, REQ), `ip`(IP Address, REQ), `ip_version`(IP Version), `method`(Authentication Method), `all`(DeAuthenticate All Users), `users`(Users) |
| `add_users_to_banned_list` | Add Users to Banned List | investigation | ✓ | `ip_addresses`(IP Addresses, REQ), `expiry`(Expiry, REQ) |
| `get_all_banned_users_list` | Get All Banned Users List | investigation | ✓ | — |
| `clear_all_banned_users_list` | Clear All Banned Users List | investigation | ✓ | — |
| `clear_banned_users_list_by_ip` | Clear Banned Users List by IP | investigation | ✓ | `ip_addresses`(IP Addresses, REQ) |

### `fortinet-fortirecon-aci`

version 2.1.2 — FortiRecon is a Digital Risk Protection Service (DRPS) product that provides an outside-the-network view to the risks posed to your enterpri…

- GitHub: connector-fortinet-fortirecon-aci
- Category: Attack surface management
- Operations: 37

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_leaked_cards` | Get Leaked Cards | investigation | ✓ | `type`(Type), `bin`(Bin), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_widgets` | Get Widgets | investigation | ✓ | `page`(Page), `size`(Size) |
| `get_osint_feeds` | Get OSINT Feeds | investigation | ✓ | `widget_id`(Widget ID), `keyword`(Keyword), `page`(Page), `size`(Size) |
| `get_icl_saved_searches` | Get ICL Saved Searches | investigation | ✓ | `q`(Search By Keyword), `alert`(Alert), `query_type`(Query Type), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_icl_saved_searches_by_id` | Get ICL Saved Searches By ID | investigation | ✓ | `based_on`(Get ICL Saved Searches Result Based On, REQ), `id`(ID, REQ), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_stealers_infections_leaked_count` | Get Stealers Infections Leaked Count | investigation | ✓ | `based_on`(Based On, REQ) |
| `get_leaked_stealers_infections` | Get Leaked Stealers Infections | investigation | ✓ | `q`(Search By Keyword), `stealer_name`(Stealer Name), `affiliated_domain`(Affiliated Domain), `status`(Status), `show_plaintext_password`(Show plaintext password), `user_type`(User Type), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_vendor_exposures_by_id` | Get Vendor Exposures By Vendor ID | investigation | ✓ | `type_of_info`(Get Exposures For, REQ), `id`(ID, REQ) |
| `get_vendor_watchlist` | Get Vendor Watchlist | investigation | ✓ | `domain`(Filter By Domain), `name`(Filter By Name), `approval_status`(Approval Status), `status`(Status), `page`(Page), `size`(Size) |
| `get_vendor_details_by_id` | Get Vendor Details By ID | investigation | ✓ | `id`(ID, REQ) |
| `get_vulnerability_intelligence_cves` | Get Vulnerability Intelligence CVEs | investigation | ✓ | `input_src_type`(Input Source Type, REQ), `recon_severity`(Fortirecon Severity), `nvd_severity`(NVD Severity), `years`(CVE Year), `input_src_subtype`(Addition), `vuln_exploitation`(Vulnerability Exploitation), `vendors`(Vendors), `products`(Products), `tags`(Tag IDs), `keyword`(Keyword), `is_elevated`(Elevated), `sort`(Sort By Recon Score), `data_sources`(Data Sources), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_vulnerability_intelligence_cves_by_id` | Get Vulnerability Intelligence CVEs By ID | investigation | ✓ | `id`(ID, REQ) |
| `get_vulnerability_intelligence_vulnerable_products` | Get Vulnerability Intelligence vulnerable products | investigation | ✓ | `input_src_type`(Input Source Type, REQ), `sort`(Sort By Product Count), `page`(Page), `size`(Size) |
| `get_vulnerability_intelligence_vulnerable_vendors` | Get Vulnerability Intelligence vulnerable vendors | investigation | ✓ | `input_src_type`(Input Source Type, REQ), `sort`(Sort By Vendor Count), `page`(Page), `size`(Size) |
| `get_vulnerability_intelligence_hits_by_cve_id` | Get Vulnerability Intelligence hits By CVE ID | investigation | ✓ | `based_on`(Get the CVE hits for a given CVE ID Based On, REQ), `id`(CVE ID, REQ), `page`(Page), `size`(Size) |
| `get_vulnerability_intelligence_stats_for_cve_id` | Get Vulnerability Intelligence Stats For CVE ID | investigation | ✓ | `based_on`(Get stats for the given CVE ID Based On, REQ), `id`(CVE ID, REQ), `page`(Page), `size`(Size) |
| `get_stealers_infections_on_sale_count` | Get Stealers Infections On Sale Count | investigation | ✓ | `based_on`(Based On, REQ) |
| `get_stealers_infections_on_sale` | Get Stealers Infections On Sale | investigation | ✓ | `search_string`(Search By Keyword), `stealers`(Stealer Name), `marketplaces`(Marketplace Name), `isps`(ISP Name), `countries`(Country Name), `states`(State Name), `matched_domains`(Matched Domain), `status`(Status), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_ransomware_victims` | Get Ransomware Victims | investigation | ✓ | `q`(Search By Keyword), `ransomware_name`(Filter By Ransomware Name), `country`(Country), `sectors`(Sectors), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_ransomware_victims_details_by_id` | Get Ransomware Victim Details By ID | investigation | ✓ | `id`(ID, REQ) |
| `get_ransomware_intel_vendors_watchlist` | Get Ransomware Vendors Added For Ransomware Intelligence Monitoring | investigation | ✓ | `page`(Page), `size`(Size) |
| `get_ransomware_intel_vendors_watchlist_matched` | Get Ransomware Vendors Matched | investigation | ✓ | `page`(Page), `size`(Size) |
| `get_ransomware_intelligence_statistics` | Get Ransomware Intelligence Stats | investigation | ✓ | `type_of_info`(Get Ransomware Intelligence Stats For, REQ), `time_range_type`(Time Range Type), `start_date`(Start Date), `end_date`(End Date) |
| `get_ransomware_threat_campaigns` | Get Ransomware Threat Campaign | investigation | ✓ | `page`(Page), `size`(Size) |
| `get_ransomware_potential_victims` | Get Potential Ransomware Victims | investigation | ✓ | `actor`(Filter By Actor Name), `country`(Country), `sectors`(Sectors), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_ransomware_intel_org_watchlist` | Get Ransomware Intelligence Orgs Watchlist To Monitor | investigation | ✓ | `type`(Added Type), `page`(Page), `size`(Size) |
| `get_ransomware_intel_org_watchlist_matched` | Get The Matched Organizations For Ransomware Intelligence Monitoring | investigation | ✓ | `page`(Page), `size`(Size) |
| `get_technical_indicators_for_given_ransomware_group` | Get The Technical Indicators For The Given Ransomware Group | investigation | ✓ | `group_name`(Ransomware Group Name, REQ), `page`(Page), `size`(Size) |
| `get_ransomware_group_info` | Get Ransomware Group Information | investigation | ✓ | `group_name`(Ransomware Group Name, REQ) |
| `update_stealers_leaked_status` | Update Stealers Leaked Status | investigation | ✓ | `stealers_leaked_id`(Stealers Leaked Record ID, REQ), `status`(Status, REQ) |
| `update_stealers_on_sale_status` | Update Stealers On Sale(Marketplaces) Status | investigation | ✓ | `stealers_on_sale_id`(Stealers On Sale(Marketplaces) Record ID, REQ), `status`(Status, REQ) |
| `get_intel_reports` | Get Adversary Centric Intelligence ACI Reports | investigation | ✓ | `report_id`(Report Id), `tag`(Tag), `adversaries`(Adversaries), `source`(Source), `source_category`(Source Category), `report_type`(Report Type), `industries`(Industries), `geographies`(Geographies), `iocs`(Iocs), `source_reliability`(Source Reliability), `information_reliability`(Information Reliability), `report_generator_source`(Report Generator Source), `insight_relevance`(Report insight relevance), `motivations`(Motivations), `keyword`(Keyword), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_intel_report` | Get Specific Adversary Centric Intelligence ACI Report | investigation | ✓ | `report_id`(ACI Report ID, REQ) |
| `get_intel_iocs` | Get Intel IOCs | investigation | ✓ | `name`(IOC Name), `report_ids`(Report ID's), `type`(IOC Type), `first_seen`(First seen), `last_seen`(Last seen), `keyword`(Keyword), `sort`(Sort), `page`(Page), `size`(Size), `get_all_records`(Get All Records) |
| `get_intel_ioc` | Get Specific Adversary Centric Intelligence ACI IOCs | investigation | ✓ | `ioc_id`(IOC ID, REQ) |
| `create_task` | Create Task | investigation | ✓ | `requester`(Requester), `request`(Request), `taskId`(Task ID) |
| `update_task` | Update task | investigation | ✓ | `task_id`(Task ID, REQ), `status`(Status, REQ) |

### `fortinet-fortirecon-brand-protection`

version 2.1.1 — FortiRecon is a Digital Risk Protection Service (DRPS) product that provides an outside-the-network view to the risks posed to your enterpri…

- GitHub: connector-fortinet-fortirecon-brand-protection
- Category: Attack Surface Management
- Operations: 25

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_code_repo_exposures` | Get Code Repo Exposures | investigation | ✓ | `q`(Search By Keyword), `matched_domain`(Matched Domain), `risk_level`(Risk Level), `attribute_type`(Attribute Type), `status`(Status), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_code_repos` | Get Code Repositories | investigation | ✓ | `q`(Search By Keyword), `matched_domain`(Matched Domain), `risk_level`(Risk Level), `attribute_type`(Attribute Type), `status`(Status), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_code_repos_stats` | Get Code Repos Statistics | investigation | ✓ | — |
| `get_code_repo_matched_domains_stats` | Get Code Repo Matched Domains Statistics | investigation | ✓ | — |
| `get_domain_threats` | Get Domain Threats | investigation | ✓ | `q`(Search By Keyword), `original_domain`(Original Domain), `tags`(Tags), `online_status`(Online Status), `status`(Status), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_domain_threats_by_id` | Get Domain Threats By ID | investigation | ✓ | `id`(Domain Threat ID, REQ) |
| `get_executive_exposures` | Get Executive Exposures | investigation | ✓ | `source_type`(Source Type), `executive_id`(Executive ID), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_executive_profiles` | Get Executive Profiles | investigation | ✓ | `name`(Executive Name), `page`(Page), `size`(Size) |
| `get_open_bucket_exposures` | Get Open Bucket Exposures | investigation | ✓ | `q`(Search By Keyword), `file_type`(File Type), `bucket_type`(Bucket Type), `status`(Status), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_rogue_apps` | Get Rogue Apps | investigation | ✓ | `status`(Status), `q`(Search By Keyword), `appstore`(App Store Name), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_rogue_app_by_id` | Get Rogue App By ID | investigation | ✓ | `id`(Rogue App ID, REQ) |
| `get_social_media_threats` | Get Social Media Threats | investigation | ✓ | `q`(Search By Keyword), `media_type`(Media Type), `profile_name`(Profile Name), `handle_name`(Handle Name), `is_verified`(Is Verified), `status`(Status), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_domain_threats_stats` | Get Domain Threats Statistics | investigation | ✓ | — |
| `get_original_domains_stats` | Get Original Domains Statistics | investigation | ✓ | — |
| `get_open_bucket_exposures_stats` | Get Open Bucket Exposures Statistics | investigation | ✓ | — |
| `get_social_media_threats_stats` | Get Social Media Threats Statistics | investigation | ✓ | — |
| `get_tags` | Get Tags | investigation | ✓ | — |
| `get_takedown_requests` | Get Takedown Requests | investigation | ✓ | `q`(Search By Keyword), `status`(Status), `category`(Category), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `update_code_repo_status` | Update Code Repo Status | investigation | ✓ | `repo_id`(Code Repo ID, REQ), `status`(Status, REQ) |
| `update_domain_threat_status` | Update Domain Threat Status | investigation | ✓ | `domain_threat_id`(Domain Threat ID, REQ), `status`(Status, REQ) |
| `update_open_bucket_exposure_status` | Update Open Bucket Exposure Status | investigation | ✓ | `open_bucket_exposure_id`(Open Bucket Exposure ID, REQ), `status`(Status, REQ) |
| `update_rogue_app_exposure_status` | Update Rogue App Status | investigation | ✓ | `rogue_app_exposure_id`(Rogue App ID, REQ), `status`(Status, REQ) |
| `update_social_media_threat_status` | Update Social Media Threat Status | investigation | ✓ | `social_media_threat_id`(Social Media Threat ID, REQ), `status`(Status, REQ) |
| `create_task` | Create Task | investigation | ✓ | `requester`(Requester), `request`(Request), `taskId`(Task ID) |
| `update_task` | Update task | investigation | ✓ | `task_id`(Task ID, REQ), `status`(Status, REQ) |

### `fortinet-fortirecon-easm`

version 1.2.2 — FortiRecon is a Digital Risk Protection Service (DRPS) product that provides an outside-the-network view to the risks posed to your enterpri…

- GitHub: connector-fortinet-fortirecon-easm
- Category: Attack Surface Management
- Operations: 43

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_leaked_credentials` | Get Leaked Credentials | investigation | ✓ | `q`(Keyword), `breach_id`(Breach ID), `email`(Email ID), `domain`(Domain), `status`(Status), `has_password`(Has Password), `show_plaintext_password`(Show Plaintext Password), `start_date`(Start Date), `end_date`(End Date), `page`(Page), `size`(Size) |
| `get_scan_statistics` | Get Scan Statistics | investigation | ✓ | `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)) |
| `get_issues_discovered` | Get Issues Discovered | investigation | ✓ | `status`(Status), `severity`(Severity), `nvd_severity`(NVD Severity), `recon_severity`(Recon Severity), `countries`(Countries), `bucket_id`(Bucket ID), `issue_name_identifier`(Issue Name Identifier), `asset_type`(Asset Type), `asset`(Asset), `search_type`(Search Type), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_issue_by_id` | Get Issue By ID | investigation | ✓ | `issue_id`(Issue ID, REQ) |
| `get_issue_summary` | Get Issue Summary | investigation | ✓ | `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan) |
| `get_archived_issues` | Get Archived Issues | investigation | ✓ | `status`(Status), `asset_type`(Asset Type), `asset`(Asset), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_archived_assets` | Get Archived Assets | investigation | ✓ | `user_action`(User Action), `asset_type`(Asset Type), `asset`(Asset), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_asset_asns` | Get Asset ASNs | investigation | ✓ | `search_type`(Search Type), `asset`(Asset), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan), `discovered_by_fgt_integration`(Discovered By FortiGate Integration), `cloud_metadata`(Cloud Metadata), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_asns_by_asset_id` | Get ASNs by Asset ID | investigation | ✓ | `asset_id`(Asset ID, REQ), `linked_assets`(Linked Assets) |
| `get_domains` | Get Domains | investigation | ✓ | `ports`(Ports), `technologies`(Technologies), `asset`(Asset), `search_type`(Search Type), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan), `discovered_by_fgt_integration`(Discovered By FortiGate Integration), `is_live`(Is Live), `discovered_by_cloud_integration`(Discovered By Cloud Integration), `cloud_metadata`(Cloud Metadata), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_domain_by_asset_id` | Get Domain by Asset ID | investigation | ✓ | `asset_id`(Asset ID, REQ), `linked_assets`(Linked Assets) |
| `get_ips` | Get IPs | investigation | ✓ | `ports`(Ports), `countries`(Countries), `asset`(Asset), `search_type`(Search Type), `ip_prefix`(IP Prefix), `version`(Version), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan), `discovered_by_fgt_integration`(Discovered By FortiGate Integration), `is_live`(Is Live), `discovered_by_cloud_integration`(Discovered By Cloud Integration), `cloud_metadata`(Cloud Metadata), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_ips_by_asset_id` | Get IP by Asset ID | investigation | ✓ | `asset_id`(Asset ID, REQ), `linked_assets`(Linked Assets) |
| `get_prefixes` | Get Prefixes | investigation | ✓ | `asset`(Asset), `search_type`(Search Type), `asn`(ASN), `version`(Version), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan), `discovered_by_fgt_integration`(Discovered By FortiGate Integration), `cloud_metadata`(Cloud Metadata), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_prefixes_by_asset_id` | Get Prefixes by Asset ID | investigation | ✓ | `asset_id`(Asset ID, REQ), `linked_assets`(Linked Assets) |
| `get_subdomains` | Get Subdomains | investigation | ✓ | `ports`(Ports), `technologies`(Technologies), `domain`(Domain), `asset`(Asset), `search_type`(Search Type), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan), `discovered_by_fgt_integration`(Discovered By FortiGate Integration), `is_live`(Is Live), `discovered_by_cloud_integration`(Discovered By Cloud Integration), `cloud_metadata`(Cloud Metadata), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_subdomain_by_asset_id` | Get Subdomain by Asset ID | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `get_asset_statistics` | Get Asset Statistics | investigation | ✓ | `ports`(Ports), `countries`(Countries), `technologies`(Technologies), `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)), `after_primary_scan`(After Primary Scan) |
| `get_breaches` | Get Breaches | investigation | ✓ | `name`(Breach Name), `q`(Keyword), `has_password`(Has Password), `is_relevant`(Is Relevant), `page`(Page), `size`(Size) |
| `get_breaches_by_id` | Get Breaches by ID | investigation | ✓ | `breach_id`(Breach ID, REQ) |
| `generate_report` | Generate Report | investigation | ✓ | `tags_in`(Tags In (Match Any)), `tags_match_all`(Tags In (Match All)), `groups_in`(Groups In (Match Any)), `groups_match_all`(Groups In (Match All)) |
| `get_report` | Get Report | investigation | ✓ | `report_id`(Report ID, REQ), `get_link`(Get Report Link) |
| `get_exposed_services` | Get Exposed Services | investigation | ✓ | `asset`(Asset), `ports`(Ports), `services`(Services), `products`(Products), `service_banner`(Services Banner), `after_primary_scan`(After Primary Scan), `has_ssl`(Has SSL), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_cloud_integrations` | Get Cloud Integrations | investigation | ✓ | `provider`(Provider), `connection_status`(Connection Status), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_fgt_integrations` | Get FortiGate Integrations | investigation | ✓ | `connection_status`(Connection Status), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_security_insights` | Get Security Insights | investigation | ✓ | `domain`(Domain, REQ) |
| `get_archived_issue_comments` | Get Archived Issue Comments | investigation | ✓ | `issue_id`(Issue ID, REQ), `comment_type`(Comment Type), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_issue_comments` | Get Issue Comments | investigation | ✓ | `issue_id`(Issue ID, REQ), `comment_type`(Comment Type), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_tags` | Get Tags | investigation | ✓ | `scope`(Scope), `name`(Name), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_tag_by_id` | Get Tag Details | investigation | ✓ | `tag_id`(Tag ID, REQ), `linked_assets`(Linked Asset) |
| `get_groups` | Get Groups | investigation | ✓ | `scope`(Scope), `name`(Group Name), `created_ts`(Created Time), `modified_ts`(Modified Time), `page`(Page), `size`(Size) |
| `get_group_by_id` | Get Group Details | investigation | ✓ | `group_id`(Group ID, REQ), `linked_assets`(Linked Asset) |
| `update_archived_asset` | Update Archived Asset | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `update_archived_issue` | Mark Archived Issue as Active | investigation | ✓ | `issue_id`(Issue ID, REQ) |
| `update_issue_status` | Update Issue Status | investigation | ✓ | `issue_id`(Issue ID, REQ), `status`(Status, REQ) |
| `update_asn_asset_status_to_false_positive` | Update ASN Asset To False Positive | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `update_prefix_asset_status_to_false_positive` | Update IP Prefix Asset To False Positive | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `update_ip_asset_status_to_false_positive` | Update IP Asset To False Positive | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `update_domain_asset_status_to_false_positive` | Update Domain Asset To False Positive | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `update_subdomain_asset_status_to_false_positive` | Update Sub-Domain Asset To False Positive | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `update_leaked_credential_status` | Update Leaked Credential Status | investigation | ✓ | `leaked_cred_id`(Leaked Credential ID, REQ), `status`(Status, REQ) |
| `create_task` | Create Task | investigation | ✓ | `requester`(Requester), `request`(Request), `taskId`(Task ID) |
| `update_task` | Update task | investigation | ✓ | `task_id`(Task ID, REQ), `status`(Status, REQ) |

### `fortinet-fortisandbox`

version 2.1.0 — FortiSandbox utilizes advanced detection, dynamic antivirus scanning, and threat scanning technology to detect viruses and APTs. FortiSandbo…

- GitHub: connector-fortinet-fortisandbox
- Category: Sandbox
- Operations: 17

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `submit_file` | Submit File | investigation | ✓ | `input_type`(Indicator IRI/Attachment ID, REQ), `overwrite_vm_list`(VM Name), `un_zip_file`(Unzip File) |
| `submit_urlfile` | Submit URL | investigation | ✓ | `url`(URL, REQ), `overwrite_vm_list`(VM Name), `timeout`(Timeout), `depth`(Depth) |
| `get_system_status` | Get System Status | investigation | ✓ | — |
| `get_scan_stats` | Get Scan Stats | investigation | ✓ | — |
| `get_submission_job_list` | Get Submission Job List | investigation | ✓ | `sid`(Submission ID, REQ) |
| `get_scan_result_job` | Get Job Verdict Detail | investigation | ✓ | `jid`(Job ID, REQ) |
| `get_file_rating` | Get File Rating | investigation | ✓ | `hash_type`(Hash Type, REQ), `file_hash`(Filehash, REQ) |
| `get_url_rating` | Get URL Rating | investigation | ✓ | `url`(URL, REQ) |
| `get_file_verdict` | Get File Verdict | investigation | ✓ | `hash_type`(Hash Type, REQ), `file_hash`(Filehash, REQ) |
| `get_job_behaviour` | Get Job Behaviour | investigation | ✓ | `hash_type`(Hash Type, REQ), `file_hash`(Filehash, REQ), `decode_file_string`(Decode Behavior File String) |
| `get_avrescan` | Get AV-Rescan Result | investigation | ✓ | `stime`(From, REQ), `etime`(To, REQ), `need_av_ver`(Need AV Version) |
| `get_installed_vm` | Get All Installed VM | investigation | ✓ | — |
| `get_pdf_report` | Get PDF Report | investigation | ✓ | `qtype`(Query Type, REQ), `qval`(Query Value, REQ) |
| `download_hashes_url_from_mwpkg` | List Filehash or URL From Malware Package or URL Package | investigation | ✓ | `type`(Type, REQ), `lazy`(Lazy, REQ) |
| `mark_sample_fp_fn` | Toggle FPN State | miscellaneous | ✓ | `jid`(Job ID, REQ), `comments`(Comments, REQ) |
| `handle_white_black_list` | Update White or Black List | miscellaneous | ✓ | `list_type`(List Type, REQ), `indicator_type`(Indicator Type, REQ), `action`(Action, REQ) |
| `handle_allow_block_list` | Update Allow or Block List | miscellaneous | ✓ | `list_type`(List Type, REQ), `indicator_type`(Indicator Type, REQ), `action`(Action, REQ) |

### `fortinet-fortisase`

version 1.0.0 — FortiSASE is a cloud-delivered security service edge (SSE) solution that provides always-on secure access to private applications. This conn…

- GitHub: connector-fortinet-fortisase
- Category: Network Security
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_service` | Get Service | investigation | ✓ | `service_name`(Service Name, REQ) |
| `get_services` | Get Services List | investigation | ✓ | — |
| `create_service` | Create Service | investigation | ✓ | `primaryKey`(Primary Key, REQ), `category`(Category, REQ), `protocol`(Protocol, REQ), `port_range`(Port Range, REQ) |
| `delete_service` | Delete Service | investigation | ✓ | `primaryKey`(Primary Key, REQ) |
| `get_host` | Get Host | investigation | ✓ | `host_name`(Host Name, REQ) |
| `create_host` | Create Host | investigation | ✓ | `primaryKey`(Host Name, REQ), `location`(Location, REQ) |
| `delete_host` | Delete Host | investigation | ✓ | `primaryKey`(Primary Key, REQ) |
| `create_to_hub_policy` | Create To Hub Policy | investigation | ✗ | `policy_config`(Policy Configuration, REQ) |
| `create_from_hub_policy` | Create From Hub Policy | investigation | ✗ | `policy_config`(Policy Configuration, REQ) |
| `generic_api_call` | Generic API Call | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(API Endpoint, REQ), `data`(Request Data) |

### `fortinet-fortivoice`

version 1.0.0 — FortiVoice Secure Unified Communications, along with FortiFone IP phones, helps organizations keep up with changing communication needs due …

- GitHub: connector-fortinet-fortivoice
- Category: Communication and Coordination
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_devices_list` | Get Devices List | investigation | ✓ | `search_mac_address`(Mac Address Pattern), `get_non_assigned_devices`(Get Unassigned Devices), `start_index`(Start Index), `size`(Size) |

### `fortinet-fortiweb-cloud`

version 2.0.0 — FortiAppSec Cloud simplifies and strengthens application security and delivery across hybrid and cloud environments. This SaaS platform secu…

- GitHub: connector-fortinet-fortiweb-cloud
- Category: Cloud Security
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_incident_dashboard_details` | Get Incident Dashboard Details | investigation | ✓ | `widget_id`(Widget Name, REQ), `action`(Action Name), `host`(Host Name), `time_range`(Time Range) |
| `get_incident_list` | Get Incidents List | investigation | ✓ | `time_range`(Time Range, REQ), `filter`(Filter), `size`(Page Size), `page`(Page Number) |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `get_incident_timeline_details` | Get Incident Timeline Details | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `get_insight_events_summary` | Get Insight Events Summary | investigation | ✓ | — |
| `get_incident_aggregated_details` | Get Incident Aggregated Details | investigation | ✓ | `incident_id`(Incident ID, REQ), `name`(Group By, REQ) |
| `get_insight_events` | Get Insight Events | investigation | ✓ | `type`(Event Type, REQ), `cursor`(Cursor), `size`(Page Size), `forward`(Forward) |
| `get_ip_protection` | Get IP Protection | investigation | ✓ | `epid`(Application ID, REQ) |
| `add_ip_protection` | Add IP Protection | investigation | ✓ | `epid`(Application ID, REQ), `iptype`(IP Type, REQ), `ipaddress`(IP Address, REQ) |
| `delete_ip_protection` | Delete IP Protection | investigation | ✓ | `epid`(Application ID, REQ), `iptype`(IP Type, REQ), `ipaddress`(IP Address, REQ) |
| `get_application_list` | Get Applications List | investigation | ✓ | `filter`(Filter), `size`(Page Size), `cursor`(Cursor), `forward`(Forward) |
| `update_geo_ip_block_list` | Update Geo IP Block List | investigation | ✓ | `epid`(Application ID, REQ), `operation_to_perform`(Operation To Perform, REQ), `block_country_list`(Countries) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `fortinet-web-filter-lookup`

version 2.0.0 — Fortinet Web Filter Lookup allows users to check category and classification for any Domain

- GitHub: connector-fortinet-web-filter-lookup
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `url_review` | Check Category of Domain or URL | investigation | ✓ | `sample_url`(Submit Domain/URL, REQ) |

### `fortisoar-soc-simulator`

version 2.0.0 — The FortiSOAR SOC Simulator connector is a special type of connector that is used to simulate a SOC environment. It creates various scenario…

- GitHub: connector-fortisoar-soc-simulator
- Category: information
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `bad_ip` | Fetch Malicious IP | investigation | ✓ | `random`(Random) |
| `bad_url` | Fetch Malicious URL | investigation | ✓ | `random`(Random) |
| `bad_filehash` | Fetch Malicious Filehash | investigation | ✓ | `random`(Random) |
| `bad_domain` | Fetch Malicious Domain | investigation | ✓ | `random`(Random) |
| `replace_variables` | Replace Variables | — | ✓ | `variables`(Variable String, REQ) |
| `malicious_file_indicator` | Create Malicious File Indicator | — | ✓ | `file_name`(File Name), `malicious_url`(Embedded Malicious URL), `malicious_email`(Embedded Malicious Email), `custom_parameters`(Custom Indicator Parameters), `attachment_also`(Also Create Attachment) |
| `create_simulated_alert` | Create Simulated Alert | — | ✓ | `alert_json`(Alert Data, REQ), `fields_to_ignore`(Fields To Ignore) |

### `fresh-service-desk-msp`

version 1.1.0 — Fresh Service Desk MSP is a cloud-based service desk and IT service management (ITSM) platform designed to streamline service management for…

- GitHub: connector-fresh-service-desk-msp
- Category: Ticket Management
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_ticket` | Create Ticket | investigation | ✗ | `subject`(Subject, REQ), `email`(Email, REQ), `cc_emails`(CC Email), `status`(Status, REQ), `priorities`(Priorities, REQ), `description`(Description, REQ) |
| `get_ticket_by_id` | Get Ticket By ID | investigation | ✗ | `ticket_id`(Ticket ID, REQ) |
| `delete_ticket_by_id` | Delete Ticket By ID | investigation | ✗ | `ticket_id`(Ticket ID, REQ) |
| `update_ticket` | Update Ticket | investigation | ✗ | `ticket_id`(Ticket ID, REQ), `subject`(Subject), `description`(Description), `email`(Email), `status`(Status), `priorities`(Priorities), `path`(File IRI or Attachment IRI) |
| `filter_tickets_by_query` | Filter Tickets By Query | investigation | ✗ | `query`(Query, REQ) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `fsr-change-management`

version 1.0.0 — Synchronize the FortiSOAR Change Request record from one FortiSOAR instance to another

- GitHub: connector-fsr-change-management
- Category: Change Management
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `sync_change_request` | Sync Change Request | investigation | ✓ | `cr_payload`(Change Request Payload, REQ) |

### `fullhunt`

version 1.0.0 — FullHunt enables companies to discover all of their attack surfaces, monitor them for exposure and continuously scan them for the latest sec…

- GitHub: connector-fullhunt
- Category: Vulnerability and Risk Management
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_domain_details` | Get Domain Details | investigation | ✗ | `domain`(Domain, REQ) |
| `get_subdomain_of_domain` | Get Subdomains of a Domain | investigation | ✗ | `domain`(Domain, REQ) |
| `get_specific_host_details` | Get Details of a Specific Host | investigation | ✗ | `host`(Host, REQ) |

### `fuzzy-search`

version 1.0.0 — Connector provides actions to find relevant results even when they do not know the exact term by filtering the provided JSON data and also s…

- GitHub: connector-fuzzy-search
- Category: Utilities
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `filter_json_by_key_value` | Filter JSON by Key Value | investigation | ✓ | `inputJSON`(Input JSON, REQ), `targetKeyValue`(Target Key Value, REQ), `similarityThreshold`(Similarity Threshold, REQ), `fuzzyMatch`(Fuzzy Match) |
| `search_keyword_in_text` | Search Keyword In Text | investigation | ✗ | `inputText`(Input Text, REQ), `keywordToSearch`(Keyword To Search, REQ), `limit`(Limit, REQ), `cutoff`(Cut Off, REQ) |

### `gcp-ca-service`

version 1.0.1 — Certificate Authority Service is a highly available and scalable Google Cloud service that enables you to simplify, automate, and customize …

- GitHub: connector-gcp-ca-service
- Category: Utilities
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_certificate_authorities` | Get Certificate Authorities | investigation | ✓ | `location`(Location, REQ), `ca_pool_name`(CA Pool Name, REQ) |
| `get_ca_crl` | Get CA and CRL | investigation | ✓ | `location`(Location, REQ), `ca_name`(CA Name, REQ), `ca_pool_name`(CA Pool Name, REQ) |
| `csr` | Submit CSR | investigation | ✓ | `location`(Location, REQ), `ca_pool_name`(CA Pool Name, REQ), `ca_name`(Certificate Authority (CA), REQ), `certificate_name`(Certificate Name, REQ), `certificate_lifetime`(Certificate Lifetime, REQ), `pem_csr`(CSR with a PEM Formatted Key, REQ) |
| `revoke_certificate` | Revoke Certificate | investigation | ✓ | `location`(Location, REQ), `ca_pool_name`(CA Pool Name, REQ), `certificate_name`(Certificate Name, REQ) |

### `git-guardian`

version 1.0.0 — GitGuardian is a cybersecurity platform that specializes in detecting and preventing the exposure of sensitive information in source code re…

- GitHub: connector-git-guardian
- Category: Vulnerability and Risk Management
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_secret_incidents` | Get Secret Incidents List | investigation | ✓ | `per_page`(Number of Incidents Per Page), `date_after`(Incidents After the Date), `date_before`(Incidents Before the Date), `status`(Status), `severity`(Severity), `validity`(Validity), `tags`(Tags), `ordering`(Ordering), `assignee_email`(Assignee Email), `assignee_id`(Assignee ID), `detector_group_name`(Detector Group Name), `ignorer_id`(Ignorer ID), `resolver_id`(Resolver ID), `cursor`(Cursor) |
| `retrieve_a_secret_incident` | Get Secret Incident Details | investigation | ✓ | `incident_id`(Incident ID, REQ), `with_occurrences`(Number of Occurrences) |
| `update_a_secret_incident` | Update Secret Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `severity`(Severity, REQ) |
| `assign_a_secret_incident` | Assign Secret Incident  | investigation | ✓ | `incident_id`(Incident ID, REQ), `email`(Email), `member_id`(Member ID) |
| `unassign_a_secret_incident` | Unassign Secret Incident  | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `resolve_a_secret_incident` | Resolve Secret Incident  | investigation | ✓ | `secret_revoked`(Secret Revoked, REQ), `incident_id`(Incident ID, REQ) |
| `content_scan` | Scan Documents Content | investigation | ✓ | `input`(Type, REQ), `value`(Reference ID, REQ), `filename`(Filename, REQ) |
| `list_secret_occurrences` | Get Secret Occurrences List | investigation | ✓ | `per_page`(Number of Occurrences per page), `source_id`(Source ID), `source_name`(Source Name), `incident_id`(Incident ID), `date_after`(Occurrences After Date), `date_before`(Occurrences Before Date), `presence`(Presence), `author_name`(Author Name), `author_info`(Author Info), `sha`(Sha), `filepath`(Filepath), `ordering`(Ordering), `cursor`(Cursor), `tags`(Tags) |
| `get_members_list` | Get Members List | investigation | ✓ | `per_page`(Number of Members per page), `role`(Role), `search`(Search), `ordering`(Ordering), `cursor`(Cursor) |
| `list_sources` | Get Sources List | investigation | ✓ | `per_page`(Per Page), `search`(Search), `last_scan_status`(Last Scan Status), `health`(Health), `type`(Type), `ordering`(Ordering), `visibility`(Visibility), `cursor`(Cursor), `external_id`(External ID) |

### `git-guardian-enterprise`

version 1.0.0 — GitGuardian Enterprise is a security platform designed to detect, monitor, and remediate secrets (like API keys, passwords, and tokens) and …

- GitHub: connector-git-guardian-enterprise
- Category: Vulnerability and Risk Management
- Operations: 23

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_audit_logs` | Get All Audit Logs | investigation | ✓ | `actor__in`(Include Actor(s)), `actor__nin`(Exclude Actor(s)), `actor_email`(Actor Email), `ordering`(Ordering), `search`(Full-Text Search), `type`(Type), `type__in`(Include Types), `type__nin`(Exclude Types), `page`(Page Number), `per_page`(Results Per Page) |
| `get_audit_log_details` | Get Audit Log Details | investigation | ✓ | `id`(Audit Log ID) |
| `get_audit_log_actors_types` | Get Audit Log Actors/Types | investigation | ✓ | `audit_log_metadata`(Audit Log Metadata, REQ), `page`(Page Number), `per_page`(Results Per Page) |
| `get_all_git_users` | Get All Git Users | investigation | ✓ | `git_type`(Git Type, REQ), `page`(Page Number), `per_page`(Results Per Page) |
| `get_git_user_details` | Get Git User Details | investigation | ✓ | `git_type`(Git Type, REQ) |
| `create_keyword` | Create Keyword | investigation | ✓ | `id`(Keyword ID, REQ), `name`(Keyword Name, REQ), `keyword`(Keyword, REQ), `categories`(Categories, REQ), `status`(Status, REQ), `type`(Keyword Type, REQ), `labels`(Labels, REQ), `created_at`(Created At, REQ) |
| `get_all_keywords` | Get All Keywords | investigation | ✓ | `keyword_type`(Keyword Type, REQ), `categories`(Categories), `status`(Status), `type`(Keyword Type), `ordering`(Ordering), `search`(Full-Text Search), `labels__in`(Include Labels), `labels__nin`(Exclude Labels), `status__in`(Include Status), `status__nin`(Exclude Status), `type__in`(Include Types), `type__nin`(Exclude Types), `page`(Page Number), `per_page`(Results Per Page) |
| `get_keyword_details` | Get Keyword Details | investigation | ✓ | `keyword_type`(Keyword Type, REQ) |
| `update_keyword_details` | Update Keyword Details | investigation | ✓ | `keyword_type`(Keyword Type, REQ), `labels`(Labels, REQ), `name`(New Keyword Name, REQ) |
| `delete_keyword` | Delete Keyword | investigation | ✓ | `keyword_type`(Keyword Type, REQ) |
| `export_keywords` | Export Keywords | investigation | ✓ | — |
| `get_all_incident_secrets` | Get All Incident Secrets | investigation | ✓ | `search`(Full-Text Search), `severity`(Severity), `status`(Status), `created_at__current`(Created At (Current Period)), `created_at__from`(Created From), `created_at__to`(Created To), `ordering`(Ordering), `page`(Page Number), `per_page`(Results Per Page), `additional_fields`(Additional Parameters) |
| `get_incident_secret_details` | Get Incident Secret Details | investigation | ✓ | `id`(Incident Secret ID) |
| `update_incident_secret_status` | Update Incident Secret Status | investigation | ✓ | `id`(Incident Secret ID), `action`(Status, REQ) |
| `create_incident_secret_shared_link` | Create Incident Secret Shared Link | investigation | ✓ | `id`(Incident Secret ID) |
| `rotate_incident_secret_shared_link` | Rotate Incident Secret Shared Link | investigation | ✓ | `id`(Incident Secret ID) |
| `delete_incident_secret_shared_link` | Delete Incident Secret Shared Link | investigation | ✓ | `id`(Incident Secret ID) |
| `get_all_incident_keywords` | Get All Incident Keywords | investigation | ✓ | `page`(Page Number), `per_page`(Results Per Page) |
| `get_incident_keyword_details` | Get Incident Keyword Details | investigation | ✓ | `id`(Incident Keyword ID, REQ) |
| `update_incident_keyword_status` | Update Incident Keyword Status | investigation | ✓ | `id`(Incident Keyword ID), `action`(Status, REQ) |
| `get_incident_secret_note` | Get Incident Secret Note | investigation | ✓ | `id`(Incident Secret ID) |
| `get_incident_keyword_note` | Get Incident Keyword Note | investigation | ✓ | `id`(Incident Keyword ID, REQ) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `github`

version 2.1.0 — GitHub is a code hosting platform for collaboration and version control. This connector facilitates automated interactions with Github, such…

- GitHub: connector-github
- Category: Source Code Management
- Operations: 45

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_repository` | Create Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `name`(Repository Name, REQ), `description`(Description), `homepage`(Homepage), `private`(Private), `has_issues`(Has Issues), `has_projects`(Has Projects), `has_wiki`(Has Wiki), `is_template`(Is Template), `other_fields`(Other Fields) |
| `create_repository_using_template` | Create Repository Using Template | investigation | ✓ | `template_owner`(Template Owner, REQ), `template_repo`(Template Repository, REQ), `name`(New Repository Name, REQ), `owner`(New Repository Owner), `description`(Description), `include_all_branches`(Include All Branches), `private`(Private) |
| `get_repository` | Get Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ) |
| `list_organization_repositories` | List Organization Repositories | investigation | ✓ | `org`(Organization Name, REQ), `type`(Repository Type, REQ), `sort`(Sort, REQ), `direction`(Direction, REQ), `per_page`(Per Page), `page`(Page) |
| `list_user_repositories` | List User Repositories | investigation | ✓ | `username`(Username, REQ), `type`(Repository Type, REQ), `sort`(Sort, REQ), `direction`(Direction, REQ), `per_page`(Per Page), `page`(Page) |
| `list_authenticated_user_repositories` | List Authenticated User Repositories | investigation | ✓ | `affiliation`(Affiliation), `visibility`(Visibility), `type`(Repository Type), `sort`(Sort), `direction`(Direction), `since`(Updated After), `before`(Updated Before), `per_page`(Per Page), `page`(Page) |
| `update_repository` | Update Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Old Repository Name, REQ), `name`(New Repository Name, REQ), `description`(Description), `homepage`(Homepage), `private`(Private), `has_issues`(Has Issues), `has_projects`(Has Projects), `has_wiki`(Has Wiki), `other_fields`(Other Fields) |
| `delete_repository` | Delete Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ) |
| `fork_organization_repository` | Fork Organization Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `organization`(Organization Name), `name`(New Fork Name), `default_branch_only`(Default Branch) |
| `list_fork_repositories` | List Fork Repositories | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `sort`(Sort Repository By, REQ), `per_page`(Per Page), `page`(Page) |
| `create_update_file_contents` | Create or Update File Contents | investigation | ✓ | `repo_type`(Repository Type, REQ), `name`(Repository Name, REQ), `path`(File Name, REQ), `message`(Commit Message, REQ), `content`(File Content, REQ), `branch`(Branch Name), `sha`(SHA) |
| `get_file_from_repository` | Get File | investigation | ✓ | `repo_type`(Repository Type, REQ), `name`(Repository Name, REQ), `path`(File Name, REQ), `branch`(Branch Name), `decode_content`(Decode Content) |
| `delete_file_from_repository` | Delete File | investigation | ✓ | `repo_type`(Repository Type, REQ), `name`(Repository Name, REQ), `path`(File Name, REQ), `message`(Commit Message, REQ), `sha`(SHA, REQ), `branch`(Branch Name) |
| `add_repository_collaborator` | Add Repository Collaborator | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `username`(Collaborator Username, REQ), `permission`(Permission) |
| `list_repository_collaborator` | List Repository Collaborator | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `affiliation`(Collaborator Affiliation), `permission`(Permission), `per_page`(Per Page), `page`(Page) |
| `get_branch_revision` | Get Branch Revision | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `base`(Base Branch, REQ) |
| `create_branch` | Create Branch | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `new_branch_name`(New Branch Name, REQ), `checkout_branch`(Base Branch Name/SHA, REQ) |
| `merge_branch` | Merge Branch | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `base`(Base Branch Name, REQ), `head`(Head, REQ), `commit_message`(Commit Message) |
| `list_branches` | List Branches | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `protected`(Protected), `per_page`(Per Page), `page`(Page) |
| `get_commit` | Get Commit | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `ref`(Reference, REQ), `per_page`(Per Page), `page`(Page) |
| `compare_commit` | Get Commit Comparison | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `base`(Base, REQ), `head`(Head, REQ), `per_page`(Per Page), `page`(Page) |
| `delete_branch` | Delete Branch | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `branch_name`(Branch Name, REQ) |
| `fetch_upstream` | Fetch Upstream | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `branch`(Branch Name, REQ) |
| `clone_repository` | Clone Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `name`(Repository Name, REQ), `branch`(Branch Name), `clone_zip`(Clone As ZIP, REQ) |
| `update_clone_repository` | Update Remote Repository | investigation | ✓ | `file_iri`(FortiSOAR File IRI, REQ), `clone_path`(Cloned Repository Path, REQ) |
| `push_repository` | Push Changes | investigation | ✓ | `repo_type`(Repository Type, REQ), `name`(Repository Name, REQ), `clone_path`(Cloned Repository Path, REQ), `branch`(Branch Name, REQ), `commit_message`(Commit Summary, REQ), `commit_description`(Commit Description) |
| `create_pull_request` | Create Pull Request | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `head`(Head Repository, REQ), `base`(Base Branch, REQ), `title`(Pull Request Title), `body`(Pull Request Comments), `maintainer_can_modify`(Allow Edits By Maintainers), `draft`(Draft) |
| `list_pull_request` | List Pull Request | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `pull_number`(Pull Number), `state`(State), `head`(Head Repository), `base`(Base Branch), `sort`(Sort), `direction`(Direction), `per_page`(Per Page), `page`(Page) |
| `add_reviewers` | Add Reviewers for a Pull Request | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `pull_number`(Pull Number, REQ), `reviewers`(Reviewers), `team_reviewers`(Team Reviewers) |
| `list_review_comments` | List Review Comments on a Pull Request | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `pull_number`(Pull Number, REQ), `sort`(Sort), `direction`(Direction) |
| `list_pr_reviews` | List Pull Request Reviews | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `pull_number`(Pull Number, REQ), `per_page`(Per Page), `page`(Page) |
| `add_pr_review` | Add Pull Request Review | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `pull_number`(Pull Number, REQ), `commit_id`(Commit ID), `body`(Review Comment), `event`(Review Action) |
| `merge_pull_request` | Merge Pull Request | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `pull_number`(Pull Number, REQ), `commit_title`(Commit Title), `commit_message`(Commit Message), `sha`(SHA), `merge_method`(Merge Method) |
| `create_issue` | Create Issue | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `title`(Title, REQ), `body`(Contents), `assignees`(Assignees), `milestone`(Milestone), `labels`(Labels) |
| `list_repository_issue` | List Repository Issue | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `milestone`(Milestone), `state`(State), `assignee`(Assignee), `creator`(Creator), `mentioned`(Mentioned), `labels`(Labels), `sort`(Sort), `direction`(Direction), `since`(Since), `per_page`(Per Page), `page`(Page) |
| `update_issue` | Update Issue | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `issue_number`(Issue Number, REQ), `title`(Title), `body`(Contents), `state`(State), `state_reason`(State Reason), `milestone`(Milestone), `labels`(Labels), `assignees`(Assignees) |
| `create_issue_comment` | Create Issue Comment | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `issue_number`(Issue Number, REQ), `body`(Comment, REQ) |
| `create_release` | Create Release | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `tag_name`(Tag Name, REQ), `target_commitish`(Target Branch), `name`(Release Title), `body`(Release Description), `generate_release_notes`(Generate Release Notes) |
| `list_releases` | List Releases | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `per_page`(Per Page), `page`(Page) |
| `list_stargazers` | List Stargazers | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `per_page`(Per Page), `page`(Page) |
| `star_repository` | Star Repository | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ) |
| `list_watchers` | List Watchers | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `per_page`(Per Page), `page`(Page) |
| `set_repo_subscription` | Set Repository Subscription | investigation | ✓ | `repo_type`(Repository Type, REQ), `repo`(Repository Name, REQ), `subscribed`(Subscribed), `ignored`(Ignored) |
| `get_web_url` | Get Server URL | investigation | ✓ | — |
| `search_code` | Search Code | investigation | ✓ | `query`(Search Query, REQ), `per_page`(Per Page), `page`(Page) |

### `goanywhere`

version 1.0.0 — GoAnywhere MFT is a secure file transfer solution that organizations use to exchange their data safely. The solution helps organizations aut…

- GitHub: connector-goanywhere
- Category: IT Services
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_file_transfer_summary` | Get File Transfer Summary | investigation | ✓ | `module`(Module), `date_range`(Date Range), `group_by`(Group By) |
| `get_active_sessions_details` | Get Active Sessions Details | investigation | ✓ | `services`(Services), `max_rows`(Limit) |
| `get_completed_jobs_summary` | Get Completed Jobs Summary | investigation | ✓ | `date_range`(Date Range), `group_by`(Group By), `status`(Status) |

### `gogetssl`

version 1.0.0 — GOGETSSL offers SSL/TLS certificates and digital security solutions to secure websites, emails, and networks. With this connector, users can…

- GitHub: connector-gogetssl
- Category: Authentication
- Operations: 18

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_domain_alternative` | Get Domain Alternative | investigation | ✓ | `csr`(Certificate Signing Request (CSR), REQ) |
| `get_domain_emails` | Get Domain Emails | investigation | ✓ | `domain`(Domain, REQ) |
| `get_domain_emails_for_geo_trust` | Get Geotrust Approval Emails | investigation | ✓ | `domain`(Domain, REQ) |
| `get_domain_from_whois` | Get Approver Emails | investigation | ✓ | `domain`(Domain, REQ) |
| `get_all_products` | Get All Products | investigation | ✓ | — |
| `get_product_details` | Get Product Details | investigation | ✓ | `product_id`(Product ID, REQ) |
| `get_orders_metadata` | Get Orders Metadata | investigation | ✓ | — |
| `get_orders_details` | Get Orders Details | investigation | ✓ | `order_id`(Order ID, REQ) |
| `get_all_orders_status` | Get All Orders Status | investigation | ✓ | `cids`(CIDs, REQ) |
| `get_total_order_count` | Get Total Order Count | investigation | ✓ | — |
| `generate_csr` | Generate CSR | investigation | ✓ | `csr_commonname`(Common Name, REQ), `csr_organization`(Organization Name, REQ), `csr_department`(Department, REQ), `csr_city`(City, REQ), `csr_state`(State, REQ), `csr_country`(Country, REQ), `csr_email`(Email Address, REQ) |
| `validate_csr` | Validate CSR | investigation | ✓ | `csr`(Certificate Signing Request (CSR), REQ) |
| `decode_csr` | Decode CSR | investigation | ✓ | `csr`(Certificate Signing Request (CSR), REQ) |
| `add_ssl_order` | Add SSL Order | investigation | ✓ | `product_id`(Product ID, REQ), `csr`(Certificate Signing Request (CSR), REQ), `server_count`(Server Count, REQ), `period`(Period, REQ), `webserver_type`(Web Server Type, REQ), `additional_field`(Additional Field) |
| `reissue_ssl_order` | Reissue SSL Order | investigation | ✓ | `order_id`(Order ID, REQ), `csr`(Certificate Signing Request (CSR), REQ), `webserver_type`(Web Server Type, REQ), `dcv_method`(DCV Method, REQ), `dns_names`(DNS Names, REQ), `approver_emails`(Approver Emails), `approver_email`(Approver Email), `signature_hash`(Signature Hash), `additional_field`(Additional Field) |
| `add_ssl_renew_order` | Add SSL Renew Order | investigation | ✓ | `product_id`(Product ID, REQ), `csr`(Certificate Signing Request (CSR), REQ), `server_count`(Server Count, REQ), `period`(Period, REQ), `approver_emails`(Approver Emails, REQ), `additional_field`(Additional Field) |
| `add_ssl_san_order` | Add SSL SAN Order | investigation | ✓ | `order_id`(Order ID, REQ), `wildcard_san_count`(Wildcard SAN Count), `single_san_count`(Single SAN Count) |
| `cancel_order` | Cancel Order | investigation | ✓ | `order_id`(Order ID, REQ), `reason`(Reason) |

### `google-bard`

version 2.1.0 — Google Gemini is a conversational AI chatbot, based initially on the LaMDA family of large language models and later the PaLM LLM.

- GitHub: connector-google-bard
- Category: Miscellaneous
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_models` | Get All Model List | investigation | ✓ | `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_model_details` | Get Model Details | investigation | ✓ | `name`(Model Name, REQ) |
| `generate_text` | Generate Text | investigation | ✓ | `name`(Model Name, REQ), `contents`(Contents, REQ), `safetySettings`(Safety Settings), `system_instruction`(System Instructions), `stopSequences`(Stop Sequences), `temperature`(Temperature), `maxOutputTokens`(Maximum Output Tokens), `topP`(Cumulative Probability (TopP)), `topK`(Token (TopK)), `thinkingLevel`(Thinking Levels) |
| `generate_embeddings` | Generate Embedding | investigation | ✓ | `name`(Model Name, REQ), `content`(Content, REQ), `taskType`(Task Type), `outputDimensionality`(Output Dimensionality) |
| `count_message_token` | Count Message Token | investigation | ✓ | `name`(Model Name, REQ), `messages`(Messages, REQ) |

### `google-calendar`

version 1.0.0 — Google Calendar is a web-based calendar service developed by Google, allowing users to organize their schedules, appointments, and events se…

- GitHub: connector-google-calendar
- Category: Utilities
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_calendar_list` | Get All Calendar List | investigation | ✓ | `minAccessRole`(Minimum Access Role), `showDeleted`(Include Deleted Calendar), `showHidden`(Show Hidden Calendar), `maxResults`(Maximum Results), `pageToken`(Page Token), `syncToken`(Sync Token) |
| `get_calendar_list_details` | Get Calendar List Details | investigation | ✓ | `calendar_id`(Calendar ID, REQ) |
| `delete_calendar_list` | Delete Calendar List | investigation | ✓ | `calendar_id`(Calendar ID, REQ) |
| `get_calendar_access_control_list` | Get Calendar Access Control List | investigation | ✓ | `calendar_id`(Calendar ID, REQ), `showDeleted`(Include Deleted Access Control List (ACL)), `maxResults`(Maximum Results), `pageToken`(Page Token), `syncToken`(Sync Token) |
| `get_access_control_rule_details` | Get Access Control Rule Details | investigation | ✓ | `calendar_id`(Calendar ID, REQ), `rule_id`(Rule ID, REQ) |
| `delete_access_control_rule` | Delete Access Control Rule | investigation | ✓ | `calendar_id`(Calendar ID, REQ), `rule_id`(Rule ID, REQ) |
| `get_events_list` | Get Events List | investigation | ✓ | `calendar_id`(Calendar ID, REQ), `eventTypes`(Event Types), `timeMax`(Created After), `timeMin`(Created Before), `updatedMin`(Last Modification Time), `orderBy`(Order By), `maxAttendees`(Maximum Attendees), `maxResults`(Maximum Results), `pageToken`(Page Token), `additional_parameters`(Additional Fields) |
| `get_event_details` | Get Event Details | investigation | ✓ | `calendar_id`(Calendar ID, REQ), `event_id`(Event ID, REQ), `maxAttendees`(Maximum Attendees), `timeZone`(TimeZone) |

### `google-cloud-compute`

version 1.2.0 — Google Compute Engine's tooling and workflow supports to create advanced networks on the regional levels and load balancing capabilities in …

- GitHub: connector-google-cloud-compute
- Category: Compute Platform
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_instances_within_zone` | List Instances within Zone | investigation | ✓ | `zone`(Zone, REQ), `filter`(Filter), `order_by`(OrderBy), `page_token`(Page Token), `max_results`(Max Results) |
| `describe_instance` | Get Instance Details | investigation | ✓ | `zone`(Zone, REQ), `resource_id`(Resource ID, REQ) |
| `start_instance` | Start Instance | miscellaneous | ✓ | `zone`(Zone, REQ), `resource_id`(Resource ID, REQ) |
| `stop_instance` | Stop Instance | miscellaneous | ✓ | `zone`(Zone, REQ), `resource_id`(Resource ID, REQ) |
| `delete_instance` | Delete Instance | miscellaneous | ✓ | `zone`(Zone, REQ), `resource_id`(Resource ID, REQ) |
| `reset_instance` | Reset Instance | miscellaneous | ✓ | `zone`(Zone, REQ), `resource_id`(Resource ID, REQ) |
| `get_aggregated_list_instances` | Aggregated List Instances | investigation | ✓ | `include_all_scopes`(Include all scopes), `filter`(Filter), `order_by`(OrderBy), `page_token`(Page Token), `max_results`(Max Results), `return_partial_success`(Return partial success) |
| `set_label` | Set Instance Label | investigation | ✓ | `instance_name`(Instance Name, REQ), `zone`(Zone, REQ), `new_key`(Key Name, REQ), `new_value`(Key Value, REQ) |
| `disk_snapshot` | Disk Snapshot | investigation | ✓ | `zone`(Zone, REQ), `instance_name`(instance_name, REQ) |

### `google-cloud-functions`

version 1.0.0 — Google Cloud Functions is a serverless execution environment for building and connecting cloud services.

- GitHub: connector-google-cloud-functions
- Category: Utilities
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_locations_list` | Get Locations List | investigation | ✓ | `project_name`(Project Name, REQ), `filter`(Filter), `pageSize`(PageSize), `pageToken`(PageToken) |
| `get_functions_list` | Get Functions List | investigation | ✓ | `project_name`(Project Name, REQ), `location_name`(Location, REQ), `filter`(Filter), `orderBy`(Order By) |
| `get_function_details` | Get Function Details | investigation | ✓ | `project_name`(Project Name, REQ), `location_name`(Location, REQ), `function_name`(Function Name, REQ) |
| `get_access_control_policy` | Get Access Control Policy | investigation | ✓ | `project_name`(Project Name, REQ), `location_name`(Location, REQ), `function_name`(Function Name, REQ), `requestedPolicyVersion`(Policy Version) |
| `set_access_control_policy` | Set Access Control Policy | investigation | ✓ | `project_name`(Project Name, REQ), `location_name`(Location, REQ), `function_name`(Function Name, REQ), `auditConfigs`(Audit Configs, REQ), `bindings`(Bindings, REQ), `etag`(Etag, REQ), `version`(Policy Version, REQ), `updateMask`(Update Mask) |

### `google-cloud-logging`

version 1.0.0 — Cloud Logging is a fully managed service that allows you to store, search, analyze, monitor, and alert on logging data and events from Googl…

- GitHub: connector-google-cloud-logging
- Category: Logging
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_log_entries_list` | Get Log Entries List | investigation | ✓ | `resourceNames`(Resource Names, REQ), `filter`(Filter), `orderBy`(Order By), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_exclusions_list` | Get Exclusions List | investigation | ✓ | `resourceNames`(Parent Resource Name, REQ), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_sinks_list` | Get Sinks List | investigation | ✓ | `resourceNames`(Parent Resource Name, REQ), `filter`(Filter), `pageSize`(Page Size), `pageToken`(Page Token) |

### `google-cloud-platform-whitelist-feed`

version 1.0.0 — Google Cloud Platform publishes its current IP address ranges in JSON format. This connector facilitates automated operations to fetch these…

- GitHub: connector-google-cloud-platform-whitelist-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `ip_ranges` | Get IP Ranges | investigation | ✓ | `file_value`(File, REQ) |

### `google-cloud-storage`

version 1.0.0 — Google Cloud Storage is a RESTful online file storage web service for storing and accessing data on Google Cloud Platform infrastructure. Th…

- GitHub: connector-google-cloud-storage
- Category: IT Services
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_bucket` | Create Bucket | investigation | ✓ | `project`(Project, REQ), `bucket`(Bucket Name, REQ), `predefinedAcl`(Predefined Access Control), `predefinedDefaultObjectAcl`(Predefined Default Object Access Control), `projection`(Projection), `additional_fields`(Additional Fields) |
| `get_buckets_list` | Get Buckets List | investigation | ✓ | `project`(Project, REQ), `maxResults`(Page Size), `pageToken`(Page Token), `prefix`(Prefix), `projection`(Projection) |
| `get_bucket_details` | Get Bucket Details | investigation | ✓ | `bucket`(Bucket Name, REQ), `ifMetagenerationMatch`(Metageneration Match), `ifMetagenerationNotMatch`(Metageneration Not Match), `projection`(Projection) |
| `delete_bucket` | Delete Bucket | investigation | ✓ | `bucket`(Bucket Name, REQ), `ifMetagenerationMatch`(Metageneration Match), `ifMetagenerationNotMatch`(Metageneration Not Match) |
| `create_bucket_policy` | Create Bucket Policy | investigation | ✓ | `bucket`(Bucket Name, REQ), `entity`(Entity, REQ), `role`(Role, REQ), `additional_fields`(Additional Fields) |
| `get_buckets_list_policy` | Get Bucket's List Policy | investigation | ✓ | `bucket`(Bucket Name, REQ) |
| `get_bucket_policy_details` | Get Bucket Policy Details | investigation | ✓ | `bucket`(Bucket Name, REQ), `entity`(Entity, REQ) |
| `update_bucket_policy` | Update Bucket Policy | investigation | ✓ | `bucket`(Bucket Name, REQ), `entity`(Entity, REQ), `role`(Role), `additional_fields`(Additional Fields) |
| `delete_bucket_policy` | Delete Bucket Policy | investigation | ✓ | `bucket`(Bucket Name, REQ), `entity`(Entity, REQ) |
| `create_bucket_object_policy` | Create Bucket Object Policy | investigation | ✓ | `bucket`(Bucket Name, REQ), `bucket`(Object Name, REQ), `entity`(Entity, REQ), `role`(Role, REQ), `generation`(Generation) |
| `get_buckets_list_object_policy` | Get Bucket's List Object Policy | investigation | ✓ | `bucket`(Bucket Name, REQ), `bucket`(Object Name, REQ), `generation`(Generation) |
| `get_bucket_object_policy_details` | Get Bucket Policy Object Details | investigation | ✓ | `bucket`(Bucket Name, REQ), `bucket`(Object Name, REQ), `entity`(Entity, REQ), `generation`(Generation) |
| `update_bucket_object_policy` | Update Bucket Object Policy | investigation | ✓ | `bucket`(Bucket Name, REQ), `bucket`(Object Name, REQ), `entity`(Entity, REQ), `role`(Role), `generation`(Generation), `additional_fields`(Additional Fields) |
| `delete_bucket_object_policy` | Delete Bucket Object Policy | investigation | ✓ | `bucket`(Bucket Name, REQ), `bucket`(Object Name, REQ), `entity`(Entity, REQ), `generation`(Generation) |

### `google-cloud-translate`

version 1.0.0 — Google Cloud translation technology to instantly translate texts into more than one hundred languages

- GitHub: connector-google-cloud-translate
- Category: Google service
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `translate_text` | Translate Text | investigation | ✓ | `input_text`(Input Text, REQ), `target`(Target, REQ), `format`(Format), `source`(Source), `model`(Model) |
| `get_supported_languages` | Get Languages | investigation | ✓ | — |

### `google-docs`

version 1.0.0 — Google Docs is a cloud-based word processing application developed by Google. It allows users to create, edit, and collaborate on documents …

- GitHub: connector-google-docs
- Category: Utilities
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_document` | Create Document | investigation | ✓ | `title`(Title, REQ) |
| `get_document_details` | Get Document Details | investigation | ✓ | `document_id`(Document ID, REQ), `suggestionsViewMode`(Suggestions View Mode) |
| `update_documents` | Update Documents | investigation | ✓ | `document_id`(Document ID, REQ), `additional_parameters`(Additional Fields, REQ) |

### `google-dorking`

version 1.0.0 — Google Dorking refers to the practice of using advanced search operators in Google's search engine to discover information that may not be r…

- GitHub: connector-google-dorking
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `custom_search` | Custom Search | investigation | ✓ | `cx`(Search Engine ID, REQ), `q`(Search Query, REQ), `exactTerms`(Include Phrase), `excludeTerms`(Exclude Phrase), `safe`(Safe Search), `num`(Count), `start`(Start), `additional_fields`(Additional Fields) |

### `google-drive`

version 1.0.0 — Google drive connector can be used to list, add, remove, download and upload files from google drive using playbook.

- GitHub: connector-google-drive
- Category: IT Service
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_files` | Get File List | investigation | ✓ | `pageSize`(Page Size) |
| `delete_file` | Delete File | containment | ✓ | `fileId`(File ID, REQ) |
| `empty_trash` | Empty Trash | containment | ✓ | — |
| `upload_file` | Upload File | containment | ✓ | `fileIRI`(Attachment IRI, REQ), `new_file_name`(New File Name) |
| `download_file` | Download File | containment | ✓ | `file_id`(File ID, REQ) |

### `google-key-management-service`

version 1.0.0 — Google Key Management Service allows you to create, import, and manage cryptographic keys and perform cryptographic operations in a single c…

- GitHub: connector-google-key-management-service
- Category: Network Security
- Operations: 15

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_locations_list` | Get Locations List | investigation | ✓ | `project_id`(Project ID, REQ), `pageSize`(Page Size), `filter`(Filter), `pageToken`(Page Token) |
| `create_keyring` | Create KeyRing | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ) |
| `get_keyring_list` | Get KeyRing List | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `pageSize`(Page Size), `pageToken`(Page Token), `filter`(Filter), `orderBy`(Order By) |
| `get_keyring_details` | Get KeyRing Details | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ) |
| `create_cryptokey` | Create CryptoKey | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `skipInitialVersionCreation`(Skip Initial Version Creation), `purpose`(Purpose), `nextRotationTime`(Next Rotation Time), `protectionLevel`(Protection Level), `algorithm`(Algorithm), `labels`(Labels), `rotationPeriod`(Rotation Period) |
| `get_cryptokey_list` | Get CryptoKey List | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `pageSize`(Page Size), `versionView`(Version), `pageToken`(Page Token), `filter`(Filter), `orderBy`(Order By) |
| `get_cryptokey_details` | Get CryptoKey Details | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ) |
| `decrypt_cryptokey_details` | Decrypt CryptoKey Details | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `ciphertext`(CipherText, REQ), `additionalAuthenticatedData`(Additional Authenticated Data), `ciphertextCrc32c`(CipherText Crc32c), `additionalAuthenticatedDataCrc32c`(Additional Authenticated Data Crc32c) |
| `encrypt_cryptokey_details` | Encrypt CryptoKey Details | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `plaintext`(PlainText, REQ), `additionalAuthenticatedData`(Additional Authenticated Data), `plaintextCrc32c`(PlainText Crc32c), `additionalAuthenticatedDataCrc32c`(Additional Authenticated Data Crc32c) |
| `create_cryptokey_version` | Create CryptoKey Version | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `state`(State), `externalKeyUri`(External Key URI) |
| `get_cryptokey_version_list` | Get CryptoKey Version List | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `pageSize`(Page Size), `versionView`(Version), `pageToken`(Page Token), `filter`(Filter), `orderBy`(Order By) |
| `get_cryptokey_version_details` | Get CryptoKey Version Details | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `cryptoKeyVersionId`(CryptoKey Version ID, REQ) |
| `destroy_cryptokey_version` | Destroy CryptoKey Version | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `cryptoKeyVersionId`(CryptoKey Version ID, REQ) |
| `restore_cryptokey_version` | Restore CryptoKey Version | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `cryptoKeyVersionId`(CryptoKey Version ID, REQ) |
| `get_public_key_for_cryptokey_version` | Get Public key for CryptoText Version | investigation | ✓ | `project_id`(Project ID, REQ), `location_id`(Location ID, REQ), `key_ring_id`(KeyRing ID, REQ), `cryptoKeyId`(CryptoKey ID, REQ), `cryptoKeyVersionId`(CryptoKey Version ID, REQ) |

### `google-maps`

version 1.0.0 — Google Maps is use for the process of converting addresses into geographic coordinates, which you can use to place markers on a map, or posi…

- GitHub: connector-google-maps
- Category: Utilities
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_maps_geocode` | Get Maps Geocode | investigation | ✓ | `address`(Address, REQ) |

### `google-resource-manager`

version 1.0.0 — Google Cloud Resource Manager is a service provided by Google Cloud Platform (GCP) that helps you manage your GCP resources across projects.…

- GitHub: connector-google-resource-manager
- Category: IT Services
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_organizations` | Search Organizations | investigation | ✓ | `query`(Query), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_organization_details` | Get organization Details | investigation | ✓ | `organization_name`(Organization Name, REQ) |
| `create_project` | Create Project | investigation | ✓ | `projectId`(Project ID, REQ), `displayName`(Display Name), `labels`(Labels), `tags`(Tags), `additional_parameters`(Additional Fields) |
| `search_projects` | Search Projects | investigation | ✓ | `query`(Query), `pageSize`(Page Size), `pageToken`(Page Token) |
| `get_project_details` | Get Project Details | investigation | ✓ | `project_name`(Project Name, REQ) |
| `update_project` | Update Project | investigation | ✓ | `project_name`(Project Name, REQ), `displayName`(Display Name), `labels`(Labels), `tags`(Tags), `additional_parameters`(Additional Fields) |
| `delete_project` | Delete Project | investigation | ✓ | `project_name`(Project Name, REQ) |
| `restore_project` | Restore Project | investigation | ✓ | `project_name`(Project Name, REQ) |

### `google-secops-siem`

version 1.0.0 — Google Security Operations (SecOps) is a cloud-native security information and event management (SIEM) platform built on Google Cloud's infr…

- GitHub: connector-google-secops-siem
- Category: ['Analytics and SIEM']
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `check_health` | Check Health | — | ✗ | — |
| `execute_api_endpoint` | Execute API Endpoint | — | ✗ | `apidomain`(API Domain, REQ), `method`(Method, REQ), `api_endpoint`(API Endpoint, REQ), `headers`(Headers), `data`(Body), `params`(Query Parameters) |
| `legacygetalert` | Get Legacy Alert | investigation | ✗ | `alertId`(Alert ID, REQ), `includeDetections`(Include Detections, REQ) |
| `legacyfetchalertsview` | Fetch Legacy Alerts View | investigation | ✗ | `baselineQuery`(Base Line Query), `timeRangeStartTime`(StartTime, REQ), `timeRangeEndTime`(EndTime, REQ), `alertListOptionsMaxReturnedAlerts`(Limit, REQ) |
| `udm_search` | UDM Search | investigation | ✓ | `udm_type`(UDM Type, REQ), `query`(Query, REQ), `time_range.start_time`(StartTime, REQ), `time_range.end_time`(EndTime, REQ), `limit`(Limit) |

### `google-secops-soar`

version 1.0.0 — Google Security Operations SOAR (Security Orchestration, Automation, and Response) is a cloud-native platform designed to help security team…

- GitHub: connector-google-secops-soar
- Category: ['Analytics and SOAR']
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `generic_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `api_endpoint`(Endpoint, REQ), `headers`(Headers), `params`(Query Parameters), `data`(Request Payload) |

### `google-sheets`

version 1.0.0 — Google Sheets is a web-based application that enables users to create, update and modify spreadsheets and share the data online in real time…

- GitHub: connector-google-sheets
- Category: Utilities
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_spreadsheet` | Create Spreadsheet | investigation | ✓ | `title`(Title), `locale`(Locale/Language), `autoRecalc`(Recalculation Interval), `timeZone`(TimeZone), `maxIterations`(Maximum Iterations), `convergenceThreshold`(Convergence Threshold), `primaryFontFamily`(Primary Font Family), `themeColors`(Theme Colors), `sheets`(Sheets), `namedRanges`(Named Ranges), `developerMetadata`(Developer Metadata), `dataSources`(Data Sources) |
| `get_spreadsheet_details` | Get Spreadsheet Details | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `ranges`(Ranges), `includeGridData`(Include Grid Data) |
| `filter_spreadsheet` | Filter Spreadsheet | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `dataFilters`(Data Filters), `includeGridData`(Include Grid Data) |
| `add_row_to_spreadsheet` | Add Row to a Spreadsheet | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `range`(Range, REQ), `valueInputOption`(Value Input Option, REQ), `insertDataOption`(Insert Data Option), `includeValuesInResponse`(Include Values in Response), `responseValueRenderOption`(Response Value Render Option), `responseDateTimeRenderOption`(Response DateTime Render Option), `majorDimension`(Major Dimension), `data`(Data) |
| `get_spreadsheet_rows` | Get Spreadsheet Rows | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `range`(Range, REQ), `majorDimension`(Major Dimension), `valueRenderOption`(Value Render Option), `dateTimeRenderOption`(DateTime Render Option) |
| `update_rows_in_spreadsheet` | Updates Rows in a Spreadsheet | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `valueInputOption`(Value Input Option, REQ), `data`(Data), `includeValuesInResponse`(Include Values in Response), `responseValueRenderOption`(Response Value Render Option), `responseDateTimeRenderOption`(Response DateTime Render Option) |
| `update_rows_of_spreadsheet_by_filter` | Update Rows of Spreadsheet by Filter | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `valueInputOption`(Value Input Option, REQ), `data`(Data Filters), `includeValuesInResponse`(Include Values in Response), `responseValueRenderOption`(Response Value Render Option), `responseDateTimeRenderOption`(Response DateTime Render Option) |
| `clear_rows_from_spreadsheet` | Clear Rows from a Spreadsheet | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `ranges`(Ranges) |
| `clear_rows_of_spreadsheet_by_filter` | Clear Rows of Spreadsheet by Filter | investigation | ✓ | `spreadsheetId`(Spreadsheet ID, REQ), `data`(Data Filters) |
| `move_sheet` | Move Sheet | investigation | ✓ | `spreadsheetId`(Source Spreadsheet ID, REQ), `sheetId`(Source Sheet ID, REQ), `destinationSpreadsheetId`(Destination Spreadsheet ID, REQ) |

### `google-threat-intelligence`

version 1.0.0 — Google Threat Intelligence is a cloud-based threat intelligence service provided by Google (via Google Cloud) that helps organizations gain …

- GitHub: connector-google-threat-intelligence
- Category: Threat Intelligence
- Operations: 34

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_entities_list` | Get Entities List | investigation | ✓ | `collection_type`(Collection Type), `creation_date`(Created/Last Modified After), `origin`(Origin Type), `limit`(Limit), `cursor`(Cursor) |
| `get_entities_details` | Get Entities Details | investigation | ✓ | `id`(Object ID, REQ) |
| `get_mitre_tactics_and_techniques` | Get Mitre Tactics and Techniques | investigation | ✓ | `id`(Object ID, REQ) |
| `get_widget_rendering_url` | Get Widget Rendering URL | investigation | ✓ | `query`(Indicator, REQ), `theme`(Theme), `fg1`(Primary Foreground Color), `fg2`(Secondary Foreground Color), `fg3`(Tertiary Foreground Color), `bg1`(Primary Background Color), `bg2`(Secondary Background Color), `bg3`(Tertiary Background Color), `acc`(Theme Accent Color) |
| `submit_sample` | Submit File | investigation | ✓ | `input`(Type, REQ), `value`(Reference ID, REQ) |
| `scan_url` | Submit URL for Scanning | investigation | ✓ | `url`(URL, REQ) |
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `ip`(IP, REQ), `relationships`(Relationships to Include) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `domain`(Domain, REQ), `relationships`(Relationships to Include) |
| `get_url_reputation` | Get URL Reputation | investigation | ✓ | `url`(URL, REQ), `relationships`(Relationships to Include) |
| `get_file_reputation` | Get File Reputation | investigation | ✓ | `file_hash`(File Hash, REQ), `relationships`(Relationships to Include) |
| `analysis_file` | Get File Or URL Analysis Report | investigation | ✓ | `type`(Type), `analysis_id`(Analysis ID, REQ) |
| `download_file` | Download File | investigation | ✓ | `id`(Hash Value, REQ) |
| `create_zip_file` | Create ZIP File | investigation | ✓ | `hashes`(Hashes, REQ), `password`(Password) |
| `get_zip_file_status` | Get ZIP File Status | investigation | ✓ | `id`(ZIP File ID, REQ) |
| `get_zip_file_url` | Get ZIP File URL | investigation | ✓ | `id`(ZIP File ID, REQ) |
| `download_zip_file` | Download ZIP File | investigation | ✓ | `id`(ZIP File ID, REQ) |
| `get_pcap_file_behaviour` | Get PCAP File Behaviour | investigation | ✓ | `sandbox_id`(Report ID, REQ) |
| `search_intelligence` | Search Intelligence | investigation | ✓ | `query`(Query, REQ), `order`(Order By), `limit`(Limit), `descriptors_only`(Descriptors Only), `cursor`(Cursor) |
| `create_livehunt_ruleset` | Create Livehunt Ruleset | investigation | ✓ | `name`(Ruleset Name, REQ), `rules`(Rules, REQ), `enabled`(Enabled), `limit`(Limit), `notification_emails`(Notification Emails) |
| `get_livehunt_rulesets_list` | Get Livehunt Rulesets List | investigation | ✓ | `filter`(Filter), `order`(Order By), `limit`(Limit), `cursor`(Cursor) |
| `get_livehunt_ruleset_details` | Get Livehunt Ruleset Details | investigation | ✓ | `id`(Ruleset ID, REQ) |
| `update_livehunt_ruleset` | Update Livehunt Ruleset | investigation | ✓ | `id`(Ruleset ID, REQ), `name`(Ruleset Name, REQ), `rules`(Rules, REQ), `enabled`(Enabled), `limit`(Limit), `notification_emails`(Notification Emails) |
| `delete_livehunt_ruleset` | Delete Livehunt Ruleset | investigation | ✓ | `id`(Ruleset ID, REQ) |
| `create_retrohunt_job` | Create Retrohunt Job | investigation | ✓ | `rules`(Rules, REQ), `notification_emails`(Notification Emails), `corpus`(Corpus), `start_time`(Start Time), `end_time`(End Time) |
| `abort_retrohunt_job` | Abort Retrohunt Job | investigation | ✓ | `id`(Job ID, REQ) |
| `get_retrohunt_jobs_list` | Get Retrohunt Jobs List | investigation | ✓ | `filter`(Filter), `limit`(Limit), `cursor`(Cursor) |
| `get_retrohunt_job_details` | Get Retrohunt Job Details | investigation | ✓ | `id`(Job ID, REQ) |
| `get_retrohunt_job_matching_files` | Get Retrohunt Job Matching Files | investigation | ✓ | `id`(Job ID, REQ), `limit`(Limit), `cursor`(Cursor) |
| `delete_retrohunt_job` | Delete Retrohunt Job | investigation | ✓ | `id`(Job ID, REQ) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |
| `get_output_schema_ip` | Get Output Schema for IP Reputation | — | ✓ | — |
| `get_output_schema_domain` | Get Output Schema for Domain Reputation | — | ✓ | — |
| `get_output_schema_url` | Get Output Schema for URL Reputation | — | ✓ | — |
| `get_output_schema_file` | Get Output Schema for File Reputation | — | ✓ | — |

### `google-vision-ai`

version 1.0.0 — Google Vision AI allows you to Integrates Google Vision features, including image labeling, face, logo, and landmark detection, optical char…

- GitHub: connector-google-vision-ai
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `submit_images` | Submit Images | investigation | ✓ | `value`(Attachment ID, REQ), `type`(Type, REQ), `maxResults`(Limit, REQ) |
| `get_locations_operations` | Get Locations Operations | investigation | ✓ | `location_id`(Location ID, REQ), `operation_id`(Operation ID, REQ) |
| `get_operations` | Get Operations | investigation | ✓ | `operation_id`(Operation ID, REQ) |

### `graylog`

version 1.0.0 — Graylog is a leading centralized log management solution for capturing, storing, and enabling real-time analysis of terabytes of machine dat…

- GitHub: connector-graylog
- Category: Analytics and SIEM
- Operations: 15

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alerts | investigation | ✓ | `limit`(Limit), `since`(Since) |
| `search_events` | Search Events | investigation | ✓ | `time_range`(Time Range, REQ), `query`(Query), `filter`(Filter), `limit`(Limit), `offset`(Offset), `sort`(Order By) |
| `search_relative` | Search Relative | investigation | ✓ | `query`(Query, REQ), `time_range`(Time Range), `filter`(Filter), `limit`(Limit), `offset`(Offset), `fields`(Fields to Retrieve), `sort`(Order By), `decorate`(Decorate) |
| `search_absolute` | Search Absolute | investigation | ✓ | `query`(Query, REQ), `start_time`(Start Time, REQ), `end_time`(End Time, REQ), `filter`(Filter), `limit`(Limit), `offset`(Offset), `fields`(Fields to Retrieve), `sort`(Order By), `decorate`(Decorate) |
| `get_clusters` | Get Clusters | investigation | ✓ | — |
| `get_cluster_node_jvm` | Get Cluster Node JVM | investigation | ✓ | `id`(Node ID, REQ) |
| `get_cluster_input_states` | Get Cluster Input States | investigation | ✓ | — |
| `get_cluster_processing_status` | Get Cluster Processing Status | investigation | ✓ | — |
| `get_cluster_metrics` | Get Cluster Metrics | investigation | ✓ | `metrics`(Metrics) |
| `get_cluster_node_metrics` | Get Cluster Node Metrics | investigation | ✓ | `id`(Node ID, REQ), `metrics`(Metrics) |
| `get_cluster_node_metrics_names` | Get Cluster Node Metrics Names | investigation | ✓ | `id`(Node ID, REQ) |
| `get_cluster_lookup_tables` | Get Clusters Lookup Tables | investigation | ✓ | `id`(ID/Name, REQ), `key`(Query) |
| `get_indexer_cluster_health` | Get Indexer Cluster Health | investigation | ✓ | — |
| `get_streams` | Get Streams | investigation | ✓ | — |
| `get_system_lookup_tables` | Get System Lookup Tables | investigation | ✓ | `sort`(Filter, REQ), `per_page`(Limit), `order`(Order By), `query`(Query), `resolve`(Resolved) |

### `greensnow-feed`

version 1.0.0 — GreenSnow is a team consisting of the best specialists in computer security, we harvest a large number of IPs from different computers locat…

- GitHub: connector-greensnow-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | — |

### `greynoise`

version 2.0.0 — GreyNoise provides information on devices observed mass-scanning the internet. This integration provides a set of actions to lookup IPs or q…

- GitHub: connector-greynoise
- Category: CTI
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `lookup_ip_context` | Lookup GreyNoise IP Context Information | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `lookup_ip_complete` | Lookup GreyNoise IP Information (Noise, RIOT, Tags) | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `lookup_ip_riot` | Lookup GreyNoise IP RIOT Information | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `lookup_ip_community` | Lookup GreyNoise IP Community Information | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `lookup_ip_quick` | Lookup GreyNoise IP Quick Information | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `gnql_query` | GreyNoise GNQL Query | investigation | ✓ | `query`(Query, REQ), `max_results`(Max Results, REQ) |
| `stats_query` | Stats Query | investigation | ✓ | `query`(Query, REQ) |
| `get_all_tag_metadata` | Get All GreyNoise Tag Metadata | investigation | ✓ | — |
| `get_tag_details` | Get GreyNoise Tag Details | investigation | ✓ | `tag_name`(Tag Name, REQ) |

### `group-ib-threat-intelligence-attribution-feed`

version 1.2.0 — Use Group-IB Threat Intelligence & Attribution Feed integration to fetch IOCs from various Group-IB collections.

- GitHub: connector-group-ib-threat-intelligence-attribution-feed
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_indicator` | Search Indicator | investigation | ✓ | `q`(Indicator, REQ), `limit`(Limit) |
| `get_indicators` | Get Indicators | investigation | ✓ | `collection`(Collection, REQ), `id`(Incident ID), `limit`(Limit) |

### `harfanglab-edr`

version 1.1.0 — The connector allows FortiSOAR users to fetch data and take actions on Hurukai HarfangLab EDR platform

- GitHub: connector-harfanglab-edr
- Category: Endpoint Security
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `search_endpoint` | Search Endpoints | investigation | ✓ | `param@hostname`(Hostname), `param@ostype`(OS Type), `param@status`(Status), `param@fields`(Select Fields), `param@offset`(Records To Skip), `param@limit`(Max Records) |
| `fetch_security_events` | Fetch Security Events | investigation | ✓ | `param@first_fetch`(Fetch Since), `param@alert_status`(Alert Status), `param@alert_type`(Alert Type), `param@min_severity`(Severity), `param@max_fetch`(Max Records), `param@delay`(Delay) |
| `get_event_by_id` | Get Event By ID | investigation | ✓ | `param@event_id`(Event ID, REQ) |
| `isolate_endpoint` | Isolate an Endpoint | response | ✓ | `param@agent_id`(Agent ID, REQ) |
| `unisolate_endpoint` | Unisolate an Endpoint | response | ✓ | `param@agent_id`(Agent ID, REQ) |
| `change_security_event_status` | Change Security Event Status | incident_management | ✓ | `param@security_event_id`(Event ID, REQ), `param@status`(Event Status, REQ) |
| `search_multiple_iocs_in_telemetry` | Search Multiple IoCs | incident_management | ✓ | `param@iocs`(IoCs, REQ), `param@search_types`(Search Types, REQ), `param@format`(Output Format, REQ), `param@limit`(Limit, REQ) |

### `hatching-triage`

version 1.0.0 — A state-of-the-art malware analysis sandbox, with all the features you need. High-volume sample submission in a customizable environment wit…

- GitHub: connector-hatching-triage
- Category: Malware Analysis
- Operations: 12

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `submit_sample` | Submit Sample | investigation | ✓ | `kind`(Type of Sample, REQ), `target`(Target), `interactive`(Interactive), `password`(Password), `profiles`(Profiles), `user_tags`(User Tags), `timeout`(Timeout), `network`(Network) |
| `query_samples` | Query Samples | investigation | ✓ | `subset`(Subset) |
| `get_sample` | Get Sample by ID | investigation | ✓ | `sample_id`(Sample ID, REQ) |
| `get_sample_summary` | Get Sample Summary | investigation | ✓ | `sample_id`(Sample ID, REQ) |
| `set_sample_profile` | Set Sample Profile | investigation | ✓ | `sample_id`(Sample ID, REQ), `auto`(Auto), `pick`(Pick), `profiles`(Profiles) |
| `get_static_report` | Get Static Report | investigation | ✓ | `sample_id`(Sample ID, REQ) |
| `get_report_triage` | Get Triage Report | investigation | ✓ | `sample_id`(Sample ID, REQ), `task_id`(Task ID, REQ) |
| `create_profile` | Create Profile | investigation | ✓ | `name`(Name, REQ), `tags`(Tags, REQ), `timeout`(Timeout, REQ), `network`(Network) |
| `get_profiles` | Get Profiles | investigation | ✓ | — |
| `update_profile` | Update Profile | investigation | ✓ | `profile_id`(Profile ID, REQ), `name`(Name, REQ), `tags`(Tags, REQ), `timeout`(Timeout, REQ), `network`(Network) |
| `delete_profile` | Delete Profile | investigation | ✓ | `profile_id`(Profile ID, REQ) |
| `search_by_query` | Search By Query | investigation | ✓ | `query`(Query, REQ) |

### `hikvision-nvr`

version 1.0.0 — Hikvision's Network Video Recorders (NVRs) provide advanced artificial intelligence capabilities for any connected data stream, even those f…

- GitHub: connector-hikvision-nvr
- Category: ['OT & IoT Security']
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_device_info` | Get NVR Device Details | investigation | ✓ | — |
| `get_ntp_details` | Get NVR Time | investigation | ✓ | — |
| `get_http_listening_servers` | Get HTTP Listening Servers | investigation | ✓ | — |
| `get_interface` | Get Management Interface | investigation | ✓ | — |
| `get_channel` | Get Channels | investigation | ✓ | — |
| `search_log` | Search Log | investigation | ✓ | `metaid`(Log Type, REQ), `start_date`(Start Date, REQ), `enddate`(End Date, REQ), `limit`(Limit) |
| `get_video_recording_details` | Get Videos Recording Details | investigation | ✓ | `trackid`(Channel ID, REQ), `start_date`(Start Date, REQ), `enddate`(End Date, REQ), `limit`(Limit) |
| `download_video` | Download Videos Recording | investigation | ✓ | `trackid`(Channel ID, REQ), `videoname`(Video Name, REQ), `create_fortisoar_attachment`(Create FortiSOAR Attachments) |

### `horizon3-ai`

version 1.0.0 — Horizon3.ai is a cybersecurity company specializing in automated security solutions. Their flagship product, NodeZero, is an autonomous pene…

- GitHub: connector-horizon3-ai
- Category: Attack surface management
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_pentests` | Get Pentests | investigation | ✗ | `text_search`(Text Search), `order_by`(Sort By), `sort_order`(Sort Direction), `date_field`(Date Filter Field), `date_from`(Date From), `date_to`(Date To), `state`(Operation Status), `client_name`(Client Name), `include_attack_paths`(Include Attack Paths), `include_weaknesses`(Include Weaknesses), `page_num`(Page Number), `page_size`(Page Size) |
| `get_attack_paths` | Get Attack Paths | investigation | ✗ | `op_id`(Operation ID, REQ), `page_num`(Page Number), `page_size`(Page Size) |
| `get_weaknesses` | Get Weaknesses | investigation | ✗ | `op_id`(Operation ID, REQ), `page_num`(Page Number), `page_size`(Page Size) |

### `host_io`

version 1.0.0 — host.io helps to get comprehensive domain name data, uncover new domains and the relationships between them, get DNS details, scraped websit…

- GitHub: connector-host_io
- Category: Threat Intelligence
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_web_domain_details` | Get Web Domain Details | investigation | ✓ | `web_domain`(Web Domain, REQ) |
| `get_dns_domain_details` | Get DNS Domain Details | investigation | ✓ | `dns_domain`(DNS Domain, REQ) |
| `get_related_domains` | Get Related Domains | investigation | ✓ | `domain_name`(Domain Name, REQ) |
| `get_full_domains_data` | Get Full Domains Data | investigation | ✓ | `domain_name`(Domain Name, REQ) |
| `get_all_domains` | Get All Domains | investigation | ✓ | `field`(Field, REQ), `value`(Value, REQ), `limit`(Limit), `page`(Page) |

### `hubspot`

version 1.0.0 — HubSpot is a CRM platform with all the software, integrations, and resources you need to connect marketing, sales, content management, and c…

- GitHub: connector-hubspot
- Category: Ticket Management
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_tickets` | Get All Tickets | investigation | ✓ | `properties`(Ticket Properties), `propertiesWithHistory`(Ticket Properties With History), `offset`(Offset) |
| `get_tickets_by_id` | Get Tickets By ID | investigation | ✓ | `ticket_ids`(Ticket ID, REQ), `properties`(Ticket Properties), `propertiesWithHistory`(Ticket Properties With History), `includeDeletes`(Include Deleted) |
| `create_tickets` | Create Tickets | investigation | ✓ | `create`(Create, REQ) |
| `update_tickets` | Update Tickets | investigation | ✓ | `update`(Update, REQ) |
| `delete_tickets` | Delete Tickets | investigation | ✓ | `ticket_ids`(Ticket ID, REQ) |
| `get_tickets_changes_log` | Get Tickets Changes Log | investigation | ✓ | `timestamp`(Timestamp), `change_type`(Change Type), `object_id`(Object ID) |
| `get_ticket_pipelines` | Get Ticket Pipelines | investigation | ✓ | — |
| `get_owners_list` | Get Owners List | investigation | ✓ | — |

### `hybrid-analysis`

version 2.1.0 — Hybrid Analysis provides a malware analysis service that allows users to automate the analysis of files and URLs for potential threats. This…

- GitHub: connector-hybrid-analysis
- Category: Malware Analysis
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `hashes_search` | Get Analysis Report for Hashcode | investigation | ✓ | `hashcodes`(Hash Code, REQ) |
| `get_environment` | Get Environment | investigation | ✓ | — |
| `submit_file` | Submit File | investigation | ✓ | `value`(Attachment/Indicator ID, REQ), `environment_id`(Environment ID, REQ), `priority`(Priority), `action_script`(Action Script), `network_settings`(Network Settings), `hybrid_analysis`(Required Memory Dump?), `experimental_anti_evasion`(Experimental Anti-Evasion?), `script_logging`(Set the IN-Depth Script Logging), `input_sample_tampering`(Allow Sample Tampering), `email`(Email Notification), `comment`(Comment), `custom_date_time`(Custom Date Time for the Analysis System), `custom_cmd_line`(Custom CMD Line Pass to the Analysis File), `custom_run_time`(Custom Run Time), `submit_name`(Submit Name), `document_password`(Document Password), `environment_variable`(Environment Variable (Format name=value)) |
| `submit_url` | Submit URL | investigation | ✓ | `url`(URL, REQ), `environment_id`(Environment ID, REQ), `priority`(Priority), `action_script`(Action Script), `hybrid_analysis`(Required Memory Dump?), `experimental_anti_evasion`(Experimental Anti-Evasion?), `script_logging`(Set the IN-Depth Script Logging), `input_sample_tampering`(Allow Sample Tampering), `network_settings`(Network Settings), `email`(Email Notification), `comment`(Comment), `custom_date_time`(Custom Date Time for the Analysis System), `custom_cmd_line`(Custom CMD Line Pass to the Analysis File), `custom_run_time`(Custom Run Time), `submit_name`(Submit Name), `document_password`(Document Password), `environment_variable`(Environment Variable (Format name=value)) |
| `url_quick_scan` | Quick Scan URL | investigation | ✓ | `url_to_scan`(URL, REQ), `comment`(Comment), `submit_name`(Submit Name) |
| `quick_scan_by_id` | Quick Scan by ID | investigation | ✓ | `id`(Scan ID, REQ) |
| `get_report` | Get Analysis Report | investigation | ✓ | `job_id`(Job ID), `file_hash`(File SHA256), `environmentId`(Environment ID) |
| `conditional_search` | Advanced Search | investigation | ✓ | `filename`(File Name), `filetype`(File Type), `filetype_desc`(File Type Description), `env_id`(Environment ID), `verdict`(Verdict), `av_detect`(AV Multiscan range), `vx_family`(AV Family Substring), `tag`(Hash Tag), `port`(Port), `host`(Host), `domain`(Domain), `url`(HTTP Request Substring), `similar_to`(Similar Samples), `context`(Sample Context), `date_from`(Start DateTime), `date_to`(End DateTime), `imp_hash`(IMP Hash), `ssdeep`(SS Deep), `authentihash`(Authenti Hash), `uses_tactic`(Uses Tactic), `uses_technique`(Uses Technique) |
| `get_sample_dropped_file` | Get Files Dropped by Sample | investigation | ✓ | `job_id`(Job ID), `file_hash`(File SHA256), `environmentId`(Environment ID) |
| `get_sample_screenshots` | Get Sample Screenshot | investigation | ✓ | `job_id`(Job ID), `file_hash`(File SHA256), `environmentId`(Environment ID), `is_attach`(Attach Screenshots to FortiSOAR) |
| `get_submitted_sample_state` | Get Submission State | investigation | ✓ | `job_id`(Job ID), `file_hash`(File SHA256), `environmentId`(Environment ID) |
| `get_feed` | Get Latest Analysis Reports | investigation | ✓ | — |
| `get_api_quota` | Get API Quota | investigation | ✓ | — |

### `ibm-iam`

version 1.0.0 — The IBM IAM Identity Service API is used to manage service IDs, API key identities, trusted profiles, account security settings and to creat…

- GitHub: connector-ibm-iam
- Category: Identity and Access Management
- Operations: 21

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_api_keys` | Get API Keys | investigation | ✗ | `account_id`(Account ID, REQ), `iam_id`(IAM ID, REQ), `pagesize`(Page Size), `pagetoken`(Page Token), `scope`(Scope), `type_value`(Type), `sort`(Sort), `order`(Order), `include_history`(Include History) |
| `create_an_api_key` | Create An API Key | investigation | ✗ | `account_id`(Account ID), `name`(Name, REQ), `iam_id`(IAM ID, REQ), `description`(Description) |
| `get_api_key_details_by_value` | Get API Key Details By Value | investigation | ✗ | `iam_apiKey`(IAM ApiKey, REQ), `include_history`(Include History) |
| `get_api_key_details` | Get API Key Details | investigation | ✗ | `api_key_unique_id`(Api Key Unique ID, REQ), `include_history`(Include History), `include_activity`(Include Activity) |
| `update_api_key` | Update API Key | investigation | ✗ | `entity_tag`(Entity Tag, REQ), `api_key_unique_id`(Api Key Unique ID, REQ), `name`(Name, REQ), `description`(Description), `support_sessions`(Support Sessions), `action_when_leaked`(Action When Leaked) |
| `delete_api_key` | Delete API Key | investigation | ✗ | `api_key_unique_id`(Api Key Unique ID, REQ) |
| `lock_api_key` | Lock API Key | investigation | ✗ | `api_key_unique_id`(Api Key Unique ID, REQ) |
| `unlock_api_key` | UnLock API Key | investigation | ✗ | `api_key_unique_id`(Api Key Unique ID, REQ) |
| `disable_the_api_key` | Disable the API key | investigation | ✗ | `api_key_unique_id`(Api Key Unique ID, REQ) |
| `enable_the_api_key` | Enable the API key | investigation | ✗ | `api_key_unique_id`(Api Key Unique ID, REQ) |
| `list_service_id_by_name` | List Service IDs By Name | investigation | ✗ | `account_id`(Account ID, REQ), `name`(Name, REQ), `pagesize`(Page Size), `pagetoken`(Page Token), `sort`(Sort), `order`(Order), `include_history`(Include History) |
| `list_service_id_by_account_id` | List Service IDs | investigation | ✗ | `account_id`(Account ID, REQ) |
| `create_a_service_id` | Create A Service ID | investigation | ✗ | `account_id`(Account ID, REQ), `name`(Name, REQ), `description`(Description), `unique_instance_crns`(Unique Instance CRNs) |
| `update_service_id` | Update Service ID | investigation | ✗ | `service_id`(Service ID, REQ), `name`(Name, REQ), `description`(Description), `unique_instance_crns`(Unique Instance CRNs), `entity_tag`(Entity Tag, REQ) |
| `delete_service_id_and_associated_api_keys` | Delete Service ID and Associated API keys | investigation | ✗ | `service_id`(Service ID, REQ) |
| `lock_service_id` | Lock The Service ID | investigation | ✗ | `service_id`(Service ID, REQ) |
| `unlock_service_id` | Unlock The Service ID | investigation | ✗ | `service_id`(Service ID, REQ) |
| `get_account_configurations` | Get Account Configurations | investigation | ✗ | `account_id`(Account ID, REQ) |
| `update_account_configurations` | Update Account Configurations | investigation | ✗ | `entity_tag`(Entity Tag, REQ), `account_id`(Account ID, REQ), `restrict_create_service_id`(Restrict Create Service ID, REQ), `restrict_create_platform_apikey`(Restrict Create Platform Api key, REQ), `allowed_ip_addresses`(Allowed IP Addresses), `mfa`(MFA, REQ), `user_mfa`(User MFA), `session_expiration_in_seconds`(Session Expiration In Seconds, REQ), `session_invalidation_in_seconds`(Session Invalidation In Seconds, REQ), `max_sessions_per_identity`(Max Sessions Per Identity, REQ), `system_access_token_expiration_in_seconds`(System Access Token Expiration In Seconds, REQ), `system_refresh_token_expiration_in_seconds.`(System Refresh Token Expiration In Seconds, REQ) |
| `trigger_activity_report_for_the_account` | Trigger Activity Report | investigation | ✗ | `account_id`(Account ID, REQ), `type`(Type), `duration`(Duration) |
| `get_activity_report_for_the_account` | Get Activity Report | investigation | ✗ | `account_id`(Account ID, REQ), `reference`(Reference, REQ) |

### `ibm-randori`

version 1.0.0 — IBM Randori is an attack surface management SaaS that monitors internal and external attack surfaces for unexpected changes, blind spots, mi…

- GitHub: connector-ibm-randori
- Category: Attack surface management
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ips` | Get IP Objects | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_ips_for_hostname` | Get IPs for Hostname | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_ips_for_network` | Get IPs for Network | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_hostnames` | Get Hostname List | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_networks` | Get Network List | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_targets` | Get Target List | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_services` | Get Service List | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_all_detections_for_target` | Get All Detections for Target | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_single_detection_for_target` | Get Single Detection for Target | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_policy` | Get Policy List | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_report` | Get Report List | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_statistics` | Get Statistics List | investigation | ✓ | `q`(Query), `limit`(Limit), `offset`(Offset) |
| `get_artifact` | Get Artifact by UUID | investigation | ✓ | `artifact_uuid`(Artifact UUID, REQ) |

### `ibm-security-guardium-insights`

version 1.0.0 — IBM Security Guardium Insights is a data security platform that provides real-time monitoring, analysis, and protection for sensitive inform…

- GitHub: connector-ibm-security-guardium-insights
- Category: Monitoring
- Operations: 15

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_report_categories_list` | Get Report Categories List | investigation | ✓ | `report_id`(Report ID) |
| `get_reports_list` | Get Reports List | investigation | ✓ | `category_id`(Category ID) |
| `get_policies_list` | Get Policies List | investigation | ✓ | — |
| `get_policy_details` | Get Policy Details | investigation | ✓ | `policy_id`(Policy ID, REQ) |
| `get_cases_list` | Get Cases List | investigation | ✓ | `case_id`(Case ID), `limit`(Limit), `offset`(Offset) |
| `get_tasks_list` | Get Tasks List | investigation | ✓ | `case_id`(Case ID, REQ), `task_id`(Task ID) |
| `get_groups_list` | Get Groups List | investigation | ✓ | — |
| `get_group_members_list` | Get Group Members List | investigation | ✓ | `group_id`(Group ID, REQ) |
| `get_compliance_data` | Get Compliance Data | investigation | ✓ | — |
| `get_connections_list` | Get Connections List | investigation | ✓ | `account_id`(Account ID), `access_key`(Account Access Key) |
| `get_datasets_list` | Get Datasets List | investigation | ✓ | `filter.start_time`(Start Time), `filter.end_time`(End Time), `limit`(Limit), `offset`(Offset) |
| `get_dataset_data` | Get Dataset Data | investigation | ✓ | `dataset_name`(Dataset Name, REQ), `limit`(Limit), `offset`(Offset) |
| `get_notifications_list` | Get Notifications List | investigation | ✓ | `filter.start_time`(Start Time), `filter.end_time`(End Time), `filter.state`(State), `limit`(Limit), `offset`(Offset) |
| `get_schedules_list` | Get Schedules List | investigation | ✓ | `Limit`(Limit), `Offset`(Offset) |
| `get_scheduled_job_details` | Get Scheduled Job Details | investigation | ✓ | `schedule_id`(Schedule ID, REQ) |

### `ibm-security-qradar-edr`

version 1.0.0 — IBM Security QRadar EDR, formerly ReaQta, remediates known and unknown endpoint threats in near real time with easy-to-use intelligent autom…

- GitHub: connector-ibm-security-qradar-edr
- Category: Endpoint Security
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alert_list` | Get Alert List | investigation | ✓ | `id`(Alert ID), `endpointId`(Endpoint ID), `triggerCondition`(Trigger Condition), `tag`(Tag), `activityState`(Activity State), `severity`(Severity), `status`(Status), `happenedAfter`(Happened After), `happenedBefore`(Happened Before), `receivedAfter`(Received After), `receivedBefore`(Received Before), `closedAfter`(Closed After), `closedBefore`(Closed Before), `lastChangedAfter`(Last Changed After), `lastChangedBefore`(Last Changed Before), `country`(Country), `gid`(Group ID), `count`(Count), `lastSeenId`(Last Seen ID), `get_all_records`(Get All Records) |
| `get_events_related_to_alerts` | Get Events Related To Alerts | investigation | ✓ | `alert_id`(Alert ID, REQ), `processId`(Process ID), `processPid`(Process PID), `eventType`(Event Type), `severity`(Severity), `happenedAfter`(Happened After), `happenedBefore`(Happened Before), `country`(Country), `mitreTechnique`(Mitre Technique), `gid`(Group ID), `get_all_records`(Get All Records) |
| `close_alert_by_id` | Close Alert By ID | investigation | ✓ | `alert_id`(Alert ID, REQ), `malicious`(Malicious) |
| `get_alert_by_id` | Get Alert By ID | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `add_notes_to_alert` | Add Notes To Alert | investigation | ✓ | `alert_id`(Alert ID, REQ), `notes`(Notes, REQ) |

### `ibm-security-qradar-soar`

version 1.1.0 — IBM Security QRadar SOAR is a software platform designed to help organizations manage and respond to security incidents effectively. It prov…

- GitHub: connector-ibm-security-qradar-soar
- Category: SOAR
- Operations: 12

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_incident` | Create Incident | investigation | ✓ | `name`(Incident Name, REQ), `discovered_date`(Discovered Date, REQ), `description`(Description), `want_full_data`(Include Full Data), `want_tasks`(Include Tasks Property), `dtm`(Incident Data Types), `cm`(Record Counts), `regulators`(Regulators), `hipaa`(Hipaa), `artifacts`(Artifacts), `findings`(Findings), `comments`(Comments), `additional_fields`(Custom Properties) |
| `search_incidents` | Search Incidents | investigation | ✓ | `filters`(Filters), `include_records_total`(Include Records), `return_level`(Return Level), `field_handle`(Field Handle), `length`(Length), `start`(Start), `recordsTotal`(Records Total), `sorts`(Sorts), `logic_type`(Logic Type) |
| `get_incident_simulations` | Get Incidents Simulations | investigation | ✓ | `want_closed`(Want Closed) |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `incident_id`(Incident ID, REQ), `vers`(Version), `want_findings`(Include Findings) |
| `get_incident_tasks` | Get Incident Tasks | investigation | ✓ | `incident_id`(Incident ID, REQ), `want_layouts`(Want Layouts), `want_notes`(Want Notes) |
| `update_incident` | Update Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `changes`(Changes), `version`(Version) |
| `close_incident` | Close Incident | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `get_incident_artifacts` | Get Incident Artifacts | investigation | ✓ | `incident_id`(Incident ID, REQ), `filters`(Filters), `include_records_total`(Include Records), `return_level`(Return Level), `field_handle`(Field Handle), `start`(Start), `length`(Length), `recordsTotal`(Records Total), `sorts`(Sorts), `logic_type`(Logic Type) |
| `get_incident_notes` | Get Incident Notes | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `get_incident_attachments` | Get Incident Attachments | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `get_incident_attachment_details` | Get Incident Attachment Details | investigation | ✓ | `incidentID`(Incident ID, REQ) |
| `get_all_incident_details` | Get All Incident Details | investigation | ✓ | `incidentID`(Incident ID, REQ), `filters`(Filters), `start`(Start), `length`(Length) |

### `ibm-xforce-threat-intel-feed`

version 2.1.0 — IBM X-Force Threat Intelligence Feed is a preconfigured set of intelligence feeds that STAXX users can access immediately upon download, and…

- GitHub: connector-ibm-xforce-threat-intel-feed
- Category: Threat Intelligence
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_api_root_information` | Get API Root Information | investigation | ✓ | — |
| `get_collections` | Get Collections | investigation | ✓ | `collectionID`(Collection ID) |
| `get_objects_by_collection_id` | Get Objects By Collection ID | investigation | ✓ | `collectionID`(Collection ID, REQ), `added_after`(Created After), `added_before`(Created Before), `output_mode`(Process Response As) |
| `download_indicators` | Download Indicators | investigation | ✓ | `added_after`(Last Pull Time) |
| `get_output_schema` | Get Output Schema | — | ✓ | — |
| `get_objects_by_object_id` | Get Object By Object ID | investigation | ✓ | `collectionID`(Collection ID, REQ), `objectID`(Object ID, REQ) |
| `get_manifest_by_collection_id` | Get Manifest By Collection ID | investigation | ✓ | `collectionID`(Collection ID, REQ), `added_after`(Created After), `added_before`(Created Before) |

### `illumio-core`

version 1.0.0 — Illumio that provides a platform designed to help organizations protect their critical applications and data by creating secure zones and co…

- GitHub: connector-illumio-core
- Category: ['Network Security', 'Cloud Security', 'Endpoint Security']
- Operations: 20

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_workload` | Create Workload | investigation | ✓ | `org_id`(Organization ID, REQ), `name`(Workload Name, REQ), `description`(Description), `hostname`(Hostname), `service_principal_name`(Service Principal Name), `public_ip`(Public IP), `additional_properties`(Additional Properties) |
| `get_workloads` | Get Workloads | investigation | ✓ | `org_id`(Organization ID, REQ), `enforcement_mode`(Enforcement Mode), `include_deleted`(Included Deleted), `security_policy_sync_state`(Security Policy Sync State), `security_policy_update_mode`(Security Policy Update Mode), `visibility_level`(Visibility Level), `policy_health`(Policy Health), `max_results`(Limit), `additional_properties`(Additional Properties) |
| `get_workload_by_id` | Get Workload by ID | investigation | ✓ | `org_id`(Organization ID, REQ), `workload_id`(Workload ID, REQ) |
| `update_workload` | Update Workload | investigation | ✓ | `org_id`(Organization ID, REQ), `workload_id`(Workload ID, REQ), `name`(Workload Name), `description`(Description), `service_provider`(Service Provider), `enforcement_mode`(Enforcement Mode), `additional_properties`(Additional Properties) |
| `delete_workload` | Delete Workload | investigation | ✓ | `org_id`(Organization ID, REQ), `workload_id`(Workload ID, REQ) |
| `get_ransomware_details` | Get Ransomware Details | investigation | ✓ | `org_id`(Organization ID, REQ), `workload_id`(Workload ID, REQ) |
| `create_ip_list` | Create IP List | investigation | ✓ | `org_id`(Organization ID, REQ), `pversion`(Security Policy Version, REQ), `name`(IP List Name, REQ), `ip_ranges`(IP Ranges), `fqdns`(Fully Qualified Domain Name (FQDN), REQ), `description`(Description), `additional_properties`(Additional Properties) |
| `get_ip_list` | Get IP List | investigation | ✓ | `org_id`(Organization ID, REQ), `pversion`(Security Policy Version, REQ), `description`(Description), `external_data_reference`(External Data Reference), `max_results`(Limit), `additional_properties`(Additional Properties) |
| `get_ip_list_by_id` | Get IP List by ID | investigation | ✓ | `org_id`(Organization ID, REQ), `pversion`(Security Policy Version, REQ), `ip_list_id`(IP List ID, REQ) |
| `update_ip_list` | Update IP List | investigation | ✓ | `org_id`(Organization ID, REQ), `pversion`(Security Policy Version, REQ), `ip_list_id`(IP List ID, REQ), `ip_ranges`(IP Ranges), `fqdns`(Fully Qualified Domain Name (FQDN), REQ), `description`(Description), `additional_properties`(Additional Properties) |
| `delete_ip_list` | Delete IP List | investigation | ✓ | `org_id`(Organization ID, REQ), `pversion`(Security Policy Version, REQ), `ip_list_id`(IP List ID, REQ) |
| `create_label` | Create Label | investigation | ✓ | `org_id`(Organization ID, REQ), `key`(Label Key, REQ), `value`(Label Value, REQ), `external_data_set`(External Data Set), ` external_data_reference`(External Data Reference) |
| `get_labels` | Get Labels | investigation | ✓ | `org_id`(Organization ID, REQ), `include_deleted`(Include Deleted), `external_data_reference`(External Data Reference), `max_results`(Limit), `additional_properties`(Additional Properties) |
| `get_label_by_id` | Get Label by ID | investigation | ✓ | `org_id`(Organization ID, REQ), `label_id`(Label ID, REQ), `usage`(Include Label Usage Flag) |
| `update_label` | Update Label | investigation | ✓ | `org_id`(Organization ID, REQ), `label_id`(Label ID, REQ), `value`(Label Value), `external_data_set`(External Data Set), `external_data_reference`(External Data Reference) |
| `delete_label` | Delete Label | investigation | ✓ | `org_id`(Organization ID, REQ), `label_id`(Label ID, REQ) |
| `get_pending_security_policy` | Get Pending Security Policy | investigation | ✓ | `org_id`(Organization ID, REQ), `max_results`(Limit) |
| `revert_pending_uncommitted_security_policy_list` | Revert Pending Uncommitted Security Policy List | investigation | ✓ | `org_id`(Organization ID, REQ) |
| `restore_previous_security_policy` | Restore Previous Security Policy | investigation | ✓ | `org_id`(Organization ID, REQ), `pversion`(Security Policy Version, REQ) |
| `send_custom_request` | Execute an API Call | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `imap`

version 3.5.9 — Steps related to fetching and parsing email

- GitHub: connector-imap
- Category: utilities
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_email` | Fetch Email(s) Deprecated | — | ✓ | — |
| `fetch_email_new` | Fetch Email(s) | — | ✓ | `limit_count`(Maximum number of emails to fetch), `parse_inline_image`(Parse inline images), `save_raw_email`(Save Raw Email as Attachment) |

### `infraon-itsm`

version 1.0.0 — Infraon ITSM is a cloud-ready, AI-powered IT Service Management (ITSM) platform that helps organizations manage, automate, and optimize thei…

- GitHub: connector-infraon-itsm
- Category: Ticket Management
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_incident` | Create Incident | remediation | ✓ | `summary`(Summary, REQ), `requester_email`(Requester Email, REQ), `description`(Description, REQ), `team_name`(Team), `assignee_email`(Assignee Email), `urgency`(Urgency), `priority`(Priority), `impact`(Impact), `status`(Status), `severity`(Severity), `other_fields`(Other Fields) |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `ticket_id`(Ticket ID, REQ) |
| `get_all_incident_details` | Get All Incident Details | investigation | ✓ | `items_per_page`(Items Per Page), `page`(Page Number), `filters`(Filters) |
| `update_incident` | Update Incident | remediation | ✓ | `display_id`(Ticket ID, REQ), `summary`(Summary), `description`(Description), `status`(Status), `urgency`(Urgency), `severity`(Severity), `priority`(Priority), `priority_change_reason`(Priority Change Reason), `team_name`(Team Name), `team_id`(Team ID), `assignee_name`(Assignee Name), `assignee_profile`(Assignee Profile), `assignee_profile_id`(Assignee Profile ID), `assignee_email`(Assignee Email), `other_fields`(Other Fields) |
| `delete_incident` | Delete Incident | remediation | ✓ | `display_id`(Ticket ID, REQ) |
| `add_comment` | Add Comment | remediation | ✓ | `display_id`(Ticket ID, REQ), `comment`(Comment Text, REQ) |
| `submit_file` | Add Attachment | remediation | ✓ | `display_id`(Ticket ID, REQ), `issue_key`(Issue Key), `path`(Type, REQ), `value`(Reference ID, REQ) |

### `insider-security-ueba`

version 1.0.0 — InsiderSecurity UEBA (User and Entity Behaviour Analytics) detects malicious user activity early in your on-premise or cloud infrastructure,…

- GitHub: connector-insider-security-ueba
- Category: Insider Threat
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts_by_id` | Get Alerts by ID | investigation | ✓ | `id`(Alert ID, REQ) |
| `search_data_enrichment` | Search Data Enrichment | investigation | ✓ | `index`(Index, REQ), `entity_ip`(Entity IP), `entity_name`(Entity Name), `query`(Query), `time_start`(Time Start), `time_end`(Time End), `limit`(Limit) |
| `search_alerts` | Search Alerts | investigation | ✓ | `risk_entity`(Risk Entity, REQ), `threat_name`(Threat Name, REQ), `time_end`(Time End, REQ) |

### `ip-api`

version 1.0.0 — IP-API helps to get the following information for any IP address: city, region (name & code), country (name & code), continent, postal code …

- GitHub: connector-ip-api
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `execute_batch_api` | Get IP Geolocation | investigation | ✓ | `list_of_ip_addr`(IP Addresses, REQ) |
| `execute_dns_api` | Get DNS Geolocation | investigation | ✓ | — |

### `ip-quality-score`

version 1.0.1 — The IPQualityScore (IPQS) Threat Intelligence application provides threat intelligence for IP addresses, email addresses, URLs, and domains.…

- GitHub: connector-ip-quality-score
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `ip_address`(IP Address, REQ), `strictness`(Strictness), `user_agent`(User Agent), `user_language`(User Language), `fast`(Fast), `mobile`(Mobile), `allow_public_access_points`(Allow Public Access Points), `lighter_penalties`(Lighter Penalties), `transaction_strictness`(Transaction Strictness) |
| `get_email_reputation` | Get Email Reputation | investigation | ✓ | `email_address`(Email Address, REQ), `fast`(Fast), `timeout`(Timeout), `suggest_domain`(Suggest Domain), `strictness`(Strictness), `abuse_strictness`(Abuse Strictness) |
| `get_url_reputation` | Get URL Reputation | investigation | ✓ | `url`(URL, REQ), `strictness`(Strictness), `fast`(Fast) |

### `ipsum-threat-intelligence-feed`

version 1.0.0 — IPsum is a threat intelligence feed based on 30+ different publicly available lists of suspicious and/or malicious IP addresses. This connec…

- GitHub: connector-ipsum-threat-intelligence-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `output_mode`(Process Response As) |

### `itglue`

version 1.0.0 — ITGlue is IT documentation software designed to help you maximize the efficiency, transparency and consistency of your team. This connector …

- GitHub: connector-itglue
- Category: IT Services
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_organizations` | Get Organizations | investigation | ✓ | `org_id`(Organization ID), `org_name`(Organization Name), `org_type_id`(Organization Type ID), `org_status_id`(Organization Status ID), `created_at`(Created At), `updated_at`(Updated At), `page_size`(Page Size), `page_number`(Page Number), `additional_fields`(Additional Fields) |
| `get_locations` | Get Locations | investigation | ✓ | `org_id`(Organization ID, REQ), `loc_id`(Location ID), `loc_name`(Location Name), `country_id`(Country), `region_id`(Region ID), `page_size`(Page Size), `page_number`(Page Number), `additional_fields`(Additional Fields) |
| `get_configurations` | Get Configurations | investigation | ✓ | `org_id`(Organization ID, REQ), `config_id`(Configuration ID), `config_name`(Configuration Name), `config_type_id`(Configuration Type ID), `config_status_id`(Configuration Status ID), `page_size`(Page Size), `page_number`(Page Number), `additional_fields`(Additional Fields) |
| `get_domains` | Get Domains | investigation | ✓ | `org_id`(Organization ID, REQ), `domain_id`(Domain ID), `page_size`(Page Size), `page_number`(Page Number), `additional_fields`(Additional Fields) |
| `get_flexible_asset` | Get Flexible Asset | investigation | ✓ | `flex_type_id`(Flexible Asset Type ID, REQ), `flexible_asset_name`(Flexible Asset Name), `org_id`(Organization ID), `page_size`(Page Size), `page_number`(Page Number), `additional_fields`(Additional Fields) |

### `jenkins`

version 1.0.0 — Jenkins is an open-source automation server widely used to implement Continuous Integration (CI) and Continuous Delivery (CD) pipelines. It …

- GitHub: connector-jenkins
- Category: DevOps and Digital Operations
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_list_jobs` | Get List Jobs | investigation | ✓ | `job_path`(Job Path) |
| `trigger_job` | Trigger Job | investigation | ✓ | `job_path`(Job Path, REQ), `build_parameters`(Build Parameters) |
| `get_job_status` | Get Job Status | investigation | ✓ | `job_path`(Job Path, REQ), `build_number`(Build Number, REQ) |
| `resume_jenkins_job_with_input` | Resume Jenkins Job with Input | investigation | ✓ | `job_path`(Job Path, REQ), `build_number`(Build Number, REQ), `input_id`(Input ID, REQ), `input_parameters`(Input Parameters, REQ), `job_status`(Job Status, REQ) |
| `generic_rest_api_call` | Execute an API Request | investigation | ✓ | `endpoint`(Endpoint URL, REQ), `method`(Method, REQ), `query_params`(Query Parameters), `payload`(Payload) |

### `jira`

version 2.0.0 — The Jira allows users to seamlessly interact with Jira Cloud by creating, updating, and deleting issues. It simplifies task management and i…

- GitHub: connector-jira
- Category: Ticket Creation
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_ticket` | Create Ticket | investigation | ✓ | `project_key`(Project Key, REQ), `ticket_summary`(Ticket Summary, REQ), `ticket_description`(Ticket Description, REQ), `issue_type`(Ticket Type, REQ), `parent`(Parent Key ID), `priority`(Priority), `other_fields`(Other Fields) |
| `get_ticket_details` | Get Ticket Details | investigation | ✓ | `issue_key`(Ticket ID, REQ) |
| `list_projects` | List Projects | investigation | ✓ | — |
| `list_tickets` | List Tickets | investigation | ✓ | `jql_query`(JQL Query, REQ), `start_time`(From Date), `maxResults`(Max Results), `nextPageToken`(Next Page Token), `fields`(Fields) |
| `validate_jql_query` | Validate JQL query | utilities | ✓ | `jql_query`(JQL Query, REQ) |
| `search_users` | Search Users | investigation | ✓ | `startAt`(Start At), `maxResults`(Max Results) |
| `get_user_details` | Get User Details | investigation | ✓ | `accountId`(Account ID, REQ) |
| `assign_issue` | Assign Issue to User | investigation | ✓ | `accountId`(Account ID, REQ), `issue_key`(Ticket ID, REQ) |
| `submit_file` | Add Attachment | investigation | ✓ | `issue_key`(Ticket ID, REQ), `path`(File or Attachment IRI, REQ) |
| `add_remote_link` | Add Remote Link | investigation | ✓ | `issue_key`(Ticket ID, REQ), `url`(URL, REQ), `title`(Title, REQ) |
| `add_comment` | Add Comment | investigation | ✓ | `issue_key`(Ticket ID, REQ), `comment`(Comment, REQ) |
| `get_comments` | Get Comments | investigation | ✓ | `issue_key`(Ticket ID, REQ), `startAt`(Start At), `maxResults`(Max Results), `orderBy`(OrderBy) |
| `set_status` | Set Ticket Status | investigation | ✓ | `issue_key`(Ticket ID, REQ), `status`(Status, REQ) |
| `update_ticket` | Update Ticket | investigation | ✓ | `issue_key`(Ticket ID, REQ), `project_key`(Project Key, REQ), `summary`(Summary, REQ), `comment`(Comment, REQ), `priority`(Priority, REQ), `description`(Description), `status`(Status), `other_fields`(Other Fields) |
| `update_fortisoar` | Update FortiSOAR Record | investigation | ✓ | `jira_key`(Ticket ID, REQ), `cyops_username`(FortiSOAR Username, REQ), `cyops_password`(FortiSOAR Password, REQ) |
| `delete_ticket` | Delete Ticket | investigation | ✓ | `issue_key`(Ticket ID, REQ), `delete_subtask`(Delete Subtasks, REQ) |

### `jira-insight-db`

version 1.1.0 — Jira Insight gives teams a simple and quick way to tie assets and configuration items to service requests, incidents, problems, changes, and…

- GitHub: connector-jira-insight-db
- Category: Ticket Management
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_object` | Create Object | investigation | ✓ | `objectTypeId`(Object Type ID), `objectTypeAttributeId`(Object Type Attribute ID), `object_attribute_value`(Object Attribute Values), `other_fields`(Other Fields) |
| `update_object` | Update Object | investigation | ✓ | `object_id`(Object ID), `objectTypeId`(Object Type ID), `objectTypeAttributeId`(Object Type Attribute ID), `object_attribute_value`(Object Attribute Values), `other_fields`(Other Fields) |
| `get_assets` | Get Assets List | investigation | ✓ | `iql`(Insight Query Language(IQL)), `page`(Page Number), `resultPerPage`(Result Per Page), `includeAttributes`(Include Attributes), `includeAttributesDeep`(Include Attributes Deep), `includeTypeAttributes`(Include Type Attributes), `includeExtendedInfo`(Include Extended Info) |
| `get_asset_details` | Get Asset Details | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `get_asset_attributes` | Get Asset Attributes | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `get_asset_history` | Get Asset History | investigation | ✓ | `asset_id`(Asset ID, REQ), `asc`(Sort in Ascending Order), `abbreviate`(Abbreviate) |
| `get_asset_reference_info` | Get Asset Reference Information | investigation | ✓ | `asset_id`(Asset ID, REQ) |
| `get_asset_connected_tickets` | Get Asset Connected Tickets | investigation | ✓ | `asset_id`(Asset ID, REQ) |

### `jscode-snippet`

version 1.0.0 — JS code snippet integration for FortiSOAR allows you to seamlessly incorporate JavaScript code snippets into your playbooks. With this integ…

- GitHub: connector-jscode-snippet
- Category: Utilities
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `run_js_code` | Execute JavaScript Code | — | ✓ | `js_code`(JavaScript Code, REQ) |

### `json-convert`

version 1.0.0 — Convert the output of many commands and file-types to structured objects using the open-source JSON Convert (JC) library. The JC project det…

- GitHub: connector-json-convert
- Category: Utilities
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `convert` | Convert | miscellenous | ✓ | `parser`(JC Parser, REQ), `command_output`(Command or File Output to Parse, REQ), `raw`(Raw Output) |
| `get_parser_list` | Get Parser List | — | ✓ | — |

### `juniper-junos`

version 1.0.0 — Provides JunOS REST API Integration covering Juniper MX, PTX, QFX, T and SRX Series platforms

- GitHub: connector-juniper-junos
- Category: Firewall and Network Protection
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `op_action` | Run Command | information | ✓ | `command_to_run`(Command to Run, REQ), `method_params`(Method Parameters) |
| `config_action` | Run Configuration Command | Configuration | ✓ | `request_payload`(Request Payload, REQ) |
| `get_address_set` | Get Address Set | Configuration | ✓ | `address_set`(Address Set, REQ), `get_count`(Get Entries Count) |
| `add_to_address_set` | Add an Object to Global Address Set | Configuration | ✓ | `address_set`(Address Set, REQ), `object_type`(Object Types, REQ), `object_to_add`(Object(s) To Add, REQ) |
| `delete_from_address_set` | Delete Object from Global Address Set | Configuration | ✓ | `address_set`(Address set, REQ), `object_type`(Object Types, REQ), `object_to_delete`(Object(s) To Delete, REQ) |
| `get_prefix_list` | Get Prefix List | Configuration | ✓ | `prefix_list`(Prefix List, REQ), `get_count`(Get Entries Count) |
| `add_to_prefix_list` | Add Address(es) to a Prefix List | Configuration | ✓ | `prefix_list`(Prefix List, REQ), `address_to_add`(Address(es) To Add, REQ) |
| `delete_from_prefix_list` | Delete Address(es) from a Prefix List | Configuration | ✓ | `prefix_list`(Prefix List, REQ), `address_to_delete`(Address(es) To Delete, REQ) |

### `kafka`

version 1.0.0 — Kafka is an open-source distributed event streaming platform. This Kafka Connector is use to publish/consume a messages to/from a topic.

- GitHub: connector-kafka
- Category: Communication and Coordination
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `topic_list` | Kafka Topic List | investigation | ✓ | — |
| `topic_details` | Kafka Topic Details | investigation | ✓ | `topics`(Topic Names, REQ), `timeout_ms`(Poll Timeout in ms), `max_records`(Max Records, REQ), `seek_partition`(Seek Partition) |
| `send_str_message_to_topic` | Send String Message to Topic | investigation | ✓ | `topic`(Topic, REQ), `message`(Message, REQ) |
| `send_b64encoded_message_to_topic` | Send b64encoded Message to Topic | investigation | ✓ | `topic`(Topic), `base64msg`(Base64 Message) |

### `kaspersky-security-center`

version 1.0.2 — Kaspersky Security Center makes it easy to manage and secure both physical and virtual endpoints from a single, unified management console.

- GitHub: connector-kaspersky-security-center
- Category: Endpoint Security
- Operations: 12

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_listhost_group` | Get Host List | investigation | ✓ | `group_id`(Group ID, REQ) |
| `get_host_details` | Get Host Details | investigation | ✓ | `host_id`(Host ID, REQ) |
| `get_hosts_group_static_info` | Get Host Group Static Info | investigation | ✓ | — |
| `get_software_installed` | Get Software Installed on Specific Host | investigation | ✓ | `host_id`(Workstation Hostname (KLHST_WKS_HOSTNAME), REQ) |
| `get_product_installed` | Get Products Installed | investigation | ✓ | `host_id`(Host ID, REQ) |
| `add_group` | Add Group | investigation | ✓ | `parent_id`(Group Parent ID, REQ), `name`(Group Name, REQ) |
| `get_groups` | Get All Groups Details | investigation | ✓ | — |
| `move_hosts` | Move Host to Specific Group | investigation | ✓ | `newgroup`(New Group ID, REQ), `pHostNames`(Host Name, REQ) |
| `delete_group` | Delete Specific Group | investigation | ✓ | `group_id`(Group ID, REQ), `flag`(Flag, REQ) |
| `add_policy_request` | Add Policy | investigation | ✓ | `KLPOL_DN`(Policy Display Name, REQ), `KLPOL_PRODUCT`(Policy Product Name, REQ), `KLPOL_VERSION`(Policy Product Version, REQ), `KLPOL_GROUP_ID`(Policy GROUP ID, REQ) |
| `list_policies_request` | Get All Policies on Specific Group | investigation | ✓ | `group_id`(Group ID, REQ) |
| `get_policy_request` | Get Specific Policy | investigation | ✓ | `policy_id`(Policy ID, REQ) |

### `keeper-secrets-manager`

version 1.0.0 — Keeper Secrets Manager is a tool designed to securely manage sensitive information, such as passwords, API keys, and other credentials, with…

- GitHub: connector-keeper-secrets-manager
- Category: Vault
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_credentials` | Get Credentials | investigation | ✓ | — |
| `get_credentials_details` | Get Credentials Details | investigation | ✓ | `secret_id`(Secret ID, REQ) |
| `get_credential` | Get Credential | investigation | ✓ | `secret_id`(Secret ID, REQ), `attribute_name`(Attribute Name, REQ) |

### `kiuwan`

version 1.2.0 — Kiuwan is a software as a service (SaaS) static application security testing multi-technology software for software analysis, code quality, …

- GitHub: connector-kiuwan
- Category: DevOps and Digital Operations
- Operations: 25

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_application_list` | Get Application List | investigation | ✓ | `app_name`(Application Name), `activityInfo`(Activity Info), `initDateAnalysis`(StartDate Analysis), `endDateAnalysis`(EndDate Analysis), `exactApplicationName`(Exact Application Name), `count`(Limit), `page`(Page), `orderBy`(Order By), `sort_by`(Sort By) |
| `get_application_details` | Get Application Details | investigation | ✓ | `app_name`(Application Name, REQ) |
| `get_application_defects_list` | Get Application Defects List | investigation | ✓ | `app_name`(Application Name, REQ), `characteristics`(Characteristics), `fileContains`(File Contains), `languages`(Languages), `priorities`(Priorities), `count`(Limit), `page`(Page), `orderBy`(Order By), `sort_by`(Sort By) |
| `get_progress_summary_for_action_plan` | Get Progress Summary for Action Plan | investigation | ✓ | `app_name`(Application Name, REQ), `action_name`(Action Plan Name, REQ), `creation_date`(Creation Date) |
| `get_defects_list_for_action_plan` | Get Defects List for Action Plan | investigation | ✓ | `app_name`(Application Name, REQ), `action_name`(Action Plan Name, REQ), `creation_date`(Creation Date) |
| `get_pending_defects_for_action_plan` | Get Pending Defects for Action Plan | investigation | ✓ | `app_name`(Application Name, REQ), `action_name`(Action Plan Name, REQ), `creation_date`(Creation Date), `analysisLabel`(Analysis Label), `characteristics`(Characteristics), `fileContains`(File Contains), `languages`(Languages), `priorities`(Priorities), `limit`(Limit), `orderBy`(Order By), `sort_by`(Sort By) |
| `get_removed_defects_for_action_plan` | Get Removed Defects for Action Plan | investigation | ✓ | `app_name`(Application Name, REQ), `action_name`(Action Plan Name, REQ), `creation_date`(Creation Date), `analysisLabel`(Analysis Label) |
| `get_available_action_plans` | Get Available Action Plans | investigation | ✓ | `app_name`(Application Name, REQ) |
| `get_analysis_list` | Get Analysis List | investigation | ✓ | `app_name`(Application Name), `audit_status`(Audit Status), `deliveries`(Deliveries), `start_date`(Start Time), `end_date`(End Time), `status`(Status), `count`(Limit), `page`(Page) |
| `get_analysis_codes_list` | Get Analysis Codes List | investigation | ✓ | `app_name`(Application Name, REQ), `filterPurgedAnalyses`(Purged Analyses), `success`(Success), `count`(Limit) |
| `get_latest_analysis_files_list` | Get Latest Analysis Files List | investigation | ✓ | `app_name`(Application Name, REQ) |
| `get_last_analysis` | Get Latest Analysis | investigation | ✓ | `app_name`(Application Name, REQ) |
| `get_application_analysis` | Get Application Analysis | investigation | ✓ | `code`(Analysis Code, REQ) |
| `get_analysis_defects_list` | Get Analysis Defects List | investigation | ✓ | `code`(Analysis Code, REQ), `characteristics`(Characteristics), `fileContains`(File Contains), `languages`(Languages), `muted`(Mutes), `priorities`(Priorities), `count`(Limit), `page`(Page), `orderBy`(Order By), `sort_by`(Sort By) |
| `get_comparison_defects` | Get Comparison Defects | investigation | ✓ | `code`(Analysis Code, REQ), `prev_code`(Previous Analysis Code, REQ) |
| `get_new_removed_defects_list` | Get New/Removed Defects List | investigation | ✓ | `code`(Analysis Code, REQ), `prev_code`(Previous Analysis Code, REQ), `defectstype`(Defect Type, REQ) |
| `get_files_defects_details` | Get Files Defects Details | investigation | ✓ | `code`(Analysis Code, REQ) |
| `delete_analysis` | Delete Analysis | investigation | ✓ | `analysis_code`(Analysis Code, REQ) |
| `create_mutes_for_rule_or_file` | Create Mutes for Rule or File | investigation | ✓ | `app_name`(Application Name, REQ), `comment`(Comment), `file_name`(File Name), `file_pattern`(File Pattern), `rule`(Rule), `reason`(Mute Reason) |
| `create_suppression_rule` | Create Suppression Rule | investigation | ✓ | `defect_id`(Defect ID, REQ), `comment`(Comment), `muteBy`(Mute By), `reason`(Mute Reason) |
| `get_defect_notes` | Get Defect Notes | investigation | ✓ | `defect_id`(Defect ID, REQ) |
| `get_violated_rules` | Get Violated Rules | investigation | ✓ | `app_name`(Application Name, REQ), `analysisCode`(Analysis Code), `onlyCodeSecurity`(Code Security), `characteristics`(Characteristics), `languages`(Languages), `priority`(Priority), `tag`(Tag), `vuln_type`(Vulnerability Type) |
| `get_violated_rule_files` | Get Violated Rule Files | investigation | ✓ | `app_name`(Application Name, REQ), `analysisCode`(Analysis Code, REQ), `ruleCode`(Rule Code, REQ) |
| `get_file_defects` | Get File Defects | investigation | ✓ | `app_name`(Application Name, REQ), `analysisCode`(Analysis Code, REQ), `file_name`(File Name, REQ), `ruleCode`(Rule Code, REQ) |
| `update_defect_status` | Update Defect Status | investigation | ✓ | `defect_id`(Defect ID, REQ), `status`(Status, REQ), `note`(Note) |

### `know-b4-phisher`

version 1.0.1 — KnowBe4 PhishER helps your InfoSec and Security Operations team cut through the inbox noise and respond to the most dangerous threats more q…

- GitHub: connector-know-b4-phisher
- Category: Email Security
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_message_list` | Get Messages | investigation | ✓ | `query`(Query), `all`(Fetch All Records), `page`(Page Number), `per`(Page Size) |
| `get_message_by_id` | Get Message by ID | investigation | ✓ | `id`(Message ID, REQ) |
| `update_message` | Update Message | investigation | ✓ | `id`(Message ID, REQ), `category`(Category), `status`(Status), `severity`(Severity) |
| `add_comment` | Add Comment | investigation | ✓ | `id`(Message ID, REQ), `comment`(Comment, REQ) |
| `add_tags` | Add Tags | investigation | ✓ | `id`(Message ID, REQ), `tags`(Tags, REQ) |
| `remove_tags` | Remove Tags | investigation | ✓ | `id`(Message ID, REQ), `tags`(Tags, REQ) |

### `kubernetes`

version 1.0.0 — Kubernetes, also known as K8s, is an open-source system for automating deployment, scaling, and management of containerized applications.

- GitHub: connector-kubernetes
- Category: Container Services
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `apply_yml_file` | Apply YAML File | investigation | ✓ | `file_name`(Attachment IRI, REQ) |
| `list_namespace_pod` | Get Namespace Pods List | investigation | ✓ | `namespace`(Namespace, REQ) |
| `list_pod_for_all_namespaces` | Get Pod For All Namespaces | investigation | ✓ | — |
| `get_pod_logs` | Get Pod logs | investigation | ✓ | `pod_name`(Pod Name, REQ), `namespace`(Namespace, REQ) |
| `delete_namespace_pod` | Delete Namespace Pod | investigation | ✓ | `pod_name`(Pod Name, REQ), `namespace`(Namespace, REQ) |
| `delete_collection_namespace_pod` | Delete Collection Namespace Pods | investigation | ✓ | `namespace`(Namespace, REQ) |
| `delete_collection_namespace_secret` | Delete Collection Namespace Secret | investigation | ✓ | `namespace`(Namespace, REQ) |
| `delete_namespace_secret` | Delete Namespace Secret | investigation | ✓ | `secret_name`(Secret Name, REQ), `namespace`(Namespace, REQ) |
| `list_secret_for_all_namespaces` | List Secret For All Namespaces | investigation | ✓ | — |
| `delete_collection_namespace_config_map` | Delete Collection Namespace ConfigMap | investigation | ✓ | `namespace`(Namespace, REQ) |
| `delete_namespace_config_map` | Delete Namespace ConfigMaps | investigation | ✓ | `configmap_name`(ConfigMap Name, REQ), `namespace`(Namespace, REQ) |
| `list_config_map_for_all_namespaces` | Get ConfigMap For All Namespaces | investigation | ✓ | — |
| `list_event_for_all_namespaces` | Get Events For All Namespaces | investigation | ✓ | — |

### `logicmonitor`

version 1.0.0 — LogicMonitor is a SaaS-based performance monitoring platform that provides full visibility into complex, hybrid infrastructures, offering gr…

- GitHub: connector-logicmonitor
- Category: Monitoring
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alert_list` | Get Alert List | investigation | ✓ | `filter`(Filter Criteria), `fields`(Fields to Retrieve), `size`(Limit), `offset`(Offset) |
| `get_device_group_list` | Get Device Group List | investigation | ✓ | `filter`(Filter Criteria), `fields`(Fields to Retrieve), `size`(Limit), `offset`(Offset) |
| `get_device_list` | Get Device List | investigation | ✓ | `start`(Start Time), `end`(End Time), `netflowFilter`(Netflow Filter), `filter`(Filter Criteria), `includeDeletedResources`(Include Deleted Resources), `fields`(Fields to Retrieve), `size`(Limit), `offset`(Offset) |
| `get_device_alerts` | Get Device Alerts | investigation | ✓ | `id`(Device ID, REQ), `start`(Start Time), `end`(End Time), `netflowFilter`(Netflow Filter), `needMessage`(Need Message), `customColumns`(Custom Columns), `bound`(Bound), `filter`(Filter Criteria), `fields`(Fields to Retrieve), `size`(Limit), `offset`(Offset) |
| `get_report_list` | Get Report List | investigation | ✓ | `filter`(Filter Criteria), `fields`(Fields to Retrieve), `size`(Limit), `offset`(Offset) |
| `get_report_by_id` | Get Report by ID | investigation | ✓ | `id`(Report ID, REQ), `fields`(Fields to Retrieve) |

### `logz-io`

version 1.0.0 — Logz.io delivers unified, full stack observability and security as a fully-managed SaaS based on best-of-breed open source. The Open 360 pla…

- GitHub: connector-logz-io
- Category: Analytics and SIEM
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `retrieve_all_alerts` | Get Alerts List | investigation | ✗ | — |
| `retrieve_alert_by_id` | Get Alert By ID | investigation | ✗ | `alert_id`(Alert ID, REQ) |
| `enable_alert_by_id` | Enable Alert By ID | investigation | ✗ | `alert_id`(Alert ID, REQ) |
| `disable_alert_by_id` | Disable Alert By ID | investigation | ✗ | `alert_id`(Alert ID, REQ) |
| `search_logs` | Search Logs | investigation | ✗ | `query`(Query) |
| `get_list_of_insights` | Get Insights List | investigation | ✗ | `startDate`(Start Date), `endDate`(End Date), `from`(Offset), `size`(Size), `insightTypes`(Insight Types), `tagNames`(Tag Names), `logTypes`(Log Types), `onlyNew`(Only New), `sortBy`(Sort By), `asc`(Sort Order), `search`(Search) |
| `fetch_security_events` | Get Security Events List | investigation | ✗ | `searchTerm`(Search Term), `severities`(Severities), `fromDate`(From Date, REQ), `toDate`(To Date, REQ), `_source`(Include Muted Events), `field`(Sort By, REQ), `descending`(Sort Order), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `delete_an_alert` | Delete Alert By ID | investigation | ✗ | `alert_id`(Alert ID, REQ) |

### `lumu`

version 1.0.0 — LUMU provides Real-time detection, analysis, and response to network threats.

- GitHub: connector-lumu
- Category: Threat Detection
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_incidents` | Get Incidents | investigation | ✓ | `fromDate`(From Date), `toDate`(To Date), `status`(Incident Status), `adversary-types`(Adversary Type), `labels`(Labels), `page`(Page), `items`(Limit) |
| `get_incident_by_uuid` | Get Incident by UUID | investigation | ✓ | `incident_uuid`(Incident UUID, REQ) |
| `get_incident_context` | Get Incident Context | investigation | ✓ | `incident_uuid`(Incident UUID, REQ), `hash`(Hash Type, REQ) |
| `get_incident_endpoints` | Get Incident Endpoints | investigation | ✓ | `incident_uuid`(Incident UUID, REQ), `endpoints`(Endpoint IDs), `labels`(Labels), `page`(Page), `items`(Limit) |
| `close_incident` | Close Incident | investigation | ✓ | `incident_uuid`(Incident UUID, REQ), `comment`(Comment) |

### `mailboxlayer`

version 1.0.0 — Mailboxlayer simple and powerful API offering instant email address validation & verification via syntax checks, typo and spelling checks, S…

- GitHub: connector-mailboxlayer
- Category: Email Security
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_email_verification_details` | Get Email Verification Detail | investigation | ✗ | `email_address`(Email Address, REQ) |

### `majestic-million-feed`

version 1.0.0 — Majestic crawls the web and analyzes the data to create a huge Link Intelligence dataset describing how the world wide web links together. U…

- GitHub: connector-majestic-million-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_domain_records` | Get Domain Records | investigation | ✓ | `process_response_as`(Process Response As, REQ) |

### `malsilo`

version 2.0.1 — Ingest Threat Intel Feeds from MalSilo Gitlab. <br/><br/>This connector has a dependency on the <a href="/content-hub/all-content/?contentTy…

- GitHub: connector-malsilo
- Category: ThreatIntel
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ipv4_feed` | Get IPv4 Feeds | get_feed | ✓ | `last_pull_time`(Last Pull Time) |
| `get_url_feed` | Get URL Feeds | get_feed | ✓ | `last_pull_time`(Last Pull Time) |
| `get_domain_feed` | Get Domain Feeds | get_feed | ✓ | `last_pull_time`(Last Pull Time) |

### `maltiverse`

version 1.0.0 — Maltiverse Threat Intelligence Feeds can be integrated with your security stack to provide improvement in terms of detections and protection…

- GitHub: connector-maltiverse
- Category: Threat Intelligence
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `ip`(IP, REQ) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `domain`(Domain, REQ) |
| `get_url_reputation` | Get URL Reputation | investigation | ✓ | `url`(URL, REQ) |
| `get_file_reputation` | Get File Reputation | investigation | ✓ | `filehash_type`(File Hash Type, REQ), `filehash`(File Hash, REQ) |

### `malwarebazaar`

version 1.0.0 — MalwareBazaar is a project from abuse.ch with the goal of sharing malware samples with the InfoSec community, AV vendors and threat intellig…

- GitHub: connector-malwarebazaar
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_filehash_reputation` | Get File Hash Reputation | investigation | ✓ | `hash`(File Hash, REQ) |
| `get_malware_samples` | Get Malware Samples | investigation | ✓ | `sha256_hash`(File Hash, REQ) |
| `add_comment_to_malware_sample` | Add a Comment to Malware Sample | investigation | ✓ | `sha256_hash`(File Hash, REQ), `comment`(Comment, REQ) |

### `malwarebazaar-feed`

version 1.0.0 — MalwareBazaar is a project from abuse.ch with the goal of sharing malware samples with the InfoSec community, AV vendors and threat intellig…

- GitHub: connector-malwarebazaar-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `selector_type`(Filter Records, REQ) |

### `manage-engine-key-manager-plus`

version 1.0.0 — ManageEngine Key Manager Plus connector provides a 'key management' solution that helps you consolidate, control, manage, monitor, and audit…

- GitHub: connector-manage-engine-key-manager-plus
- Category: Identity and Access Management
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ssh_keys` | Get SSH Keys | investigation | ✓ | — |
| `get_ssl_certificates` | Get SSL Certificates | investigation | ✓ | `search_type`(Discover Using, REQ), `time_out`(Time Out, REQ), `port`(Port Number, REQ) |
| `update_credentials` | Update Credentials | investigation | ✓ | `resource_name`(Resource Name, REQ), `user_name`(User Name, REQ), `password`(Password, REQ), `is_admin`(Is Admin) |

### `manage-engine-log360`

version 1.0.0 — ManageEngine Log360 is a unified SIEM solution with integrated DLP and CASB capabilities that detects, prioritizes, investigates, and respon…

- GitHub: connector-manage-engine-log360
- Category: SIEM
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `invoke_search` | Get Events List | investigation | ✓ | `query`(Search Query), `from`(From), `to`(To), `hosts`(Hosts), `groups`(Groups) |
| `get_alerts` | Get Alerts List | investigation | ✓ | `from`(From), `to`(To), `query`(Search Query), `alert_profiles`(Alert Profiles), `severity`(Alert Severity), `status`(Alert Status) |
| `get_alert_profiles` | Get Alert Profiles List | investigation | ✓ | `type`(Alert Profile Type), `severity`(Alert Profile Severity), `status`(Alert Profile Status) |

### `manage-engine-service-desk-plus`

version 3.0.0 — ManageEngine ServiceDesk Plus is used in turning IT teams from daily fire-fighting to delivering awesome customer service. It provides great…

- GitHub: connector-manage-engine-service-desk-plus
- Category: Ticket Management
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `add_request` | Create Ticket | investigation | ✓ | `subject`(Subject, REQ), `description`(Description), `request_type`(Request Type), `status`(Status), `priority`(Priority), `urgency`(Urgency), `group`(Group), `requester`(Requester, REQ), `other_fields`(Other Fields) |
| `add_resolution` | Add Resolution | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `resolution`(Resolution, REQ) |
| `add_note` | Add Note | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `description`(Description, REQ), `show_to_requester`(Show to Requester), `mark_first_response`(Mark First Response), `add_to_linked_requests`(Add to Linked Requests), `notify_technician`(Notify Technician) |
| `get_request` | Get Ticket Details | investigation | ✓ | `request_id`(Ticket Request ID, REQ) |
| `get_all_requester` | Get All Requesters | investigation | ✓ | `id`(Requester ID), `name`(Name), `employee_id`(Employee ID), `email_id`(Email ID), `type`(Type), `other_fields`(Other Fields), `fields_required`(Fields Required), `sort_field`(Sort By), `sort_order`(Sort Order), `start_index`(Start Index), `size`(Record Count) |
| `get_all_open_requests` | Get All Open Tickets | investigation | ✓ | `id`(Ticket Request ID), `subject`(Subject), `priority.name`(Priority), `requester.name`(Requester Name), `other_fields`(Other Fields), `sort_field`(Sort By), `sort_order`(Sort Order), `from`(Start From), `limit`(Limit Upto) |
| `update_request` | Update Ticket | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `subject`(Subject), `description`(Description), `status`(Status), `urgency`(Urgency), `priority`(Priority), `other_fields`(Other Fields) |
| `close_request` | Close Ticket | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `is_fcr`(FCR, REQ), `requester_ack_resolution`(Has requester acknowledged the resolution?, REQ), `requester_ack_comments`(Comments), `closure_code`(Request Closure Code), `closure_comments`(Request Closure Comments) |
| `delete_request` | Delete Ticket | investigation | ✓ | `request_id`(Ticket Request ID, REQ) |
| `delete_request_from_trash` | Delete Ticket From Trash | investigation | ✓ | `request_id`(Ticket Request ID, REQ) |

### `manage-engine-service-desk-plus-msp`

version 1.0.0 — ServiceDesk Plus MSP is a web based, full-fledged ITSM suite designed specifically for managed service providers. This all-in-one ITSM solut…

- GitHub: connector-manage-engine-service-desk-plus-msp
- Category: Ticket Management
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_requests` | Get All Tickets | investigation | ✓ | `id`(Ticket Request ID), `subject`(Subject), `status.name`(Status), `priority.name`(Priority), `requester.name`(Requester Name), `other_fields`(Other Fields), `filter_by`(Filter By), `sort_field`(Sort By), `sort_order`(Sort Order), `from`(Start From), `size`(Size) |
| `add_request` | Create Ticket | investigation | ✓ | `subject`(Subject, REQ), `requester`(Requester, REQ), `description`(Description), `request_type`(Request Type), `status`(Status), `priority`(Priority), `urgency`(Urgency), `group`(Group), `site`(MSP Site Details), `account`(MSP Account Details), `other_fields`(Other Fields) |
| `update_request` | Update Ticket | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `subject`(Subject), `description`(Description), `status`(Status), `urgency`(Urgency), `priority`(Priority), `site`(MSP Site Details), `other_fields`(Other Fields) |
| `close_request` | Close Ticket | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `is_fcr`(FCR, REQ), `requester_ack_resolution`(Has Requester Acknowledged The Resolution?, REQ), `requester_ack_comments`(Comments), `closure_code`(Request Closure Code), `closure_comments`(Request Closure Comments) |
| `delete_request` | Delete Ticket | investigation | ✓ | `request_id`(Ticket Request ID, REQ) |
| `delete_request_from_trash` | Delete Ticket From Trash | investigation | ✓ | `request_id`(Ticket Request ID, REQ) |
| `add_resolution` | Add Resolution | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `resolution`(Resolution, REQ) |
| `add_note` | Add Note | investigation | ✓ | `request_id`(Ticket Request ID, REQ), `description`(Description, REQ), `show_to_requester`(Show to Requester), `mark_first_response`(Mark First Response), `add_to_linked_requests`(Add to Linked Requests), `notify_technician`(Notify Technician) |
| `get_request` | Get Ticket Details | investigation | ✓ | `request_id`(Ticket Request ID, REQ) |
| `get_all_user` | Get All Users | investigation | ✓ | `id`(User ID), `name`(User Name), `employee_id`(Employee ID), `email_id`(Email ID), `type`(User Type), `other_fields`(Other Fields), `fields_required`(Fields Required), `sort_field`(Sort By), `sort_order`(Sort Order), `start_index`(Start From), `size`(Size) |
| `get_all_sites` | Get All Sites | investigation | ✓ | `from`(Start From), `size`(Size) |
| `get_all_accounts` | Get All Accounts | investigation | ✓ | — |
| `get_all_statuses` | Get All Statuses | investigation | ✓ | — |
| `get_all_priorities` | Get All Priorities | investigation | ✓ | — |
| `get_all_urgencies` | Get All Urgencies | investigation | ✓ | — |
| `get_all_request_closure_codes` | Get All Request Closure Codes | investigation | ✓ | — |

### `mandiant-advantage-threat-intelligence`

version 1.0.0 — Mandiant Advantage Threat Intelligence provides automated access to indicators of compromise (IOCs) IP addresses, domain names, URLs threat …

- GitHub: connector-mandiant-advantage-threat-intelligence
- Category: Threat Intelligence
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators List | investigation | ✓ | `start_epoch`(Start DateTime, REQ), `end_epoch`(End DateTime), `gte_mscore`(Confidence Score), `exclude_osint`(Exclude Open Source Indicator), `include_reports`(Include Reports), `report_limit`(Report Limit), `include_campaigns`(Include Campaigns), `sort_by`(Sort By), `sort_order`(Sort Order), `limit`(Limit), `next`(Skip Token) |
| `get_indicator_details` | Get Indicator Details | investigation | ✓ | `value`(Indicator Value, REQ) |
| `get_actors` | Get Threat Actors List | investigation | ✓ | `limit`(Limit), `offset`(Offset) |
| `get_actor_details` | Get Threat Actor Details | investigation | ✓ | `id`(Actor ID/Name, REQ) |
| `get_malware` | Get Malware Families List | investigation | ✓ | `limit`(Limit), `offset`(Offset) |
| `get_malware_details` | Get Malware Family Details | investigation | ✓ | `id`(Malware ID/Name, REQ) |
| `get_campaign` | Get Campaigns List | investigation | ✓ | `start_date`(Start DateTime), `end_date`(End DateTime), `limit`(Limit), `offset`(Offset) |
| `get_campaign_details` | Get Campaign Details | investigation | ✓ | `id`(Campaign ID, REQ) |
| `get_vulnerability` | Get Vulnerabilities List | investigation | ✓ | `start_epoch`(Start DateTime), `end_epoch`(End DateTime), `rating_types`(Rating Types), `risk_ratings`(Risk Ratings), `sort_by`(Sort By), `sort_order`(Sort Order), `limit`(Limit), `next`(Skip Token) |
| `get_reports` | Get Reports List | investigation | ✓ | `start_epoch`(Start DateTime), `end_epoch`(End DateTime), `limit`(Limit), `offset`(Offset), `next`(Skip Token) |
| `get_report_details` | Get Report Details | investigation | ✓ | `id`(Report ID, REQ) |

### `mandiant-feed`

version 1.0.0 — Mandiant Threat Intelligence provides automated access to indicators of compromise (IOCs) — IP addresses, domain names, URLs threat actors a…

- GitHub: connector-mandiant-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `added_after`(Created After), `length`(Limit), `id`(STIX UUID), `status`(Status) |

### `mandiant-threat-intel`

version 1.2.0 — Mandiant Threat Intelligence provides automated access to indicators of compromise (IOCs) — IP addresses, domain names, URLs threat actors a…

- GitHub: connector-mandiant-threat-intel
- Category: Threat Intelligence
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `added_after`(Created At), `length`(Size), `id`(STIX UUID), `status`(Status) |
| `get_reports` | Get Reports | investigation | ✓ | `added_after`(Created At, REQ), `length`(Size), `report_id`(Report ID), `document_id`(Document ID), `status`(Status), `subscription`(Subscription), `report_type`(Report Type), `actor_name`(Actor Name), `malware_name`(Malware Name) |
| `get_alerts` | Get Alerts | investigation | ✓ | `added_after`(Created At), `length`(Size), `id`(ID), `alert_type`(Alert Type), `alert_status`(Alert Status), `alert_categories`(Alert Categories), `alert_severity`(Alert Severity) |
| `search_collections` | Search Collections | investigation | ✓ | `queries`(Queries, REQ), `include_connected_objects`(Include Connected Objects), `connected_objects`(Connected Objects), `sort_by`(Sort By), `sort_order`(Order By) |
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `added_after`(Created At), `length`(Size), `id`(STIX UUID), `status`(Status) |
| `get_reputation_of_indicators` | Get Indicator Reputation | investigation | ✓ | `indicatorValue`(Indicator Value, REQ) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `maxmind-geoip2`

version 1.0.0 — GeoIP2 IP Intelligence provides an extensive breadth of data on IP addresses for content customization, geofencing, user analysis, research,…

- GitHub: connector-maxmind-geoip2
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_country` | Get Country | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `get_city` | Get City | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `get_insights` | Get Insights | investigation | ✓ | `ip_address`(IP Address, REQ) |

### `mcafee-mvision-insights`

version 1.1.0 — MVISION Insights APIs provide intelligence about Campaigns, associated IOCs and Events. They also provide classification information on file…

- GitHub: connector-mcafee-mvision-insights
- Category: Threat Intelligence
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ioc_list` | Get All IOC List | investigation | ✓ | `offset`(Offset), `limit`(Limit), `id`(Campaign ID), `type`(IOC Type), `fields`(Fields) |
| `get_ioc_details` | Get IOC Details | investigation | ✓ | `id`(IOC ID, REQ), `fields`(Fields) |
| `get_ioc_campaigns` | Get IOC Campaigns | investigation | ✓ | `id`(IOC ID, REQ) |
| `get_ioc_relationship_campaigns` | Get IOC Relationship Campaigns | investigation | ✓ | `id`(IOC ID, REQ) |
| `get_artefacts` | Get Artefacts | investigation | ✓ | `hashtype`(Hash Type, REQ), `hashvalue`(Hash Value, REQ) |
| `get_campaigns_list` | Get All Campaigns List | investigation | ✓ | `offset`(Offset), `limit`(Limit), `filter_by`(Filter By), `campaign_name`(Campaign Name), `sector`(Sector), `include`(Include), `fields`(Fields) |
| `get_campaign_details` | Get Campaign Details | investigation | ✓ | `id`(Campaign ID, REQ), `include`(Include), `fields`(Fields) |
| `get_campaign_iocs` | Get Campaign IOCs | investigation | ✓ | `id`(Campaign ID, REQ) |
| `get_campaigns_relationship_iocs` | Get Campaign Relationship IOCs | investigation | ✓ | `id`(Campaign ID, REQ) |
| `get_campaign_galaxies` | Get Campaign Galaxies | investigation | ✓ | `id`(Campaign ID, REQ) |
| `get_campaigns_relationship_galaxies` | Get Campaign Relationship Galaxies | investigation | ✓ | `id`(Campaign ID, REQ) |
| `get_campaigns_detected` | Get All Campaigns Detected | investigation | ✓ | `offset`(Offset), `limit`(Limit), `filter_by`(Filter By), `campaign_name`(Campaign Name), `sector`(Sector), `last_detected_on`(Last Detected On), `include`(Include), `fields`(Fields) |
| `get_events_list` | Get All Events List | investigation | ✓ | `offset`(Offset), `limit`(Limit), `artefact_type`(Artefact Type), `artefact_value`(Artefact Value), `agent_guid`(Agent GUID), `id`(Campaign ID), `from_date`(From Date), `to_time`(To Date), `fields`(Fields) |
| `get_galaxies_list` | Get All Galaxies List | investigation | ✓ | `offset`(Offset), `limit`(Limit), `category`(Category), `id`(Campaign ID), `fields`(Fields) |
| `get_insights_events_list` | Get Insights Events List | investigation | ✓ | `artefact_type`(Artefact Type), `artefact_value`(Artefact Value), `agent_guid`(Agent GUID), `id`(Campaign ID), `from_date`(From Date), `to_date`(To Date), `offset`(Offset), `limit`(Limit) |
| `get_related_samples` | Get Related Samples | investigation | ✓ | `samplemd5`(Sample MD5 Hash, REQ), `sfvecmd5`(Static Feature MD5 Hash, REQ), `version`(Static Feature Version, REQ), `lastseen`(Days Since Last Seen), `offset`(Offset), `limit`(Limit) |

### `micro-focus-service-manager`

version 1.4.0 — Micro Focus service manager connector helps you to create incident, update incident, list incidents, get incident, get device list and get d…

- GitHub: connector-micro-focus-service-manager
- Category: IT Service Management
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_incident` | Create Incident | investigation | ✓ | `title`(Title, REQ), `description`(Description, REQ), `impact`(Impact, REQ), `urgency`(Urgency, REQ), `category`(Category, REQ), `service`(Primary Affected Service, REQ), `affected_ci`(Affected CI), `subcategory`(Subcategory), `area`(Area), `assignment_group`(Assignment Group), `source`(Source), `contact_person`(Contact Person), `outage_start_time`(Outage Start Time), `outage_end_time`(Outage End Time), `assignee`(Assignee), `service_recipient`(Service Recipient), `location`(Location), `solution`(Solution), `json_input`(Additional Fields) |
| `list_incidents` | Get Incident List | investigation | ✓ | `query`(Query), `sort`(Sort), `start`(Start), `count`(Count), `view`(View) |
| `get_incident` | Get Incident | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `update_incident` | Update Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `title`(Title), `description`(Description), `impact`(Impact), `urgency`(Urgency), `category`(Category), `service`(Primary Affected Service), `affected_ci`(Affected CI), `subcategory`(Subcategory), `area`(Area), `assignment_group`(Assignment Group), `source`(Source), `contact_person`(Contact Person), `outage_start_time`(Outage Start Time), `outage_end_time`(Outage End Time), `assignee`(Assignee), `service_recipient`(Service Recipient), `location`(Location), `solution`(Solution), `json_input`(Additional Fields) |
| `get_device_list` | Get Device List | investigation | ✓ | `query`(Query), `sort`(Sort), `start`(Start), `count`(Count), `view`(View) |
| `get_device` | Get Device | investigation | ✓ | `config_item`(configuration Item, REQ) |
| `create_change` | Create Change | investigation | ✓ | `Title`(Title, REQ), `Description`(Description, REQ), `Category`(Category, REQ), `Subcategory`(Subcategory, REQ), `InitiatedBy`(Initiated By, REQ), `Service`(Primary Affected Service, REQ), `AffectedCI`(Affected CI), `ChangeOriginator`(Change Originator, REQ), `ChangeCoordinator`(Change Coordinator, REQ), `ReasonForChange`(Reason For Change, REQ), `PlannedStart`(Target Start Time), `PlannedEnd`(Target End Time), `json_input`(Additional Fields) |
| `list_changes` | Get Change List | investigation | ✓ | `query`(Query), `sort`(Sort), `start`(Start), `count`(Count), `view`(View) |
| `get_change_request` | Get Change Request | investigation | ✓ | `change_request_id`(Change Request Number, REQ) |
| `update_change` | Update Change | investigation | ✓ | `change_id`(Change ID, REQ), `ClosureCode`(Closure Code, REQ), `SubClosureCode`(SubClosure Code, REQ), `ClosingComments`(Closing Comments, REQ), `Phase`(Phase, REQ), `PlannedStart`(Actual Start Time), `PlannedEnd`(Actual End Time) |
| `create_rf` | Create RF - Request Fulfillment Ticket | investigation | ✓ | `BriefDescription`(Title or Brief Description, REQ), `Description`(Description, REQ), `Category`(Category, REQ), `Subcategory`(Subcategory, REQ), `AssignedTo`(Assigned To, REQ), `AssignedGroup`(Assigned Group, REQ), `Impact`(Impact, REQ), `Priority`(Priority, REQ), `Urgency`(Urgency, REQ), `ProductType`(Product Type, REQ), `RequestorName`(Requester Name, REQ) |
| `get_rf` | Get RF - Request Fulfillment Ticket | investigation | ✓ | `rf_id`(RF - Request Fulfillment Ticket Number, REQ) |
| `update_rf_attachment` | Update RF - Request Fulfillment Ticket for an attachment | investigation | ✓ | `rf_id`(RF-Request Fulfillment Ticket ID , REQ), `attachment_name`(Attachment Name, REQ), `msg_body`(Message Body, REQ) |
| `retrieve_attachment_information` | Retrieve Attachment Information | investigation | ✓ | `incident_id`(Incident ID, REQ) |
| `download_an_attachment` | Download Attachment | investigation | ✓ | `incident_id`(Incident ID, REQ), `attachment_id`(Attachment ID, REQ) |
| `delete_an_attachment` | Delete Attachment | investigation | ✓ | `incident_id`(Incident ID, REQ), `attachment_id`(Attachment ID, REQ) |

### `microfocus_smax`

version 1.0.0 — Micro Focus SMAX connector is used for fetch SMAX incidents, requests and automate different SMAX case management actions.

- GitHub: connector-microfocus_smax
- Category: Ticket Creation
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_entities` | Create Entities | investigation | ✓ | `entities`(Entities, REQ) |
| `create_incident` | Create Incident | investigation | ✓ | `incident_name`(Incident Name, REQ), `incident_description`(Incident Description, REQ), `impacted_service_id`(Impacted Service ID, REQ), `requested_by_user_id`(Requested By User ID), `incident_urgency`(Incident Urgency), `impact_scope`(Impact Scope), `service_desk_group_id`(Service Desk Group ID), `other_properties`(Other Properties) |
| `create_request` | Create Request | investigation | ✓ | `request_name`(Request Name, REQ), `request_description`(Request Description, REQ), `requested_for_user_id`(Requested for User ID, REQ), `requested_by_user_id`(Requested By User ID), `request_urgency`(Request Urgency), `impact_scope`(Impact Scope), `other_properties`(Other Properties) |
| `get_entity_details` | Get Entity Details | investigation | ✓ | `entity_type`(Entity Type, REQ), `entity_id`(Entity ID, REQ), `entity_fields`(Entity Fields) |
| `query_entities` | Query Entities | investigation | ✓ | `entity_type`(Entity Type, REQ), `entity_fields`(Entity Fields), `query_filter`(Query Filter), `order_by`(Order By), `size`(Size), `skip`(Skip) |
| `update_entities` | Update Entities | investigation | ✓ | `entities`(Entities, REQ) |
| `update_incident` | Update Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `incident_description`(Incident Description, REQ), `incident_urgency`(Incident Urgency), `impact_scope`(Impact Scope), `incident_status`(Incident Status, REQ), `incident_closure_category_id`(Incident Closure Category ID, REQ), `incident_completion_code`(Incident Completion Code), `incident_solution`(Incident Solution), `other_properties`(Other Properties) |
| `update_request` | Update Request | investigation | ✓ | `request_id`(Request ID, REQ), `request_description`(Request Description, REQ), `request_urgency`(Request Urgency), `impact_scope`(Impact Scope), `request_status`(Request Status, REQ), `other_properties`(Other Properties) |

### `microsoft-advanced-threat-analytics`

version 1.0.0 — Microsoft Advanced Threat Analytics (ATA) is an on-premises platform that helps protect your enterprise from multiple types of advanced targ…

- GitHub: connector-microsoft-advanced-threat-analytics
- Category: Threat Detection
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_suspicious_activities_list` | Get Suspicious Activities List | investigation | ✓ | `activity_id`(Suspicious Activity ID, REQ) |
| `set_suspicious_activity_status` | Set Suspicious Activity Status | investigation | ✓ | `activity_id`(Suspicious Activity ID, REQ), `status`(Status, REQ) |
| `get_monitoring_alerts_list` | Get Monitoring Alerts List | investigation | ✓ | — |
| `get_entity` | Get Entity | investigation | ✓ | `entity_id`(Entity ID, REQ) |

### `microsoft-bing`

version 1.0.0 — Microsoft Bing is a web search engine it provides a standard web search, as well as specialized searches for images, videos, shopping, news,…

- GitHub: connector-microsoft-bing
- Category: Miscellaneous
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `web_search` | Web Search | investigation | ✓ | `q`(Search Query, REQ), `freshness`(Filter Search), `responseFilter`(Response Filter), `answerCount`(Answer Count), `promote`(Promote), `safeSearch`(Safe Search), `textDecorations`(Text Decorations), `setLang`(Supported Languages), `cc`(Country Code), `count`(Count), `offset`(Offset), `additional_fields`(Additional Fields) |

### `microsoft-defender-for-iot`

version 1.0.0 — Microsoft Defender for IoT consolidates real-time asset discovery, vulnerability management, and cyberthreat protection for your Internet of…

- GitHub: connector-microsoft-defender-for-iot
- Category: OT & IoT Security 
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_alerts` | Get Alert List | investigation | ✓ | `state`(State), `type`(Type), `fromTime`(Created After), `toTime`(Created Before) |
| `list_timeline_events` | Get Timeline Events | investigation | ✓ | `type`(Type), `minutesTimeFrame`(Reported in Last x Minutes) |
| `list_devices` | Get Device List | investigation | ✓ | `authorized`(Authorized) |
| `list_device_cves` | Get Device CVEs List | investigation | ✓ | `ipAddress`(IP Address), `top`(Size) |
| `get_device_vulnerability_report` | Get Device Vulnerability Information | investigation | ✓ | — |
| `get_vulnerability_assessment_report` | Get Security Vulnerabilities | investigation | ✓ | — |
| `get_operational_assessment_report` | Get Operational Vulnerabilities | investigation | ✓ | — |
| `get_mitigation_assessment` | Get Mitigation Steps | investigation | ✓ | — |

### `microsoft-defender-threat-intelligence`

version 1.0.0 — The Microsoft Defender Threat Intelligence FortiSOAR Connector enables automated threat intelligence gathering, enrichment, and response wit…

- GitHub: connector-microsoft-defender-threat-intelligence
- Category: Threat Intelligence
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_host_reputation` | Get Host Reputation | containment | ✓ | `hostId`(Host ID, REQ) |
| `get_host_details` | Get Host Details | containment | ✓ | `hostId`(Host ID, REQ) |
| `get_whoisrecord` | Get Whois Record | containment | ✓ | `type`(Select Host ID or whoisRecord ID, REQ) |
| `list_components` | Get Components List | containment | ✓ | `hostId`(Host ID, REQ) |
| `list_passiveDns` | Get Passive DNS List | containment | ✓ | `hostId`(Host ID, REQ) |
| `list_passiveDns_reverse` | Get Passive DNS Reverse List | containment | ✓ | `hostId`(Host ID, REQ) |
| `list_hostPorts` | Get Host Ports List | containment | ✓ | `hostId`(Host ID, REQ) |
| `list_host_ssl_certificates` | Get Host SSL Certificates List | containment | ✓ | `hostId`(Host ID, REQ) |
| `get_host_ssl_certificate` | Get Host SSL Certificate | containment | ✓ | `hostSslCertificateId`(Host Certificate ID, REQ) |
| `get_host_component` | Get Host Component | containment | ✓ | `hostComponentId`(Host Component ID, REQ) |
| `list_indicators` | Get Indicators List | containment | ✓ | `intelligenceProfileId`(Intelligence Profile ID, REQ) |

### `microsoft-defender-vulnerability-management`

version 1.0.0 — Microsoft's Defender Vulnerability Management is a built-in module in Microsoft Defender for Endpoint that can discover vulnerabilities and …

- GitHub: connector-microsoft-defender-vulnerability-management
- Category: Vulnerability and Risk Management
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_vulnerabilities` | Get All Vulnerabilities | investigation | ✓ | `id`(CVE ID), `publishedOn`(Published On), `severity`(Severity), `$filter`(Filter Query), `$skip`(Offset), `$top`(Number of Vulnerabilities to Fetch) |
| `list_vulnerabilities_by_machine_and_software` | Get Vulnerabilities By Machine And Software | investigation | ✓ | `id`(Vulnerabilities ID), `cveId`(CVE ID), `machineId`(Machine ID), `severity`(Severity), `$filter`(Filter Query), `$skip`(Offset), `$top`(Number of Vulnerabilities to Fetch) |
| `get_vulnerability_by_id` | Get Vulnerability By CVE ID | investigation | ✓ | `id`(CVE ID, REQ) |
| `list_devices_by_vulnerability` | Get Devices By Vulnerability | investigation | ✓ | `id`(Vulnerability ID, REQ) |
| `get_specific_cve_details` | Get Specific CVE ID Details | investigation | ✓ | `cveId`(CVE ID, REQ) |

### `microsoft-graph`

version 2.2.0 — Microsoft Graph API is a powerful and unified programming interface provided by Microsoft that allows developers to access a wide range of d…

- GitHub: connector-microsoft-graph
- Category: Utilities
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_risky_users_list` | Get Risky Users List | investigation | ✓ | — |
| `get_risky_user_details` | Get Risky User Details | investigation | ✓ | `risk_id`(Risky User ID, REQ) |
| `get_all_security_alerts` | Get All Security Alerts | investigation | ✓ | `api_version`(API Version), `assigned_to`(Assigned To), `top`(Limit), `skip`(Offset) |
| `get_security_alert` | Get Security Alert | investigation | ✓ | `api_version`(API Version), `alert_id`(Alert ID, REQ) |
| `update_security_alert` | Update Security Alert | investigation | ✓ | `alert_id`(Alert ID, REQ), `api_version`(API Version), `assigned_to`(Assigned To) |
| `add_comment_on_security_alert` | Add Comment on Security Alert | investigation | ✓ | `alert_id`(Alert ID, REQ), `comment`(Comment, REQ) |
| `get_groups` | Get Groups | investigation | ✓ | — |
| `get_group_users` | Get Users Within A Group | investigation | ✓ | `group_id`(Group ID, REQ) |
| `search_message` | Search Message in Users Mailbox | investigation | ✓ | `subject`(Subject, REQ), `user_list`(User List, REQ), `size`(Page Size), `skip`(Offset) |
| `del_message` | Delete Message | investigation | ✓ | `user_id`(User ID, REQ), `message_id`(Message ID, REQ) |
| `del_message_bulk` | Delete Message Bulk | investigation | ✓ | `user_list`(User List, REQ) |
| `revoke_user_sessions` | Revoke User Session | remediation | ✓ | `user`(User ID or PrincipalName, REQ) |
| `get_all_named_locations` | Get All Named Locations | investigation | ✓ | `name`(Display Name), `select`(Required Fields), `order_by`(Order By), `count`(Count), `size`(Size), `skip`(Offset) |
| `block_new_ips` | Block New IP Ranges | containment | ✓ | `namedLocationUuid`(IP Named Location's UUID, REQ), `ipv4_ips`(IPv4 Ranges), `ipv6_ips`(IPv6 Ranges) |
| `unblock_new_ips` | Unblock IP Ranges | remediation | ✓ | `namedLocationUuid`(IP Named Location's UUID, REQ), `ipv4_ips`(IPv4 Ranges), `ipv6_ips`(IPv6 Ranges) |
| `create_ip_range_location` | Create IP Named Location | investigation | ✓ | `name`(Display Name, REQ), `is_trusted`(Is Trusted), `ipv4_ips`(IPv4 Ranges), `ipv6_ips`(IPv6 Ranges) |

### `microsoft-graph-mail`

version 1.4.0 — Using Microsoft Graph integrate with Outlook by creating an app and get authorized access to a user's Outlook mail in a personal or organiza…

- GitHub: connector-microsoft-graph-mail
- Category: Email Server
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_unread_emails` | Get Unread Emails | investigation | ✓ | `user_id`(User ID/User Principal Name, REQ), `source`(Source Folder, REQ), `mark_as_read`(Mark as Read), `parse_inline`(Parse Inline Images), `save_email`(Save Email), `limit`(Limit) |
| `search_emails` | Search Emails | investigation | ✓ | `user_id`(User ID/User Principal Name, REQ), `source`(Source Folder, REQ), `odata_query`(Odata Query), `search`(Search), `mark_read`(Mark as Read), `parse_inline`(Parse Inline Images), `limit`(Limit) |
| `get_folders` | Get Folders | investigation | ✓ | `user_id`(User ID/User Principal Name, REQ), `limit`(Limit) |
| `get_child_folders` | Get Child Folders | investigation | ✓ | `user_id`(User ID/User Principal Name, REQ), `source_folder`(Source Folder, REQ), `limit`(Limit) |
| `move_email` | Move Email | miscellaneous | ✓ | `user_id`(User ID/User Principal Name, REQ), `destination_folder`(Destination Folder, REQ), `message_id`(Message ID, REQ) |
| `copy_email` | Copy Email | miscellaneous | ✓ | `user_id`(User ID/User Principal Name, REQ), `destination_folder`(Destination Folder, REQ), `message_id`(Message ID, REQ) |
| `delete_email` | Delete Email | investigation | ✓ | `user_id`(User ID/User Principal Name, REQ), `source`(Source Folder), `message_id`(Message ID, REQ) |
| `get_email_templates` | Get Email Templates | investigation | ✓ | — |
| `send_email` | Send Email | investigation | ✓ | `from`(From, REQ), `body_type`(Body Type), `to_recipients`(To Recipients, REQ), `cc_recipients`(Cc Recipients), `bcc_recipients`(Bcc Recipients), `iri_list`(Attachment IRIs), `flag`(Flag), `importance`(Importance) |
| `forward_email` | Forward Email | investigation | ✓ | `to_recipients`(To Recipients, REQ), `from_recipients`(From Recipients, REQ), `message_id`(Message ID, REQ), `body`(Body) |
| `send_email_as_reply` | Send Mail as Reply | investigation | ✓ | `message_id`(Message ID, REQ), `from_recipients`(From Recipients, REQ), `to`(To Recipients), `cc_recipients`(Cc Recipients), `bcc_recipients`(Bcc Recipients), `body`(Body), `iri_list`(Attachment IRIs) |
| `create_email_threat_submission` | Create Email Threat Submission | investigation | ✓ | `input`(Threat Submission Type, REQ), `other_params`(Other Parameters) |
| `get_email_categories` | Get Email Categories | investigation | ✓ | `user_id`(User ID/User Principal Name, REQ), `message_id`(Message ID, REQ) |
| `add_email_category` | Add Email Category | investigation | ✓ | `user_id`(User ID/User Principal Name, REQ), `message_id`(Message ID, REQ), `category`(Category, REQ) |
| `remove_email_category` | Remove Email Category | miscellaneous | ✓ | `user_id`(User ID/User Principal Name, REQ), `message_id`(Message ID, REQ), `category`(Category, REQ) |
| `execute_api_request` | Execute an API Request | investigation | ✓ | `endpoint`(Endpoint, REQ), `method`(Method, REQ), `query_params`(Query Parameters), `payload`(Payload) |

### `microsoft-intune`

version 1.0.0 — Microsoft Intune is a cloud-based endpoint management solution. This connector facilitates automated operation related to managed device.

- GitHub: connector-microsoft-intune
- Category: Communication
- Operations: 20

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_managed_devices` | Get Managed Devices List | investigation  | ✓ | — |
| `get_managed_device_details` | Get Managed Device Details | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `retire_device` | Retire Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `wipe_device` | Wipe Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `reset_passcode_of_device` | Reset Passcode Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `remote_lock_of_device` | Remote Lock Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `request_remote_assistance_of_device` | Request Remote Assistance for Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `disable_lost_mode_of_device` | Disable Lost Mode for Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `locate_device` | Locate a Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `bypass_activation_lock_of_device` | Bypass Activation Lock for Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `reboot_device` | Reboot Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `shutdown_device` | Shutdown Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `recover_passcode_of_device` | Recover Passcode for Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `clean_windows_device` | Clean Windows Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `logout_shared_apple_device_active_user` | Logout Apple Device for Active User | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `delete_user_from_shared_apple_device` | Delete User from Apple Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `sync_device` | Sync Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `windows_defender_scan` | Windows Defender Scan | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `windows_defender_update_signature` | Update Signature for Windows Defender | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |
| `update_windows_device_account` | Update Account for Windows Device | investigation  | ✓ | `managedDeviceId`(Managed Device ID, REQ) |

### `microsoft-office-365-feed`

version 1.0.0 — Ingest the IP, URLs used by Office 365 using the web service provided by Microsoft. The fetched indicators can be used to create a whitelist…

- GitHub: connector-microsoft-office-365-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicator` | Fetch Indicators | investigation | ✓ | `indicator_type`(Indicator Type, REQ), `last_pull_time`(Modified After), `limit`(Limit) |

### `microsoft-onedrive`

version 1.0.0 — OneDrive is a cloud storage and file synchronization service developed by Microsoft. It allows users to store their files and documents secu…

- GitHub: connector-microsoft-onedrive
- Category: Asset Management
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_folder` | Create Folder | investigation | ✓ | `associated_with`(Associated With, REQ), `folder_structure`(Folder Structure, REQ), `parent_item_id`(Parent Item ID, REQ) |
| `get_user_onedrive` |  Get User OneDrive | investigation | ✓ | `user_id`(User ID or Principal Name, REQ) |
| `get_document_library` | Get Document Library | investigation | ✓ | `select_option`(Associated With, REQ) |
| `get_drive_by_id` | Get Drive By ID | investigation | ✓ | `drive_id`(Drive ID, REQ) |
| `list_drives` | List Drives | investigation | ✓ | — |
| `download_file` | Download File | investigation | ✓ | `associated_with`(Associated With, REQ), `item_id`(Item ID, REQ) |
| `upload_file` | Upload File | investigation | ✓ | `associated_with`(Associated With, REQ), `input`(Type, REQ), `value`(Reference ID, REQ), `parent_item_id`(Parent Item ID, REQ), `filename`(File Name, REQ) |

### `microsoft-sccm`

version 1.0.0 — Microsoft SCCM Connector

- GitHub: connector-microsoft-sccm
- Category: Windows Endpoint Management
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_patches` | Get All Software Updates | investigation | ✓ | — |
| `get_device_collections` | Get All Device Collections | investigation | ✓ | — |
| `deploy_patch` | Deploy Patch | remediation | ✓ | `patch_name`(Software Patch Name, REQ), `collection_name`(Device Collection Name, REQ), `additional_params`(Additional Deployment Parameters) |

### `microsoft-sentinel`

version 1.1.0 — Microsoft Sentinel is Cloud-native SIEM for intelligent security analytics for your entire enterprise. These connector connects to Microsoft…

- GitHub: connector-microsoft-sentinel
- Category: Analytics and SIEM
- Operations: 31

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_threat_intelligence_indicator` | Create Threat Intelligence Indicator | investigation | ✓ | `displayName`(Display Name, REQ), `patternType`(Pattern Type, REQ), `source`(Source, REQ), `confidence`(Confidence), `description`(Description), `threatIntelligenceTags`(Tags), `threatTypes`(Threat Type), `indicatorTypes`(Indicator Type), `labels`(Labels), `additional_fields`(Additional Fields) |
| `get_all_threat_intelligence_indicators` | Get All Threat Intelligence Indicators | investigation | ✓ | `$filter`(Search Query), `$orderby`(Order By), `$top`(Number of Indicators to Fetch), `$skipToken`(Skip Token) |
| `get_threat_intelligence_indicator` | Get Threat Intelligence Indicator | investigation | ✓ | `id`(Threat Intelligence Indicator ID, REQ) |
| `update_threat_intelligence_indicator` | Update Threat Intelligence Indicator | investigation | ✓ | `id`(Threat Intelligence Indicator ID, REQ), `displayName`(Display Name, REQ), `patternType`(Pattern Type, REQ), `source`(Source, REQ), `confidence`(Confidence), `description`(Description), `threatIntelligenceTags`(Tags), `threatTypes`(Threat Type), `indicatorTypes`(Indicator Type), `labels`(Labels), `additional_fields`(Additional Fields) |
| `delete_threat_intelligence_indicator` | Delete Threat Intelligence Indicator | investigation | ✓ | `id`(Threat Intelligence Indicator ID, REQ) |
| `get_incident_list` | Get Incident List | investigation | ✓ | `created_datetime`(Created DateTime), `Severity`(Severity), `Status`(Status), `$filter`(Search Query), `$orderby`(Order By), `$top`(Number of Incidents to Fetch), `$skipToken`(Skip Token) |
| `get_incident` | Get Incident Details | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `get_alert_list` | Get Incident Alert List | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `get_entities_list` | Get Incident Entities List | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `get_bookmarks_list` | Get Incident Bookmarks List | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `update_incident` | Update Incident | investigation | ✓ | `incidentId`(Incident ID, REQ), `Severity`(Severity, REQ), `Status`(Status, REQ), `Title`(Title, REQ), `labels`(Labels), `etag`(ETag), `Description`(Description), `custom_attributes`(Custom Properties) |
| `create_incident_relations` | Create Incident Relations | investigation | ✓ | `incidentId`(Incident ID, REQ), `relationName`(Relation Name, REQ), `resourceId`(Resource ID, REQ) |
| `get_all_incident_relations` | Get All Incident Relations | investigation | ✓ | `incidentId`(Incident ID, REQ), `$filter`(Search Query), `$orderby`(Order By), `$top`(Number of Incident Relations to Fetch), `$skipToken`(Skip Token) |
| `get_incident_relations` | Get Incident Relation | investigation | ✓ | `incidentId`(Incident ID, REQ), `relationName`(Relation Name, REQ) |
| `update_incident_relations` | Update Incident Relations | investigation | ✓ | `incidentId`(Incident ID, REQ), `relationName`(Relation Name, REQ), `resourceId`(Resource ID, REQ) |
| `delete_incident_relation` | Delete Incident Relation | investigation | ✓ | `incidentId`(Incident ID, REQ), `relationName`(Relation Name, REQ) |
| `create_incident_comment` | Create Incident Comment | investigation | ✓ | `incidentId`(Incident ID, REQ), `message`(Message, REQ) |
| `get_all_incident_comments` | Get All Incident Comments | investigation | ✓ | `incidentId`(Incident ID, REQ), `$filter`(Search Query), `$orderby`(Order By), `$top`(Number of Incident Comments to Fetch), `$skipToken`(Skip Token) |
| `get_incident_comment` | Get Incident Comment | investigation | ✓ | `incidentcommentId`(Incident Comment ID, REQ), `incidentId`(Incident ID, REQ) |
| `update_incident_comment` | Update Incident Comment | investigation | ✓ | `incidentcommentId`(Incident Comment ID, REQ), `incidentId`(Incident ID, REQ), `message`(Message, REQ) |
| `delete_incident_comment` | Delete Incident Comment | investigation | ✓ | `incidentcommentId`(Incident Comment ID, REQ), `incidentId`(Incident ID, REQ) |
| `create_watchlist` | Create Watchlist | investigation | ✓ | `watchlistAlias`(Watchlist Alias, REQ), `displayName`(Display Name, REQ), `itemsSearchKey`(Item Search key, REQ), `provider`(Provider, REQ), `source`(Source, REQ), `description`(Description), `etag`(ETag), `custom_attributes`(Custom Properties) |
| `get_all_watchlist` | Get All Watchlist | investigation | ✓ | `$skipToken`(Skip Token) |
| `get_watchlist` | Get Watchlist | investigation | ✓ | `watchlistAlias`(Watchlist Alias, REQ) |
| `update_watchlist` | Update Watchlist | investigation | ✓ | `watchlistAlias`(Watchlist Alias, REQ), `displayName`(Display Name, REQ), `itemsSearchKey`(Item Search key, REQ), `provider`(Provider, REQ), `source`(Source, REQ), `description`(Description), `etag`(ETag), `custom_attributes`(Custom Properties) |
| `delete_watchlist` | Delete Watchlist | investigation | ✓ | `watchlistAlias`(Watchlist Alias, REQ) |
| `create_watchlist_item` | Create Watchlist Item | investigation | ✓ | `watchlistAlias`(Watchlist Alias, REQ), `itemsKeyValue`(Item Key Value, REQ), `watchlistItemId`(Watchlist Item ID), `etag`(ETag), `custom_attributes`(Custom Properties) |
| `get_all_watchlist_items` | Get All Watchlist Items | investigation | ✓ | `watchlistAlias`(Watchlist Alias, REQ), `$skipToken`(Skip Token) |
| `get_watchlist_item` | Get Watchlist Item | investigation | ✓ | `watchlistItemId`(Watchlist Item ID, REQ), `watchlistAlias`(Watchlist Alias, REQ) |
| `update_watchlist_item` | Update Watchlist Item | investigation | ✓ | `watchlistItemId`(Watchlist Item ID, REQ), `watchlistAlias`(Watchlist Alias, REQ), `itemsKeyValue`(Item Key Value, REQ), `etag`(ETag), `custom_attributes`(Custom Properties) |
| `delete_watchlist_item` | Delete Watchlist Item | investigation | ✓ | `watchlistItemId`(Watchlist Item ID, REQ), `watchlistAlias`(Watchlist Alias, REQ) |

### `middesk`

version 1.0.0 — Middesk is an identity platform that automates business verification and underwrites decisions. It also provides data on businesses and noti…

- GitHub: connector-middesk
- Category: IT Service Management
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_business` | Create Business | investigation | ✓ | `name`(Name, REQ), `tin`(Tax Identification Number), `website`(Website), `phone_numbers`(Phone Numbers), `external_id`(External ID), `orders`(Orders), `tags`(Tags), `formation`(Formation), `names`(Names), `addresses`(Addresses, REQ), `people`(People) |
| `get_businesses_list` | Get Businesses List | investigation | ✓ | `page`(Offset), `per_page`(Limit) |
| `get_business` | Get Business | investigation | ✓ | `id`(Business ID, REQ) |
| `update_business` | Update Business | investigation | ✓ | `id`(Business ID, REQ), `name`(Name of Business), `status`(Status), `assignee_id`(Assignee ID), `website`(Website), `external_id`(External ID), `phone_numbers`(Phone Number), `addresses`(Addresses), `people`(People) |

### `misp`

version 2.2.0 — MISP connector allows to create MISP event, delete MISP event, add and delete attributes (IOCs), add and delete tags, into existing MISP eve…

- GitHub: connector-misp
- Category: Threat Intelligence
- Operations: 15

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_event` | Add Event | investigation | ✓ | `event_info`(Event Information, REQ), `date`(Date), `distribution`(Distribution), `threat_level`(Threat Level), `analysis`(Analysis Status), `published`(Published), `extends_uuid`(Extends Event), `additional_attributes`(Additional Attributes) |
| `get_events` | Search Events | investigation | ✓ | `searchJSONBody`(Search JSON Body, REQ) |
| `get_event` | Get Event | investigation | ✓ | `event_id`(Event ID, REQ) |
| `add_attributes_to_event` | Add Attributes to Event | investigation | ✓ | `event_id`(Event ID, REQ), `category`(Category, REQ), `type`(Attribute Type, REQ), `value`(Attribute Value, REQ), `distribution`(Attribute Distribution), `to_ids`(Use Attribute as an IDS Signature), `comment`(Comment) |
| `delete_event` | Delete Event | investigation | ✓ | `event_id`(Event ID, REQ) |
| `delete_attribute` | Delete Attribute from Event | investigation | ✓ | `attribute_id`(Attribute ID, REQ) |
| `run_search` | Run Search | investigation | ✓ | `controller`(Controller, REQ), `search_type`(Search Type, REQ) |
| `add_tag` | Add Tag | investigation | ✓ | `name`(Tag Name, REQ), `colour`(Color, REQ), `exportable`(Exportable), `hide_tag`(Hide Tag), `org_id`(Organisation ID), `user_id`(User ID) |
| `get_tags` | List All Tags | investigation | ✓ | — |
| `add_tag_to_event` | Add Tag to Event | investigation | ✓ | `event_id`(Event ID, REQ), `tag`(Tag, REQ) |
| `remove_tag_from_event` | Remove Tag from Event | investigation | ✓ | `event_id`(Event ID, REQ), `tag`(Tag, REQ) |
| `get_attribute_type` | Get Attribute Type | investigation | ✓ | — |
| `get_organisations` | Get Organisations | investigation | ✓ | — |
| `get_users` | Get Users | investigation | ✓ | — |
| `generic_rest_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Payload) |

### `mitre-attack`

version 2.0.2 — The MITRE ATT&CK knowledge base is used as a foundation for the development of specific threat models and methodologies. Connector helps to …

- GitHub: connector-mitre-attack
- Category: Information
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_mitre_data` | Get MITRE Data | — | ✓ | `modules`(Modules, REQ), `force_ingestion`(Force Ingestion) |
| `get_mitre_data_sample` | Get MITRE Sample Data | — | ✓ | — |

### `mobile-security-framework`

version 1.0.0 — Mobile Security Framework (MobSF) is an automated, all-in-one mobile application (Android/iOS/Windows) pen-testing, malware analysis and sec…

- GitHub: connector-mobile-security-framework
- Category: Threat Hunting and Search
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `upload_file` | Upload File | investigation | ✓ | `input`(Type, REQ), `value`(Reference ID, REQ) |
| `scan_file` | Scan File | investigation | ✓ | `scan_type`(Scan Type, REQ), `file_name`(File Name, REQ), `hash`(Hash, REQ), `re_scan`(Rescan File) |
| `delete_scan` | Delete Scan Result | investigation | ✓ | `hash`(Hash, REQ) |
| `display_recent_scans` | List Recent Scans | investigation | ✓ | `page`(Page), `page_size`(Page Size) |
| `get_app_scorecard` | Get App Scorecard | investigation | ✓ | `hash`(Hash, REQ) |
| `generate_pdf_report` | Generate PDF Report | investigation | ✓ | `hash`(Hash, REQ), `file_name`(File Name, REQ) |
| `generate_json_report` | Generate JSON Report | investigation | ✓ | `hash`(Hash, REQ) |
| `view_source_files` | View Source Files | investigation | ✓ | `file`(File Path, REQ), `hash`(Hash, REQ), `type`(File Type, REQ) |
| `compare_scan_results` | Compare Scan Results | investigation | ✓ | `hash1`(Hash of First Scan, REQ), `hash2`(Hash of Second Scan, REQ) |
| `suppress_by_rule` | Suppress by Rule | investigation | ✓ | `hash`(Hash, REQ), `type`(Type, REQ), `rule`(Rule, REQ) |
| `suppress_by_files` | Suppress by Files | investigation | ✗ | `hash`(Hash, REQ), `type`(Type, REQ), `rule`(Rule, REQ) |
| `view_suppressions` | List Suppressions | investigation | ✓ | `hash`(Hash, REQ) |
| `delete_suppressions` | Delete Suppressions | investigation | ✓ | `hash`(Hash, REQ), `type`(Type, REQ), `rule`(Rule, REQ), `kind`(Kind of Scan, REQ) |

### `netapp-ontap`

version 1.0.0 — ONTAP helps you create a storage infrastructure that reduces costs, accelerates critical workloads, and protects and secures data across you…

- GitHub: connector-netapp-ontap
- Category: Cloud Security
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_security_accounts` | Get Security Accounts | investigation | ✓ | `fields`(Fields), `max_records`(Limit), `return_records`(Return Records), `return_timeout`(Return Timeout), `order_by`(Sort Order) |
| `get_security_audit_messages` | Get Security Audit Messages | investigation | ✓ | `timestamp`(Timestamp), `state`(State), `application`(Application), `session_id`(Session ID), `scope`(Scope), `command_id`(Command ID), `index`(Index), `location`(Location), `fields`(Fields), `max_records`(Limit), `return_records`(Return Records), `return_timeout`(Return Timeout), `order_by`(Sort Order) |
| `get_security_roles` | Get Security Roles | investigation | ✓ | `fields`(Fields), `max_records`(Limit), `return_records`(Return Records), `return_timeout`(Return Timeout), `order_by`(Sort Order) |
| `update_user_password` | Update User Password | investigation | ✓ | `name`(Name, REQ), `max_records`(Password, REQ), `owner_name`(Owner Name), `owner_uuid`(Owner UUID) |

### `netbox`

version 1.0.0 — NetBox is the leading solution for modeling and documenting modern networks. By combining the traditional disciplines of IP address manageme…

- GitHub: connector-netbox
- Category: Asset Management
- Operations: 24

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_address_list` | Get IP Address List | investigation | ✓ | `id`(IDs), `address`(Address), `role`(Roles), `tag`(Tags), `q`(Search), `family`(Address Family), `status`(Status), `ordering`(Order by Field), `offset`(Offset), `limit`(Limit), `other_fields`(Other Fields) |
| `get_ip_address` | Get IP Address | investigation | ✓ | `id`(IP Address ID, REQ) |
| `update_ip_address` | Update IP Address | investigation | ✓ | `id`(IP Address ID, REQ), `patch_fields`(Fields to be updated, REQ) |
| `delete_ip_address` | Delete IP Address | investigation | ✓ | `id`(IP Address ID, REQ) |
| `get_prefix_list` | Get Prefix List | investigation | ✓ | `id`(IDs), `prefix`(Prefix), `site`(Sites), `role`(Roles), `tag`(Tags), `q`(Search Query), `family`(Address Family), `status`(Status), `ordering`(Order by Field), `offset`(Offset), `limit`(Limit), `other_fields`(Other Fields) |
| `get_prefix` | Get Prefix | investigation | ✓ | `id`(Prefix ID, REQ) |
| `update_prefix` | Update Prefix | investigation | ✓ | `id`(Prefix ID, REQ), `patch_fields`(Fields to be updated, REQ) |
| `delete_prefix` | Delete Prefix | investigation | ✓ | `id`(Prefix ID, REQ) |
| `get_vm_list` | Get Virtual Machines List | investigation | ✓ | `id`(IDs), `name`(Name), `site`(Sites), `role`(Roles), `tag`(Tags), `status`(Status), `q`(Search Query), `ordering`(Order by Field), `offset`(Offset), `limit`(Limit), `other_fields`(Other Fields) |
| `get_vm` | Get Virtual Machine | investigation | ✓ | `id`(VM ID, REQ) |
| `update_vm` | Update Virtual Machine | investigation | ✓ | `id`(VM ID, REQ), `patch_fields`(Fields to be updated, REQ) |
| `delete_vm` | Delete Virtual Machine | investigation | ✓ | `id`(VM ID, REQ) |
| `get_rack_list` | Get Rack List | investigation | ✓ | `id`(IDs), `name`(Name), `site`(Sites), `role`(Roles), `tag`(Tags), `type`(Type), `q`(Search Query), `status`(Status), `ordering`(Order by Field), `offset`(Offset), `limit`(Limit), `other_fields`(Other Fields) |
| `get_rack` | Get Rack | investigation | ✓ | `id`(Rack ID, REQ) |
| `update_rack` | Update Rack | investigation | ✓ | `id`(Rack ID, REQ), `patch_fields`(Fields to be updated, REQ) |
| `delete_rack` | Delete Rack | investigation | ✓ | `id`(Rack ID, REQ) |
| `get_device_list` | Get Devices List | investigation | ✓ | `id`(IDs), `name`(Name), `region_id`(Region IDs), `site`(Sites), `rack_id`(Rack IDs), `tag`(Tags), `device_type`(Device Type), `asset_tag`(Asset Tags), `tenant`(Tenants), `q`(Search Query), `status`(Status), `ordering`(Order by Field), `offset`(Offset), `limit`(Limit), `other_fields`(Other Fields) |
| `get_device` | Get Device | investigation | ✓ | `id`(Device ID, REQ) |
| `update_device` | Update Device | investigation | ✓ | `id`(Device ID, REQ), `device_type`(Type ID), `name`(Name), `description`(Description), `status`(Status), `site`(Site ID), `comments`(Comments), `rack`(Rack ID), `tags`(Tags), `other_fields`(Other Fields) |
| `delete_device` | Delete Device | investigation | ✓ | `id`(Device ID, REQ) |
| `get_cable_list` | Get Cables List | investigation | ✓ | `id`(IDs), `tag`(Tags), `type`(Type), `q`(Search Query), `status`(Status), `ordering`(Order by Field), `offset`(Offset), `limit`(Limit), `other_fields`(Other Fields) |
| `get_cable` | Get Cable | investigation | ✓ | `id`(Cable ID, REQ) |
| `update_cable` | Update Cable | investigation | ✓ | `id`(Cable ID, REQ), `patch_fields`(Fields to be updated, REQ) |
| `delete_cable` | Delete Cable | investigation | ✓ | `id`(Cable ID, REQ) |

### `netscaler-adc`

version 1.0.1 — The NetScaler appliance is an application switch which performs application-specific traffic analysis to intelligently distribute, optimize,…

- GitHub: connector-netscaler-adc
- Category: Firewall and Network Protection
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_acl_resource` | Create NetScaler ACL Resource | investigation | ✓ | `acl_type`(ACL Type, REQ), `aclname`(ACL Name, REQ), `srcip`(Source IP, REQ), `destip`(Destination IP), `aclaction`(ACL Action), `other_fields`(Other Fields) |
| `get_acl_resource` | Get NetScaler ACL Resource | investigation | ✓ | `acl_type`(ACL Type, REQ), `aclname`(ACL Name), `pagesize`(Page Size), `pageno`(Page Number), `other_fields`(Other Fields) |
| `change_acl_resource_state` | Change NetScaler ACL Resource State | investigation | ✓ | `acl_type`(ACL Type, REQ), `aclname`(ACL Name, REQ), `action`(Action, REQ) |
| `delete_acl_resource` | Delete NetScaler ACL Resource | investigation | ✓ | `acl_type`(ACL Type, REQ), `aclname`(ACL Name, REQ) |

### `netskope`

version 2.1.0 — Netskope provides smart cloud security which controls activities across any cloud service or website and provides 360-degree data and threat…

- GitHub: connector-netskope
- Category: Network Security
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts_list` | Get Alerts List | investigation | ✓ | `query`(Query), `type`(Alert Type), `acked`(Acknowledged Alerts), `starttime`(Start DateTime), `endtime`(End DateTime), `insertionstarttime`(Insertion Start DateTime), `insertionendtime`(Insertion End DateTime), `limit`(Limit), `offset`(Offset) |
| `get_events_list` | Get Events List | investigation | ✓ | `type`(Event Type, REQ), `query`(Query), `starttime`(Start DateTime), `endtime`(End DateTime), `insertionstarttime`(Insertion Start DateTime), `insertionendtime`(Insertion End DateTime), `limit`(Limit), `offset`(Offset) |
| `create_url_list` | Create URL List | investigation | ✓ | `name`(URL List Name, REQ), `type`(URL List Type, REQ), `urls`(URLs, REQ) |
| `get_url_list` | Get All URL List | investigation | ✓ | `pending`(Pending), `field`(Field) |
| `get_url_list_details` | Get URL List Details | investigation | ✓ | `url_list_id`(URL List ID, REQ) |
| `add_url_list` | Add URL List | investigation | ✓ | `url_list_id`(URL List ID, REQ), `type`(URL List Type), `urls`(URLs) |
| `apply_url_list` | Apply Pending URL Changes | investigation | ✓ | — |
| `update_url_list` | Update URL List | investigation | ✓ | `url_list_id`(URL List ID, REQ), `name`(URL List Name), `type`(URL List Type), `urls`(URLs) |
| `delete_url_list` | Delete URL List | investigation | ✓ | `url_list_id`(URL List ID, REQ) |
| `get_client_list` | Get Client List | investigation | ✓ | `filter`(Filter), `count`(Limit), `startIndex`(Offset) |
| `send_custom_request` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `nexthink`

version 1.0.0 — Nexthink is an automation and remediation platform which delivers visibility across all environments so IT teams can continuously improve th…

- GitHub: connector-nexthink
- Category: Endpoint Security
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `nexthink_query_language` | Run Query | investigation | ✓ | `query`(Query, REQ), `platform`(Platform, REQ) |

### `nist-nvd`

version 1.0.2 — The NIST National Vulnerability Database (NVD) is the U.S. government repository of standards based vulnerability management data represente…

- GitHub: connector-nist-nvd
- Category: Vulnerability Management
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_specific_cve_details` | Get Specific CVE ID Details | investigation | ✓ | `cveId`(CVE ID, REQ) |
| `cve_search` | Advance CVE Search | investigation | ✓ | `useCveId`(Filter By CVE ID), `useCpeName`(Filter by CPE Name), `useCweId`(Filter By CWE ID), `useCVSSv2`(Filter By CVSSv2 Metrics), `useCVSSv3`(Filter By CVSSv3 Metrics), `useSearchFlags`(Use Search Flags), `usePublishDate`(Filter By Publish Date), `useLastModDate`(Filter By Last Modified Date), `startIndex`(Page Index), `resultsPerPage`(Page Size) |
| `cve_search_by_keywords` | CVE Search by Keywords | investigation | ✓ | `keywordSearch`(Keyword(s), REQ), `startIndex`(Page Index), `resultsPerPage`(Page Size) |
| `get_cve_change_history` | Get CVE Change History | investigation | ✓ | `cveId`(CVE ID), `eventName`(Change Event Type), `useChangeDate`(Filter By Change Date), `startIndex`(Page Index), `resultsPerPage`(Page Size) |
| `cpe_search` | CPE Search | investigation | ✓ | `filterBy`(Filter By), `useLastModDate`(Use Last Modified Date), `startIndex`(Page Index), `resultsPerPage`(Page Size) |

### `ocr-space`

version 1.0.0 — The OCR API provides a simple way of parsing images and multi-page PDF documents (PDF OCR) and extract text results. This connector facilita…

- GitHub: connector-ocr-space
- Category: utilities
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `parse_image` | Parse Image | investigation | ✓ | `image_source`(Image Source Type, REQ) |

### `odbc`

version 1.0.0 — ODBC (Open Database Connectivity) allows applications to access data from different database systems (e.g., MySQL, SQL Server, Oracle). It e…

- GitHub: connector-odbc
- Category: Database
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `execute_query` | Execute Query | investigation | ✓ | `query`(Query, REQ) |

### `oletools`

version 1.0.0 — OLEtools is a suite of Python tools used for analyzing Microsoft OLE2 files (also known as Structured Storage, Compound File Binary Format, …

- GitHub: connector-oletools
- Category: ['Digital Forensics & Incident Response']
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `oleid` | Oleid | investigation | ✓ | `file_iri`(File IRI, REQ), `file_password`(File Password) |
| `oleobj` | Oleobj | investigation | ✓ | `file_iri`(File IRI, REQ), `file_password`(File Password) |
| `olevba` | Olevba | investigation | ✓ | `file_iri`(File IRI, REQ), `file_password`(File Password), `show_decoded_strings`(Show Decoded Strings), `deobfuscate`(Deobfuscate) |

### `openai`

version 4.0.0 — This integration supports interacting with OpenAI's powerful language model, ChatGPT from FortiSOAR workflows

- GitHub: connector-openai
- Category: ['LLM Provider']
- Operations: 43

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `chat_completions` | Ask a Question | miscellaneous | ✓ | `message`(Message, REQ), `model`(Model), `temperature`(Temperature), `top_p`(Top Probability), `max_tokens`(Max Tokens), `timeout`(Timeout), `other_fields`(Additional Inputs) |
| `chat_completions_new` | Chat Completions New | miscellaneous | ✓ | `message`(Message, REQ), `model`(Model), `temperature`(Temperature), `top_p`(Top Probability), `max_tokens`(Max Tokens), `timeout`(Timeout), `other_fields`(Additional Inputs) |
| `chat_conversation` | Converse With OpenAI | miscellaneous | ✓ | `messages`(Messages, REQ), `model`(Model), `temperature`(Temperature), `top_p`(Top Probability), `max_tokens`(Max Tokens), `timeout`(Timeout), `other_fields`(Additional Inputs) |
| `list_models` | List Available Models | miscellaneous | ✓ | — |
| `get_usage` | Get Tokens Usage | miscellaneous | ✓ | `date`(Date, REQ) |
| `count_tokens` | Get Token Count | miscellaneous | ✓ | `input_text`(Input Text, REQ), `model`(Model, REQ) |
| `create_assistant` | Create Assistant | miscellaneous | ✓ | `model`(Model, REQ), `name`(Name), `description`(Description), `instructions`(Instructions), `tools`(Tools), `tool_resources`(Tool Resources), `temperature`(Temperature), `top_p`(Top Probability), `metadata`(Metadata) |
| `list_assistants` | List Assistants | miscellaneous | ✓ | `order`(Sort Order), `after`(Starting ID), `before`(Ending ID), `limit`(Limit) |
| `get_assistant` | Get Assistant Details | miscellaneous | ✓ | `assistant_id`(Assistant ID, REQ) |
| `update_assistant` | Update Assistant | miscellaneous | ✓ | `assistant_id`(Assistant ID, REQ), `model`(Model), `name`(Name), `description`(Description), `instructions`(Instructions), `tools`(Tools), `tool_resources`(Tool Resources), `temperature`(Temperature), `top_p`(Top Probability), `metadata`(Metadata) |
| `delete_assistant` | Delete Assistant | miscellaneous | ✓ | `assistant_id`(Assistant ID, REQ) |
| `create_thread` | Create Thread | miscellaneous | ✓ | `messages`(Messages), `tool_resources`(Tool Resources), `metadata`(Metadata) |
| `get_thread` | Get Thread Details | miscellaneous | ✓ | `thread_id`(Thread ID, REQ) |
| `update_thread` | Update Thread | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `tool_resources`(Tool Resources), `metadata`(Metadata) |
| `delete_thread` | Delete Thread | miscellaneous | ✓ | `thread_id`(Thread ID, REQ) |
| `create_thread_message` | Create Thread Message | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `role`(Role, REQ), `content`(Content, REQ), `attachments`(Attachments), `metadata`(Metadata) |
| `list_thread_messages` | List Thread Messages | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `run_id`(Run ID), `order`(Sort Order), `after`(Starting ID), `before`(Ending ID), `limit`(Limit) |
| `get_thread_message` | Get Thread Message Details | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `message_id`(Message ID, REQ) |
| `update_thread_message` | Update Thread Message | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `message_id`(Message ID, REQ), `metadata`(Metadata) |
| `delete_thread_message` | Delete Thread Message | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `message_id`(Message ID, REQ) |
| `create_run` | Create Run | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `assistant_id`(Assistant ID, REQ), `model`(Model), `instructions`(Instructions), `additional_instructions`(Additional Instructions), `additional_messages`(Additional Messages), `tools`(Tools), `temperature`(Temperature), `top_p`(Top Probability), `metadata`(Metadata), `max_prompt_tokens`(Max Prompt Tokens), `other_fields`(Additional Inputs) |
| `list_runs` | List Runs | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `order`(Sort Order), `after`(Starting ID), `before`(Ending ID), `limit`(Limit) |
| `get_run` | Get Run Details | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `run_id`(Run ID, REQ) |
| `create_thread_and_run` | Create Thread and Run | miscellaneous | ✓ | `assistant_id`(Assistant ID, REQ), `thread`(Thread, REQ), `model`(Model), `instructions`(Instructions), `tools`(Tools), `tool_resources`(Tool Resources), `metadata`(Metadata), `temperature`(Temperature), `top_p`(Top Probability), `max_prompt_tokens`(Max Prompt Tokens), `other_fields`(Additional Inputs) |
| `update_run` | Update Run | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `run_id`(Run ID, REQ), `metadata`(Metadata) |
| `cancel_run` | Cancel Run | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `run_id`(Run ID, REQ) |
| `submit_tool_outputs_to_run` | Submit Tool Outputs To Run | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `run_id`(Run ID, REQ), `tool_outputs`(Tool Outputs, REQ) |
| `list_run_steps` | List Run Steps | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `run_id`(Run ID, REQ), `order`(Sort Order), `after`(Starting ID), `before`(Ending ID), `limit`(Limit) |
| `get_run_step` | Get Run Step Details | miscellaneous | ✓ | `thread_id`(Thread ID, REQ), `run_id`(Run ID, REQ), `step_id`(Step ID, REQ) |
| `create_vector_store` | Create Vector Store | miscellaneous | ✓ | `name`(Name, REQ), `file_ids`(File IDs), `expires_after`(Expiration Policy), `metadata`(Metadata) |
| `get_vector_store` | Get Vector Store Details | miscellaneous | ✓ | `vector_store_id`(Vector Store ID, REQ) |
| `create_vector_store_file` | Create Vector Store File | miscellaneous | ✓ | `vector_store_id`(Vector Store ID, REQ), `file_id`(File ID, REQ) |
| `create_vector_store_file_batch` | Create Vector Store File Batch | miscellaneous | ✓ | `vector_store_id`(Vector Store ID, REQ), `file_ids`(File IDs, REQ) |
| `get_vector_store_file_batch` | Get Vector Store File Batch | miscellaneous | ✓ | `vector_store_id`(Vector Store ID, REQ), `batch_id`(Batch ID, REQ) |
| `cancel_vector_store_file_batch` | Cancel Vector Store File Batch | miscellaneous | ✓ | `vector_store_id`(Vector Store ID, REQ), `batch_id`(Batch ID, REQ) |
| `create_speech` | Create Speech | miscellaneous | ✓ | `model`(Model, REQ), `input`(Input, REQ), `voice`(Voice, REQ), `file_path`(File Path, REQ), `response_format`(Audio Format), `speed`(Speed) |
| `create_transcription` | Create Transcription | miscellaneous | ✓ | `model`(Model, REQ), `file`(File, REQ), `language`(Language), `prompt`(Prompt), `temperature`(Temperature), `timestamp_granularities`(Timestamp Granularities) |
| `create_translation` | Create Translation | miscellaneous | ✓ | `model`(Model, REQ), `file`(File, REQ), `prompt`(Prompt), `temperature`(Temperature) |
| `list_files` | List Files | miscellaneous | ✓ | `purpose`(Purpose) |
| `get_file` | Get File Details | miscellaneous | ✓ | `file_id`(File ID, REQ) |
| `upload_file` | Upload File | miscellaneous | ✓ | `file`(File, REQ), `purpose`(Purpose, REQ) |
| `delete_files` | Delete File | miscellaneous | ✓ | `file_ids`(File IDs, REQ) |
| `get_llm_response` | Get LLM Response | investigation | ✓ | `assistant_id`(Assistant ID), `thread_id`(Thread ID), `role`(Role), `content`(Content, REQ), `attachments`(Attachments) |

### `openbao-vault`

version 1.0.0 — OpenBao Vault is an identity-based system for securely managing and distributing secrets such as API keys, passwords, and certificates.

- GitHub: connector-openbao-vault
- Category: Vault
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_credentials` | Get Credentials | investigation | ✓ | — |
| `get_credentials_details` | Get Credentials Details | investigation | ✓ | `secret_id`(Secret ID, REQ) |
| `get_credential` | Get Credential | investigation | ✓ | `secret_id`(Secret ID, REQ), `attribute_name`(Attribute Name, REQ) |

### `opencti`

version 1.0.2 — OpenCTI is an open threat intelligence platform where you can store, organize, visualize and share knowledge about cyber threats.

- GitHub: connector-opencti
- Category: Threat Intelligence
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_organization` | Create Organization | investigation | ✓ | `name`(Organization Name, REQ), `description`(Organization Description), `reliability`(Reliability) |
| `get_organizations` | Get Organizations | investigation | ✓ | `limit`(Limit), `end_cursor_id`(End Cursor ID) |
| `create_label` | Create Label | investigation | ✓ | `name`(Label Name, REQ) |
| `get_labels` | Get Labels | investigation | ✓ | `limit`(Limit), `end_cursor_id`(End Cursor ID) |
| `create_external_reference` | Create External Reference | investigation | ✓ | `url`(External Reference URL, REQ), `name`(Source Name, REQ) |
| `get_external_references` | Get External References | investigation | ✓ | `limit`(Limit), `end_cursor_id`(End Cursor ID) |
| `get_marking_definition` | Get Marking Definition | investigation | ✓ | `limit`(Limit), `end_cursor_id`(End Cursor ID) |
| `create_indicator` | Create Indicator | investigation | ✓ | `type`(Indicator Type, REQ), `value`(Indicator Value, REQ), `x_opencti_create_indicator`(Associate Indicator To Observable), `description`(Description), `score`(Score), `created_by`(Created By), `marking_id`(Marking Definition ID), `label_id`(Label ID), `external_reference_id`(External Reference ID) |
| `get_indicators` | Get Indicators | investigation | ✓ | `search_value`(Search By Value), `limit`(Limit), `end_cursor_id`(End Cursor ID), `type`(Indicator Type), `min_score`(Minimum Score), `max_score`(Maximum Score) |
| `delete_indicator` | Delete Indicator | investigation | ✓ | `indicator_id`(Indicator ID, REQ) |
| `add_indicator_field` | Add Indicator Field | investigation | ✓ | `indicator_id`(Indicator ID, REQ), `field`(Field, REQ), `field_id`(Field ID, REQ) |
| `update_indicator_field` | Update Indicator Field | investigation | ✓ | `indicator_id`(Indicator ID, REQ), `field`(Field, REQ), `field_value`(Field Value, REQ) |
| `remove_indicator_field` | Remove Indicator Field | investigation | ✓ | `indicator_id`(Indicator ID, REQ), `field`(Field, REQ), `field_id`(Field ID, REQ) |

### `openphish`

version 1.0.0 — OpenPhish helps to automatically identify zero-day phishing sites and provide comprehensive, actionable, real-time threat intelligence by us…

- GitHub: connector-openphish
- Category: Threat Intelligence
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators_for_latest_feed` | Get Indicators For Latest Feed  | investigation | ✗ | — |
| `get_indicators_for_24h_feed` | Get Indicators For 24 Hr Feed  | investigation | ✗ | — |

### `opswat-metadefender-core`

version 1.0.0 — OPSWAT MetaDefender Core prevents malicious file uploads on web applications that bypass sandboxes and other detection-based security soluti…

- GitHub: connector-opswat-metadefender-core
- Category: Malware Analysis
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `submit_file` | Submit File | investigation | ✓ | `submit_type`(Submission Type, REQ) |
| `get_hashcode_reputation` | Get Hashcode Reputation | investigation | ✓ | `hashcode`(HashCode, REQ) |
| `download_sanitized_files` | Download Sanitized Files | investigation | ✓ | `data_id`(Data ID, REQ) |

### `oracle-access-manager`

version 1.0.0 — Oracle Access Manager (OAM) is a robust identity and access management solution that provides secure authentication, single sign-on, and aut…

- GitHub: connector-oracle-access-manager
- Category: Identity and Access Management
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `retrieve_sessions` | Get Sessions List | investigation | ✓ | `clientIp`(Client IP), `sessionId`(Session ID), `userId`(User ID), `idStoreName`(ID Store Name), `isImpersonating`(Is Impersonating), `lastAccessTime`(Last Access Time), `updateTime`(Update Time), `expiryTime`(Expiry Time), `userAttributes`(User Attributes), `fromIndex`(Start Index), `pageSize`(Size) |
| `delete_sessions` | Delete Session | investigation | ✓ | `based_on`(Based On, REQ) |
| `get_user_status_by_user_id` | Get User Status by User ID | investigation | ✓ | `userId`(User ID, REQ) |
| `change_user_status_by_user_id` | Change User Status By User ID | investigation | ✓ | `userId`(User ID, REQ), `enabled`(Enable), `forcepwdchange`(Force Password Change), `unlocked`(Unlocked) |

### `oracle-db`

version 1.0.1 — Use Oracle Database connector to connect to a database and then query the database and retrieve data. supports Oracle v12c onward.

- GitHub: connector-oracle-db
- Category: Database
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `db_query` | Query DB | — | ✓ | `query_string`(Query String, REQ) |

### `otbase-inventory`

version 1.1.0 — Enterprise-grade OT asset management software. OTbase is the gold standard for large scale OT asset inventories. It inventories OT devices f…

- GitHub: connector-otbase-inventory
- Category: OT & IoT Security
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_devices_list` | Get Devices List | investigation | ✓ | `name`(Device Name), `locationid`(Location ID), `otsystemid`(OT System ID), `otsystem`(OT System Name), `ipaddress`(IP Address), `include`(Include Data), `networkid`(Network ID), `modified`(Modified DateTime), `count`(Limit), `offset`(Offset) |
| `get_device_details` | Get Device Details | investigation | ✓ | `device_id`(Device ID, REQ), `include`(Include Data) |
| `delete_device_details` | Delete Device Details | investigation | ✓ | `device_id`(Device ID, REQ) |
| `get_vulnerabilities_list` | Get Vulnerabilities List | investigation | ✓ | `priority`(Priority), `locationid`(Location ID), `count`(Limit), `offset`(Offset) |
| `get_vulnerability_details` | Get Vulnerability Details | investigation | ✓ | `cve_id`(CVE ID, REQ) |
| `get_data_flow` | Get Data Flow | investigation | ✓ | `last_seen`(Last Seen) |
| `get_network_list` | Get Network List | investigation | ✓ | `offset`(Offset) |
| `get_network_details` | Get Network Details | investigation | ✓ | `network_id`(Network ID, REQ) |

### `otrs`

version 1.0.3 — OTRS is a service management suite. OTRS connector provides functionality to create, modify, and search tickets.

- GitHub: connector-otrs
- Category: Service Management/Ticketing System
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_ticket` | Create Ticket | miscellaneous | ✓ | `title`(Title, REQ), `queue`(Queue, REQ), `state`(State, REQ), `priority`(Priority, REQ), `customer`(Customer User, REQ), `article_subject`(Article Subject, REQ), `article_body`(Article Body), `dynamicField`(Custom Field), `newTicketType`(Ticket-Type), `articleSenderType`(Article Sender Type), `newDynamicField`(DynamicField) |
| `search_tickets` | List Tickets | miscellaneous | ✓ | `state`(State, REQ), `ticket_title`(Title), `tickettype`(Type), `timeSpanMinutes`(Time Span Minutes) |
| `get_ticket` | Get Ticket | miscellaneous | ✓ | `ticket_id`(Ticket ID, REQ) |
| `update_ticket` | Update Ticket | miscellaneous | ✓ | `ticket_id`(Ticket ID, REQ), `title`(Title), `queue`(Queue), `state`(State), `priority`(Priority), `customer`(Customer User), `article_subject`(Article Subject), `article_body`(Article Body), `newTicketType`(Ticket-Type), `newDynamicField`(DynamicField), `oTRSArticle`(OTRS Article) |

### `paloalto-autofocus`

version 2.0.0 — Palo Alto Networks AutoFocus™ is a threat intelligence service that provides an interactive, graphical interface for analyzing and contextua…

- GitHub: connector-paloalto-autofocus
- Category: Threat Intelligence
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `indicatorValue`(IP Address, REQ), `includeTags`(Include Tags, REQ) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `indicatorValue`(Domain, REQ), `includeTags`(Include Tags, REQ) |
| `get_url_reputation` | Get URL Reputation | investigation | ✓ | `indicatorValue`(URL, REQ), `includeTags`(Include Tags, REQ) |
| `get_file_reputation` | Get File Reputation | investigation | ✓ | `indicatorValue`(File Hash, REQ), `includeTags`(Include Tags, REQ) |
| `get_threat_indicator_feed` | Get Threat Indicator Feed | investigation | ✓ | — |
| `samples_search` | Samples Searches | investigation | ✓ | `scope`(Scope, REQ), `query`(Filter Query), `operator`(Operator), `sort_field`(Sort By), `sort_order`(Sort Order), `size`(Page Size), `from`(Page Number), `type`(Type) |
| `get_sample_details` | Get Sample Details | investigation | ✓ | `public_tag_name`(Public Tag Name, REQ) |
| `top_tags_search` | Top Tags Search | investigation | ✓ | `scope`(Scope, REQ), `query`(Filter Query, REQ), `operator`(Operator), `tagScopes`(Tag Scopes), `size`(Page Size) |
| `get_tags_list` | Get Tags List | investigation | ✓ | `scope`(Scope), `query`(Filter Query), `sortBy`(Sort By), `order`(Sort Order), `pageSize`(Page Size), `pageNum`(Page Number) |
| `get_tag_details` | Get Tag Details | investigation | ✓ | `public_tag_name`(Public Tag Name, REQ) |
| `get_session_details` | Get Session Details | investigation | ✓ | `session_id`(Session ID, REQ) |

### `paloalto-cortex-xdr`

version 1.4.0 — Cortex XDR applies machine learning at cloud scale to rich network, endpoint, and cloud data, so you can quickly find and stop targeted atta…

- GitHub: connector-paloalto-cortex-xdr
- Category: Endpoint Security
- Operations: 32

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_incidents` | Fetch Incidents | investigation | ✓ | `filter.in.incident_id_list`(Incident ID List), `filter.gte.creation_time`(Created After), `filter.lte.creation_time`(Created Before), `filter.gte.modification_time`(Modified After), `filter.lte.modification_time`(Modified Before), `filter.in.alert_sources`(Alert Sources), `filter.eq.status`(Status), `filter.contains.description`(Description), `cursor.search_from`(Search From), `cursor.search_to`(Search To), `sort.field`(Sort by Field), `sort.keyword`(Sort by Order) |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `incident_id`(Incident ID, REQ), `alerts_limit`(Alerts Limit) |
| `update_incident` | Update Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `assigned_user_mail`(Assigned User Mail), `assigned_user_pretty_name`(Assigned User Pretty Name), `manual_severity`(Manual Severity), `status`(Status), `comment`(Comment), `resolve_comment`(Resolve Comment) |
| `insert_cef_alerts` | Insert CEF Alerts | investigation | ✓ | `alerts`(Alerts, REQ) |
| `insert_parsed_alerts` | Insert Parsed Alerts | investigation | ✓ | `alert_name`(Alert Name, REQ), `product`(Product, REQ), `vendor`(Vendor, REQ), `local_port`(Local Port, REQ), `remote_ip`(Remote IP, REQ), `remote_port`(Remote Port, REQ), `local_ip`(Local IP), `event_timestamp`(Event Timestamp), `severity`(Severity), `alert_description`(Alert Description), `action_status`(Action Status) |
| `isolate_endpoints` | Isolate Endpoints | investigation | ✓ | `isolate_endpoint`(Endpoint IDs, REQ), `incident_id`(Incident ID) |
| `unisolate_endpoints` | Unisolate Endpoints | investigation | ✓ | `endpoint_ids`(Endpoint IDs), `incident_id`(Incident ID) |
| `get_all_endpoints` | Get All Endpoints | investigation | ✓ | — |
| `get_endpoints` | Get Endpoints | investigation | ✓ | `filter.in.endpoint_id_list`(Endpoint ID List), `filter.in.dist_name`(Distribution Name), `filter.in.group_name`(Group Name), `filter.in.alias`(Alias), `filter.in.hostname`(Hostname), `filter.in.username`(Username), `filter.in.endpoint_status`(Endpoint Status), `filter.in.ip_list`(IP List), `filter.in.platform`(Platform), `filter.in.isolate`(Isolate), `filter.in.scan_status`(Scan Status), `filter.gte.first_seen`(First Seen After), `filter.lte.first_seen`(First Seen Before), `filter.gte.last_seen`(Last Seen After), `filter.lte.last_seen`(Last Seen Before), `cursor.search_from`(Search From), `cursor.search_to`(Search To), `sort.field`(Sort by Field), `sort.keyword`(Sort by Order) |
| `scan_endpoints` | Scan Endpoints | investigation | ✓ | `filter.in.endpoint_id_list`(Endpoint ID List), `filter.in.dist_name`(Distribution Name), `filter.in.group_name`(Group Name), `filter.in.alias`(Alias), `filter.in.hostname`(Hostname), `filter.in.username`(Username), `filter.in.ip_list`(IP List), `filter.in.platform`(Platform), `filter.in.isolate`(Isolate), `filter.in.scan_status`(Scan Status), `filter.gte.first_seen`(First Seen After), `filter.lte.first_seen`(First Seen Before), `filter.gte.last_seen`(Last Seen After), `filter.lte.last_seen`(Last Seen Before), `incident_id`(Incident ID) |
| `cancel_scan_endpoints` | Cancel Scan Endpoints | investigation | ✓ | `filter.in.endpoint_id_list`(Endpoint ID List), `filter.in.dist_name`(Distribution Name), `filter.in.group_name`(Group Name), `filter.in.alias`(Alias), `filter.in.hostname`(Hostname), `filter.in.username`(Username), `filter.in.ip_list`(IP List), `filter.in.platform`(Platform), `filter.in.isolate`(Isolate), `filter.in.scan_status`(Scan Status), `filter.gte.first_seen`(First Seen After), `filter.lte.first_seen`(First Seen Before), `filter.gte.last_seen`(Last Seen After), `filter.lte.last_seen`(Last Seen Before), `incident_id`(Incident ID) |
| `delete_endpoints` | Delete Endpoints | investigation | ✓ | `endpoint_id_list`(Endpoint ID List, REQ) |
| `get_policy` | Get Policy | investigation | ✓ | `endpoint_id`(Endpoint ID, REQ) |
| `get_device_violations` | Get Device Violations | investigation | ✓ | `filter.in.endpoint_id_list`(Endpoint ID List), `filter.in.vendor`(Vendor), `filter.in.vendor_id`(Vendor ID), `filter.in.product`(Product), `filter.in.product_id`(Product ID), `filter.in.serial`(Serial), `filter.in.hostname`(Hostname), `filter.in.username`(Username), `filter.in.type`(Type), `filter.in.ip_list`(IP List), `filter.in.violation_id_list`(Violation ID List), `filter.gte.timestamp`(Timestamp After), `filter.lte.timestamp`(Timestamp Before), `cursor.search_from`(Search From), `cursor.search_to`(Search To), `sort.field`(Sort by Field), `sort.keyword`(Sort by Order) |
| `get_distribution_version` | Get Distribution Version | investigation | ✓ | — |
| `create_distributions` | Create Distributions | investigation | ✓ | `name`(Name, REQ), `package_type`(Package Type, REQ), `description`(Description, REQ) |
| `get_distribution_status` | Get Distribution Status | investigation | ✓ | `distribution_id`(Distribution ID, REQ) |
| `get_distribution_url` | Get Distribution URL | investigation | ✓ | `distribution_id`(Distribution ID, REQ), `package_type`(Package Type, REQ) |
| `get_audit_management_log` | Get Audit Management Logs | investigation | ✓ | `filter.in.email`(Email), `filter.in.type`(Type), `filter.in.sub_type`(Sub Type), `filter.in.result`(Result), `filter.gte.timestamp`(Timestamp After), `filter.lte.timestamp`(Timestamp Before), `cursor.search_from`(Search From), `cursor.search_to`(Search To), `sort.field`(Sort by Field), `sort.keyword`(Sort by Order) |
| `get_audit_agent_report` | Get Audit Agent Report | investigation | ✓ | `filter.in.endpoint_id`(Endpoint ID), `filter.in.endpoint_name`(Endpoint Name), `filter.in.type`(Type), `filter.in.sub_type`(Sub Type), `filter.in.result`(Result), `filter.in.domain`(Domain), `filter.in.xdr_version`(xdr_version), `filter.in.category`(Category), `filter.gte.timestamp`(Timestamp After), `filter.lte.timestamp`(Timestamp Before), `cursor.search_from`(Search From), `cursor.search_to`(Search To), `sort.field`(Sort by Field), `sort.keyword`(Sort by Order) |
| `blacklist_files` | Blacklist Files | investigation | ✓ | `hash_list`(Hash List, REQ), `comment`(Comment), `incident_id`(Incident ID) |
| `whitelist_files` | Whitelist Files | investigation | ✓ | `hash_list`(Hash List, REQ), `comment`(Comment), `incident_id`(Incident ID) |
| `quarantine_files` | Quarantine Files | investigation | ✓ | `filter.in.endpoint_id_list`(Endpoint ID List, REQ), `file_path`(File Path, REQ), `file_hash`(File Hash, REQ) |
| `get_quarantine_status` | Get Quarantine Status | investigation | ✓ | `endpoint_id`(Endpoint ID, REQ), `file_hash`(File Hash, REQ), `file_path`(File Path, REQ) |
| `restore_file` | Restore File | investigation | ✓ | `file_hash`(File Hash, REQ), `endpoint_id`(Endpoint ID), `incident_id`(Incident ID) |
| `retrieve_file` | Retrieve File | investigation | ✓ | `filter.in.endpoint_id_list`(Endpoint ID List, REQ), `files`(Files, REQ), `file_path`(File Path, REQ), `filter.in.dist_name`(Distribution Name), `filter.in.group_name`(Group Name), `filter.in.alias`(Alias), `filter.in.hostname`(Hostname), `filter.in.ip_list`(IP List), `filter.in.platform`(Platform), `filter.in.isolate`(Isolate), `filter.gte.first_seen`(First Seen After), `filter.gte.last_seen`(Last Seen After), `filter.lte.first_seen`(First Seen Before), `filter.lte.last_seen`(Last Seen Before) |
| `retrieve_file_details` | Retrieve File Details | investigation | ✓ | `group_action_id`(Action ID, REQ) |
| `xql_query` | Execute XQL Query | investigation | ✓ | `query`(Query, REQ), `tenants`(Tenants ID), `from`(Start Datetime), `to`(End Datetime) |
| `get_query_result_by_query_id` | Get Query Results By Query ID | investigation | ✓ | `query_id`(Query ID, REQ), `pending_flag`(Pending Flag), `limit`(Limit) |
| `update_alerts` | Update Alerts | investigation | ✓ | `alert_ids`(Alert IDs, REQ), `severity`(Severity), `status`(Status), `comment`(Comment) |
| `get_alerts` | Get Alerts | investigation | ✓ | `alert_id_list`(Alert IDs), `severity`(Severity), `alert_source`(Alert Sources), `creation_time_gte`(Created After), `creation_time_lte`(Created Before), `sort_field`(Sort Field), `sort_order`(Sort Order), `search_from`(Search From), `search_to`(Search To) |
| `insert_simple_indicators` | Insert Simple Indicators | investigation | ✓ | `indicator`(Indicator, REQ), `type`(Type, REQ), `severity`(Severity, REQ), `expiry`(Expiry), `class`(Class), `comment`(Comment), `reputation`(Reputation), `reliability`(Reliability), `vendors`(Vendors), `validate`(Validate) |

### `paloalto-enterprise-dlp`

version 1.0.1 — Palo Alto Enterprise DLP discovers and protects company data across every data channel and repository.

- GitHub: connector-paloalto-enterprise-dlp
- Category: Network Security
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_report_details` | Get Report Details | investigation | ✓ | `report_id`(Report ID, REQ), `fetchSnippets`(Fetch Snippets) |

### `pcap-tools`

version 1.0.0 — PCAP Tools decodes a pcap file and converts it to human readable format

- GitHub: connector-pcap-tools
- Category: Network Analysis and Monitoring
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `pcap_to_json` | PCAP To JSON | investigation | ✓ | `file_iri`(File IRI, REQ) |

### `pdf-reader`

version 1.0.2 — PDF Reader connector reads PDF documents and extract text.

- GitHub: connector-pdf-reader
- Category: Document Reader
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `read_all_pages` | Read all Pages | investigation | ✓ | `type`(FortiSOAR File IRI/Filepath, REQ), `password`(Password) |
| `read_page` | Read a Page | investigation | ✓ | `type`(FortiSOAR File IRI/Filepath, REQ), `page_num`(Page Number, REQ), `password`(Password) |

### `pensando-policy-servicemanager`

version 1.0.1 — Pensando's Policy and Services Manager (PSM) is a distributed system that leverages an intent-based model to deliver network and security po…

- GitHub: connector-pensando-policy-servicemanager
- Category: Network Security
- Operations: 17

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `debug_remove_session_state` | Debug - Remove Session State | investigation | ✗ | — |
| `debug_reset_session_state` | Debug - Reset Session State | investigation | ✗ | — |
| `debug_expire_cookie` | Debug - Expire Auth Cookie | investigation | ✗ | — |
| `get_network_security_policies` | Get Network Security Policies | investigation | ✓ | — |
| `get_alerts` | Get Alerts | investigation | ✓ | — |
| `get_workloads` | Get Workloads | investigation | ✓ | — |
| `get_networks` | Get Networks | investigation | ✓ | — |
| `get_distributedservicecards` | Get Distributed Service Cards | investigation | ✓ | — |
| `enable_ipfix_export` | Enable IPFIX Export for Host | investigation | ✓ | `host_source_ip`(Host Source IP, REQ), `interval`(Interval, REQ), `template_interval`(Template Interval, REQ), `ipfix_collector_ip`(IPFIX Collector Destination IP, REQ), `ipfix_collector_gw_ip`(IPFIX Collector Destination Gateway IP), `ipfix_collector_protocol`(IPFIX Collector Destination Protocol, REQ), `ipfix_collector_port`(IPFIX Collector Destination Port, REQ) |
| `delete_ipfix_export` | Delete existing IPFIX Export for Host | investigation | ✓ | `host_source_ip`(Host Source IP, REQ), `ipfix_collector_ip`(IPFIX Collector Destination IP, REQ) |
| `enable_mirror_export` | Enable Mirror Traffic Export for Host | investigation | ✓ | `host_source_ip`(Host Source IP, REQ), `erspan_id`(ERSPAN ID, REQ), `packet_size`(Packet Size), `erspan_type`(ERSPAN Type, REQ), `erspan_collector_ip`(ERSPAN Collector Destination IP, REQ), `erspan_collector_gw_ip`(ERSPAN Collector Destination Gateway IP), `strip_vlan`(Strip VLAN, REQ), `erspan_match_dest_ip`(Match Destination IP Addresses), `erspan_match_protocols`(Match Protocols and Ports) |
| `delete_mirror_export` | Delete Existing Mirror Traffic Export for Host | investigation | ✓ | `host_source_ip`(Host Source IP, REQ), `erspan_collector_ip`(ERSPAN Collector Destination IP, REQ) |
| `isolate_host` | Isolate Host | containment | ✓ | `host_source_ip`(Host Source IP, REQ) |
| `unisolate_host` | Unisolate Host | remediation | ✓ | `host_source_ip`(Host Source IP, REQ) |
| `ioc_block_add_ip` | Add IOC IPs to Blocklist | containment | ✓ | `ioc_ip`(IOC IP Address(es), REQ) |
| `ioc_block_remove_ip` | Remove IOC IPs from Blocklist | remediation | ✓ | `ioc_ip`(IOC IP Address(es), REQ) |
| `ioc_delete_list` | Remove IOC Blocklist | remediation | ✓ | — |

### `plain-text-feed`

version 1.0.0 — Plain Text Feed can be used to fetch IP addresses from a text file from any publicly hosted url. <br/><br/>This connector has a dependency o…

- GitHub: connector-plain-text-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | — |

### `polar-security`

version 1.0.0 — An agentless platform that connects within minutes, Polar Security can automatically find unknown and sensitive data across the cloud.

- GitHub: connector-polar-security
- Category: Network Security
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_linked_vendors` | Get Linked Vendors | investigation | ✓ | — |
| `get_data_stores` | Get Data Stores | investigation | ✓ | `limit`(Limit), `page_size`(Page Size), `next_token`(Next Token) |
| `get_data_stores_summary` | Get Data Stores Summary | investigation | ✓ | — |
| `get_vendors_data_stores` | Get Vendors Data Stores | investigation | ✓ | `vendor_id`(Vendor ID, REQ), `limit`(Limit), `page_size`(Page Size), `next_token`(Next Token) |
| `get_data_store` | Get Data Store | investigation | ✓ | `store_id`(Store ID, REQ) |
| `get_vendor_accessible_data_store` | Get Vendor Accessible Data Store | investigation | ✓ | — |
| `apply_label` | Apply Label | investigation | ✓ | `label`(Label, REQ), `store_id`(Store ID, REQ) |

### `polyswarm`

version 1.0.0 — PolySwarm is a real-time threat intelligence from a crowdsourced network of security experts and antivirus companies. This connector facilit…

- GitHub: connector-polyswarm
- Category: Threat Intelligence
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_url_reputation` | Get URL Reputation | investigation | ✓ | `artifact`(URL, REQ) |
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `artifact`(IP, REQ) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `artifact`(Domain, REQ) |
| `get_file_reputation` | Get File Reputation | investigation | ✓ | `hash`(Hash, REQ) |
| `file_scan` | File Scan | investigation | ✓ | `input`(Type, REQ), `value`(Reference ID, REQ) |
| `file_rescan` | File Rescan | investigation | ✓ | `hash`(Hash, REQ) |

### `progress-whatsup-gold`

version 1.0.0 — WhatsUp Gold provides complete visibility into the status and performance of applications, network devices and servers in the cloud or on-pr…

- GitHub: connector-progress-whatsup-gold
- Category: Network Security
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_device_attributes` | Get Device Attributes | investigation | ✓ | `device_id`(Device ID, REQ), `names`(Attribute Names), `limit`(Limit), `pageId`(Page ID) |
| `get_device_groups` | Get Device Groups | investigation | ✓ | `device_id`(Device ID, REQ), `view`(View), `limit`(Limit), `pageId`(Page ID) |
| `get_device_monitors` | Get Device Monitors | investigation | ✓ | `device_id`(Device ID, REQ), `limit`(Limit), `pageId`(Page ID) |
| `get_device_polling_configuration` | Get Device Polling Configuration | investigation | ✓ | `device_id`(Device ID, REQ) |
| `get_device_summary` | Get Device Summary | investigation | ✓ | `device_id`(Device ID, REQ) |
| `get_device_overview` | Get Device Overview | investigation | ✓ | `device_id`(Device ID, REQ) |
| `get_device_report` | Get Device Report | investigation | ✓ | `report_type`(Report Type, REQ), `device_id`(Device ID, REQ), `range`(Report Duration), `limit`(Limit), `pageId`(Page ID) |

### `proofpoint-tap`

version 1.0.2 — Perform actions like get events, get campaign details and get forensic information using Proofpoint TAP

- GitHub: connector-proofpoint-tap
- Category: Information
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_clicks_blocked_event` | Get Blocked Malicious URL Events | investigation | ✓ | `interval`(Time Interval, REQ), `format`(Format), `threat_type`(Threat Type), `threat_status`(Threat Status) |
| `get_clicks_permitted_event` | Get Permitted Malicious URL Events | investigation | ✓ | `interval`(Time Interval, REQ), `format`(Format), `threat_type`(Threat Type), `threat_status`(Threat Status) |
| `get_messages_blocked_event` | Get Blocked Threat Message Events | investigation | ✓ | `interval`(Time Interval, REQ), `format`(Format), `threat_type`(Threat Type), `threat_status`(Threat Status) |
| `get_clicks_delivered_event` | Get Delivered Threat Message Events | investigation | ✓ | `interval`(Time Interval, REQ), `format`(Format), `threat_type`(Threat Type), `threat_status`(Threat Status) |
| `get_all_events` | Get All Events | investigation | ✓ | `interval`(Time Interval, REQ), `format`(Format), `threat_type`(Threat Type), `threat_status`(Threat Status) |
| `get_issues_event` | Get Events for All Issues | investigation | ✓ | `interval`(Time Interval, REQ), `format`(Format), `threat_type`(Threat Type), `threat_status`(Threat Status) |
| `get_campaign_details` | Get Campaign Details | — | ✓ | `campaign_id`(Campaign ID, REQ) |
| `get_forensic` | Get Forensic Details | — | ✓ | `id`(ID Type, REQ), `value`(Value, REQ), `include_campaign_forensics`(Include Campaign Forensics) |

### `proofpoint-threat-response`

version 1.0.0 — Proofpoint Threat Response is a solution designed to help organizations manage and respond to cybersecurity threats. It provides tools and f…

- GitHub: connector-proofpoint-threat-response
- Category: Threat Response
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_list` | Get Indicators List | investigation | ✓ | `list_id`(List ID, REQ) |
| `add_to_list` | Add Indicators | investigation | ✓ | `list_id`(List ID, REQ), `indicator`(Indicator, REQ), `description`(Comment), `expiration`(Expiration) |
| `block_ip` | Block IP Addresses | containment | ✓ | `indicator`(IP Address, REQ), `list_id`(Blacklist ID, REQ), `expiration`(Expiration) |
| `block_domain` | Block Domain | containment | ✓ | `indicator`(Domain, REQ), `list_id`(Blacklist ID, REQ), `expiration`(Expiration) |
| `block_url` | Block URL | containment | ✓ | `indicator`(URL, REQ), `list_id`(Blacklist ID, REQ), `expiration`(Expiration) |
| `block_hash` | Block File Hash | containment | ✓ | `indicator`(File Hash, REQ), `list_id`(Blacklist ID, REQ), `expiration`(Expiration) |
| `search_indicator` | Search Indicator | investigation | ✓ | `filter`(Filter), `list_id`(Blacklist ID, REQ) |
| `delete_indicator` | Delete Indicator | investigation | ✓ | `list_id`(List ID, REQ), `indicator_id`(Indicator ID, REQ) |
| `get_incident` | Get Incident By ID | investigation | ✓ | `incident_id`(Incident ID, REQ), `expand_events`(Expand Events, REQ) |
| `get_incidents` | Get Incidents List | investigation | ✓ | `state`(State), `created_after`(Create After), `created_before`(Created Before), `closed_after`(Closed After), `closed_before`(Closed Before), `expand_events`(Expand Events), `limit`(Limit) |
| `add_comment_to_incident` | Add Comment To Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `comment`(Comment, REQ), `description`(Description) |
| `update_comment_to_incident` | Update Comment To Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `comment`(Comment), `description`(Description) |
| `add_user_to_incident` | Add User To Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `targets`(Targets, REQ), `attackers`(Attackers, REQ) |
| `ingest_alert` | Ingest Alert | investigation | ✓ | `json_version`(JSON Version, REQ), `post_url_id`(Post URL ID), `attacker`(Attacker), `classification`(Classification), `cnc_hosts`(CNC Hosts), `detector`(Detector), `email`(Email), `forensics_hosts`(Forensics Hosts), `link_attribute`(Link Attribute), `severity`(Severity), `summary`(Summary), `target`(Target), `threat_info`(Threat Info), `custom_fields`(Custom Fields) |
| `close_incident` | Close Incident | investigation | ✓ | `incident_id`(Incident ID, REQ), `comment`(Comment, REQ), `description`(Description, REQ) |
| `verify_quarantine` | Verify Quarantine | investigation | ✓ | `message_id`(Message ID, REQ), `time`(Time, REQ), `recipient`(Recipient, REQ) |

### `proofpoint-trap`

version 1.1.0 — Perform actions like Get incident details, Retrieve incidents, Close Incidents and Create Alert from JSON source using Proofpoint TRAP

- GitHub: connector-proofpoint-trap
- Category: ['Case Management', 'Threat Intelligence']
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_alert_from_json_source` | Create Alert from JSON Source | investigation | ✓ | `alertSourceID`(Alert Source ID, REQ), `data`(Data, REQ) |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `incidentID`(Incident ID, REQ) |
| `get_incidents` | Get Incidents | investigation | ✓ | `state`(State, REQ), `createdAfterDate`(Created After Date), `createdBeforeDate`(Created Before Date), `emailMessageID`(Email Message ID) |
| `close_incidents` | Close Incidents | investigation | ✓ | `incidentIDs`(Incident IDs, REQ), `closeSummary`(Close Summary, REQ), `closeDetail`(Close Detail, REQ) |
| `execute_api_request` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `proxmox`

version 1.0.0 — Proxmox VE (Virtual Environment) is an open-source server virtualization platform used to manage virtual machines, containers, storage, netw…

- GitHub: connector-proxmox
- Category: Compute Platform
- Operations: 27

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_version` | Get Version | investigation | ✓ | — |
| `get_next_vmid` | Get Next VMID | investigation | ✓ | — |
| `clone_vm` | Clone VM | investigation | ✓ | `node`(Node, REQ), `vmid`(Template VMID, REQ), `newid`(New VMID, REQ), `name`(Name, REQ), `storage`(Storage), `full`(Full Clone), `timeout`(Clone wait timeout (seconds)) |
| `create_container` | Create Container | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ), `hostname`(Hostname, REQ), `ostemplate`(OS Template, REQ), `cores`(Cores), `memory`(Memory (MB)), `rootfs`(Root FS, REQ), `net0`(Network, REQ), `password`(Root Password), `swap`(Swap (MB)), `nameserver`(Nameserver), `unprivileged`(Unprivileged), `features`(Features) |
| `config_container` | Configure Container | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ), `body_params`(Body Parameters, REQ) |
| `config_vm` | Configure VM | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ), `body_params`(Body Parameters, REQ) |
| `resize_vm_disk` | Resize VM Disk | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ), `disk`(Disk), `target_gb`(Target size (GB)), `assume_current_gb`(Assume current size (GB)), `size`(Size), `timeout`(Resize wait timeout (seconds)) |
| `update_vm_cloudinit` | Update VM Cloud-Init | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ) |
| `start_vm` | Start VM | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ) |
| `stop_vm` | Stop VM | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ) |
| `start_container` | Start Container | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ) |
| `stop_container` | Stop Container | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ) |
| `destroy_vm` | Destroy VM | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ), `purge`(Purge) |
| `destroy_container` | Destroy Container | investigation | ✓ | `node`(Node, REQ), `vmid`(VMID, REQ), `force`(Force) |
| `list_vms` | List VMs | investigation | ✓ | `node`(Node), `include_config`(Include config) |
| `list_containers` | List Containers | investigation | ✓ | `node`(Node), `include_config`(Include config) |
| `get_vm_config` | Get VM Config | investigation | ✓ | `node`(Node), `vmid`(VMID, REQ) |
| `get_container_config` | Get Container Config | investigation | ✓ | `node`(Node), `vmid`(VMID, REQ) |
| `get_task_status` | Get Task Status | investigation | ✓ | `node`(Node), `upid`(UPID, REQ) |
| `get_nodes` | Get Nodes | investigation | ✓ | — |
| `get_cluster_resources` | Get Cluster Resources | investigation | ✓ | `type`(Type Filter) |
| `get_vm_status` | Get VM Status | investigation | ✓ | `node`(Node), `vmid`(VMID, REQ) |
| `get_container_status` | Get Container Status | investigation | ✓ | `node`(Node), `vmid`(VMID, REQ) |
| `get_node_status` | Get Node Status | investigation | ✓ | `node`(Node) |
| `get_storage_status` | Get Storage Status | investigation | ✓ | `node`(Node), `storage`(Storage, REQ) |
| `get_storage_content` | Get Storage Content | investigation | ✓ | `node`(Node), `storage`(Storage, REQ), `content`(Content Filter) |
| `api_request` | API Request (Generic) | investigation | ✓ | `method`(Method, REQ), `url_path`(URL Path, REQ), `body`(Body (form)), `body_json`(Body (JSON)) |

### `pulsedive`

version 1.0.0 — Pulsedive is a free threat intelligence platform that allows users to search, scan, and enrich IP addresses, URLs, domains, and other Indica…

- GitHub: connector-pulsedive
- Category: ['Threat Intelligence']
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `indicator`(IP Address, REQ) |
| `get_links_of_indicator` | Get Links of Indicator | investigation | ✓ | `indicator`(Indicator, REQ) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `indicator`(Domain Name, REQ) |

### `pure-storage-flasharray`

version 1.0.0 — Pure Storage is a leading provider of enterprise data storage solutions. It is specialize in all-flash storage arrays, delivering high-perfo…

- GitHub: connector-pure-storage-flasharray
- Category: Storage
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alert List | investigation | ✓ | `based_on`(Based on), `filter`(Filter Query), `sort`(Sort Fields), `flagged`(Flagged), `total_item_count`(Total Count), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_arrays` | Get Array List | investigation | ✓ | `based_on`(Based on), `filter`(Filter Query), `fqdns`(FQDNs), `sort`(Sort Fields), `total_item_count`(Total Count), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_controllers` | Get Controller List | investigation | ✓ | `names`(Controller Names), `filter`(Filter Query), `sort`(Sort Fields), `total_item_count`(Total Count), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_directories` | Get Directory List | investigation | ✓ | `based_on`(Based on), `filesystem_filter`(File System Filter), `filter`(Filter Query), `sort`(Sort Fields), `destroyed`(Destroyed), `total_item_count`(Total Count), `total_only`(Total Only), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_drives` | Get Drive List | investigation | ✓ | `names`(Drive Names), `filter`(Filter Query), `sort`(Sort Fields), `total_item_count`(Total Count), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_audits` | Get Audit List | investigation | ✓ | `based_on`(Based on), `filter`(Filter Query), `sort`(Sort Fields), `total_item_count`(Total Count), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_volumes` | Get Volume List | investigation | ✓ | `based_on`(Based on), `filter`(Filter Query), `sort`(Sort Fields), `destroyed`(Destroyed), `total_item_count`(Total Count), `total_only`(Total Only), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_protection_groups` | Get Protection Group List | investigation | ✓ | `names`(Protection Group Names), `filter`(Filter Query), `sort`(Sort Fields), `destroyed`(Destroyed), `total_item_count`(Total Count), `total_only`(Total Only), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |
| `get_sessions` | Get Session List | investigation | ✓ | `based_on`(Based on), `filter`(Filter Query), `sort`(Sort Fields), `total_item_count`(Total Count), `continuation_token`(Continuation Token), `offset`(Offset), `limit`(Limit) |

### `qianxin-threat-intel`

version 1.1.0 — QiAnxin Threat Intelligence Center provides automate processing and the manual operation of top security research teams to provide users wit…

- GitHub: connector-qianxin-threat-intel
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `ip_reputation` | Get IP Reputation | investigation | ✓ | `reputation_of`(Reputation of, REQ) |
| `file_reputation` | Get File Reputation | investigation | ✓ | `advance`(Advanced File Reputation), `reputation_of`(Reputation of, REQ) |
| `get_loss_detection_data` | Get Loss Detection Data | investigation | ✓ | `request_of`(Request of, REQ), `ignore_url`(Ignore URL), `ignore_port`(Ignore Port), `ignore_top`(Ignore Top) |

### `qradar`

version 1.6.2 — IBM QRadar is an enterprise security information and event management (SIEM) product. Fortinet FortiSOAR connector for IBM QRadar allows use…

- GitHub: connector-qradar
- Category: Analytics and SIEM
- Operations: 23

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_offenses` | Get Offenses from QRadar | investigation | ✓ | `filter_string`(Filter String, REQ) |
| `query_qradar` | Make an Ariel Query to QRadar | investigation | ✓ | `search_string`(Ariel Search String, REQ) |
| `get_closing_reasons` | Get Offense Closing Reasons | remediation | ✓ | — |
| `get_offense_type` | Get Offense Types | investigation | ✓ | — |
| `get_notes` | Get Offense Notes | remediation | ✓ | `offense_id`(Offense ID, REQ) |
| `close_offense` | Close Offense | remediation | ✓ | `offense_id`(Offense ID, REQ), `offense_close_id`(Offense Closing Reason - ID, REQ), `closure_note`(Closure Note) |
| `add_notes` | Create Note | remediation | ✓ | `offense_id`(Offense ID, REQ), `closure_note`(Closure Note, REQ) |
| `get_events_related_to_offense` | Get Events Related to an Offense | investigation | ✓ | `offense_id`(QRadar Offense ID, REQ), `start_time`(Offense Start Time, REQ), `last_updated_time`(Offense Last Update Time, REQ), `max_results`(Max Events to return) |
| `get_source_ip` | Get Source IP Addresses | investigation | ✓ | `source_address_ids`(Source Address Ids, REQ) |
| `get_destination_ip` | Get Destination IP Addresses | investigation | ✓ | `destination_address_ids`(Destination Address Ids, REQ) |
| `invoke_api` | Invoke QRadar REST API | investigation | ✓ | `endpoint`(Endpoint, REQ), `method`(Request Method, REQ), `headers`(Headers in json format) |
| `handle_reference_set_value` | Manipulate Reference Set Content | investigation | ✓ | `method`(Request Method, REQ) |
| `get_assets_properties` | Get Assets Properties | investigation | ✓ | `max_results`(Limit), `filter_string`(Filter), `query.fields`(Fields) |
| `get_assets` | Get Assets | investigation | ✓ | `filter_string`(Filter), `max_results`(Limit), `query.fields`(Fields), `query.sort`(Sort) |
| `update_asset` | Update Asset | investigation | ✓ | `path.asset_id`(Asset ID, REQ), `body.asset`(Asset Properties, REQ), `content_type`(Content Type) |
| `get_cases` | Get Cases | investigation | ✓ | `query.fields`(Fields), `filter_string`(Filter), `max_results`(Limit) |
| `create_case` | Create Case | investigation | ✓ | `body.case`(Case Properties, REQ), `content_type`(Content Type) |
| `get_reference_tables` | Get Reference Tables | investigation | ✓ | `filter_string`(Filter), `max_results`(Limit), `query.fields`(Fields) |
| `delete_reference_table` | Delete or Purge Reference Table | investigation | ✓ | `path.name`(Reference Table Name, REQ), `query.purge_only`(Purge Table), `query.fields`(Fields), `query.namespace`(Namespace) |
| `get_table_elements` | Get Table Elements | investigation | ✓ | `path.name`(Reference Table Name, REQ), `max_results`(Limit), `query.fields`(Fields), `query.namespace`(Namespace) |
| `add_table_element` | Add or Update Table Element | investigation | ✓ | `path.name`(Reference Table Name, REQ), `query.outer_key`(Outer Key, REQ), `query.inner_key`(Inner Key, REQ), `query.value`(Value, REQ), `query.domain_id`(Domain ID), `query.source`(Element Source), `query.fields`(Fields), `query.namespace`(Namespace) |
| `delete_table_element` | Delete Table Element | investigation | ✓ | `path.name`(Reference Table Name, REQ), `path.outer_key`(Outer Key, REQ), `path.inner_key`(Inner Key, REQ), `query.value`(value, REQ), `query.domain_id`(Domain ID), `query.fields`(Fields), `query.namespace`(Namespace) |
| `fetch_offenses` | Fetch Offenses from QRadar | investigation | ✓ | `filter_string`(Filter String, REQ), `start_time`(Created After, REQ) |

### `qrcode-tools`

version 1.0.2 — QR Code Tools helps users working with QR and Bar codes

- GitHub: connector-qrcode-tools
- Category: Utilities
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `read_qr_code` | Read QR Code | investigation | ✓ | `type`(Input Type, REQ) |

### `qualys-fim`

version 1.0.0 — Qualys File Integrity Monitoring (FIM) is a highly scalable cloud app that enables a simple way to monitor critical files, directories, and …

- GitHub: connector-qualys-fim
- Category: IT Services
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_events` | Get Events | investigation | ✓ | `filter`(Filter), `sort`(Sort), `incidentContext`(Incident Context), `incidentIds`(Incident IDs), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `get_event_details` | Get Event Details | investigation | ✓ | `eventId`(Event ID, REQ) |
| `create_manual_incident ` | Create Manual Incident | investigation | ✓ | `filter`(Filter, REQ), `name`(Incident Name, REQ), `comment`(Comment), `reviewers`(Reviewers Name), `userInfo`(User Information) |
| `approve_incident ` | Approve Incident | investigation | ✓ | `incidentId`(Incident ID, REQ), `approvalStatus`(Approval Status, REQ), `changeType`(Change Type, REQ), `comment`(Comment, REQ), `dispositionCategory`(Disposition Category, REQ) |
| `get_incidents` | Get Incidents | investigation | ✓ | `filter`(Filter), `sort`(Sort), `attributes`(Attributes), `searchAfter`(Search After), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `fetch_incident_events` | Fetch Incident Events | investigation | ✓ | `incidentId`(Incident ID, REQ), `filter`(Filter), `sort`(Sort), `attributes`(Attributes), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `get_assets` | Get Assets | investigation | ✓ | `attributes`(Attributes), `filter`(Filter), `includeTagData`(Include Tag Data), `searchAfter`(Search After), `notSentEventsForHours`(Not Sent Events For Hours), `sort`(Sort), `pageNumber`(Page Number), `pageSize`(Page Size) |

### `qualys-web-application-scanner`

version 2.0.0 — Qualys Web Application Scanning (WAS) is a robust cloud-based application security product that continuously discovers, detects, and catalog…

- GitHub: connector-qualys-web-application-scanner
- Category: Vulnerability and Risk Management
- Operations: 22

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `scan_count` | Get Scan Count | investigation | ✓ | `id`(Scan ID), `name`(Scan Name), `webApp.name`(Web App Name), `webApp.id`(Web App ID), `webApp.tags.id`(Web App Tag ID), `reference`(Reference), `launchedDate`(Launch Date), `type`(Type), `mode`(Mode), `status`(Status), `authStatus`(Authentication Status), `resultsStatus`(Result Status) |
| `search_scans` | Search Scans | investigation | ✓ | `id`(Scan ID), `name`(Scan Name), `webApp.name`(Web App Name), `webApp.id`(Web App ID), `webApp.tags.id`(Web App Tag ID), `reference`(Reference), `launchedDate`(Launch Date), `type`(Type), `mode`(Mode), `status`(Status), `authStatus`(Authentication Status), `resultsStatus`(Result Status), `limitResults`(Limit), `startFromOffset`(Offset) |
| `get_scan_details` | Get Scan Details | investigation | ✓ | `scan_id`(Scan ID, REQ) |
| `launch_scans` | Launch Scans | investigation | ✓ | `scan_name`(Scan Name, REQ), `scan_type`(Scan Type, REQ), `web_app_id`(Web App ID, REQ), `web_app_auth_record`(Target Web App Auth Record, REQ), `scanner_appliance`(Target Scanner Appliance Type, REQ), `profile_id`(Scan Profile ID, REQ) |
| `retrieve_scan_status` | Get Scan Status | investigation | ✓ | `scan_id`(Scan ID, REQ) |
| `retrieve_scan_results` | Get Scan Results | investigation | ✓ | `scan_id`(Scan ID, REQ) |
| `delete_scan` | Delete Scan | investigation | ✓ | `scan_id`(Scan ID, REQ) |
| `count_webapp` | Get Web Applications Count | investigation | ✓ | `id`(ID), `name`(Name), `url`(URL), `tags.id`(Tags ID), `tags.name`(Tags Name), `createdDate`(Created Date), `updatedDate`(Updated Date), `isScheduled`(Scheduled), `isScanned`(Scanned), `lastScan.status`(Last Scan Status), `lastScan.date`(Last Scan Date) |
| `search_webapp` | Search Web Applications | investigation | ✓ | `id`(ID), `name`(Name), `url`(URL), `tags.id`(Tags ID), `tags.name`(Tags Name), `createdDate`(Created Date), `updatedDate`(Updated Date), `isScheduled`(Scheduled), `isScanned`(Scanned), `lastScan.status`(Last Scan Status), `lastScan.date`(Last Scan Date), `limitResults`(Limit), `startFromOffset`(Offset), `verbose`(Verbose) |
| `get_webapp_details` | Get Web Application Details | investigation | ✓ | `id`(App ID, REQ) |
| `create_web_app` | Create Web Application | investigation | ✓ | `name`(Web App Name, REQ), `url`(Web App URL, REQ), `id`(Web App Auth Record ID) |
| `delete_webapp` | Delete Web Applications | investigation | ✓ | `app_id`(App ID, REQ) |
| `search_reports` | Search Reports | investigation | ✓ | `id`(ID), `name`(Name), `tags.id`(Tags ID), `tags.name`(Tags Name), `creationDate`(Creation Date), `type`(Type), `format`(Format), `status`(Status), `limitResults`(Limit), `startFromOffset`(Offset) |
| `download_report` | Download Report | investigation | ✓ | `report_id`(Report ID, REQ) |
| `search_option_profiles` | Search Option Profiles | investigation | ✓ | `id`(ID), `name`(Name), `tags.id`(Tags ID), `tags.name`(Tags Name), `createdDate`(Created Date), `updatedDate`(Updated Date), `usedByWebApps`(Used By Web Apps), `usedBySchedules`(Used By Schedules), `owner.id`(Owner ID), `owner.name`(Owner Name), `owner.username`(Owner Username), `limitResults`(Limit), `startFromOffset`(Offset) |
| `search_schedule` | Search Schedule | investigation | ✓ | `id`(ID), `name`(Name), `owner.id`(Owner ID), `createdDate`(Created Date), `updatedDate`(Updated Date), `active`(Active), `type`(Type), `webApp.name`(Web App Name), `webApp.id`(Web App ID), `webApp.tags.id`(Web App Tag ID), `lastScan.status`(Last Scan Status), `lastScan.launchedDate`(Last Scan Launch Date), `multi`(Multi), `limitResults`(Limit), `startFromOffset`(Offset) |
| `get_schedule_details` | Get Schedule Details | investigation | ✓ | `schedule_id`(Schedule ID, REQ) |
| `search_tags` | Search Tags | investigation | ✓ | `id`(ID), `name`(Name), `parent`(Parent ID), `criticalityScore`(Criticality Score), `ruleType`(Rule Type), `provider`(Provider), `color`(Color), `limitResults`(Limit), `startFromOffset`(Offset) |
| `create_tag` | Create Tag | investigation | ✓ | `name`(Tag Name, REQ), `criticalityScore`(Criticality Score), `ruleType`(Rule Type), `ruleText`(Rule Text), `provider`(Provider), `color`(Color), `children`(Child tags) |
| `update_tag` | Update Tag | investigation | ✓ | `id`(Tag ID, REQ), `name`(Tag Name), `criticalityScore`(Criticality Score), `ruleType`(Rule Type), `ruleText`(Rule Text), `color`(Color) |
| `delete_tag` | Delete Tag | investigation | ✓ | `tag_id`(Tag ID, REQ) |
| `search_users` | Search Users | investigation | ✓ | `id`(User ID), `username`(Username), `limitResults`(Limit), `startFromOffset`(Offset) |

### `quttera`

version 1.0.0 — Quttera helps to scan website/domain for malware, ssl and open ports. This connector facilitates automated operations like scan website, get…

- GitHub: connector-quttera
- Category: Threat Intelligence
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `start_url_scan` | Start URL Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_status_of_url_scan` | Get Status of URL Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_report_of_url_scan` | Get Report of URL Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `start_ssl_scan` | Start SSL Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_status_of_ssl_scan` | Get Status of SSL Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_report_of_ssl_scan` | Get Report of SSL Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `start_integrity_scan` | Start Integrity Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_status_of_integrity_scan` | Get Status of Integrity Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_report_of_integrity_scan` | Get Report of Integrity Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `start_port_scan` | Start Port Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_status_of_port_scan` | Get Status of Port Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_report_of_port_scan` | Get Report of Port Scan | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_blacklist_status` | Get Blacklist Status | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |
| `get_blacklist_report` | Get Blacklist Report | investigation | ✓ | `domain_name`(Domain/URL Name, REQ), `response_format`(Response Format) |

### `radware-alteon`

version 1.0.0 — Radware Alteon is a robust and feature-rich application delivery controller that helps organizations optimize application performance, enhan…

- GitHub: connector-radware-alteon
- Category: Automation controller
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `add_table_element` | Add Table Element | investigation | ✓ | `ip_address`(IP Address, REQ), `mask`(Mask, REQ), `index`(Index) |
| `view_table` | View Table | investigation | ✓ | — |
| `view_table_element` | View Table Element | investigation | ✓ | `index`(Index, REQ) |
| `edit_table_element` | Edit Table Element | investigation | ✓ | `ip_address`(IP Address, REQ), `mask`(Mask), `index`(Index) |
| `delete_table_element` | Delete Table Element | investigation | ✗ | `index`(Index, REQ) |

### `rapid7-insightcloudsec`

version 1.0.0 — InsightCloudSec secures your public cloud environment from development to production with a modern, integrated, and automated approach. This…

- GitHub: connector-rapid7-insightcloudsec
- Category: Cloud Security
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_resource_details` | Get Resource Details | investigation | ✓ | `resource_id`(Resource ID, REQ) |
| `run_resource_query` | Run Resource Query | investigation | ✓ | `badges`(Badges), `badge_filter_operator`(Badge Filter Operator), `filters`(Filters), `insight`(Insight), `scopes`(Scopes), `selected_resource_type`(Selected Resource Type), `tags`(Tags), `order_by`(Order By), `limit`(Limit, REQ), `offset`(Offset) |
| `get_list_resource_tags` | Get Resource Tags List | investigation | ✓ | `resource_id`(Resource ID, REQ) |

### `rapid7-insightvm-cloud`

version 1.0.0 — The Rapid7 InsightVM Cloud platform integrates Rapid7's library of Nexpose vulnerability research, Metasploit exploit knowledge, global atta…

- GitHub: connector-rapid7-insightvm-cloud
- Category: ['Analytics and SIEM']
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `generic_api_call` | Generic API call | — | ✓ | `api_endpoint`(api_endpoint, REQ), `method`(method, REQ), `params`(params), `data`(data), `headers`(headers) |
| `search_assets` | Search Assets | investigation | ✗ | `asset`(asset), `vulnerability`(vulnerability), `cursor`(cursor), `page`(page), `size`(size), `sort`(sort, REQ) |
| `get_asset` | Get Asset | investigation | ✓ | `id`(Asset ID, REQ), `current_time`(Current Time), `comparison_time`(Comparison Time), `include_same`(Include Same), `include_unique_identifiers`(Include Unique Identifiers) |
| `list_sites` | List Sites | investigation | ✓ | `cursor`(cursor), `page`(page), `size`(size), `sort`(sort, REQ) |
| `search_vulnerabilities` | Search Vulnerabilities | investigation | ✓ | `vulnerability`(vulnerability), `cursor`(cursor), `page`(page), `size`(size), `sort`(sort, REQ) |

### `rapid7-threat-command-cloud`

version 1.1.1 — Rapid7 Threat Command Cloud is a digital risk protection and external threat intelligence platform that helps organizations monitor, detect,…

- GitHub: connector-rapid7-threat-command-cloud
- Category: ['Threat Intelligence']
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ioc_sources` | Get IOC Sources | investigation | ✗ | — |
| `get_iocs_by_filter` | Get IOCs by Filter | investigation | ✗ | `lastUpdatedFrom`(Last Updated From, REQ), `offset`(Offset), `limit`(Page Size) |
| `get_ioc_by_value` | Get IOC by Value | investigation | ✗ | `iocValue`(IOC, REQ) |
| `add_iocs_to_source` | Add IOCs to Source | investigation | ✗ | `sourceID`(Source ID, REQ), `iocs`(IOCs, REQ) |
| `change_ioc_severity` | Change IOC Severity | investigation | ✗ | `iocValue`(IOC, REQ), `severity`(Severity, REQ) |
| `get_cves_by_ids` | Get CVEs by IDs | investigation | ✗ | `cveList`(CVE IDs, REQ) |
| `get_cves_list_from_account` | Get CVEs List from Account | investigation | ✗ | `publishDateFrom`(Publish Date From) |
| `get_alerts_list` | Get Alerts List | investigation | ✗ | `alertType`(Alert Type), `severity`(Severity), `sourceType`(Source Type), `networkType`(Network Type), `matchedAssetValue`(Matched Asset Value), `tags`(Tags), `remediationStatus`(Remediation Status), `sourceDateFrom`(Source Date From), `sourceDateTo`(Source Date To), `foundDateFrom`(Found Date From), `foundDateTo`(Found Date To) |
| `get_alert_by_id` | Get Alert Details | investigation | ✗ | `alertID`(Alert ID, REQ) |
| `generic_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `api_endpoint`(Endpoint, REQ), `params`(Query Parameters), `json_data`(Request Payload) |

### `rapid7-velociraptor`

version 1.0.0 — Rapid7 Velociraptor is a unique, advanced open-source endpoint monitoring, digital forensic and cyber response platform. It provides you wit…

- GitHub: connector-rapid7-velociraptor
- Category: Endpoint Security
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_clients` | Get Clients List | investigation | ✓ | `search`(Search String), `client_id`(Client ID), `count`(Count), `start`(Offset) |
| `run_artifacts_collection` | Run Artifacts Collection | investigation | ✓ | `client_id`(Client ID, REQ), `artifacts`(Artifacts, REQ), `env`(Env), `spec`(Spec), `timeout`(Timeout), `ops_per_sec`(Ops Per Sec), `cpu_limit`(CPU Limit), `iops_limit`(Iops Limit), `max_rows`(Max Rows), `max_bytes`(Max Bytes), `urgent`(Urgent), `org_id`(Org ID) |
| `get_flow_results` | Get Flow Results | investigation | ✓ | `flow_id`(Flow ID, REQ), `client_id`(Client ID, REQ), `artifact`(Artifact), `source`(Source) |
| `list_flows` | Get Flows List | investigation | ✓ | `client_id`(Client ID, REQ), `flow_id`(Flow ID) |
| `create_flow_download` | Create Flow Download | investigation | ✓ | `client_id`(Client ID, REQ), `flow_id`(Flow ID, REQ), `wait`(Wait), `password`(Password), `format`(Format), `name`(Name), `expand_sparse`(Expand Sparse) |
| `dump_artifact_definitions` | Dump Artifact Definitions | investigation | ✓ | `names`(Artifact Name), `deps`(Include Dependencies), `sanitize`(Sanitize) |
| `create_hunt` | Create Hunt | investigation | ✓ | `artifacts`(Artifacts, REQ), `description`(Description), `expires`(Expiry Time), `spec`(Spec), `timeout`(Timeout), `ops_per_sec`(Ops Per Sec), `cpu_limit`(CPU Limit), `iops_limit`(Iops Limit), `max_rows`(Max Rows), `max_bytes`(Max Bytes), `pause`(Pause), `include_labels`(Include Labels), `exclude_labels`(Exclude Labels), `os`(OS), `org_id`(Org ID) |
| `list_hunts` | Get Hunts List | investigation | ✓ | `hunt_id`(Hunt ID), `count`(Count), `offset`(Offset) |
| `get_hunt_results` | Get Hunt Results | investigation | ✓ | `hunt_id`(Hunt ID, REQ), `artifact`(Artifact), `source`(Source), `brief`(Brief) |
| `create_hunt_download` | Create Hunt Download | investigation | ✓ | `hunt_id`(Hunt ID, REQ), `only_combined`(Only Combined), `wait`(Wait), `format`(Format), `base`(Base), `password`(Password), `expand_sparse`(Expand Sparse) |
| `run_vql_query` | Run VQL Query | investigation | ✓ | `query`(VQL Query, REQ) |

### `recorded-future`

version 2.0.0 — Recorded Future is a threat intelligence product that automatically collects and analyzes threat intelligence from technical, open, and dark…

- GitHub: connector-recorded-future
- Category: Threat Intelligence
- Operations: 41

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `domain_reputation` | Get Domain Reputation | investigation | ✓ | `domain`(Domain, REQ), `fields`(Fields), `metadata`(Metadata) |
| `domain_risklist` | Get Domain Risk List | investigation | ✓ | `risk_rule_list`(Risk Rule List) |
| `search_domain` | Search Domain | investigation | ✓ | `fields`(Fields), `metadata`(Metadata), `limit`(Limit), `from`(From), `riskScore`(Risk Score), `firstSeen`(First Seen), `lastSeen`(Last Seen), `list`(List ID), `riskRule`(Risk Rule), `parent`(Parent), `orderby`(Order By), `direction`(Direction) |
| `ip_reputation` | Get IP Reputation | investigation | ✓ | `ip`(IP Address, REQ), `fields`(Fields), `metadata`(Metadata) |
| `ip_risklist` | Get IP Risk List | investigation | ✓ | `risk_rule_list`(Risk Rule List) |
| `search_ip` | Search IP | investigation | ✓ | `fields`(Fields), `metadata`(Metadata), `limit`(Limit), `from`(From), `range`(Range), `riskScore`(Risk Score), `firstSeen`(First Seen), `lastSeen`(Last Seen), `list`(List ID), `riskRule`(Risk Rule), `orderby`(Order By), `direction`(Direction) |
| `file_reputation` | Get File Reputation | investigation | ✓ | `hash`(Filehash, REQ), `fields`(Fields), `metadata`(Metadata) |
| `file_risklist` | Get File Risk List | investigation | ✓ | `risk_rule_list`(Risk Rule List) |
| `search_file` | Search Filehash | investigation | ✓ | `fields`(Fields), `metadata`(Metadata), `limit`(Limit), `from`(From), `riskScore`(Risk Score), `algorithm`(Algorithm), `firstSeen`(First Seen), `lastSeen`(Last Seen), `list`(List ID), `riskRule`(Risk Rule), `orderby`(Order By), `direction`(Direction) |
| `lookup_vulnerability` | Lookup Vulnerability | investigation | ✓ | `cve_id`(CVE/RF ID, REQ), `fields`(Fields), `metadata`(Metadata) |
| `vulnerability_risklist` | Get vulnerability Risk List | investigation | ✓ | `risk_rule_list`(Risk Rule List) |
| `search_vulnerability` | Search Vulnerabilities | investigation | ✓ | `freetext`(Free Text), `fields`(Fields), `metadata`(Metadata), `limit`(Limit), `from`(From), `riskScore`(Risk Score), `cvssScore`(CVSS Score), `firstSeen`(First Seen), `lastSeen`(Last Seen), `list`(List ID), `riskRule`(Risk Rule), `orderby`(Order By), `direction`(Direction) |
| `lookup_url` | Lookup URL | investigation | ✓ | `url`(URL, REQ), `fields`(Fields), `metadata`(Metadata) |
| `url_risklist` | Get URL Risk List | investigation | ✓ | `risk_rule_list`(Risk Rule List) |
| `search_url` | Search URL | investigation | ✓ | `fields`(Fields), `metadata`(Metadata), `limit`(Limit), `from`(From), `riskScore`(Risk Score), `firstSeen`(First Seen), `lastSeen`(Last Seen), `list`(List ID), `riskRule`(Risk Rule), `orderby`(Order By), `direction`(Direction) |
| `lookup_malware` | Lookup Malware | — | ✓ | `malware_id`(ID, REQ), `fields`(Fields), `metadata`(Metadata) |
| `search_malware` | Search Malware | — | ✓ | `freetext`(Free Text), `fields`(Fields), `metadata`(Metadata), `limit`(Limit), `from`(From), `firstSeen`(First Seen), `lastSeen`(Last Seen), `list`(List ID), `orderby`(Order By), `direction`(Direction) |
| `get_alert` | Get Alert | investigation | ✓ | `alert_ID`(Alert ID, REQ) |
| `search_alerts` | Search Alerts | — | ✓ | `triggered`(Triggered), `assignee`(Assignee), `status`(Status), `alertRule`(Alert Rule ID), `freetext`(Free Text), `limit`(Limit), `from`(From), `orderby`(Order By), `direction`(Direction) |
| `search_alert_rule` | Search Alert Rules | — | ✓ | `freetext`(Free Text), `limit`(Limit) |
| `get_riskrules` | Get Risk Rules | — | ✓ | `type`(Risk Rules For, REQ) |
| `get_maps_list` | Get Maps List | investigation | ✓ | — |
| `get_threat_map` | Get Threat Map | investigation | ✓ | `actors`(Actors), `categories`(Categories), `watchlists`(Watch Lists) |
| `get_threat_map_by_org_id` | Get Threat Map By Org ID | investigation | ✓ | `orgId`(Organization ID, REQ), `actors`(Actors), `categories`(Categories), `watchlists`(Watch Lists) |
| `get_malware_threat_map` | Get Malware Threat Map | investigation | ✓ | `malware`(Malware), `categories`(Categories), `watchlists`(Watch Lists) |
| `get_malware_threat_map_by_org_id` | Get Malware Threat Map By Org ID | investigation | ✓ | `orgId`(Organization ID, REQ), `malware`(Malware), `categories`(Categories), `watchlists`(Watch Lists) |
| `get_threat_actors_list` | Get Threat Actors List | investigation | ✓ | `name`(Name), `limit`(Limit), `offset`(Offset) |
| `get_threat_actors_categories` | Get Threat Actors Categories | investigation | ✓ | — |
| `get_malware_categories` | Get Malware Categories | investigation | ✓ | — |
| `get_third_party_risk_alert_by_alert_id` | Get Third Party Risk Alert By Alert ID | investigation | ✓ | `playbook_alert_id`(Playbook Alert ID, REQ), `panels`(Panels) |
| `get_bulk_third_party_risk_alerts` | Get Bulk Third Party Risk Alerts | investigation | ✓ | `playbook_alert_ids`(Playbook Alert IDs), `panels`(Panels) |
| `get_identity_novel_exposures_alert_by_alert_id` | Get Identity Novel Exposures Alert By Alert ID | investigation | ✓ | `playbook_alert_id`(Playbook Alert ID, REQ), `panels`(Panels) |
| `get_bulk_identity_novel_exposures_alerts` | Get Bulk Identity Novel Exposures Alerts | investigation | ✓ | `playbook_alert_ids`(Playbook Alert IDs), `panels`(Panels) |
| `create_user_list` | Create User List | investigation | ✓ | `name`(Name), `type`(Type) |
| `get_user_lists` | Get User Lists | investigation | ✓ | `name`(Name), `type`(Type), `limit`(Limit) |
| `get_user_list_by_list_id` | Get User List By List ID | investigation | ✓ | `listId`(List ID, REQ) |
| `get_user_list_status_by_list_id` | Get User List Status By List ID | investigation | ✓ | `listId`(List ID, REQ) |
| `get_entities_by_list_id` | Get Entities By List ID | investigation | ✓ | `listId`(List ID, REQ) |
| `add_entity_to_user_list` | Add Entity To User List | investigation | ✓ | `listId`(List ID, REQ), `id`(Entity ID, REQ), `context`(Context) |
| `remove_entity_from_user_list` | Remove Entity From User List | investigation | ✓ | `listId`(List ID, REQ), `id`(Entity ID, REQ) |
| `add_ioc_to_recorded_future_intelligence_cloud` | Add IOC To Recorded Future Intelligence Cloud | investigation | ✓ | `options`(Options), `organization_ids`(Organization IDs), `timestamp`(Timestamp), `ioc`(IOC), `incident`(Incident), `detection`(Detection), `mitre_codes`(Mitre codes), `malwares`(Malware's) |

### `recorded-future-feed`

version 1.0.0 — Recorded Future Threat Intel Feed connector ingests indicators (IP, Domain, URL, Hash, Vulnerability) from the Recorded Future Connect API r…

- GitHub: connector-recorded-future-feed
- Category: Threat Intelligence
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `indicator_type`(Indicator Type, REQ), `risk_rule`(Risk Rule), `limit`(Limit) |
| `get_risk_rules` | Get Risk Rules | investigation | ✓ | `indicator_type`(Indicator Type, REQ) |
| `lookup_ip` | Lookup IP | investigation | ✓ | `ip`(IP Address, REQ), `fields`(Fields) |
| `lookup_domain` | Lookup Domain | investigation | ✓ | `domain`(Domain, REQ), `fields`(Fields) |
| `lookup_url` | Lookup URL | investigation | ✓ | `url`(URL, REQ), `fields`(Fields) |
| `lookup_hash` | Lookup Hash | investigation | ✓ | `hash`(Hash, REQ), `fields`(Fields) |
| `lookup_vulnerability` | Lookup Vulnerability (CVE) | investigation | ✓ | `cve`(CVE, REQ), `fields`(Fields) |

### `red-canary`

version 1.0.0 — Red Canary collects endpoint data using Carbon Black Response and CrowdStrike Falcon. The collected data is standardized into a common schem…

- GitHub: connector-red-canary
- Category: Endpoint Protection
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `list_detections` | Get Detections List | investigation | ✓ | `page`(Page Number), `per_page`(Per Page), `since`(Since) |
| `get_detection` | Get Detection Details | investigation | ✓ | `detection_id`(Detection ID, REQ) |
| `list_detection_marked_indicators_of_compromise` | List Detection Marked Indicators of Compromise | investigation | ✓ | `detection_id`(Detection ID, REQ), `page`(Page Number), `per_page`(Items Per Page) |
| `acknowledge_detection` | Acknowledge Detection | investigation | ✓ | `detection_id`(Detection ID, REQ) |
| `update_remediation_state` | Update Remediation State | investigation | ✓ | `detection_id`(Detection ID, REQ), `remediation_state`(Remediation State, REQ), `comment`(Comment) |
| `list_endpoints` | Get Endpoints List | investigation | ✓ | `page`(Page Number), `per_page`(Per Page), `order_by`(Order By), `filter_query`(Other Fields) |
| `get_endpoint` | Get Endpoint Details | investigation | ✓ | `endpoint_id`(Endpoint ID, REQ) |
| `isolate_endpoint` | Isolate Endpoint | investigation | ✓ | `ids`(Endpoint IDs, REQ) |
| `deisolate_endpoint` | Deisolate Endpoint | investigation | ✓ | `ids`(Endpoint IDs, REQ) |

### `remote-fortisoar`

version 2.0.0 — This connector facilitates automated interactions, with a FortiSOAR endpoint using FortiSOAR playbooks. Add the Remote FortiSOAR connector a…

- GitHub: connector-remote-fortisoar
- Category: Utilities
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `make_api_call` | Make an API call | investigation | ✓ | `iri`(Endpoint IRI, REQ), `method`(HTTP method, REQ) |
| `upload_file` | Upload file to FortiSOAR | Utilities | ✓ | `file_iri`(Attachment/File IRI, REQ), `create_attachment`(Create Remote FortiSOAR Attachment) |

### `reversinglabs-a1000`

version 1.0.0 — ReversingLabs A1000 Malware Analysis

- GitHub: connector-reversinglabs-a1000
- Category: Malware Analysis
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `upload_sample` | Upload Sample | — | ✓ | `file_iri`(File IRI List, REQ) |
| `get_report` | Get Report using File Hash | — | ✓ | `file_hash`(File Hash, REQ) |
| `re_analyze_sample` | Re-analyze Sample using File Hash | — | ✓ | `file_hash`(File Hash, REQ) |

### `ridgebot`

version 1.0.1 — RidgeBot validates security vulnerabilities in your organization by using real POC codes to exploit the vulnerability. This connector facili…

- GitHub: connector-ridgebot
- Category: Breach and Attack Simulation (BAS)
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_task_info` | Get Task Info | investigation | ✓ | `task_id`(Task ID, REQ) |
| `get_task_statistics` | Get Task Statistics | investigation | ✓ | `task_id`(Task ID, REQ) |
| `generate_and_download` | Generate And Download | investigation | ✓ | `task_id`(Task ID, REQ) |
| `stop_task` | Stop Task | — | ✓ | `task_id`(Task ID, REQ) |
| `create_task` | Create Task | investigation | ✓ | `name`(Name of Scan, REQ), `temp_id`(Type of Scan, REQ), `targets`(Targets, REQ) |

### `riskiq-digital-footprint`

version 1.0.0 — RiskIQ Digital Footprint gives complete visibility beyond the firewall. Unlike scanners and IP-dependent data vendors, RiskIQ Digital Footpr…

- GitHub: connector-riskiq-digital-footprint
- Category: Threat Intelligence
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `add_assets` | Add Assets | investigation | ✓ | `request`(Request Body, REQ), `failOnError`(Fail on Error) |
| `get_assets_by_type` | Get Assets By Type | investigation | ✓ | `type`(Asset Type, REQ), `name`(Asset Name, REQ), `global`(Search in Global Inventory ), `size`(Size), `recent`(Recent Asset) |
| `get_assets_by_uuid` | Get Assets By UUID | investigation | ✓ | `uuid`(Asset UUID, REQ), `global`(Search in Global Inventory ), `recent`(Recent Asset) |
| `update_assets` | Update Assets | investigation | ✓ | `request`(Request Body, REQ), `failOnError`(Fail on Error) |
| `get_connected_asset` | Get Connected Assets | investigation | ✓ | `type`(Asset Type, REQ), `name`(Asset Name, REQ), `global`(Search in Global Inventory ), `page`(Page Number), `size`(Page Size) |
| `get_task_status` | Get Task Status | investigation | ✓ | `id`(Task ID, REQ) |
| `get_changed_asset` | Get Changed Asset | investigation | ✓ | `type`(Asset Type), `date`(Date), `range`(Range), `measure`(Measure), `brand`(Brand), `organization`(Organization), `tag`(Tag), `page`(Page Number), `size`(Page Size) |
| `get_changed_asset_summary` | Get Changed Asset Summary | investigation | ✓ | `date`(Date), `range`(Range), `brand`(Brand), `organization`(Organization), `tag`(Tag) |

### `riskiq-passivetotal`

version 1.0.0 — RiskIQ PassiveTotal used to map threat actor infrastructure, profile hostnames & IP addresses, discover web technologies on Internet hosts. …

- GitHub: connector-riskiq-passivetotal
- Category: Threat Intelligence
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_reputation` | Get Reputation | investigation | ✓ | `query`(Domain/Host/IP Address, REQ) |
| `get_components` | Get Components | investigation | ✓ | `search_by`(Get Data For, REQ), `name`(Name, REQ), `version`(Version), `category`(Category), `page`(Page), `sort`(Sort), `order`(Order) |
| `get_trackers` | Get Trackers | investigation | ✓ | `query`(Query, REQ), `start`(Start), `end`(End), `page`(Page) |
| `get_cookies` | Get Cookies | investigation | ✓ | `query`(Query, REQ), `start`(Start), `end`(End), `page`(Page) |
| `get_alerts` | Get Alerts | investigation | ✓ | `project`(Project), `artifact`(Artifact), `start`(Start), `end`(End), `page`(Page), `size`(Size) |
| `get_services` | Get Services | investigation | ✓ | `query`(IP Address, REQ) |
| `get_enrichment_data` | Get Enrichment Data | investigation | ✓ | `query`(Query, REQ), `query_for`(Get Data For) |
| `get_whois_data` | Get Whois Data | investigation | ✓ | `query`(Query, REQ), `compact_record`(Compact Record), `history`(History) |
| `search_whois_data` | Search Whois Data | investigation | ✓ | `query`(Query, REQ), `field`(Field, REQ) |
| `get_passive_dns` | Get Passive DNS | investigation | ✓ | `query`(Query, REQ), `start`(Start), `end`(End), `timeout`(Timeout) |

### `riskiq-whoisiq`

version 1.0.0 — The WHOISIQ™ allow you to search for WHOISIQ™ records by the various attributes on those records. Currently, the API supports searching by (…

- GitHub: connector-riskiq-whoisiq
- Category: Threat Intelligence
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_address` | Get Address | investigation | ✓ | `address`(Get Address, REQ), `exact`(Exact Match), `maxResults`(Maximum Results) |
| `get_domain` | Get Domain | investigation | ✓ | `domain`(Domain, REQ), `exact`(Exact Match), `maxResults`(Maximum Results) |
| `get_email` | Get Email Address | investigation | ✓ | `email`(Email, REQ), `exact`(Exact Match), `maxResults`(Maximum Results) |
| `get_name` | Get Name | investigation | ✓ | `name`(Name, REQ), `exact`(Exact Match), `maxResults`(Maximum Results) |
| `get_name_server` | Get Name Server | investigation | ✓ | `nameserver`(Name Server, REQ), `exact`(Exact Match), `maxResults`(Maximum Results) |
| `get_org` | Get Organization | investigation | ✓ | `org`(Organization, REQ), `exact`(Exact Match), `maxResults`(Maximum Results) |
| `get_phone` | Get Phone Number | investigation | ✓ | `phone`(Phone Number, REQ), `exact`(Exact Match), `maxResults`(Maximum Results) |

### `robtex`

version 1.0.0 — Robtex uses various sources to gather public information about IP numbers, domain names, host names, autonomous systems, routes, etc., doing…

- GitHub: connector-robtex
- Category: Threat Detection
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_query_details` | Get IP Query Details | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_autonomous_system_query_details` | Get Autonomous System Query Details | investigation | ✗ | `autonomous_system_number`(Autonomous System Number, REQ) |

### `rsa-netwitness-siem`

version 1.2.1 — The RSA NetWitness Platform is an evolved SIEM and threat detection and response solution that allows security teams to rapidly detect and r…

- GitHub: connector-rsa-netwitness-siem
- Category: SIEM
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_incident` | Get Incident | investigation | ✓ | `id`(Incident ID, REQ) |
| `get_incident_by_date_range` | Get Incidents by Date Range | investigation | ✓ | `since`(Start Time), `until`(End Time), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `get_incidents_alerts` | Get Incident Related Alerts | investigation | ✓ | `id`(Incident ID, REQ), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `get_alerts` | Get Alerts | investigation | ✓ | `meta_name`(Field Name), `meta_value`(Field Value), `includeFields`(Include Fields), `numberOfRecords`(Limit) |
| `get_hosts` | Get Hosts List | investigation | ✓ | `serviceId`(Service ID, REQ), `criteria`(Filter Criteria), `pageNumber`(Page Number), `pageSize`(Page Size) |
| `get_service_id` | Get Service IDs | investigation | ✓ | — |

### `rss-feed`

version 1.1.0 — An RSS feed, short for Really Simple Syndication, is a standardized format used to publish frequently updated content such as blog posts, ne…

- GitHub: connector-rss-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `url`(Feed URL, REQ) |

### `sailpoint-identitynow`

version 1.0.0 — SailPoint IdentityNow that allows you to easily control user access to all systems and applications, enhance audit response and increase you…

- GitHub: connector-sailpoint-identitynow
- Category: Identity and Access Management
- Operations: 11

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_accounts` | Get Accounts | investigation | ✓ | `filter`(Filter), `detailLevel`(Detail Level), `limit`(Limit), `offset`(Offset) |
| `get_account_details` | Get Account Details | investigation | ✓ | `id`(Account ID, REQ) |
| `get_account_activities` | Get Account Activities | investigation | ✓ | `account_type`(Type), `requested-for`(Requested For), `requested-by`(Requested By), `regarding-identity`(Regarding Identity), `sorters`(Sort By), `limit`(Limit), `offset`(Offset) |
| `get_account_activity` | Get Account Activity | investigation | ✓ | `id`(Activity ID, REQ) |
| `get_password_info` | Get Password Info | investigation | ✓ | `userName`(User Name, REQ), `sourceName`(Source Name, REQ) |
| `reset_password` | Reset Password | containment | ✓ | `userName`(User Name, REQ), `sourceName`(Source Name, REQ), `identityId`(Identity ID, REQ), `password`(Password, REQ), `publicKeyId`(Public Key ID, REQ), `accountId`(Account ID, REQ), `sourceId`(Source ID, REQ) |
| `enable_account` | Enable Account | containment | ✓ | `id`(ID, REQ), `externalVerificationId`(External Verification ID, REQ), `forceProvisioning`(Force Provisioning) |
| `disable_account` | Disable Account | containment | ✓ | `id`(ID, REQ), `externalVerificationId`(External Verification ID, REQ), `forceProvisioning`(Force Provisioning) |
| `unlock_account` | Unlock Account | containment | ✓ | `id`(ID, REQ), `externalVerificationId`(External Verification ID, REQ), `unlockIDNAccount`(Unlock IDN Account), `forceProvisioning`(Force Provisioning) |
| `grant_request` | Grant Access | containment | ✓ | `requestedFor`(Requested For, REQ), `requestedItems`(Requested Items, REQ), `clientMetadata`(Client Metadata) |
| `revoke_request` | Revoke Access | containment | ✓ | `requestedFor`(Requested For, REQ), `requestedItems`(Requested Items), `clientMetadata`(Client Metadata, REQ) |

### `sap-cloud-identity-directory-service`

version 1.0.0 — The identity directory provides a System for Cross-domain Identity Management (SCIM) 2.0 REST API for managing resources (users, groups and …

- GitHub: connector-sap-cloud-identity-directory-service
- Category: Identity and Access Management
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_user_list` | Get User List | investigation | ✓ | `id`(User UUID), `userName`(Username), `userType`(User Type), `filter`(Filter Query), `start_id`(Start ID), `count`(Size) |
| `delete_user` | Delete User | investigation | ✓ | `userUUID`(User UUID, REQ) |
| `create_user` | Create User | investigation | ✓ | `email`(Email Address, REQ), `userName`(Login Name), `givenName`(First Name), `familyName`(Last Name), `userType`(User Type), `userDetails`(User details) |
| `update_user_details` | Update User Details | investigation | ✓ | `userUUID`(User UUID, REQ), `status`(Status), `operations`(Operations), `add_operations`(Additional Operations) |
| `get_group_list` | Get Group List | investigation | ✓ | `displayName`(Display Name), `urn:sap:cloud:scim:schemas:extension:custom:2.0:Group:name`(Name), `filter`(Filter Query), `start_id`(Start ID), `count`(Size) |
| `delete_group` | Delete Group | investigation | ✓ | `group_id`(Group ID, REQ) |
| `create_group` | Create Group | investigation | ✓ | `name`(Name, REQ), `displayName`(Display Name, REQ), `description`(Description), `externalId`(External ID), `members`(Members) |
| `update_group_members` | Update Group Members | investigation | ✓ | `group_id`(Group ID, REQ), `operation`(Operation, REQ) |

### `sap-etd`

version 1.1.0 — SAP Enterprise Threat Detection (ETD) helps you to identify the real attacks as they are happening and analyze the threats quickly enough to…

- GitHub: connector-sap-etd
- Category: Threat Detection
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alert` | Get Alerts | investigation | ✓ | `$query`(Query), `$format`(Response Format), `$batchSize`(Limit), `$patternFilter`(Pattern Filter), `$includeEvents`(Include Events), `$includeTestAlerts`(Include TestAlerts), `$autoConfirm`(Auto Confirm) |

### `sap-etd-cloud`

version 1.0.0 — SAP Enterprise Threat Detection (ETD), Cloud Edition helps you to identify the real attacks as they are happening and analyze the threats qu…

- GitHub: connector-sap-etd-cloud
- Category: Threat Detection
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alerts | investigation | ✗ | `limit`(Limit), `startTime`(Start Time, REQ), `endTime`(End Time, REQ) |
| `get_alert_by_id` | Get Alert Details | investigation | ✗ | `alertID`(Alert ID, REQ) |
| `get_investigations` | Get Investigations | investigation | ✗ | `alertID`(Alert ID, REQ), `limit`(Limit) |

### `scadafence`

version 1.0.0 — SCADAfence that provides full coverage of large-scale networks, offering best-in-class network monitoring, asset discovery, governance, remo…

- GitHub: connector-scadafence
- Category: OT & IoT Security
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_alert` | Create Alert | investigation | ✓ | `ip`(IP Address, REQ), `severity`(Alert Severity), `details`(Description, REQ), `active`(Is Active, REQ), `remediation`(Remediation Text) |
| `get_alerts` | Get Alert List | investigation | ✓ | `number`(Alert Number), `type`(Alert Type ID), `site_id`(Site ID), `status`(Alert Status), `severity`(Alert Severity), `ip`(IP Address), `from`(From), `to`(To), `from_last_seen`(From LastSeen), `to_last_seen`(To LastSeen), `order`(Order By), `sort`(Sort By), `size`(Size), `page`(Page) |
| `update_alert_status` | Update Alert Status | investigation | ✓ | `id`(Alert ID, REQ), `status`(Alert Status, REQ) |
| `get_assets` | Get Asset List | investigation | ✓ | `site_id`(Site ID), `ip`(IP Address), `HostName`(hostname), `mac`(Mac Address), `order`(Order By), `sort`(Sort By), `size`(Size), `page`(Page) |
| `update_asset` | Update Asset | investigation | ✓ | `id`(Site ID, REQ), `ip`(IP Address, REQ), `override`(Override, REQ), `host`(hostname), `device_type`(Device Type), `os`(Asset OS), `vendor`(Vendor Name), `ou`(Organization Unit (OU)), `owner`(Owner), `location`(Physical Location), `comment`(Comment), `criticality`(Criticality), `cve_product`(Product CVE), `cve_version`(Version CVE) |
| `get_sites_status` | Get Sites Status | investigation | ✓ | `site_id`(Site ID), `site_name`(Site Name) |

### `seclytics-augur-pxdr`

version 1.1.0 — Seclytics Augur pXDR: This FortiSOAR connector interacts with Seclytics Augur pXDR API. It can perform IOC lookup for threat context enrichm…

- GitHub: connector-seclytics-augur-pxdr
- Category: Network Protection
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `query_domain` | Get Domain Reputation | investigation | ✓ | `domain`(Domain, REQ) |
| `query_host` | Get Host Reputation | investigation | ✓ | `host`(Host, REQ) |
| `query_file` | Get File Reputation | investigation | ✓ | `file_hash`(File Hash, REQ) |
| `download_predictions` | Download Predictions | miscellaneous | ✓ | `file_name`(File Name) |

### `security-center`

version 1.1.0 — Tenable Security Center provide actions like get all completed scans, scan specific assets and asset specific vulnerabilities

- GitHub: connector-security-center
- Category: Vulnerability Management
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_scans` | List Completed Scans | investigation | ✓ | `days`(Completion Time, REQ) |
| `get_all_assets` | List Assets | investigation | ✓ | `scan_details`(Scan Information, REQ) |
| `get_asset_vulns` | List Asset Vulnerabilities | investigation | ✓ | `asset_info`(IP/MAC/Hostname, REQ), `scan_id`(Scan ID), `scan_name`(Scan Name) |

### `security-scorecard`

version 1.0.0 — Security Scorecard Platform combines several threat intelligence sources to provide in-depth insights on threat hosts and attack infrastruct…

- GitHub: connector-security-scorecard
- Category: Threat Intelligence
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_companies_portfolio` | Get All Companies Portfolio | investigation | ✗ | `portfolio_id`(Portfolio ID, REQ) |
| `get_list_of_portfolio` | Get List of Portfolio | investigation | ✗ | — |
| `get_company_score` | Get Company Score | investigation | ✗ | `domain`(Domain, REQ) |
| `get_company_factor_score` | Get Company Factor Score | investigation | ✗ | `domain`(Domain, REQ) |
| `get_company_history_score` | Get Company History Score | investigation | ✗ | `domain`(Domain, REQ) |
| `get_company_history_factor_score` | Get Company History Factor Score | investigation | ✗ | `domain`(Domain, REQ) |
| `get_alert_list` | Get Alert List | investigation | ✗ | `email_id`(Email ID, REQ) |
| `get_ransomware_details` | Get Ransomware Details   | investigation | ✗ | `ransomware_id`(Ransomware ID, REQ) |

### `security-trails`

version 1.0.0 — SecurityTrails is a cybersecurity platform that provides domain and IP intelligence services. It offers tools for reconnaissance, asset disc…

- GitHub: connector-security-trails
- Category: Threat Intelligence
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_associated_ips` | Get Associated IPs | investigation | ✗ | `domain`(Domain, REQ) |
| `get_domain_details` | Get Domain Details | investigation | ✗ | `host`(Hostname, REQ) |
| `get_subdomain_details` | Get Subdomain Details | investigation | ✗ | `host`(Hostname, REQ), `children_only`(Children Only), `include_inactive`(Include Inactive) |
| `get_domain_tags_details` | Get Domain Tags Details | investigation | ✗ | `host`(Hostname, REQ) |
| `get_domain_whois_details` | Get Domain WHOIS Details | investigation | ✗ | `host`(Hostname, REQ) |
| `get_associated_domains` | Get Associated Domains | investigation | ✗ | `host`(Host, REQ) |
| `get_whois_history` | Get WHOIS History | investigation | ✗ | `host`(Host, REQ) |
| `get_ips_neighbors` | Get IPs Neighbors | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_whois_ips` | Get Whois IPs | investigation | ✗ | `ip_address`(IP Address, REQ) |

### `securonix-snypr`

version 2.3.0 — Connector facilitates automated operations to Analyze and detect the Threats, Violations and Risk associated with users in organisation.

- GitHub: connector-securonix-snypr
- Category: Analytics and SIEM
- Operations: 26

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `add_comment` | Add Comment | investigation | ✓ | `incidentId`(Incident ID, REQ), `comment`(Comment, REQ) |
| `create_incident` | Create Incident | investigation | ✓ | `violationName`(Policy Name, REQ), `datasourceName`(Data Source Name, REQ), `entityName`(Account Name, REQ), `entityType`(Entity Type, REQ), `actionName`(Action Name, REQ), `resourceName`(Resource Name ), `employeeid`(Employee ID), `workflow`(Workflow Name), `comment`(Comment), `criticality`(Criticality) |
| `check_task_on_incident` | Check Task on Incident | investigation | ✓ | `incidentId`(Incident ID, REQ), `actionName`(Action Name, REQ) |
| `get_available_threat_action` | Get Available Threat Action | investigation | ✓ | — |
| `get_incident_details` | Get Incident Details | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `get_incident_status` | Get Incident Status | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `get_incident_workflow` | Get Incident Workflow | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `get_possible_action_for_incident` | Get Possible Actions for Incident | investigation | ✓ | `incidentId`(Incident ID, REQ) |
| `get_risk_score` | Get Risk Score | investigation | ✓ | `query`(Query), `from`(Start Time), `to`(End Time) |
| `get_risk_history` | Get Risk History | investigation | ✓ | `query`(Query), `from`(Start Time), `to`(End Time) |
| `get_top_threats` | Get Top Threats | investigation | ✓ | `dateunit`(Last Seen, REQ) |
| `get_top_violations` | Get Top Violations | investigation | ✓ | `dateunit`(Last Seen, REQ) |
| `get_top_violators` | Get Top Violators | investigation | ✓ | `dateunit`(Last Seen, REQ), `offset`(Offset, REQ), `max`(Limit, REQ) |
| `get_workflows` | Get Workflows | investigation | ✓ | — |
| `get_workflow_default_assignee` | Get Workflow Default Assignee | investigation | ✓ | `workflow`(Workflow Name, REQ) |
| `list_incidents` | List Incidents | investigation | ✓ | `rangeType`(Range Type, REQ), `from`(Start Time, REQ), `to`(End Time, REQ), `status`(Status), `offset`(Offset), `max`(Max Limit) |
| `list_peer_groups` | List All Peer Groups | investigation | ✓ | — |
| `list_policies` | List All Policies | investigation | ✓ | — |
| `list_resource_groups` | List All Resource Groups | investigation | ✓ | — |
| `list_users` | List All Users | investigation | ✓ | — |
| `custom_query` | Custom Query | investigation | ✓ | `query`(Query, REQ), `eventtime_from`(Event Start Time), `eventtime_to`(Event End Time), `generationtime_from`(Generation Start Time), `generationtime_to`(Generation End Time) |
| `query_tpi` | Query Third Party Intelligence | investigation | ✓ | `query`(Query) |
| `query_violations` | Query Violations | investigation | ✓ | `query`(Query), `generationtime_from`(Generation Start Time, REQ), `generationtime_to`(Generation End Time) |
| `query_users` | Query Users | investigation | ✓ | `query`(Query) |
| `query_watchlist` | Query Watchlist | investigation | ✓ | `query`(Query) |
| `take_action_on_incident` | Task Action on Incident | investigation | ✓ | `incidentId`(Incident ID, REQ), `actionName`(Action Name, REQ), `other_fields`(Other Required Fields) |

### `sekoia-io-xdr`

version 1.1.0 — SEKOIA.IO eXtended Detection and Response SaaS platform leverages Cyber Threat Intelligence to combine anticipation with automated incident …

- GitHub: connector-sekoia-io-xdr
- Category: Analytics & SIEM
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_events` | Get Events | investigation | ✓ | `query`(Query, REQ), `earliest_time`(Earliest Time, REQ), `latest_time`(Latest Time, REQ) |
| `list_alerts` | List Alerts | investigation | ✓ | `status_uuid`(Filter by Status Identifier), `status_name`(Filter by Status Name), `short_id`(Short ID), `rule_uuid`(Rule UUID), `rule_name`(Rule Name), `creation_start_date`(Creation Start Date), `creation_end_date`(Creation End Date), `updated_start_date`(Updated Start Date), `updated_end_date`(Updated End Date), `offset`(Records Offset), `limit`(Records Per Page) |
| `get_alert` | Get Alert | investigation | ✓ | `alert_uuid`(Alert UUID, REQ), `include_comments`(Include Comments), `include_stix`(Include STIX), `include_history`(Include History), `include_countermeasures`(Include Countermeasures) |
| `update_alert_status` | Update Alert Status | investigation | ✓ | `alert_uuid`(Alert Identifier, REQ), `action_uuid`(Action UUID, REQ), `comment`(Comment) |
| `add_comment_to_alert` | Add Comment to Alert | investigation | ✓ | `alert_uuid`(Alert Identifier, REQ), `comment`(Comment, REQ), `author`(Author) |
| `get_asset` | Get Asset | investigation | ✓ | `asset_uuid`(Asset UUID, REQ) |
| `update_asset` | Update Asset | investigation | ✓ | `asset_uuid`(Asset UUID, REQ), `asset_name`(Asset Name, REQ), `asset_type_uuid`(Asset Type UUID, REQ), `asset_type_name`(Asset Type Name, REQ), `asset_criticity`(Asset Criticity, REQ), `asset_description`(Asset Description), `asset_attributes`(Asset Attributes), `asset_keys`(Asset Keys), `asset_owners`(Asset Owners) |
| `delete_asset` | Delete Asset | investigation | ✓ | `asset_uuid`(Asset UUID, REQ) |
| `activate_countermeasure` | Activate a Countermeasure | investigation | ✓ | `countermeasure_uuid`(Countermeasure UUID, REQ), `content`(Comment, REQ), `author`(Author) |
| `deny_countermeasure` | Deny a Countermeasure | investigation | ✓ | `countermeasure_uuid`(Countermeasure UUID, REQ), `content`(Comment, REQ), `author`(Author) |

### `sendgrid`

version 1.1.0 — SendGrid

- GitHub: connector-sendgrid
- Category: Email Server
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `send_email` | Send Email | investigation | ✓ | `from_email`(From, REQ), `to_emails`(To Recipients, REQ), `cc_recipients`(CC Recipients), `bcc_recipients`(BCC Recipients), `body_type`(Body Type), `iri_list`(Attachment IRIs), `inline_iri_list`(Inline Attachment IRIs), `batch_id`(Batch ID), `send_at`(Scheduled Timestamp) |
| `get_email_stats` | Get Email Statistics | investigation | ✓ | `stats_by`(Email Statistics By, REQ), `start_date`(Start Date, REQ), `end_date`(End Date), `aggregated_by`(Aggregate Result By) |
| `search_email` | Search Emails | investigation | ✓ | `query`(Query, REQ), `limit`(Limit) |
| `get_contact_list` | Get Contact List | investigation | ✓ | — |
| `get_alerts` | Get Alerts | investigation | ✓ | — |
| `create_batch_id` | Create Batch ID | investigation | ✓ | — |
| `get_scheduled_send` | Get Scheduled Send | investigation | ✓ | `batch_id`(Batch ID) |
| `update_scheduled_send` | Update Scheduled Send | investigation | ✓ | `batch_id`(Batch ID, REQ), `status`(Status, REQ) |
| `delete_scheduled_send` | Delete Scheduled Send | investigation | ✓ | `batch_id`(Batch ID, REQ) |
| `get_email_templates` | Get Email Templates | investigation | ✓ | — |

### `sentinelone`

version 3.5.3 — SentinelOne that provides threat detection, hunting, and response features that enable organizations to discover vulnerabilities and protect…

- GitHub: connector-sentinelone
- Category: Analytics and SIEM
- Operations: 45

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_query` | Create Query And Get Query ID | investigation | ✓ | `query`(Query, REQ), `fromDate`(From Date, REQ), `toDate`(To Date, REQ), `groupIds`(Group IDs), `tenant`(Tenant), `queryType`(Query Type), `accountIds`(Account IDs), `siteIds`(Site IDs) |
| `cancel_running_query` | Cancel Running Query | investigation | ✓ | `queryId`(Query ID, REQ) |
| `get_query_status` | Get Query Status | investigation | ✓ | `queryId`(Query ID, REQ) |
| `get_events` | Get Events | investigation | ✓ | `queryId`(Query ID, REQ), `limit`(Limit Records), `skip`(Offset), `cursor`(Cursor), `sortBy`(Sort By), `sortOrder`(Sort Order), `subQuery`(Sub Query) |
| `get_events_by_type` | Get Events By Type | investigation | ✓ | `queryId`(Query ID, REQ), `event_type`(Event Type, REQ), `limit`(Limit Records), `skip`(Offset), `cursor`(Cursor), `sortBy`(Sort By), `sortOrder`(Sort Order), `subQuery`(Sub Query) |
| `threat_forensic_details` | Threat Forensic Details | investigation | ✓ | `threat_id`(Threat ID, REQ) |
| `threat_forensics` | Get Threat Forensics | investigation | ✓ | `threat_id`(Threat ID, REQ), `siteIds`(Site IDs), `groupIds`(Group IDs), `accountIds`(Account IDs) |
| `export_forensics_threat` | Export Threat | investigation | ✓ | `threat_id`(Threat ID, REQ), `export_format`(Export Format, REQ) |
| `threat_seen_on_network` | Get Threat Seen on Network | investigation | ✓ | `threat_id`(Threat ID, REQ), `siteIds`(Site IDs), `groupIds`(Group IDs), `accountIds`(Account IDs) |
| `free_text_filters` | Free Text | investigation | ✓ | — |
| `get_application_count` | Get Application Count | investigation | ✓ | `filterBy`(Get Count By, REQ), `siteIds`(Site IDs), `groupIds`(Group IDs), `accountIds`(Account IDs), `agentMachineTypes`(Agent Machine Types), `ids`(Application IDs), `types`(Application Types), `agentIsDecommissioned`(Is Decommissioned), `riskLevels`(Risk Levels), `osTypes`(OS Types), `extra_parameters`(Additional Fields) |
| `get_cve` | Get CVEs | investigation | ✓ | `ids`(Internal CVE IDs), `cveIds`(Global CVE IDs), `limit`(Limit Records), `skipCount`(Skip Count), `sortBy`(Sort By), `sortOrder`(Sort Order), `countOnly`(Count Only), `cursor`(Cursor), `extra_parameters`(Additional Fields) |
| `export_applications_risk` | Export Applications Risk | investigation | ✓ | `siteIds`(Site IDs), `groupIds`(Group IDs), `accountIds`(Account IDs), `size__between`(Size Between), `agentMachineTypes`(Agent Machine Types), `ids`(Application IDs), `types`(Application Types), `agentIsDecommissioned`(Is Decommissioned), `riskLevels`(Risk Levels), `osTypes`(OS Types), `extra_parameters`(Additional Fields) |
| `get_applications` | Get Applications | investigation | ✓ | `agentMachineTypes`(Agent Machine Types), `ids`(Application IDs), `agentIsDecommissioned`(Is Decommissioned), `types`(Application Types), `riskLevels`(Risk Levels), `limit`(Limit Records), `skipCount`(Skip Count), `sortBy`(Sort By), `sortOrder`(Sort Order), `countOnly`(Count Only), `osTypes`(OS Types), `cursor`(Cursor), `extra_parameters`(Additional Fields) |
| `get_application_cve` | Get Application CVEs | investigation | ✓ | `agent_application_id`(Application ID, REQ) |
| `mark_threat_as_benign` | Mark Threat as Benign | remediation | ✓ | `targetScope`(Target Scope, REQ), `ids`(Threat ID, REQ), `agentId`(Agent ID), `contentHash`(Content Hash), `displayName`(Threat Name), `limit`(Limit Records) |
| `mitigate_threats` | Mitigate Threat | remediation | ✓ | `action`(Action, REQ), `ids`(Threat ID, REQ), `agentId`(Agent ID), `contentHash`(Content Hash), `displayName`(Threat Name), `limit`(Limit Records) |
| `list_all_threats` | List All Threats | investigation | ✓ | `agentIds`(Agent ID), `createdAt__gt`(Created After), `updatedAt__gt`(Updated After), `contentHash`(Content Hash), `displayName`(Threat Name), `limit`(Limit Records), `skip`(Offset), `cursor`(Cursor), `additional_fields`(Additional Fields) |
| `fetch_threats` | Fetch Threats | investigation | ✓ | `createdAt__gt`(Created After), `updatedAt__gt`(Updated After), `query`(Query), `additional_fields`(Additional Fields) |
| `get_threat_events` | Get Threat Events List | investigation | ✓ | `threat_id`(Threat ID, REQ), `eventId`(Event ID), `eventTypes`(Event Type), `eventSubTypes`(Event SubType), `limit`(Limit Records), `skip`(Offset), `cursor`(Cursor), `additional_fields`(Additional Fields) |
| `get_threat_details` | Get Threat Details | investigation | ✓ | `ids`(Threat ID, REQ) |
| `fetch_threat_file` | Fetch Threat File | investigation | ✓ | `ids`(Threat IDs, REQ), `password`(Password, REQ), `additional_fields`(Additional Fields) |
| `get_threat_timeline` | Get Threat Timeline | investigation | ✓ | `id`(Threat ID, REQ), `sortOrder`(Sort Order), `skip`(Offset), `limit`(Limit Records), `cursor`(Cursor), `additional_fields`(Additional Fields) |
| `add_note_to_a_threat` | Add Note to a Threat | investigation | ✓ | `threatID`(Threat ID, REQ), `note`(Note, REQ) |
| `get_threat_notes` | Get Threat Notes | investigation | ✓ | `id`(Threat ID, REQ), `creatorId`(Creator ID), `creator__like`(Creator Name), `sortBy`(Sort By), `sortOrder`(Sort Order), `skip`(Offset), `limit`(Limit Records), `skipCount`(Skip Count), `countOnly`(Count Only), `cursor`(Cursor) |
| `update_threat_note` | Update Threat Note | investigation | ✓ | `id`(Threat ID, REQ), `note_id`(Note ID, REQ), `text`(Text, REQ) |
| `delete_threat_note` | Delete Threat Note | investigation | ✓ | `id`(Threat ID, REQ), `note_id`(Note ID, REQ) |
| `change_incident_status` | Change Incident Status | investigation | ✓ | `threatID`(Threat ID, REQ), `incidentStatus`(Incident Status, REQ) |
| `get_hash_details` | Get Hash Details | investigation | ✓ | `hash_id`(Hash ID, REQ) |
| `agent_action` | Agent Action | containment | ✓ | `action`(Action, REQ), `ids`(Agent IDs, REQ), `groupIds`(Group IDs), `isDecommissioned`(Is Decommissioned), `isUninstalled`(Is Uninstalled) |
| `abort_agent_scan` | Abort Agent Scan | investigation | ✓ | `ids`(Agent IDs), `isActive`(Is Active), `infected`(Is Infected), `isDecommissioned`(Is Decommissioned), `computerName__like`(Computer Name Like), `totalMemory__lte`(Agent Memory Less Than (MB)), `totalMemory__gte`(Agent Memory Greater Than (MB)), `coreCount__lte`(Agent Core Count Less Than), `coreCount__gte`(Agent Core Count Greater Than), `agentVersions`(Agent Version), `osTypes`(OS Type), `networkStatuses`(Network Status), `extra_parameters`(Additional Fields) |
| `fetch_agent_logs` | Fetch Agents Logs | investigation | ✓ | `ids`(Agent IDs), `isActive`(Is Active), `infected`(Is Infected), `isDecommissioned`(Is Decommissioned), `computerName__like`(Computer Name Like), `totalMemory__lte`(Agent Memory Less Than (MB)), `totalMemory__gte`(Agent Memory Greater Than (MB)), `coreCount__lte`(Agent Core Count Less Than), `coreCount__gte`(Agent Core Count Greater Than), `agentVersions`(Agent Version), `osTypes`(OS Type), `networkStatuses`(Network Status) |
| `initiate_agent_scan` | Initiate Agent Scan | investigation | ✓ | `ids`(Agent IDs), `isActive`(Is Active), `infected`(Is Infected), `isDecommissioned`(Is Decommissioned), `computerName__like`(Computer Name Like), `totalMemory__lte`(Agent Memory Less Than (MB)), `totalMemory__gte`(Agent Memory Greater Than (MB)), `coreCount__lte`(Agent Core Count Less Than), `coreCount__gte`(Agent Core Count Greater Than), `agentVersions`(Agent Version), `osTypes`(OS Type), `networkStatuses`(Network Status), `extra_parameters`(Additional Fields) |
| `broadcast_message_to_agent` | Broadcast Message to Agent | miscellaneous | ✓ | `message`(Message, REQ), `ids`(Agent IDs), `isActive`(Is Active), `infected`(Is Infected), `isDecommissioned`(Is Decommissioned), `computerName__like`(Computer Name Like), `totalMemory__lte`(Agent Memory Less Than (MB)), `totalMemory__gte`(Agent Memory Greater Than (MB)), `coreCount__lte`(Agent Core Count Less Than), `coreCount__gte`(Agent Core Count Greater Than), `agentVersions`(Agent Version), `osTypes`(OS Type), `networkStatuses`(Network Status) |
| `reconnect_agent` | Reconnect Agent | remediation | ✓ | `ids`(Agent IDs), `isActive`(Is Active), `infected`(Is Infected), `isDecommissioned`(Is Decommissioned), `computerName__like`(Computer Name Like), `totalMemory__lte`(Agent Memory Less Than (MB)), `totalMemory__gte`(Agent Memory Greater Than (MB)), `coreCount__lte`(Agent Core Count Less Than), `coreCount__gte`(Agent Core Count Greater Than), `agentVersions`(Agent Version), `osTypes`(OS Type), `networkStatuses`(Network Status) |
| `get_agent_passphrase` | Get Agent Passphrase | miscellaneous | ✓ | `ids`(Agent ID), `cursor`(Cursor), `additional_fields`(Additional Fields) |
| `get_agent_application` | Get Agent Application | investigation | ✓ | `ids`(Agent ID, REQ) |
| `get_agents` | Get Agents | investigation | ✓ | `ids`(Agent IDs), `isActive`(Is Active), `infected`(Is Infected), `isDecommissioned`(Is Decommissioned), `computerName__like`(Computer Name Like), `totalMemory__lte`(Agent Memory Less Than (MB)), `totalMemory__gte`(Agent Memory Greater Than (MB)), `coreCount__lte`(Agent Core Count Less Than), `coreCount__gte`(Agent Core Count Greater Than), `agentVersions`(Agent Version), `networkStatuses`(Network Status), `limit`(Limit Records), `skip`(Offset), `cursor`(Cursor), `additional_fields`(Additional Fields) |
| `get_agent_count` | Get Agent Count | miscellaneous | ✓ | `ids`(Agent IDs), `isActive`(Is Active), `infected`(Is Infected), `isDecommissioned`(Is Decommissioned), `computerName__like`(Computer Name Like), `totalMemory__lte`(Agent Memory Less Than (MB)), `totalMemory__gte`(Agent Memory Greater Than (MB)), `coreCount__lte`(Agent Core Count Less Than), `coreCount__gte`(Agent Core Count Greater Than), `agentVersions`(Agent Version), `osTypes`(OS Type), `networkStatuses`(Network Status) |
| `create_blacklist_item` | Create Blocklist Item | investigation | ✓ | `osType`(OS Type, REQ), `hashValue`(SHA-1 Hash Value), `sha256Value`(SHA-256 Hash Value), `description`(Description), `tenant`(Tenant), `accountIds`(Account IDs), `groupIds`(Group IDs), `siteIds`(Site IDs) |
| `get_alerts` | Get Alerts | investigation | ✓ | `additional_fields`(Additional Fields) |
| `custom_endpoint` | Execute an API Request | query | ✓ | `method`(HTTP Method), `endpoint`(API Endpoint, REQ), `body`(Request Parameters/Body) |
| `get_output_schema_threats` | Get Output Schema for Threats | — | ✓ | — |
| `get_output_schema_threat_details` | Get Output Schema for Specific Threat | — | ✓ | — |
| `get_output_schema_agents` | Get Output Schema for Agents | — | ✓ | — |

### `servicenow-cmdb`

version 1.0.0 — ServiceNow Configuration Management Database (CMDB) is a centralized source that gives you full visibility into your IT environment. By stor…

- GitHub: connector-servicenow-cmdb
- Category: IT Services
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_configuration_item` | Create Configuration Item | investigation | ✓ | `class_name`(Class Name, REQ), `source`(Discovery Source, REQ), `name`(Configuration Item Name, REQ), `short_description`(Description), `attributes`(Attributes), `inbound_relations`(Inbound Relations), `outbound_relations`(Outbound Relations) |
| `get_configuration_items` | Get Configuration Items | investigation | ✓ | `class_name`(Class Name, REQ), `sysparm_query`(Query), `sysparm_limit`(Limit), `sysparm_offset`(Offset) |
| `get_configuration_item_details` | Get Configuration Item Details | investigation | ✓ | `class_name`(Class Name, REQ), `sys_id`(System ID, REQ) |
| `update_configuration_item` | Update Configuration Item | investigation | ✓ | `class_name`(Class Name, REQ), `sys_id`(System ID, REQ), `source`(Discovery Source, REQ), `name`(Configuration Item Name), `short_description`(Description), `attributes`(Attributes) |
| `get_cmdb_rel_type` | Get CMDB Relation Type | investigation | ✓ | `sysparm_limit`(Limit), `sysparm_offset`(Offset) |
| `get_cmdb_rel_type_by_sys_id` | Get CMDB Relation Type by System ID | investigation | ✓ | `sys_id`(System ID, REQ) |
| `add_relation_to_configuration_item` | Add Relation to Configuration Item | investigation | ✓ | `class_name`(Class Name, REQ), `sys_id`(System ID, REQ), `source`(Discovery Source, REQ), `inbound_relations`(Inbound Relations), `outbound_relations`(Outbound Relations) |
| `delete_relation_for_configuration_item` | Delete Relation for Configuration Item | investigation | ✓ | `class_name`(Class Name, REQ), `sys_id`(System ID, REQ), `rel_sys_id`(Relation System ID, REQ) |
| `custom_endpoint` | Custom API Endpoint | query | ✓ | `endpoint`(API Endpoint, REQ), `method`(HTTP method), `body`(Request Parameters/Body) |

### `shadowserver`

version 1.0.0 — Shadowserver provides you with access to the most timely, critical Internet security like data collection,network reporting,investigation su…

- GitHub: connector-shadowserver
- Category: Vulnerability and Risk Management
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_origin_query` | Get Origin Query | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_peer_query` | Get Peer Query | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `get_prefix_query` | Get Prefix Query | investigation | ✗ | `query`(Query, REQ) |
| `get_asn_query` | Get ASN Query | investigation | ✗ | `query`(Query, REQ) |
| `get_malware_query` | Get Malware Query | investigation | ✗ | `md5`(MD5, REQ) |
| `get_programs_query` | Get Programs Query | investigation | ✗ | `query`(Query, REQ) |

### `silverfort`

version 1.0.0 — Silverfort delivers adaptive authentication across all corporate networks and cloud environments from a unified platform. This integration i…

- GitHub: connector-silverfort
- Category: Identity and Access Management
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_user_risk` | Get User Risk | investigation | ✓ | `user_identification`(User Identification, REQ) |
| `get_resource_risk` | Get Resource Risk | investigation | ✓ | `resource_name`(Resource Name, REQ), `domain`(Domain, REQ) |
| `update_user_risk` | Update User Risk | investigation | ✓ | `user_identification`(User Identification, REQ), `risk_name`(Risk Name, REQ), `severity`(Severity, REQ), `valid_for`(Valid For, REQ), `description`(Description, REQ) |
| `update_resource_risk` | Update Resource Risk | investigation | ✓ | `resource_name`(Resource Name, REQ), `domain`(Domain, REQ), `risk_name`(Risk Name, REQ), `severity`(Severity, REQ), `valid_for`(Valid For, REQ), `description`(Description, REQ) |

### `smime-messaging`

version 1.0.0 — Secure/Multipurpose Internet Mail Extensions (S/MIME) is an email security protocol that uses encryption to protect the confidentiality and …

- GitHub: connector-smime-messaging
- Category: Email Security
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `sign_email` | Sign Email | investigation | ✓ | `file_name`(File Name, REQ), `body`(Message Body, REQ) |
| `verify_sign` | Verify Sign | investigation | ✓ | `sender_public_key`(Sender's Public Key, REQ), `file_iri`(Attachment/File IRI, REQ) |
| `encrypt_email` | Encrypt Email | investigation | ✓ | `receiver_public_key`(Receiver's Public Key, REQ), `file_name`(File Name, REQ), `body`(Message Body, REQ) |
| `decrypt_email` | Decrypt Email | investigation | ✓ | `file_iri`(Attachment/File IRI, REQ) |

### `snort-ip-blocklist-feed`

version 2.0.0 — Snort is an open-source, free and lightweight network intrusion detection system (NIDS) software for Linux and Windows to detect emerging th…

- GitHub: connector-snort-ip-blocklist-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | — |

### `soc-radar`

version 1.0.0 — Threat Intelligence enriched with External Attack Surface Management and Digital Risk Protection Services

- GitHub: connector-soc-radar
- Category: Attack Surface Management
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_incidents` | Get Incidents | investigation | ✓ | `start_date`(Start Date), `end_date`(End Date), `status`(Status, REQ), `limit`(Limit), `page`(Page) |
| `get_incident` | Get Incident | investigation | ✓ | `alarm_id`(Alarm ID, REQ) |
| `threat_analysis` | Threat Analysis | investigation | ✓ | `entity`(Entity, REQ), `advance_investigation`(Advance Investigation), `force_new_analysis`(Force New Analysis) |
| `change_status` | Change Status | investigation | ✓ | `alarm_id`(Alarm ID, REQ), `status`(Status, REQ), `comments`(Comments, REQ) |

### `solarwinds-pingdom`

version 1.0.0 — Solarwinds Pingdom makes your websites faster and more reliable with easy-to-use web performance and digital experience monitoring.

- GitHub: connector-solarwinds-pingdom
- Category: IT Service Management
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts_list` | Get Alerts List | investigation | ✓ | `checkids`(Check IDs), `from`(Start Datetime), `to`(End Datetime), `status`(Status), `userids`(User IDs), `via`(Via Medium), `limit`(Limit), `offset`(Offset), `fetch_all_records`(Fetch All Records) |
| `get_checks_list` | Get Checks List | investigation | ✓ | `include_severity`(Include Severity), `include_tags`(Include tags), `showencryption`(Show Encryption), `tags`(Tags), `limit`(Limit), `offset`(Offset) |
| `get_root_cause_analysis` | Get Root Cause Analysis | investigation | ✓ | `checkid`(Check ID, REQ), `from`(Start Datetime), `to`(End Datetime), `limit`(Limit), `offset`(Offset) |
| `get_result_of_analysis` | Get Result of Analysis | investigation | ✓ | `analysisid`(Analysis ID, REQ), `checkid`(Check ID, REQ) |
| `get_raw_test_results_list` | Get Raw Test Results List | investigation | ✓ | `checkid`(Check ID, REQ), `from`(Start Datetime), `to`(End Datetime), `maxresponse`(Maximum Response), `minresponse`(Minimum Response), `probes`(Probes), `status`(Status), `limit`(Limit), `offset`(Offset) |

### `sonicwall-firewall`

version 1.1.0 — SonicWall's advanced firewall appliances with various network and security systems. This connector facilitates seamless communication and da…

- GitHub: connector-sonicwall-firewall
- Category: Firewall and Network Protection
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_address_object_configuration` | Create Address Object | investigation | ✓ | `name`(Name, REQ), `zone`(Zone, REQ), `object_type`(Object Type, REQ) |
| `get_address_object_configuration` | Get Address Object | investigation | ✓ | `object_type`(Object Type, REQ), `filter_object_by`(Filter Address Object By) |
| `update_address_object_configuration` | Update Address Object | investigation | ✓ | `update_type`(Update Type, REQ), `update_object_by`(Update Address Object By, REQ), `object_type`(Object Type, REQ), `zone`(Zone, REQ) |
| `delete_address_object_configuration` | Delete Address Object | investigation | ✓ | `object_type`(Object Type, REQ), `delete_object_by`(Delete Address Object By, REQ) |
| `create_address_group` | Create Address Group | investigation | ✓ | `object_type`(Object Type, REQ), `address_group_name`(Address Group Name, REQ), `address_object_name`(Address Object Name, REQ) |
| `get_address_group` | Get Address Group | investigation | ✓ | `object_type`(Object Type, REQ), `filter_object_by`(Filter Address Group By) |
| `update_address_group` | Update Address in Group | investigation | ✓ | `update_type`(Update Type, REQ), `object_type`(Object Type, REQ), `zone`(Zone, REQ) |
| `delete_address_group` | Delete Address From Group | investigation | ✓ | `object_type`(Object Type, REQ), `delete_object_by`(Delete Address Object By, REQ) |
| `add_address_object_to_group` | Add Address Object to Group | investigation | ✓ | `object_type`(Object Type, REQ), `filter_object_by`(Filter Address Group By), `address_object_name`(Address Object Name, REQ) |
| `remove_address_object_from_group` | Remove Address Object from Group | investigation | ✓ | `object_type`(Object Type, REQ), `filter_object_by`(Filter Address Group By), `address_object_name`(Address Object Name, REQ) |

### `sonicwall-nsm`

version 1.0.1 — SonicWall Network Security Manager (NSM) is a cloud-based (or on-prem) platform designed to centrally manage, monitor, and report on SonicWa…

- GitHub: connector-sonicwall-nsm
- Category: Network Security
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_access_rules` | Get Access Rules | investigation | ✓ | `filterType`(Filter Type, REQ), `serialnum`(Device Serial Number), `ruleType`(Rule Type), `limit`(Limit), `limitCount`(Limit Total Count), `childrenObjTypes`(Children Object Types) |
| `create_address_object` | Create Address Object | investigation | ✓ | `name`(Address Object Name, REQ), `zone`(Zone, REQ), `object_type`(Object Type, REQ), `description`(Description), `serialnum`(Device Serial Number) |
| `get_address_objects` | Get Address Object | investigation | ✓ | `name`(Address Object Name/UUID, REQ), `isuuid`(Is UUID), `serialnum`(Device Serial Number) |
| `update_address_object` | Update Address Object | investigation | ✓ | `uuid`(Address Object UUID), `name`(Address Object Name, REQ), `zone`(Zone, REQ), `object_type`(Object Type, REQ), `new_name`(New Address Object Name, REQ), `serialnum`(Device Serial Number) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `spamhaus-feed`

version 1.0.0 — Spamhaus Feed provides access to expansive threat data and related information. This connector facilitates automated operations related to f…

- GitHub: connector-spamhaus-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `output_mode`(Process response as) |

### `ssl-blacklist-feed`

version 1.0.0 — The SSL Blacklist (SSLBL) is a project of abuse.ch with the goal of detecting malicious SSL connections, by identifying and blacklisting SSL…

- GitHub: connector-ssl-blacklist-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `last_pull_time`(Last Pull Time), `output_mode`(Process Response As) |

### `stealthwatch`

version 2.1.0 — Stealthwatch is the solution that detects threats across your private network, public clouds, and even in encrypted traffic.

- GitHub: connector-stealthwatch
- Category: Threat Detector
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `application_traffic_domainid` | Get Application Traffic by Domain ID | investigation | ✓ | `domain_id`(Domain ID, REQ), `start`(Start Time), `end`(End Time) |
| `application_traffic_hostgroupid` | Get Application Traffic by Host Group ID | investigation | ✓ | `domain_id`(Domain ID, REQ), `hostgroupid`(Host Group ID, REQ), `start`(Start Time), `end`(End Time) |
| `application_traffic_ip` | Get Application Traffic by Exporter IP | investigation | ✓ | `domain_id`(Domain ID, REQ), `flowcollectordeviceid`(Flow Collector Device ID, REQ), `exporterip`(Exporter IP Address, REQ), `interface`(Interface ID, REQ), `start`(Start Time), `end`(End Time) |
| `get_domain_details` | Get Domain Details | investigation | ✓ | — |
| `initiate_flow_search` | Initiate Flow Search | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `searchName`(Search Name), `startDateTime`(Start Time, REQ), `endDateTime`(End Time, REQ), `recordLimit`(Number of Records), `subject`(Subject Host Filters), `peer`(Peer Host Filters), `flow`(Flow Metadata Filters) |
| `get_flow_search_status` | Get Flow Search Status | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `query_id`(Query ID, REQ) |
| `get_flow_search_results` | Get Flow Search Results | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `query_id`(Query ID, REQ) |
| `list_host_groups` | Get Host Groups List | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `host_type`(Type, REQ), `hierarchy_view`(Hierarchy View) |
| `get_host_details` | Get Host Group Details | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `host_type`(Type, REQ), `hostGroupId`(Host Group ID) |
| `threats_top_alarms` | Get External Threats Top Alarm Host | investigation | ✓ | `tenantId`(Tenant ID, REQ), `tagId`(External Threat Tag ID, REQ) |
| `top_conversation_flow` | Initiate Top Conversation Flow Search | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `startTime`(Start Time, REQ), `endTime`(End Time, REQ), `searchName`(Search Name), `maxRows`(Number of Records), `orientation`(Orientation), `orderBy`(Order By), `standardOptions`(Default Columns), `excludeBpsPps`(Excludes BPS/PPS), `excludeOthers`(Exclude Other Records), `excludeCounts`(Exclude Counts), `flowCollectors`(Flow Collectors), `subject`(Subject Host Filters), `peer`(Peer Host Filters), `connection`(Connection Filters) |
| `get_top_conversation_status` | Get Top Conversation Flow Search Status | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `query_id`(Query ID, REQ) |
| `get_top_conversation_result` | Get Top Conversation Flow Search Result | investigation | ✓ | `tenant_id`(Tenant ID, REQ), `query_id`(Query ID, REQ) |
| `initiate_flow_analysis` | Initiate Flow Analysis | investigation | ✗ | `tenantID`(Tenant ID, REQ), `flowAnalysis`(Flow Analysis) |

### `stix`

version 1.0.0 — Structured Threat Information Expression, is a language and serialization format for exchanging threat information in cyberspace. Using this…

- GitHub: connector-stix
- Category: Threat Intelligence
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `extract_indicators` | Extract Indicators From STIX File | investigation | ✓ | `file_id`(STIX2 File IRI or Name, REQ), `output_mode`(Process Response As), `confidence`(Confidence), `reputation`(Reputation), `tlp`(TLP), `expiry`(Maximum Age (in Days)) |
| `create_indicators` | Export Indicators In STIX Spec Format | investigation | ✓ | `indicator_list`(FortiSOAR Indicator List, REQ), `tlp`(Traffic Light Protocol Level, REQ), `file_response`(Save Response to File) |
| `create_indicators_output_schema` | Get Create Indicator Output Schema | — | ✓ | — |
| `extract_indicators_output_schema` | Get Extract Indicator Output Schema | — | ✓ | — |

### `sumo-logic`

version 1.1.1 — Sumo Logic provides best-in-class cloud monitoring, log management, Cloud SIEM tools, and real-time insights for web and SaaS based apps.

- GitHub: connector-sumo-logic
- Category: Monitoring
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_search_job` | Create Search Job | investigation | ✓ | `query`(Query, REQ), `from`(From, REQ), `to`(To, REQ), `timeZone`(Time Zone, REQ) |
| `get_search_job_status` | Get Search Job Status | investigation | ✓ | `searchJobId`(Search Job ID, REQ), `cookies`(Cookies, REQ) |
| `get_messages_founded_by_search_job` | Get Messages Founded by Search Job | investigation | ✓ | `searchJobId`(Search Job ID, REQ), `offset`(Offset, REQ), `limit`(Limit, REQ), `cookies`(Cookies, REQ) |
| `get_records_founded_by_search_job` | Get Records Founded by Search Job | investigation | ✓ | `searchJobId`(Search Job ID, REQ), `offset`(Offset, REQ), `limit`(Limit, REQ), `cookies`(Cookies, REQ) |
| `delete_search_job` | Delete Search Job | investigation | ✓ | `searchJobId`(Search Job ID, REQ), `cookies`(Cookies, REQ) |
| `get_list_of_all_insights` | Get the List of All Insights | investigation | ✓ | — |
| `get_details_by_insights_id` | Get Details By Insights ID | investigation | ✓ | `insights_id`(Insights ID, REQ) |
| `get_list_of_insights_by_query` | Get the List of Insights By Query | investigation | ✓ | `query`(Query), `offset`(Offset), `limit`(Limit), `recordSummaryFields`(Record Summary Fields, REQ) |

### `symantec-management-center`

version 1.0.0 — Symantec Management Center provides a unified management environment for the Symantec Security Platform portfolio of products. Management Ce…

- GitHub: connector-symantec-management-center
- Category: Network Security
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_policy` | Create Policy | investigation | ✓ | `name`(Policy name, REQ), `contentType`(Content Type, REQ), `description`(Description), `referenceId`(Reference ID), `tenant`(Tenant), `author`(Author), `shared`(Shared), `replaceVariables`(Replace Variables) |
| `get_policies` | Get Policies | investigation | ✓ | `author`(Author), `contentType`(Content Type), `description`(Description), `name`(Name), `referenceId`(Reference ID), `shared`(Shared), `tenant`(Tenant) |
| `get_policy_details` | Get Policy Details | investigation | ✓ | `uuid`(Policy UUID, REQ) |
| `update_policy` | Update Policy | investigation | ✓ | `uuid`(Policy UUID, REQ), `name`(Policy name), `description`(Description), `referenceId`(Reference ID), `replaceVariables`(Replace Variables) |
| `delete_policy` | Delete Policy | investigation | ✓ | `uuid`(Policy UUID, REQ), `force`(Force Delete) |
| `add_policy_content` | Add or Update Policy Content | investigation | ✓ | `uuid`(Policy UUID, REQ), `changeDescription`(Description), `content`(Content), `contentType`(Content Type), `schemaVersion`(Schema Version) |
| `get_policy_content` | Get Policy Content | investigation | ✓ | `uuid`(Policy UUID, REQ) |
| `get_policy_content_by_version` | Get Policy Content By Version | investigation | ✓ | `uuid`(Policy UUID, REQ), `version`(Version, REQ) |

### `symantec-messaging-gateway`

version 1.2.0 — Symantec Messaging Gateway is an email security solution which provides inbound and outbound messaging security. Also it can perform contain…

- GitHub: connector-symantec-messaging-gateway
- Category: Email Gateway
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `blacklist_email` | Block Email | Containment | ✓ | `email_id`(Email Address, REQ) |
| `unblacklist_email` | Unblock Email | Remediation | ✓ | `email_id`(Email Address, REQ) |
| `blacklist_domain` | Block Domain | Containment | ✓ | `domain`(Domain, REQ) |
| `unblacklist_domain` | Unblock Domain | Remediation | ✓ | `domain`(Domain, REQ) |
| `blacklist_ip` | Block IP | Containment | ✓ | `ip`(IP Address, REQ) |
| `unblacklist_ip` | Unblock IP | Remediation | ✓ | `ip`(IP Address, REQ) |
| `audit_logs_search` | Quick Audit Log Search | investigation | ✓ | `mandatoryFilterId`(Search By, REQ), `mandatoryFilterValue`(Search Value, REQ), `start_time`(Start Time, REQ), `end_time`(End Time, REQ), `entriesPerPage`(Limit), `pageNumber`(Offset) |
| `advanced_audit_logs_search` | Advanced Audit Log Search | investigation | ✓ | `mandatoryFilterId`(Search By, REQ), `mandatoryFilterValue`(Search Value, REQ), `start_time`(Start Time, REQ), `end_time`(End Time, REQ), `remove_none_ascii`(Remove None ASCII characters) |

### `taegis-xdr`

version 1.2.0 — SecureWorks Taegis™ XDR offers superior detection, unmatched response and an open platform built from the ground up to integrate market-lead…

- GitHub: connector-taegis-xdr
- Category: Threat Detection
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_investigation` | Create Investigation | investigation | ✓ | `description`(Description of Investigation, REQ), `key_findings`(Key Findings), `priority`(Investigation's Priority), `status`(Investigation's Status), `assignee_id`(Assignee ID), `alerts`(Alert ID) |
| `get_investigations` | Get Investigations | investigation | ✓ | `query`(Query), `orderByField`(Order By Field), `orderDirection`(Order Direction), `page`(Page), `perPage`(Per Page) |
| `get_investigations_alerts` | Get Investigations Alerts | investigation | ✓ | `investigation_id`(Investigation ID, REQ), `page`(Page), `perPage`(Per Page) |
| `update_investigation` | Update Investigation | investigation | ✓ | `investigation_id`(Investigation ID, REQ), `description`(Description of Investigation), `key_findings`(Key Findings), `priority`(Investigation's Priority), `status`(Investigation's Status), `assignee_id`(Assignee ID) |
| `unarchive_investigation` | Unarchive Investigation | investigation | ✓ | `investigation_id`(Investigation ID, REQ) |
| `add_alerts_to_investigation` | Add Alerts to Investigation | investigation | ✓ | `investigation_id`(Investigation ID, REQ), `alerts`(Alert ID, REQ) |
| `add_events_to_investigation` | Add Events to Investigation | investigation | ✓ | `investigation_id`(Investigation ID, REQ), `events`(Event ID, REQ) |
| `create_comment` | Create Comment | investigation | ✓ | `investigationId`(Investigation ID, REQ), `comment`(Comment, REQ) |
| `get_alerts` | Get Alerts | investigation | ✓ | `cql_query`(CQL Query, REQ), `limit`(Limit), `offset`(Offset) |
| `update_alert_status` | Update Alert Status | investigation | ✓ | `alert_ids`(Alert IDs, REQ), `resolution_status`(Resolution Status, REQ), `reason`(Reason of Status Change, REQ) |
| `get_assets` | Get Assets | investigation | ✓ | `filter_asset_state`(Filter Asset State), `order_by`(Order By), `orderDirection`(Order Direction), `only_most_recent`(Only Most Recent), `limit`(Limit), `offset`(Offset) |
| `isolate_assets` | Isolate Assets | investigation | ✓ | `id`(Asset ID, REQ), `reason`(Reason of Isolation, REQ) |
| `get_user_by_id` | Get User by ID | investigation | ✓ | `id`(User ID, REQ), `tenant_id`(Tenant ID, REQ) |
| `get_endpoint` | Get Endpoint | investigation | ✓ | `id`(Endpoint ID, REQ) |
| `get_playbook_execution` | Get Playbook Execution | investigation | ✓ | `playbookExecutionId`(Playbook Execution ID, REQ) |
| `execute_playbook` | Execute Playbook | investigation | ✓ | `playbookInstanceId`(Playbook Instance ID), `parameters`(JSON Parameters) |

### `taxii2-threat-intel-feed`

version 2.0.0 — TAXII Threat Intel Feed connector acts as a STIX-compliant TAXII client. It connects to user-specified TAXII servers (TAXII v2.1), discovers…

- GitHub: connector-taxii2-threat-intel-feed
- Category: Threat Intelligence
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_collections` | Get Collections | investigation | ✓ | `collectionID`(Collection ID), `headers`(Headers) |
| `get_objects_by_collection_id` | Fetch Indicators | investigation | ✓ | `collectionID`(Collection ID, REQ), `added_after`(Added After), `output_mode`(Process Response As), `fetch_all_records`(Fetch All Records), `headers`(Headers) |
| `get_objects` | Get Objects | investigation | ✓ | `collectionID`(Collection ID, REQ), `added_after`(Added After), `fetch_all_records`(Fetch All Records), `headers`(Headers) |
| `download_indicators` | Download Indicators | investigation | ✓ | `added_after`(Last Pull Time), `fetch_all_records`(Fetch All Records), `headers`(Headers) |
| `get_output_schema` | Get Output Schema | — | ✓ | — |

### `tcp-wave`

version 1.0.0 — TCPWave offers automated DDI (DNS, DHCP, IPAM) workflow management, providing significant benefits to large-scale organizations. It reduces …

- GitHub: connector-tcp-wave
- Category: ['IT Service Management', 'Network Security', 'Compliance and Reporting']
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_object_details_by_ipaddress` | Get Object Details By IP Address | investigation | ✗ | `ip_address`(IP Address, REQ) |
| `check_object_exists` | Check Object Exists | investigation | ✗ | `ip_address`(IP Address, REQ), `organization_name`(Organization Name, REQ) |
| `get_network_details_by_ipaddress` | Get Network Details by IP Address | investigation | ✗ | `ip_address`(IP Address, REQ) |

### `tehtris-edr`

version 1.0.0 — TEHTRIS EDR (Endpoint Detection and Response) is designed to detect, analyze, and respond to security incidents on endpoints (such as comput…

- GitHub: connector-tehtris-edr
- Category: ['Endpoint Security']
- Operations: 41

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_events` | Fetch Events | utilities | ✗ | `fromDate`(From Date, REQ), `toDate`(To Date), `eventId`(Event ID), `countOnly`(Count Only), `byTag`(By Tag), `filterID`(Filter ID), `createdOrModified`(Created or Modified), `offset`(Offset), `limit`(Limit) |
| `list_folders_and_filters` | List Folders and Filters | utilities | ✗ | `name`(Name), `module`(Module), `oldFilterId`(Old Filter ID), `filtersOnly`(Filters Only), `presetFilters`(Preset Filters) |
| `get_filter_by_id` | Get Filter by ID | utilities | ✗ | `filterId`(Filter ID, REQ), `withHistory`(With History) |
| `create_filter` | Create Filter | utilities | ✗ | `name`(Name, REQ), `lvlmin`(Minimum Severity Level, REQ), `lvlmax`(Maximum Severity Level, REQ), `description`(Description, REQ), `module`(Module, REQ) |
| `update_filter` | Update Filter | utilities | ✗ | `filterId`(Filter ID, REQ), `name`(Name, REQ), `lvlmin`(Minimum Severity Level, REQ), `lvlmax`(Maximum Severity Level, REQ), `description`(Description, REQ), `tag`(Tag), `deviceName`(Device Name), `path`(Path), `cmdline`(CMD Line), `sha256`(SHA256), `eventName`(Event Name), `egKBId`(EG Knowledge Base ID), `module`(Module) |
| `delete_filter` | Delete Filter | utilities | ✗ | `filterId`(Filter ID, REQ) |
| `set_event_status` | Set an event status | utilities | ✗ | `id`(Event ID, REQ), `status`(New Status, REQ), `oldStatus`(Old Status) |
| `get_all_endpoints` | Get All Endpoints | utilities | ✗ | `hostname`(Hostname), `hostnameRegex`(Hostname Regex), `domain`(Domain), `domainRegex`(Domain Regex), `network`(Network), `firstSeenFrom`(First Seen From), `firstSeenTo`(First Seen To), `lastSeenFrom`(Last Seen From), `lastSeenTo`(Last Seen To), `offset`(Offset), `tags`(Tags), `versions`(Versions), `configUuid`(Config UUIDs), `uuids`(UUIDs), `applianceIds`(Appliance IDs), `os`(OS) |
| `get_isolation_status` | Get Isolation Status | utilities | ✗ | `applianceId`(Appliance ID, REQ), `edrUuid`(EDR UUID, REQ) |
| `send_isolation_action` | Send Isolation Action | utilities | ✗ | `applianceId`(Appliance ID, REQ), `edrUuid`(EDR UUID, REQ), `isolationAction`(Isolation Action, REQ), `toWhitelist`(WhiteList), `power`(Power), `persist`(Persist) |
| `get_all_global_policies` | Get All Global Policies | utilities | ✗ | — |
| `create_new_global_policies` | Create New Global Policies | utilities | ✗ | `position`(Upsert/Downsert, REQ), `policyData`(Policy Data, REQ) |
| `get_tags` | Get Tags | utilities | ✗ | — |
| `update_endpoints_tags` | Update Endpoints Tags | utilities | ✗ | `edrUuidList`(EDR UUID List, REQ), `tags`(Tags, REQ) |
| `get_accesslogs` | Get Access Logs | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `hostname`(Hostname), `admin`(Admin), `logonEventTimeFrom`(Logon Event Time From), `logonEventTimeTo`(Logon Event Time To), `limit`(Limit, REQ), `offset`(Offset) |
| `get_users_connected` | Get Users Connected | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `hostname`(Hostname), `limit`(Limit, REQ), `offset`(Offset) |
| `get_network_infos` | Get Network Information | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `hostname`(Hostname) |
| `get_history_of_processes` | Get Processes History | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `userIdentifier`(User Identifier), `username`(Username), `domainName`(Domain Name), `localTime`(Local Time), `timeFilter`(Time Filter), `timeFrom`(Time From), `timeTo`(Time To), `sha256`(SHA256), `sha1`(SHA1), `md5`(MD5), `path`(Path), `cmdline`(CMD Line), `limit`(Limit, REQ), `offset`(Offset), `pids`(Process IDs), `ppids`(Parent Process IDs), `logonIds`(Logon IDs) |
| `get_process_tree` | Get Process Tree | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `pid`(Process ID, REQ), `createTime`(Created Time, REQ), `nbParents`(Number of Parents, REQ), `limit`(Limit, REQ), `offset`(Offset) |
| `get_persistence_entries` | Get Persistence Entries | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `localTime`(Local Time), `t`(Time Filter), `persistence_path`(Persistence Path), `persistence_type`(Persistence Type), `name`(Name), `sha256`(SHA256), `sha1`(SHA1), `md5`(MD5), `path`(Path), `cmdline`(CMD Line), `limit`(Limit, REQ), `offset`(Offset) |
| `get_usb_history` | Get USB History | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `hostname`(Hostname) |
| `get_browser_security` | Get Browser Security | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `hostname`(Hostname) |
| `get_software_list` | Get Software List | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `persist`(Persist) |
| `fetch_info_about_endpoint` | Fetch Endpoint Details | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ) |
| `get_last_offline_forensic_report` | Get Last Offline Forensic Report | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ) |
| `get_offline_forensic_status` | Get Offline Forensic Status | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ) |
| `start_offline_forensic` | Start Offline Forensic | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `persist`(Persist), `processes`(Processes), `startup`(Startup), `disk`(Disk), `privacy`(Privacy), `advanced`(Advanced), `commands`(Commands), `yara`(Yara), `forensic`(Forensic), `diskPaths`(Disk Paths), `extensions`(Extensions) |
| `stop_offline_forensic` | Stop Offline Forensic | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ) |
| `search_binaries` | Search Binaries | utilities | ✗ | `applianceId`(Appliance ID, REQ), `hostname`(Hostname), `hostnameRegex`(Hostname Regex), `sha256`(SHA256), `sha1`(SHA1), `md5`(MD5), `path`(Path), `pathRegex`(Path Regex), `signatureCn`(Signature CN), `signatureCnRegex`(Signature CN Regex), `lastSeenFrom`(Last Seen From), `lastSeenTo`(Last Seen To), `offset`(Offset) |
| `search_user_accesslogs` | Search User Access Logs | utilities | ✗ | `applianceId`(Appliance ID, REQ), `username`(Username), `usernameRegex`(Username Regex), `logonEventTimeFrom`(Logon Event Time From), `logonEventTimeTo`(Logon Event Time To), `logoffEventTimeFrom`(Logoff Event Time From), `logoffEventTimeTo`(Logoff Event Time To), `limit`(Limit, REQ), `offset`(Offset) |
| `search_persistent_entries_category` | Search Persistent Entries by Category | utilities | ✗ | `category`(Category, REQ), `applianceId`(Appliance ID, REQ), `hostname`(Hostname), `hostnameRegex`(Hostname Regex), `pathRegex`(Path Regex), `cmdlineRegex`(CMD Line Regex), `signatureCn`(Signature CN), `signatureCnRegex`(Signature CN Regex), `persistencePath`(Persistence Path), `persistencePathRegex`(Persistence Path Regex), `persistenceType`(Persistence Type), `persistenceTypeRegex`(Persistence Type Regex), `name`(Name), `nameRegex`(Name Regex), `sha256`(SHA256), `sha1`(SHA1), `md5`(MD5), `path`(Path), `cmdline`(CMD Line), `createdFrom`(Created From), `createdTo`(Created To), `deletedFrom`(Deleted From), `deletedTo`(Deleted To), `limit`(Limit, REQ), `offset`(Offset) |
| `search_persistent_entries` | Search Persistent Entries | utilities | ✗ | `applianceId`(Appliance ID, REQ), `hostname`(Hostname), `hostnameRegex`(Hostname Regex), `path`(Path), `pathRegex`(Path Regex), `cmdline`(CMD Line), `cmdlineRegex`(CMD Line Regex), `signatureCn`(Signature CN), `signatureCnRegex`(Signature CN Regex), `persistencePath`(Persistence Path), `persistencePathRegex`(Persistence Path Regex), `persistenceType`(Persistence Type), `persistenceTypeRegex`(Persistence Type Regex), `name`(Name), `nameRegex`(Name Regex), `sha256`(SHA256), `sha1`(SHA1), `md5`(MD5), `createdFrom`(Created From), `createdTo`(Created To), `deletedFrom`(Deleted From), `deletedTo`(Deleted To), `limit`(Limit, REQ), `offset`(Offset) |
| `get_disk_scan_status` | Get Disk Scan Status | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `scanId`(Scan ID) |
| `launch_disk_scan` | Launch Disk Scan | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `persist`(Persist), `scanADS`(Scan ADS), `scanWhitelistPaths`(Scan White List Paths), `startFolders`(Start Folders) |
| `get_current_scan_status` | Get Current Scan Status | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ) |
| `stop_current_scan` | Stop Current Scan | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ) |
| `list_quarantine_files` | Get All Quarantine Files | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ) |
| `quarantine_file` | Quarantine a File | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `path`(Path, REQ), `persist`(Persist), `notification`(Notification) |
| `restore_file_from_quarantine` | Restore File from Quarantine | utilities | ✗ | `edrUuid`(EDR UUID, REQ), `applianceId`(Appliance ID, REQ), `path`(Path, REQ), `persist`(Persist) |
| `get_unmanaged_hosts` | Get Unmanaged Hosts | utilities | ✗ | `applianceId`(Appliance ID, REQ), `lastSeenFrom`(Last Seen From), `lastSeenTo`(Last Seen To), `limit`(Limit), `offset`(Offset) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `teradata-db`

version 1.0.0 — Teradata DB is one of the popular Relational Database Management System. It is mainly suitable for building large scale data warehousing app…

- GitHub: connector-teradata-db
- Category: Database
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_list_of_all_databases` | Get List Of All Databases | investigation | ✗ | `system_name`(System Name, REQ) |
| `get_specific_database_by_name` | Get Specific Database By Name | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ) |
| `get_list_of_all_functions` | Get List Of All Functions | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ) |
| `get_list_of_all_macros` | Get List Of All Macros | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ) |
| `get_list_of_all_procedures` | Get List Of All Procedures | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ) |
| `get_list_of_all_tables` | Get List Of All Tables | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ) |
| `get_specific_table_by_name` | Get Specific Table By Name | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ), `table_name`(Table Name, REQ) |
| `get_list_of_all_views` | Get List Of All Views | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ) |
| `get_specific_view_by_name` | Get Specific View By Name | investigation | ✗ | `system_name`(System Name, REQ), `database_name`(Database Name, REQ), `view_name`(View Name, REQ) |
| `get_list_of_all_queries` | Get List Of All Queries | investigation | ✗ | `system_name`(System Name, REQ), `session`(Session), `state`(State), `clientId`(Client ID) |
| `submit_a_query` | Submit A Query | investigation | ✗ | `system_name`(System Name, REQ), `query_request`(Query Request, REQ) |
| `get_query_by_id` | Get Query By Id | investigation | ✗ | `system_name`(System Name, REQ), `id`(ID, REQ) |
| `get_query_results_by_id` | Get Query Results By ID | investigation | ✗ | `system_name`(System Name, REQ), `id`(ID, REQ), `row_offset`(Row Offset), `row_limit`(Row Limit) |
| `get_list_of_all_systems` | Get List Of All Systems | investigation | ✗ | — |

### `text-utility`

version 1.1.0 — Utilities to process text with features like sentences similarity, OCR and macro extractions from MS Office documents

- GitHub: connector-text-utility
- Category: Utility
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `sentence_similarity` | Get Sentences Similarity | utility | ✓ | `sentence`(Sentence, REQ), `sentences_to_compare_with`(Sentences To Compare, REQ) |
| `image_to_text` | Image to Text OCR | utility | ✓ | `image_iri`(Image IRI, REQ) |
| `extract_macros` | Extract Macros | utility | ✓ | `file_iri`(File IRI, REQ) |

### `thehive`

version 1.0.0 — TheHive Security Incident Response Platform involves connecting external security tools, systems, or data sources with TheHive's platform. T…

- GitHub: connector-thehive
- Category: Case Management
- Operations: 21

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_alert` | Create Alert | investigation | ✓ | `title`(Title, REQ), `description`(Description, REQ), `type`(Source Reference, REQ), `source`(Source, REQ), `type`(Alert Type, REQ), `severity`(Severity), `assignee`(Assignee), `summary`(Summary), `attachment`(Attachment), `observables`(Observables), `additional_field`(Additional Field) |
| `get_alert` | Get Alert | investigation | ✓ | `alertID`(Alert ID, REQ) |
| `update_alerts` | Update Alerts | investigation | ✓ | `action_type`(Action Type, REQ), `title`(Title), `description`(Description), `source`(Source), `type`(Alert Type), `severity`(Severity), `assignee`(Assignee), `summary`(Summary), `additional_field`(Additional Field) |
| `delete_alert` | Delete Alert | investigation | ✓ | `alertID`(Alert ID, REQ) |
| `add_alert_attachment` | Add Alert Attachment | investigation | ✓ | `alertID`(Alert ID, REQ), `attachment`(Attachment, REQ), `canRename`(Can Rename) |
| `get_alert_attachment` | Get Alert Attachment | investigation | ✓ | `alertID`(Alert ID, REQ), `attachmentId`(Attachment ID, REQ) |
| `delete_alert_attachment` | Delete Alert Attachment | investigation | ✓ | `alertID`(Alert ID, REQ), `attachmentId`(Attachment ID, REQ) |
| `download_alert_attachment` | Download Alert Attachment | investigation | ✓ | `alertID`(Alert ID, REQ), `attachmentId`(Attachment ID, REQ) |
| `create_case` | Create Case | investigation | ✓ | `title`(Title, REQ), `description`(Description, REQ), `summary`(Summary), `assignee`(Assignee), `severity`(Severity), `status`(Status), `additional_field`(Additional Field) |
| `get_case` | Get Case | investigation | ✓ | `caseID`(Case ID, REQ) |
| `update_case` | Update Case | investigation | ✓ | `action_type`(Action Type, REQ), `title`(Title), `description`(Description), `summary`(Summary), `assignee`(Assignee), `severity`(Severity), `status`(Status), `additional_field`(Additional Field) |
| `delete_case` | Delete Case | investigation | ✓ | `caseID`(Case ID, REQ) |
| `create_observable_in_case` | Create Observable in Case | investigation | ✗ | `caseID`(Case ID, REQ), `dataType`(Data Type, REQ), `message`(Message), `tags`(Tags), `tlp`(TLP), `ignoreSimilarity`(Ignore Similarity), `additional_field`(Additional Field) |
| `create_observable_in_alert` | Create Observable in Alert | investigation | ✗ | `alertID`(Alert ID, REQ), `dataType`(Data Type, REQ), `message`(Message), `tags`(Tags, REQ), `ignoreSimilarity`(Ignore Similarity), `additional_field`(Additional Field) |
| `get_observable` | Get Observable | investigation | ✓ | `observableId`(Observable ID, REQ) |
| `update_observable` | Update Observable | investigation | ✗ | `action_type`(Action Type, REQ), `dataType`(Data Type, REQ), `message`(Message), `addTags`(Add Tags), `removeTags`(Remove Tags), `ignoreSimilarity`(TLP), `additional_field`(Additional Field) |
| `delete_observable` | Delete Observable | investigation | ✓ | `observableId`(Observable ID, REQ) |
| `create_task` | Create Task in Case | investigation | ✓ | `caseId`(Case ID, REQ), `title`(Title, REQ), `description`(Description), `status`(Status), `group`(Group), `assignee`(Assignee), `additional_field`(Additional Field) |
| `get_task` | Get Task | investigation | ✓ | `TaskID`(Task ID, REQ) |
| `update_task` | Update Task | investigation | ✗ | `action_type`(Action Type, REQ), `title`(Title), `description`(Description), `status`(Status), `group`(Group), `assignee`(Assignee), `additional_field`(Additional Field) |
| `delete_task` | Delete Task | investigation | ✓ | `taskID`(Task ID, REQ) |

### `threat-intelligence-platform`

version 1.0.0 — Threat Intelligence Platform combines several threat intelligence sources to provide in-depth insights on threat hosts and attack infrastruc…

- GitHub: connector-threat-intelligence-platform
- Category: Threat Intelligence
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_domain_infrastructure_analysis_details` | Get Domain Infrastructure Analysis Details | investigation | ✗ | `domain_name`(Domain Name, REQ) |
| `get_ssl_certificate_chain_details` | Get SSL Certificate Chain Details | investigation | ✗ | `domain_name`(Domain Name, REQ) |
| `get_ssl_configuration_analysis_details` | Get SSL Configuration Analysis Details | investigation | ✗ | `domain_name`(Domain Name, REQ) |
| `get_domain_malware_check_details` | Get Domain Malware Check Details | investigation | ✗ | `domain_name`(Domain Name, REQ) |
| `get_connected_domains_details` | Get Connected Domains Details | investigation | ✗ | `domain_name`(Domain Name, REQ) |
| `get_domain_reputation_details` | Get Domain Reputation  Details | investigation | ✗ | `domain_name`(Domain Name, REQ), `mode`(Mode, REQ), `query_type`(Query Type, REQ) |

### `threat-miner`

version 1.0.0 — ThreatMiner is a threat intelligence portale that aggregates data from multiple open-source platforms like: VirusTotal, CIRCL etc... and ena…

- GitHub: connector-threat-miner
- Category: Threat Intelligence
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_domain_details` | Get Domain Details | investigation | ✗ | `domain_name`(Domain Name, REQ), `query_type`(Query Type, REQ) |
| `get_ip_details` | Get IP Details | investigation | ✗ | `ip_address`(IP Address, REQ), `query_type`(Query Type, REQ) |
| `get_file_hash_details` | Get File Hash Details | investigation | ✗ | `file_hash`(File Hash, REQ), `query_type`(Query Type, REQ) |
| `get_import_hash_details` | Get Import Hash Details | investigation | ✗ | `imphash`(Import Hash, REQ) |
| `get_ssdeep_details` | Get SSDeep Details | investigation | ✗ | `ssdeep`(SSDeep, REQ) |
| `get_email_details` | Get Email Details | investigation | ✗ | `email`(Email (Reverse WHOIS), REQ) |

### `threatbook`

version 1.0.0 — ThreatBook is China’s first security threat intelligence company, dedicated to providing real-time, accurate and actionable threat intellige…

- GitHub: connector-threatbook
- Category: Threat Intelligence
- Operations: 13

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `submit_ip` | Submit IP for Analysis | investigation | ✓ | `resource`(IP Address, REQ), `exclude`(Exclude), `lang`(Language) |
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `resource`(IP Address, REQ), `lang`(Language) |
| `domain_analysis` | Submit Domain for Analysis | investigation | ✓ | `resource`(Domain Name, REQ), `exclude`(Exclude), `lang`(Language) |
| `loss_detection` | Get Loss Detection Data | investigation | ✓ | `resource`(Resource, REQ), `lang`(Language) |
| `submit_file` | Submit File | investigation | ✓ | `input`(Type, REQ), `value`(Reference ID, REQ), `sandbox_type`(Sandbox Type), `run_time`(Run Time) |
| `get_file_reputation` | Get File Reputation | investigation | ✓ | `hash_type`(Hash Type, REQ), `hash_value`(Hash Value, REQ), `sandbox_type`(Sandbox Type), `query_fields`(Query Fields) |
| `file_detection_report` | Get File Detection Report | investigation | ✓ | `hash_type`(Hash Type, REQ), `hash_value`(Hash Value, REQ) |
| `scan_url` | Submit URL for Scanning | investigation | ✓ | `url`(URL, REQ) |
| `get_url_reputations` | Get URL Reputations | investigation | ✓ | `url`(URL, REQ) |
| `run_ip_advance_query` | Run IP Advance Query | investigation | ✓ | `resource`(IP Address, REQ), `exclude`(Exclude, REQ), `lang`(Language) |
| `run_domain_advance_query` | Run Domain Advanced Query | investigation | ✓ | `resource`(Domain Name, REQ), `exclude`(Exclude), `lang`(Language) |
| `run_sub_domain_query` | Run Sub Domain Query | investigation | ✓ | `resource`(Domain Name, REQ), `lang`(Language) |
| `get_domain_name_context` | Get Domain Name Context | investigation | ✓ | `resource`(Domain Name, REQ), `lang`(Language) |

### `threatstream`

version 2.5.1 — Anomali ThreatStream offers the most comprehensive Threat Intelligence Platform, allowing organizations to access all intelligence feeds and…

- GitHub: connector-threatstream
- Category: Threat Intelligence
- Operations: 35

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `domain_reputation` | Get Domain Reputation | investigation | ✓ | `value`(Domain Name, REQ), `filter_option`(Filter Options, REQ), `record_number`(Number of Records to Return) |
| `email_reputation` | Get Email ID Reputation | investigation | ✓ | `value`(Email ID, REQ), `filter_option`(Filter Options, REQ), `record_number`(Number of Records to Return) |
| `ip_reputation` | Get IP Reputation | investigation | ✓ | `value`(IP Address, REQ), `filter_option`(Filter Options, REQ), `record_number`(Number of Records to Return) |
| `file_reputation` | Get File Reputation | investigation | ✓ | `value`(Filehash, REQ), `filter_option`(Filter Options, REQ), `record_number`(Number of Records to Return) |
| `url_reputation` | Get URL Reputation | investigation | ✓ | `value`(URL, REQ), `filter_option`(Filter Options, REQ), `record_number`(Number of Records to Return) |
| `whois_domain` | Get Whois Domain Information | investigation | ✓ | `value`(Domain Name, REQ) |
| `whois_ip` | Get Whois IP Information | investigation | ✓ | `value`(IP Address, REQ) |
| `filter_language_query` | Run Filter Language Query | investigation | ✓ | `value`(Filter Query, REQ), `record_number`(Number of Records to Return) |
| `advance_query` | Run Advanced Search | investigation | ✓ | `value`(Advanced Query, REQ), `record_number`(Number of Records to Return) |
| `submit_observables` | Submit Observables | investigation | ✓ | `reference_id`(Attachment IRI), `data`(Observable data), `confidence`(Confidence, REQ), `source_confidence_weight`(Source Confidence Weight), `severity`(Severity, REQ), `classification`(Classification, REQ), `expiration_ts`(Expiration Time Stamp), `notes`(Tags), `ip_mapping`(IP Indicator Type), `domain_mapping`(Domain Indicator Type), `url_mapping`(URL Indicator Type), `email_mapping`(Email Indicator Type), `md5_mapping`(MD5 Indicator Type), `trusted_circles`(Trusted Circle IDs), `threat_type`(Threat Type), `require_approval`(Approval Required), `reject_benign`(Exclude Observables) |
| `get_import_job_status` | Get Import Job Status | investigation | ✓ | `value`(Import Session ID, REQ) |
| `get_import_jobs` | Get Import Job Details | investigation | ✓ | `value`(Search Query, REQ), `record_number`(Number of Records to Return) |
| `approve_import_job` | Approve IOC By Import ID | investigation | ✓ | `value`(Job ID, REQ) |
| `reject_import_job` | Reject IOC By Import ID | investigation | ✓ | `value`(Job ID, REQ) |
| `create_incident` | Create Incident | investigation | ✓ | `name`(Name, REQ), `is_public`(Is Incident Public or Private), `tags`(Tags), `intelligence`(Intelligence), `tlp`(TLP), `fields`(Fields to Include with the Incident) |
| `fetch_incidents` | Get Incident List | investigation | ✓ | `value`(Search Query), `limit`(Limit), `offset`(Offset) |
| `list_incidents_by_indicator` | Get Incident List By Indicator | investigation | ✓ | `value`(Intelligence value to filter, REQ), `limit`(Limit), `offset`(Offset) |
| `get_incident` | Get Incident | investigation | ✓ | `value`(Incident ID, REQ) |
| `update_incident` | Update Incident | investigation | ✓ | `value`(Incident ID, REQ), `name`(Incident Name), `status`(Status), `status_desc`(Status Description), `fields`(Fields to Update on Incident) |
| `delete_incident` | Delete Incident | investigation | ✓ | `value`(Incident ID, REQ) |
| `create_threat_bulletin` | Create Threat Bulletin | investigation | ✓ | `name`(Name, REQ), `body_content_type`(Format Used for Description), `body`(Description), `is_public`(Is Threat Bulletin Public or Private), `tlp`(TLP), `reference_id`(Add an Attachment), `fields`(Fields to Include with the Threat Bulletin) |
| `update_threat_bulletin` | Update Threat Bulletin | investigation | ✓ | `tb_id`(Threat Bulletin ID, REQ), `name`(Threat Bulletin Name), `status`(Publication Status), `reference_id`(Add an Attachment), `fields`(Fields to Update on Threat Bulletin) |
| `list_threat_bulletins` | Get Threat Bulletin List | investigation | ✓ | `query`(Search Query), `record_number`(Number of Records to Return) |
| `list_threat_model_entity` | Get Threat Bulletin Entities | investigation | ✓ | `id`(Threat Bulletin ID, REQ), `entity_type`(Entity Type, REQ), `record_number`(Number of Records to Return) |
| `list_observables_associated_threat_bulletin` | Get Threat Bulletin Observables | investigation | ✓ | `value`(Threat Bulletin ID, REQ), `record_number`(Number of Records to Return) |
| `submit_urls_files` | Submit URLs or Files to Sandbox | investigation | ✓ | `classification`(Classification of the Sandbox Submission, REQ), `sandbox_type`(Sandbox, REQ), `sample_type`(Sample type, REQ), `detail`(Tags, REQ), `use_premium_sandbox`(Use Premium Sandbox), `trusted_circles`(Trusted Circle IDs) |
| `get_submit_url_status` | Get Sandbox Status of Submitted URL/File | investigation | ✓ | `value`(Report ID, REQ) |
| `get_submitted_url_report` | Get Sandbox Report of Submitted URL/File | investigation | ✓ | `value`(Sandbox Report ID, REQ) |
| `intelligence_enrichments` | Get Intelligence Enrichments | investigation | ✓ | `services`(Third Party TI, REQ) |
| `get_status` | Get Status | — | ✓ | — |
| `list_incidents` | Get Incidents List | investigation | ✗ | `limit`(Limit), `offset`(Offset), `value`(Intelligence value to filter) |
| `list_investigations` | List Investigations | investigation | ✓ | `investigation_id`(Investigation ID), `name`(Investigation Name), `status`(Status), `add_related_indicators`(Add Related Indicators), `remote_api`(Remote API), `created_ts__gte`(Date From), `created_ts__lte`(Date To), `record_number`(Number of Records to Return) |
| `create_investigation` | Create Investigation | investigation | ✓ | `name`(Name, REQ), `status`(Status), `priority`(Priority), `tlp`(TLP), `description`(Description), `additional_attributes`(Additional Attributes) |
| `update_investigation` | Update Investigation | investigation | ✓ | `investigation_id`(Investigation ID, REQ), `name`(Name), `status`(Status), `priority`(Priority), `tlp`(TLP), `description`(Description), `additional_attributes`(Additional Attributes) |
| `list_investigation_elements` | List Investigation Elements | investigation | ✓ | `investigation_id`(Investigation ID), `add_related_indicators`(Add Related Indicators), `record_number`(Number of Records to Return) |

### `threatx`

version 1.0.0 — Use the ThreatX integration to enrich intel and automate enforcement actions on the ThreatX Next Gen WAF.

- GitHub: connector-threatx
- Category: Network Security
- Operations: 9

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `block_ip` | Block IP Address | investigation | ✓ | `ip_address`(IP Address, REQ), `description`(Description) |
| `unblock_ip` | Unblock IP Address | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `blacklist_ip` | Blacklist IP Address | investigation | ✓ | `ip_address`(IP Address, REQ), `description`(Description) |
| `unblacklist_ip` | Unblacklist IP Address | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `whitelist_ip` | Whitelist IP Address | investigation | ✓ | `ip_address`(IP Address, REQ), `description`(Description) |
| `unwhitelist_ip` | Unwhitelist IP Address | investigation | ✓ | `ip_address`(IP Address, REQ) |
| `get_entities` | Get Entities | investigation | ✓ | `first_seen`(Timeframe, REQ), `ip_address`(IP Address), `entity_ids`(Entity IDs), `codenames`(Codenames), `actor_ids`(Actor IDs), `attack_ids`(Attack IDs) |
| `get_entity_notes` | Get Entity Notes | investigation | ✓ | `id`(Entity ID, REQ) |
| `add_entity_note` | Add Entity Notes | investigation | ✓ | `id`(Entity ID, REQ), `content`(Content, REQ) |

### `time-series-chart-utilities`

version 1.0.0 — When using the Time Series Chart Solution Pack, this connector is used by the included playbooks to facilitate the creation of data-over-tim…

- GitHub: connector-time-series-chart-utilities
- Category: Utilities
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `assemble_query_time_windows` | Assemble Query Time Windows | utilities | ✗ | `relativeDate`(Relative Date, REQ), `time_period`(Time Period, REQ), `dateFormatString`(Date Format String, REQ), `existing_times`(Existing Times), `query_modified`(Query Modified) |
| `flatten_data_sets_and_groups` | Flatten Data Sets and Groups | utilities | ✗ | `dataSets`(Data Sets, REQ) |
| `format_data_set_output_with_fieldgrouped` | Format Data Set Output with Field-Grouped | utilities | ✗ | `queryOutput`(Query Results, REQ), `timeBucketsQueried`(Time Buckets Queried, REQ), `dataSetConfiguration`(Data Set Configuration, REQ) |
| `combine_query_results_into_data_columns` | Combine Query Results into Data Columns | utilities | ✗ | `playbookMode`(Playbook Mode), `firstIndexToKeep`(First Index to Keep), `queriedTimeBuckets`(Queried Time Buckets), `queryResults`(Query Results, REQ), `existingDataColumns`(Existing Data Columns) |

### `tor-exit-address-feed`

version 1.0.0 — The Tor Exit List service maintains lists of IP addresses used by all exit relays in the Tor network. Service providers may find it useful t…

- GitHub: connector-tor-exit-address-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | — |

### `trello`

version 1.0.0 — Trello is a collaboration tool that organizes your projects into boards. Trello tells you what's being worked on, who's working on what, and…

- GitHub: connector-trello
- Category: Case Management
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_list` | Get a List | investigation | ✓ | `list_id`(List ID, REQ) |
| `get_board` | Get a Board | investigation | ✓ | `board_id`(Board ID, REQ) |
| `create_label` | Create a Label | investigation | ✓ | `name`(Label Name, REQ), `color`(Color, REQ), `idBoard`(Board ID, REQ) |
| `get_label` | Get a Label | investigation | ✓ | `label_id`(Label ID, REQ) |
| `create_card` | Create a new Card | investigation | ✓ | `idList`(List ID, REQ), `name`(Card Name), `desc`(Card Description), `other_fields`(Other Fields) |
| `get_card` | Get a Card | investigation | ✓ | `card_id`(Card ID, REQ), `other_fields`(Other Fields) |
| `update_card` | Update a Card | investigation | ✓ | `card_id`(Card ID, REQ), `name`(Card Name), `desc`(Card Description), `other_fields`(Other Fields) |
| `delete_card` | Delete a Card | investigation | ✓ | `card_id`(Card ID, REQ) |

### `trend-micro-cloud-app-security`

version 1.0.0 — Trend Micro Cloud App Security provides advanced protection for the following cloud applications and services to enhance security with power…

- GitHub: connector-trend-micro-cloud-app-security
- Category: Cloud Security
- Operations: 10

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_security_logs` | Get Security Logs | investigation | ✓ | `service`(Service, REQ), `event`(Event Type, REQ), `start`(Start Date), `end`(End Date), `limit`(Number Of Logs To Retrieve), `get_all_pages`(Get All Pages) |
| `get_virtual_analyzer_report` | Get Virtual Analyzer Report | investigation | ✓ | `report_id`(Report ID, REQ) |
| `get_quarantine_events` | Get Quarantine Events | investigation | ✓ | `service`(Service, REQ), `start`(Start Date), `end`(End Date), `limit`(Number Of Quarantine Events To Retrieve), `get_all_pages`(Get All Pages) |
| `get_email` | Get Email | investigation | ✓ | `mailbox`(Mailbox), `lastndays`(Last N Days), `start`(Start Date), `end`(End Date), `subject`(Subject), `file_sha1`(File SHA1), `file_sha256`(File SHA256), `file_name`(File Name), `file_extension`(File Extension), `url`(URL), `sender`(Sender), `recipient`(Recipient), `message_id`(Message ID), `source_ip`(Source IP), `source_domain`(Source Domain), `limit`(Number Of Email Messages To Retrieve), `get_all_pages`(Get All Pages) |
| `take_action_on_user` | Take Action On User | investigation | ✓ | `action_type`(Action Type, REQ), `service`(Service, REQ), `account_provider`(Account Provider, REQ), `account_user_email`(Account User Email, REQ) |
| `take_action_on_email` | Take Action On Email | investigation | ✓ | `action_type`(Action Type, REQ), `service`(Service, REQ), `account_provider`(Account Provider, REQ), `mailbox`(Mail Box, REQ), `mail_message_id`(Mail Message ID, REQ), `mail_unique_id`(Mail Unique ID, REQ), `mail_message_delivery_time`(Mail Message Delivery Time, REQ), `detection_time`(Detection Time, REQ), `mail_log_id`(Mail Log ID, REQ) |
| `get_user_action_result` | Get User Action Result | investigation | ✓ | `batch_id`(Batch ID, REQ), `start`(Start Date), `end`(End Date), `limit`(Number Of Records To Retrieve), `get_all_pages`(Get All Pages) |
| `get_email_action_result` | Get Email Action Result | investigation | ✓ | `batch_id`(Batch ID, REQ), `start`(Start Date), `end`(End Date), `limit`(Number Of Records To Retrieve), `get_all_pages`(Get All Pages) |
| `get_blocked_list` | Get Blocked List | investigation | ✓ | — |
| `update_blocked_list` | Update Blocked List | investigation | ✓ | `action_type`(Action Type, REQ), `senders`(Senders), `urls`(URL's), `filehashes`(File SHA-1 Hashes), `file256hashes`(File SHA-256 Hashes) |

### `trend-micro-sms`

version 1.1.0 — Trend Micro SMS(Security Management System) Provides global vision and security policy control for threat intelligence and enables comprehen…

- GitHub: connector-trend-micro-sms
- Category: Threat Intelligence
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `import_reputation_bulk` | Import Reputation | investigation | ✓ | `input_file`(Import File, REQ), `address_type`(Address Type) |
| `add_reputation_entry` | Add Reputation Entry | investigation | ✓ | `address_type`(Address Type, REQ), `address_value`(Address values, REQ), `tag_data`(Tag Data) |
| `delete_reputation_entry` | Delete Reputation Entries | investigation | ✓ | `ip_list`(List OF IPs), `dns_list`(List OF DNS), `url_list`(List OF URLs), `criteria`(Criteria) |
| `delete_reputation_bulk` | Delete Reputation | investigation | ✓ | `input_file`(Import File, REQ), `address_type`(Address Type) |
| `query_reputation_entry` | Query Reputation Entries | investigation | ✓ | `address_type`(Address Type, REQ), `address_value`(Address values, REQ) |
| `quarantine_ip` | Quarantine IP Address | investigation | ✓ | `ip`(IP Address, REQ), `policy_name`(Policy Name, REQ), `timeout`(Timeout) |
| `unquarantine_ip` | Unquarantine IP Address | investigation | ✓ | `ip`(IP Address, REQ), `policy_name`(Policy Name, REQ), `timeout`(Timeout) |

### `trend-micro-vision-one`

version 1.0.0 — Trend Micro Vision One providing deep and broad extended detection and response (XDR) capabilities that collect and automatically correlate …

- GitHub: connector-trend-micro-vision-one
- Category: Threat Intelligence
- Operations: 17

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_list_alerts` | Search Alerts | investigation | ✓ | `query`(TMV1 Filter Query), `startDateTime`(Start Date), `endDateTime`(End Date), `dateTimeTarget`(Date Time Target), `orderBy`(Order By), `offset`(Offset) |
| `get_alert_details` | Get Alert Details | investigation | ✓ | `id`(Alert ID, REQ) |
| `get_task_details` | Get Task Details | investigation | ✓ | `task_id`(Task ID, REQ) |
| `get_detection_data` | Get Detection Data | investigation | ✓ | `query`(TMV1 Query, REQ), `startDateTime`(Start Date), `endDateTime`(End Date), `top`(Limit), `select`(Field in Result) |
| `get_endpoint_details` | Get Endpoint Details | investigation | ✓ | `query`(TMV1 Query, REQ), `top`(Limit) |
| `add_to_block_list` | Add to Block List | containment | ✓ | `indicator_type`(Indicator Type, REQ), `indicator_value`(Indicator Value, REQ), `description`(Description) |
| `add_to_suspicious_object_list` | Add to Suspicious Object List | containment | ✓ | `indicator_type`(Indicator Type, REQ), `indicator_value`(Indicator Value, REQ), `scanAction`(Scan Action), `riskLevel`(Risk Level), `daysToExpiration`(Days to Expiration), `description`(Description) |
| `add_to_exception_list` | Add to Exception List | remediation | ✓ | `indicator_type`(Indicator Type, REQ), `indicator_value`(Indicator Value, REQ), `description`(Description) |
| `isolate_endpoint` | Isolate Endpoints | containment | ✓ | `isolate_by`(Isolate By, REQ), `description`(Description) |
| `restore_endpoint` | Restore Endpoints | remediation | ✓ | `restore_by`(Restore By, REQ), `description`(Description) |
| `terminates_process` | Terminates Process | containment | ✓ | `terminates_by`(Terminate Process By, REQ), `fileSha1`(File SHA1, REQ), `fileName`(File Name), `description`(Description) |
| `collect_file` | Collect File | investigation | ✓ | `collect_by`(Collect File By, REQ), `filePath`(File Path, REQ), `description`(Description) |
| `remove_from_block_list` | Remove from Block List | remediation | ✓ | `indicator_type`(Indicator Type, REQ), `indicator_value`(Indicator Value, REQ), `description`(Description) |
| `remove_from_suspicious_object_list` | Remove from Suspicious Object List | remediation | ✓ | `indicator_type`(Indicator Type, REQ), `indicator_value`(Indicator Value, REQ) |
| `remove_from_exception_list` | Remove from Exception List | remediation | ✓ | `indicator_type`(Indicator Type, REQ), `indicator_value`(Indicator Value, REQ) |
| `delete_email_message` | Delete Email Message | remediation | ✓ | `delete_by`(Delete Message By, REQ), `description`(Description) |
| `quarantine_email_message` | Quarantine Email Message | remediation | ✓ | `quarantine_by`(Quarantine Message By, REQ), `description`(Description) |

### `twitter-feed`

version 1.0.0 — Twitter feed connector fetches threat intelligence from tweettioc.com.<br></br> This connector has a dependency on the <a href="/content-hub…

- GitHub: connector-twitter-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `feed_type`(Filter Feeds by) |

### `ultipro`

version 1.0.0 — This connector is capable of querying Ultipro for Employee, Job, and Phone details.

- GitHub: connector-ultipro
- Category: utilities
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `getPhoneInformationByEmployeeIdentifier` | Get Employee Phone Information | — | ✓ | `employeeId`(Employee ID, REQ) |
| `findEmployeePhone` | Find Employee Phones | — | ✓ | `pageNumber`(Page Number, REQ), `pageSize`(Page Size, REQ) |
| `getAllCompanyEmployees` | Get All Employees | — | ✓ | `pageNumber`(Page Number, REQ), `pageSize`(Page Size, REQ) |
| `getPersonDetails` | Get Person Details | — | ✓ | `companyId`(Company ID) |
| `getEmploymentDetails` | Get Employment Details | — | ✓ | `companyId`(Company ID) |

### `unit-42-intel-objects-feed`

version 1.0.0 — Unit 42 Intel provides threat intelligence from multiple Palo Alto Networks services. Using Unit 42 Intel data, you can investigate indicato…

- GitHub: connector-unit-42-intel-objects-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `fetch_indicators` | Fetch Indicators | investigation | ✓ | `last_pull_time`(Modified After), `limit`(Limit) |

### `urlhaus`

version 1.1.0 — URLhaus is a project operated by abuse.ch. The purpose of the project is to collect, track and share malware URLs, helping network administr…

- GitHub: connector-urlhaus
- Category: Threat Intelligence
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_hash_details` | Get Hash Details  | investigation | ✓ | `hash`(Hash Name, REQ) |
| `get_recent_urls` | Get Recent URLs | investigation | ✓ | `limit`(Limit, REQ) |
| `get_tag` | Query Tag Information | investigation | ✓ | `tag`(Tag, REQ) |
| `get_url_details_by_id` | Get URLs Details by ID | investigation | ✓ | `urlid`(URL ID, REQ) |
| `get_signature` | Query Signature Information | investigation | ✓ | `signature`(Signature, REQ) |
| `get_recent_payload` | Get Recent Payloads | investigation | ✓ | `limit`(Limit, REQ) |
| `get_host_details` | Get Host Details | investigation | ✓ | `host`(Host, REQ) |
| `get_url_details` | Get URL Details | investigation | ✓ | `URL`(URL, REQ) |

### `usom`

version 1.0.0 — USOM has URL's and it is lookup connector. This connector facilitates automated operations to fetch these indicators and ingestion of daily …

- GitHub: connector-usom
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_feed` | Fetch Indicators | investigation | ✓ | `modified_after`(Modified After) |

### `veeam-backup-replication`

version 1.0.0 — Veeam Backup & Replication is a data protection and disaster recovery solution that enables backup, recovery, and replication for virtual, p…

- GitHub: connector-veeam-backup-replication
- Category: Storage
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_server_list` | Get Server List | investigation | ✓ | `filter_mode`(Filter Mode), `sort_by`(Sort By), `skip`(Offset), `limit`(Limit) |
| `get_unstructured_data_server_list` | Get Unstructured Data Server List | investigation | ✓ | `nameFilter`(Name Filter), `orderColumn`(Sort By), `orderAsc`(Order Ascending), `skip`(Offset), `limit`(Limit) |
| `get_microsoft_entra_id_tenant_list` | Get Microsoft Entra ID Tenant List | investigation | ✓ | `nameFilter`(Name Filter), `orderColumn`(Sort By), `orderAsc`(Order Ascending), `skip`(Offset), `limit`(Limit) |
| `create_malware_event` | Create Malware Event | investigation | ✓ | `detectionTimeUtc`(Detection Time, REQ), `machine`(Machine Details, REQ), `details`(Description, REQ), `engine`(Engine, REQ) |
| `get_malware_event_list` | Get Malware Event List | investigation | ✓ | `detectedAfterTimeUtcFilter`(Start Time), `detectedBeforeTimeUtcFilter`(End Time), `typeFilter`(Event Type), `stateFilter`(Event State), `severityFilter`(Event Severity), `sourceFilter`(Event Source), `backupObjectIdFilter`(Backup Object ID), `createdByFilter`(Created By), `engineFilter`(Engine), `orderColumn`(Sort By), `orderAsc`(Order Ascending), `skip`(Offset), `limit`(Limit) |
| `scan_backup` | Scan Backups with Antivirus or YARA Rules | investigation | ✓ | `backupId`(Backup ID, REQ), `backupObjectId`(Backup Object ID, REQ), `scanMode`(Scan Mode, REQ), `scanEngine`(Scan Engine, REQ), `scanRange`(Custom Scan Range), `continueScan`(Continue Scan) |
| `start_security_compliance_analyzer` | Start Security & Compliance Analyzer | investigation | ✓ | — |
| `get_security_compliance_analyzer_results` | Get Security & Compliance Analyzer Results | investigation | ✓ | — |
| `start_configuration_backup` | Start Configuration Backup | investigation | ✓ | — |
| `get_managed_server_list` | Get Managed Server List | investigation | ✓ | `nameFilter`(Name Filter), `typeFilter`(Server Type), `viTypeFilter`(Vi Type), `orderColumn`(Sort By), `orderAsc`(Order Ascending), `skip`(Offset), `limit`(Limit) |
| `start_instant_recovery` | Start Instant Recovery | investigation | ✓ | `restorePointId`(Restore Point ID, REQ), `type`(Restore Mode, REQ), `antivirusScanEnabled`(Enable Antivirus Scan), `vmTagsRestoreEnabled`(Restore VM Tags), `nicsEnabled`(Enable NICs), `powerUp`(Power Up), `reason`(Reason) |
| `start_quick_backup` | Start Quick Backup | investigation | ✓ | `platform`(Platform, REQ), `size`(Size), `urn`(Uniform Resource Name) |
| `get_backup_list` | Get Backup List | investigation | ✓ | `nameFilter`(Name Filter), `createdAfterFilter`(Created After), `createdBeforeFilter`(Created Before), `platformIdFilter`(Platform ID), `jobIdFilter`(Job ID), `policyTagFilter`(Policy Tag), `orderColumn`(Sort By), `orderAsc`(Order Ascending), `skip`(Offset), `limit`(Limit) |
| `get_repository_state_list` | Get Repository State List | investigation | ✓ | `idFilter`(Repository ID), `nameFilter`(Name Filter), `typeFilter`(Repository Type), `capacityFilter`(Repository Capacity), `freeSpaceFilter`(Repository Free Space), `usedSpaceFilter`(Repository Used Space), `isOnlineFilter`(Is Online), `orderColumn`(Sort By), `orderAsc`(Order Ascending), `skip`(Offset), `limit`(Limit) |
| `get_restore_point_list` | Get Restore Point List | investigation | ✓ | `nameFilter`(Name Filter), `createdAfterFilter`(Created After), `createdBeforeFilter`(Created Before), `platformIdFilter`(Platform ID), `backupIdFilter`(Backup ID), `backupObjectIdFilter`(Backup Object ID), `platformNameFilter`(Platform Name), `malwareStatusFilter`(Malware Status), `orderColumn`(Sort By), `orderAsc`(Order Ascending), `skip`(Offset), `limit`(Limit) |
| `execute_an_api_request` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `viriback-c2-tracker-feed`

version 1.0.0 — ViriBack C2 Tracker is a C2 Tracker platform that instantly monitors current cyber threats. ViriBack C2 Tracker tracks malware activity and …

- GitHub: connector-viriback-c2-tracker-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `output_mode`(Process Response As) |

### `virustotal-premium`

version 1.1.2 — VirusTotal Premium Services are used to get more threat context and exposes advanced threat hunting and malware discovery endpoints and func…

- GitHub: connector-virustotal-premium
- Category: Threat Intelligence
- Operations: 35

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_widget_rendering_url` | Get Widget Rendering URL | investigation | ✓ | `query`(Indicator, REQ), `fg1`(Foreground Color), `bg1`(Primary Background Color), `bg2`(Secondary Background Color), `bd1`(Border Color) |
| `get_widget_html_content` | Get Widget HTML Content | investigation | ✓ | `token`(Token, REQ) |
| `submit_sample` | Submit File | investigation | ✓ | `input`(Type, REQ), `value`(Reference ID, REQ) |
| `scan_url` | Submit URL for Scanning | investigation | ✓ | `url`(URL, REQ) |
| `get_ip_reputation` | Get IP Reputation | investigation | ✓ | `ip`(IP, REQ), `relationships`(Relationships to Include) |
| `get_domain_reputation` | Get Domain Reputation | investigation | ✓ | `domain`(Domain, REQ), `relationships`(Relationships to Include) |
| `get_url_reputation` | Get URL Reputation | investigation | ✓ | `url`(URL, REQ), `relationships`(Relationships to Include) |
| `get_file_reputation` | Get File Reputation | investigation | ✓ | `file_hash`(File Hash, REQ), `relationships`(Relationships to Include) |
| `analysis_file` | Get File Or URL Analysis Report | investigation | ✓ | `type`(Type), `analysis_id`(Analysis ID, REQ) |
| `download_file` | Download File | investigation | ✓ | `id`(Hash Value, REQ) |
| `create_zip_file` | Create ZIP File | investigation | ✓ | `hashes`(Hashes, REQ), `password`(Password) |
| `get_zip_file_status` | Get ZIP File Status | investigation | ✓ | `id`(ZIP File ID, REQ) |
| `get_zip_file_url` | Get ZIP File URL | investigation | ✓ | `id`(ZIP File ID, REQ) |
| `download_zip_file` | Download ZIP File | investigation | ✓ | `id`(ZIP File ID, REQ) |
| `get_pcap_file_behaviour` | Get PCAP File Behaviour | investigation | ✓ | `sandbox_id`(Report ID, REQ) |
| `search_intelligence` | Search Intelligence | investigation | ✓ | `query`(Query, REQ), `order`(Order By), `limit`(Limit), `descriptors_only`(Descriptors Only), `cursor`(Cursor) |
| `create_livehunt_ruleset` | Create Livehunt Ruleset | investigation | ✓ | `name`(Ruleset Name, REQ), `rules`(Rules, REQ), `enabled`(Enabled), `limit`(Limit), `notification_emails`(Notification Emails) |
| `get_livehunt_rulesets_list` | Get Livehunt Rulesets List | investigation | ✓ | `filter`(Filter), `order`(Order By), `limit`(Limit), `cursor`(Cursor) |
| `get_livehunt_ruleset_details` | Get Livehunt Ruleset Details | investigation | ✓ | `id`(Ruleset ID, REQ) |
| `update_livehunt_ruleset` | Update Livehunt Ruleset | investigation | ✓ | `id`(Ruleset ID, REQ), `name`(Ruleset Name, REQ), `rules`(Rules, REQ), `enabled`(Enabled), `limit`(Limit), `notification_emails`(Notification Emails) |
| `delete_livehunt_ruleset` | Delete Livehunt Ruleset | investigation | ✓ | `id`(Ruleset ID, REQ) |
| `get_livehunt_notifications_list` | Get Livehunt Notifications List | investigation | ✓ | `filter`(Filter), `order`(Order By), `limit`(Limit), `cursor`(Cursor), `count_limit`(Count Limit) |
| `get_livehunt_notifications_files_list` | Get Livehunt Notifications Files List | investigation | ✓ | `filter`(Filter), `limit`(Limit), `cursor`(Cursor), `count_limit`(Count Limit) |
| `get_livehunt_notifications_details` | Get Livehunt Notifications Details | investigation | ✓ | `id`(Notification ID, REQ) |
| `get_livehunt_rule_files_list` | Get Livehunt Rule Files List | investigation | ✓ | `id`(Ruleset ID, REQ), `limit`(Limit), `cursor`(Cursor) |
| `create_retrohunt_job` | Create Retrohunt Job | investigation | ✓ | `rules`(Rules, REQ), `notification_emails`(Notification Emails), `corpus`(Corpus), `start_time`(Start Time), `end_time`(End Time) |
| `abort_retrohunt_job` | Abort Retrohunt Job | investigation | ✓ | `id`(Job ID, REQ) |
| `get_retrohunt_jobs_list` | Get Retrohunt Jobs List | investigation | ✓ | `filter`(Filter), `limit`(Limit), `cursor`(Cursor) |
| `get_retrohunt_job_details` | Get Retrohunt Job Details | investigation | ✓ | `id`(Job ID, REQ) |
| `get_retrohunt_job_matching_files` | Get Retrohunt Job Matching Files | investigation | ✓ | `id`(Job ID, REQ), `limit`(Limit), `cursor`(Cursor) |
| `delete_retrohunt_job` | Delete Retrohunt Job | investigation | ✓ | `id`(Job ID, REQ) |
| `get_output_schema_ip` | Get Output Schema for IP Reputation | — | ✓ | — |
| `get_output_schema_domain` | Get Output Schema for Domain Reputation | — | ✓ | — |
| `get_output_schema_url` | Get Output Schema for URL Reputation | — | ✓ | — |
| `get_output_schema_file` | Get Output Schema for File Reputation | — | ✓ | — |

### `vmware-nsx-t`

version 1.2.0 — VMware NSX-T Data Center focuses on providing networking, security, automation, and operational simplicity for emerging application framewor…

- GitHub: connector-vmware-nsx-t
- Category: Network Security
- Operations: 16

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_security_policies_list` | Get Security Policies List | investigation | ✓ | `domain_id`(Domain ID, REQ), `include_mark_for_delete_objects`(Include Delete Objects), `include_rule_count`(Include Rule Count), `page_size`(Page Size), `sort_by`(Sort by Field), `sort_ascending`(Sort Ascending), `cursor`(Cursor) |
| `get_security_policy_details` | Get Security Policy Details | investigation | ✓ | `domain_id`(Domain ID, REQ), `policy_id`(Policy ID, REQ) |
| `upsert_security_policy` | Upsert Security Policy | miscellaneous | ✓ | `domain_id`(Domain ID, REQ), `policy_id`(Policy ID, REQ), `display_name`(Display Name), `description`(Description), `category`(Category), `comments`(Comments), `rules`(Rules), `additional_field`(Additional Fields) |
| `delete_security_policy` | Delete Security Policy | miscellaneous | ✓ | `domain_id`(Domain ID, REQ), `policy_id`(Policy ID, REQ) |
| `get_groups_list` | Get Groups List | investigation | ✓ | `domain_id`(Domain ID, REQ), `include_mark_for_delete_objects`(Include Delete Objects), `member_types`(Member Types), `page_size`(Page Size), `sort_by`(Sort by Field), `sort_ascending`(Sort Ascending), `cursor`(Cursor) |
| `get_group_details` | Get Group Details | investigation | ✓ | `domain_id`(Domain ID, REQ), `group_id`(Group ID, REQ) |
| `upsert_group` | Upsert Group | miscellaneous | ✓ | `domain_id`(Domain ID, REQ), `group_id`(Group ID, REQ), `display_name`(Display Name), `description`(Description), `group_type`(Group Type), `state`(State), `expression`(Expression), `tags`(Tags), `extended_expression`(Extended Expression), `additional_field`(Additional Fields) |
| `delete_group` | Delete Group | miscellaneous | ✓ | `domain_id`(Domain ID, REQ), `group_id`(Group ID, REQ) |
| `add_remove_ip_addresses` | Add/Remove IP Addresses | investigation | ✓ | `domain_id`(Domain ID, REQ), `group_id`(Group ID, REQ), `expression_id`(Expression ID, REQ), `action`(Action, REQ), `ip_addresses`(IP Addresses, REQ) |
| `add_remove_mac_addresses` | Add/Remove MAC Addresses | investigation | ✓ | `domain_id`(Domain ID, REQ), `group_id`(Group ID, REQ), `expression_id`(Expression ID, REQ), `action`(Action, REQ), `mac_addresses`(MAC Addresses) |
| `get_rules_list` | Get Rules List | investigation | ✓ | `domain_id`(Domain ID, REQ), `policy_id`(Policy ID, REQ), `include_mark_for_delete_objects`(Include Delete Objects), `page_size`(Page Size), `sort_by`(Sort by Field), `sort_ascending`(Sort Ascending), `cursor`(Cursor) |
| `get_rule_details` | Get Rule Details | investigation | ✓ | `domain_id`(Domain ID, REQ), `policy_id`(Policy ID, REQ), `rule_id`(Rule ID, REQ) |
| `upsert_rule` | Upsert Rule | miscellaneous | ✓ | `domain_id`(Domain ID, REQ), `policy_id`(Policy ID, REQ), `rule_id`(Rule ID, REQ), `display_name`(Display Name), `description`(Description), `source_groups`(Source Group Paths), `destination_groups`(Destination Groups Paths), `logged`(Logged), `disabled`(Disabled), `scope`(Scope), `action`(Action), `notes`(Notes), `tags`(Tags), `additional_field`(Additional Fields) |
| `delete_rule` | Delete Rule | miscellaneous | ✓ | `domain_id`(Domain ID, REQ), `policy_id`(Policy ID, REQ), `rule_id`(Rule ID, REQ) |
| `manage_vm_tag` | Manage VM TAG | miscellaneous | ✓ | `external_id`(External ID of VM, REQ), `vm_tag_update_action`(Action, REQ), `vm_scope`(Scope, REQ), `vm_tag`(VM Tag, REQ) |
| `get_vm_externalID` | Get VM External ID | miscellaneous | ✓ | `vm_name`(VM Name, REQ) |

### `vmware-tanzu-service-mesh`

version 1.0.0 — VMware Tanzu® Service Mesh™ is VMware's enterprise-class service mesh solution that provides consistent control and security for microservic…

- GitHub: connector-vmware-tanzu-service-mesh
- Category: IT Services
- Operations: 24

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_cluster` | Create Cluster | investigation | ✓ | `cluster_id`(Cluster ID, REQ), `displayName`(Display Name, REQ), `autoInstallServiceMesh`(Auto Install ServiceMesh, REQ), `description`(Description), `enableNamespaceInclusions`(Enable Namespace Inclusions), `namespaceInclusions[]`(Namespace Inclusions) |
| `generate_security_token_for_cluster` | Generate Security Token for Cluster | investigation | ✓ | `cluster_id`(Cluster ID, REQ) |
| `upgrade_tanzu_service_mesh_version_on_cluster` | Install/Upgrade Tanzu Service Mesh Version on Cluster | investigation | ✓ | `cluster_id`(Cluster ID, REQ), `version`(Version) |
| `get_clusters` | Get Clusters List | investigation | ✓ | — |
| `get_cluster_details` | Get Clusters Details | investigation | ✓ | `cluster_id`(Cluster ID, REQ) |
| `get_cluster_onboard_url` | Get Cluster Onboard URL | investigation | ✓ | — |
| `get_tanzu_service_mesh_version` | Get Tanzu Service Mesh Version | investigation | ✓ | `cluster_id`(Cluster ID, REQ) |
| `get_cluster_logs` | Get Cluster Logs | investigation | ✓ | `cluster_id`(Cluster ID, REQ), `type`(Type, REQ), `namespace`(Namespace) |
| `update_cluster` | Update Cluster | investigation | ✓ | `cluster_id`(Cluster ID, REQ), `displayName`(Display Name, REQ), `autoInstallServiceMesh`(Auto Install ServiceMesh, REQ), `description`(Description), `enableNamespaceInclusions`(Enable Namespace Inclusions), `namespaceInclusions[]`(Namespace Inclusions) |
| `remove_cluster_from_tanzu_service_mesh` | Remove Cluster from Tanzu Service Mesh | investigation | ✓ | `cluster_id`(Cluster ID, REQ) |
| `uninstall_tanzu_service_mesh_from_cluster` | Uninstall Tanzu Service Mesh from Cluster | investigation | ✓ | `cluster_id`(Cluster ID, REQ) |
| `create_global_namespace` | Create Global Namespace | investigation | ✓ | `name`(Name, REQ), `domain_name`(Domain Name, REQ), `match_conditions`(Match Conditions, REQ), `display_name`(Display Name), `description`(Description), `color`(Color Code), `mtls_enforced`(Mutual Transport Layer Security), `ca_type`(Certificate Authority Type) |
| `get_global_namespaces` | Get Global Namespaces | investigation | ✓ | — |
| `get_global_namespace_details` | Get Global Namespace Details | investigation | ✓ | `global_namespace_id`(Global Namespace ID, REQ) |
| `get_capabilities_enabled_for_global_namespace` | Get Capabilities Enabled for Global Namespace | investigation | ✓ | `global_namespace_id`(Global Namespace ID, REQ) |
| `get_status_for_capability_enabled_for_global_namespace` | Get Status for Capability Enabled for Global Namespace | investigation | ✓ | `global_namespace_id`(Global Namespace ID, REQ), `capability`(Capability, REQ) |
| `get_member_services_in_global_namespace` | Get Member Services in Global Namespace | investigation | ✓ | `global_namespace_id`(Global Namespace ID, REQ) |
| `update_global_namespace` | Update Global Namespace | investigation | ✓ | `global_namespace_id`(Global Namespace ID, REQ), `match_conditions`(Match Conditions, REQ), `display_name`(Display Name), `description`(Description), `color`(Color Code), `mtls_enforced`(Mutual Transport Layer Security), `ca_type`(Certificate Authority Type) |
| `delete_global_namespace` | Delete Global Namespace | investigation | ✓ | `global_namespace_id`(Global Namespace ID, REQ) |
| `get_jobs` | Get Jobs List | investigation | ✓ | — |
| `get_job_details` | Get Job Details | investigation | ✓ | `job_id`(Job ID, REQ) |
| `download_job` | Download Job | investigation | ✓ | `job_id`(Job ID, REQ) |
| `delete_job` | Delete Job | investigation | ✓ | `job_id`(Job ID, REQ) |
| `get_resource_groups` | Get Resource Groups | investigation | ✓ | `type`(Resource Group Type, REQ), `from`(Next Cursor), `limit`(Limit) |

### `vmware-vsphere`

version 1.1.0 — VMware vSphere connector handle virtual machine actions like start and stop VM, snapshot VM etc.

- GitHub: connector-vmware-vsphere
- Category: Server Virtualization
- Operations: 14

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `create_vm` | Create VM | miscellaneous | ✓ | `vm_name`(VM Name, REQ), `vm_compatibility`(Compatibility), `os_type`(Guest OS Family), `datastore`(Data Storage, REQ), `cpu`(CPU, REQ), `memory_size`(Memory, REQ), `disk_size`(Disk Memory, REQ), `disk_type`(Disk Type, REQ), `network`(Network, REQ), `iso_path`(ISO File Path, REQ) |
| `start_vm` | Start VM | miscellaneous | ✓ | `vm_name`(VM Name, REQ) |
| `snapshot_vm` | Snapshot VM | miscellaneous | ✓ | `vm_name`(VM Name, REQ), `snapshot_name`(Snapshot Name, REQ), `description`(Description), `memory`(Memory), `quiesce`(Quiesce) |
| `list_vms` | Get Registered VMs List | investigation | ✓ | — |
| `get_vm_info` | Get VM Information | investigation | ✓ | `search_type`(Search By, REQ), `search_value`(Search Value, REQ) |
| `suspend_vm` | Suspend VM | miscellaneous | ✓ | `vm_name`(VM Name, REQ) |
| `revert_snapshot` | Revert Snapshot | miscellaneous | ✓ | `vm_name`(VM Name, REQ), `snapshot_name`(Snapshot Name, REQ) |
| `stop_vm` | Stop VM | miscellaneous | ✓ | `vm_name`(VM Name, REQ) |
| `get_other_os_list` | Get Other OS List | — | ✓ | — |
| `get_windows_os_list` | Get Windows OS List | — | ✓ | — |
| `get_linux_os_list` | Get Linux OS List | — | ✓ | — |
| `get_mac_os_list` | Get Mac OS List | — | ✓ | — |
| `get_datastore_list` | Get Datastore List | — | ✓ | — |
| `get_network_list` | Get Network List | — | ✓ | — |

### `vuln-db`

version 1.0.0 — VulnDB is the most comprehensive and timely vulnerability intelligence available and provides actionable information about the latest in sec…

- GitHub: connector-vuln-db
- Category: Vulnerability and Risk Management
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_vuln_list` | Get Vulnerability List | investigation | ✓ | `start_date`(Start Date), `end_date`(End Date), `limit`(Limit) |
| `get_vuln_details` | Get Vulnerability Details | investigation | ✓ | `filter_by`(Filter By, REQ), `limit`(Limit) |
| `get_vendor_details` | Get Vendor Details | investigation | ✓ | `vendor`(Vendor), `limit`(Limit) |
| `get_product_details` | Get Product Details | investigation | ✓ | `vendor`(Vendor), `limit`(Limit) |
| `get_product_version` | Get Product Version | investigation | ✓ | `product`(Product, REQ), `limit`(Limit) |
| `get_vuln_by_vendor_and_product` | Get Vulnerability By Vendor and Product | investigation | ✓ | `vendor_id`(Vendor ID, REQ), `product_id`(Product ID, REQ), `limit`(Limit) |

### `vx-vault-feed`

version 1.0.0 — VX Vault is a platform that serves as a repository for malware samples and related research. This connector facilitates automated operations…

- GitHub: connector-vx-vault-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `output_mode`(Process Response As), `limit`(Limit) |

### `web-scraper`

version 1.0.0 — Web scraping is data scraping used for extracting data from websites. This connector facilitates automated operations related to extracting …

- GitHub: connector-web-scraper
- Category: utilities
- Operations: 2

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_web_page_source` | Get Web Page Source | — | ✓ | `url`(URL, REQ) |
| `get_screenshot` | Get Web Page Screenshot | — | ✓ | `url`(URL, REQ) |

### `web-screenshot`

version 1.0.0 — Web Screenshot provides a service to take screenshot or thumbnail of any online web page in a couple of second.

- GitHub: connector-web-screenshot
- Category: Utilities
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `take_screenshot` | Take Screenshot | investigation | ✓ | `url`(URL, REQ) |

### `whats-my-browser`

version 1.0.0 — WhatIsMyBrowser parses user agent strings and gives insight into known user agents. This Connector supports executing investigative action l…

- GitHub: connector-whats-my-browser
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `user_agent_parse` | Parse User Agent | investigation | ✓ | `user_agent`(User Agent, REQ) |

### `whois-freaks`

version 1.0.0 — WhoisFreaks provide well-parsed and structured domain WHOIS data for all domain names, registrars, countries and TLDs since the birth of int…

- GitHub: connector-whois-freaks
- Category: Threat Intelligence
- Operations: 3

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `whois_lookup` | Get Whois Lookup | investigation | ✓ | `domainName`(Domain Name, REQ), `whois`(Whois Type, REQ) |
| `dns_lookup` | Get DNS Lookup | investigation | ✓ | `domainName`(Domain Name), `type`(DNS Type, REQ) |
| `ssl_certificates` | Get SSL Certificates | investigation | ✓ | `domainName`(Domain Name, REQ), `chain`(With Chain), `SSLRaw`(SSL Raw) |

### `whois-xml-api`

version 1.0.0 — WhoisXMLAPI Provides comprehensive set of real-time and historic Whois, Domain name and DNS Data

- GitHub: connector-whois-xml-api
- Category: Threat Intelligence
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `whois_history_search` | Get WHOIS History Search | investigation | ✓ | `domainName`(Domain Name, REQ), `sinceDate`(Since Date), `createdDateFrom`(Created Date From), `createdDateTo`(Created Date To), `updatedDateFrom`(Updated Date From), `updatedDateTo`(Updated Date To), `expiredDateFrom`(Expired Date From), `expiredDateTo`(Expired Date To) |
| `whois_search` | Get WHOIS Search | investigation | ✓ | `domainName`(Domain/IPv4/IPv6/Email Address , REQ), `preferFresh`(Prefer Fresh), `da`(Domain Availability), `ip`(IP Address), `ipWhois`(IP Address Whois), `checkProxyData`(Proxy Data), `other_fields`(Other Fields) |
| `reverse_whois_search` | Get Reverse WHOIS Search | investigation | ✓ | `include_domain_search_terms`(Include Domain Search Terms, REQ), `exclude_domain_search_terms`(Exclude Domain Search Terms), `include_audit_dates`(Include Audit Dates), `search_type`(Search Type), `mode`(Mode), `createdDateFrom`(Created Date From), `createdDateTo`(Created Date To), `updatedDateFrom`(Updated Date From), `updatedDateTo`(Updated Date To), `expiredDateFrom`(Expired Date From), `expiredDateTo`(Expired Date To), `search_after`(Search After) |
| `dns_lookup` | Get DNS Lookup | investigation | ✓ | `domainName`(Domain Name), `type`(DNS Type, REQ) |
| `reverse_dns_search` | Get Reverse DNS Search | investigation | ✓ | `reverse_dns_type`(DNS Type, REQ), `from`(From) |
| `domain_subdomain_discovery` | Domain or Subdomain Discovery | investigation | ✓ | `include_domain`(Include Domain, REQ), `include_subdomain`(Include Subdomain), `exclude_domains`(Exclude Domains), `exclude_subdomains`(Exclude Subdomains), `sinceDate`(Since Date) |
| `brand_monitor` | Brand Monitor | investigation | ✓ | `include_domain_search_terms`(Include Domain Search Terms, REQ), `exclude_domain_search_terms`(Exclude Domain Search Terms), `sinceDate`(Since Date), `mode`(Mode), `withTypos`(With Typos) |
| `ssl_certificates` | Get SSL Certificates | investigation | ✓ | `domainName`(Domain Name, REQ), `withChain`(With Chain), `hardRefresh`(Hard Refresh) |

### `wiz-io`

version 2.0.0 — Wiz provides a comprehensive analysis engine that integrates: Cloud Security Posture Management (CSPM) Kubernetes Security Posture Managemen…

- GitHub: connector-wiz-io
- Category: ['Asset Management', 'Attack surface management', 'Cloud Security']
- Operations: 5

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_issues` | Get Issues | investigation | ✗ | `issueID`(Issue ID), `searchQuery`(Search Query), `projectID`(Project ID), `severity`(Severity), `status`(Status), `type`(Type), `relatedEntityID`(Related Entity ID), `realtedEntityType`(Realted Entity Type), `createdBefore`(Created before), `createdAfter`(Created after), `resolvedBefore`(Resolved before), `resolvedAfter`(Resolved after), `limit`(Limit), `pagination`(Pagination), `relatedCloudPlatform`(Related Cloud Platform) |
| `get_inventory_assets` | Get Inventory Assets | investigation | ✗ | `projectID`(Project ID, REQ), `type`(Type, REQ), `searchTerm`(Search Term), `updatedBefore`(Updated before), `updatedAfter`(Updated after), `deletedBefore`(Deleted before), `deletedAfter`(Deleted after), `limit`(Limit) |
| `get_projects` | Get Projects | investigation | ✗ | `name`(Name), `businessImpact`(Business Impact), `includeArchivedProjects`(Include Archived Projects), `limit`(Limit) |
| `add_comment_to_issue` | Add Comment to Issue | investigation | ✗ | `issueID`(Issue ID, REQ), `comment`(Comment, REQ) |
| `get_vulnerabilities` | Get Vulnerabilities | investigation | ✗ | `status`(Status, REQ), `projectID`(Project ID, REQ), `assetType`(Asset Type, REQ), `vulnerabilityID`(Vulnerability ID), `externalSubscriptionID`(External Subscription ID), `severity`(Severity), `firstSeenBefore`(First Seen before), `firstSeenAfter`(First Seen after), `resolvedBefore`(Resolved before), `resolvedAfter`(Resolved after), `assetID`(Asset ID), `patchAvailable`(Patch available), `exploitAvailable`(Exploit available), `limit`(Limit), `pagination`(Pagination) |

### `zabbix`

version 1.0.0 — Zabbix is an open-source, enterprise-grade monitoring platform that provides real-time visibility into the performance and availability of I…

- GitHub: connector-zabbix
- Category: Monitoring
- Operations: 4

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_alerts` | Get Alerts | investigation | ✓ | `start_date`(Start Date), `end_date`(End Date), `alert_ids`(Alert IDs), `action_ids`(Action IDs), `event_ids`(Event IDs), `group_ids`(Group IDs), `host_ids`(Host IDs), `user_ids`(User IDs), `object_ids`(Object IDs), `event_object_type`(Event Object Type), `event_source`(Event Source), `sort_field`(Sort Fields), `sortorder`(Sort Order), `limit`(Limit), `search`(Search Pattern), `search_any`(Search By Any), `search_wildcards_enabled`(Search Wildcards Enabled), `filter`(Filter), `additional_fields`(Additional Fields) |
| `get_events` | Get Events | investigation | ✓ | `start_date`(Start Date), `end_date`(End Date), `event_ids`(Event IDs), `group_ids`(Group IDs), `host_ids`(Host IDs), `object_ids`(Object IDs), `event_object_type`(Event Object Type), `source`(Event Source), `acknowledged`(Acknowledged), `suppressed`(Suppressed), `severities`(Severities), `event_id_from`(Start Event ID), `event_id_till`(End Event ID), `sort_field`(Sort Fields), `sortorder`(Sort Order), `limit`(Limit), `search`(Search Pattern), `filter`(Filter), `additional_fields`(Additional Fields) |
| `get_problems` | Get Problems | investigation | ✓ | `start_date`(Start Date), `end_date`(End Date), `fetch_alert`(Fetch Related Alerts), `severities`(Severities), `event_ids`(Event IDs), `group_ids`(Group IDs), `host_ids`(Host IDs), `object_ids`(Object IDs), `object`(Event Object Type), `source`(Event Source), `acknowledged`(Acknowledged), `suppressed`(Suppressed), `event_id_from`(Start Event ID), `event_id_till`(End Event ID), `sort_field`(Sort Fields), `sortorder`(Sort Order), `limit`(Limit), `filter`(Filter), `search`(Search Pattern), `additional_fields`(Additional Fields) |
| `execute_generic_rest_api_call` | Execute Generic JSON RPC Request | investigation | ✓ | `?`(Request Body, REQ) |

### `zerofox`

version 1.0.1 — ZeroFox Platform combines advanced AI-driven analysis to detect complex threats on the surface, deep and dark web, fully managed services wi…

- GitHub: connector-zerofox
- Category: Threat Intelligence
- Operations: 19

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_ip_lookup` | Get IP Lookup | investigation | ✓ | `ip`(IP Address, REQ) |
| `get_domain_lookup` | Get Domain Lookup | investigation | ✓ | `domain`(Domain Name, REQ) |
| `get_email_lookup` | Get Email Lookup | investigation | ✓ | `email`(Email Address, REQ) |
| `get_filehash_lookup` | Get FileHash Lookup | investigation | ✓ | `hash`(File Hash, REQ) |
| `get_exploits_lookup` | Get Exploits Lookup | investigation | ✓ | `created_after`(Created After, REQ) |
| `get_alerts_list` | Get Alerts List | investigation | ✓ | `account`(Account Number), `alert_type`(Alert Type), `assignee`(Assignee Name), `entity`(Entity ID), `entity_term`(Term ID of Entity), `min_timestamp`(Created After), `max_timestamp`(Created Before), `last_modified`(Last Modified), `network`(Network Names), `risk_rating`(Risk Rating), `sort_direction`(Sort Direction), `sort_field`(Sort Field), `status`(Alert Status), `escalated`(Escalated), `limit`(Limit), `offset`(Offset), `additional_fields`(Additional Fields) |
| `get_alert_details` | Get Alert Details | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `assign_alert_to_user` | Assign Alert to User | investigation | ✓ | `alert_id`(Alert ID, REQ), `username`(User Name, REQ) |
| `open_alert` | Open Alert | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `close_alert` | Close Alert | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `alert_request_takedown` | Request Alert Takedown | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `alert_cancel_takedown` | Cancel Alert Takedown | investigation | ✓ | `alert_id`(Alert ID, REQ) |
| `modify_alert_tags` | Modify Alert Tags | investigation | ✓ | `alert_id`(Alert ID, REQ), `action`(Action, REQ), `tags_list`(Tags, REQ) |
| `modify_alert_notes` | Modify Alert Notes | investigation | ✓ | `alert_id`(Alert ID, REQ), `notes`(Notes, REQ) |
| `create_entity` | Create Entity | investigation | ✓ | `name`(Entity Name, REQ), `policy`(Policy ID), `strict_name_matching`(Strict Name Matching), `tags`(Tags), `organization`(Organization Name) |
| `get_entity_list` | Get Entity List | investigation | ✓ | `email_address`(Email Address), `group`(Group ID), `label`(Label ID), `network`(Network ID), `networks`(Network Name), `policy`(Policy ID), `type`(Type ID), `page`(Page Number) |
| `get_entity_types` | Get Entity Types List | investigation | ✓ | — |
| `get_policy_types` | Get Policy Types List | investigation | ✓ | — |
| `submit_threat` | Submit Threat | investigation | ✓ | `entity_id`(Entity ID, REQ), `source`(Content, REQ), `alert_type`(Content Type, REQ), `violation`(Infringement Type, REQ), `notes`(Notes) |

### `zoom-feed`

version 1.0.0 — Zoom publishes its current IP address ranges in txt files. This connector facilitates automated operations to fetch these indicators and ing…

- GitHub: connector-zoom-feed
- Category: Threat Intelligence
- Operations: 1

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_indicators` | Get Indicators | investigation | ✓ | `services`(Zoom Service, REQ), `last_pull_time`(Modified After) |

### `zscaler-client-connector`

version 1.0.0 — Zscaler Client Connector™ is a lightweight agent for user endpoints, enabling hybrid work through secure, fast, reliable access to any app o…

- GitHub: connector-zscaler-client-connector
- Category: Network Security
- Operations: 7

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_enrolled_device_list` | Get Enrolled Device List | investigation | ✓ | `username`(Username), `osType`(OS Type), `page`(Page Number), `pageSize`(Page Size) |
| `get_enrolled_device_details` | Get Enrolled Device Details | investigation | ✓ | `udid`(Unique Device Identifier (UDID), REQ), `username`(Username) |
| `get_device_otp` | Get Device OTP | investigation | ✓ | `udid`(Unique Device Identifier (UDID), REQ) |
| `get_device_app_profile_password` | Get Device App Profile Password | investigation | ✓ | `username`(Username), `osType`(OS Type) |
| `download_device_details` | Download Device Details | investigation | ✓ | `osTypes`(OS Types), `registrationTypes`(Registration Types) |
| `download_service_status_of_devices` | Download Service Status of Devices | investigation | ✓ | `osTypes`(OS Types), `registrationTypes`(Registration Types) |
| `execute_an_api_call` | Execute an API Request | investigation | ✓ | `method`(HTTP Method, REQ), `endpoint`(Endpoint, REQ), `query_params`(Query Parameters), `payload`(Request Payload) |

### `zscaler-internet-access`

version 1.0.0 — Zscaler Internet Access (ZIA) connector enables automated operations such as Get Firewall Filtering Rules, Get Specific Firewall Filtering R…

- GitHub: connector-zscaler-internet-access
- Category: Cloud Security
- Operations: 8

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_firewall_filtering_rules` | Get Firewall Filtering Rules | utilities | ✓ | — |
| `get_specific_firewall_filtering_rule` | Get Specific Firewall Filtering Rule | utilities | ✓ | `id`(ID, REQ) |
| `get_time_windows` | Get Time Windows | utilities | ✓ | — |
| `get_network_applications` | Get Network Applications | utilities | ✓ | — |
| `get_network_services` | Get Network Services | utilities | ✓ | `search`(Filter String), `protocol`(Protocol), `locale`(Language) |
| `get_network_service_groups` | Get Network Services Groups | utilities | ✓ | — |
| `get_network_application_groups` | Get Network Applications Groups | utilities | ✓ | — |
| `execute_api_request` | Execute an API Request | utilities | ✓ | `endpoint`(Endpoint, REQ), `method`(Method, REQ), `Query Parameters`(query_params), `payload`(Request Body/Payload) |

### `zscaler-private-access`

version 1.0.0 — Zscaler Private Access (ZPA) is a cloud-delivered Zero Trust Network Access (ZTNA) solution that provides secure, identity-based access to i…

- GitHub: connector-zscaler-private-access
- Category: Network Security
- Operations: 6

| operation | title | category | enabled | parameters |
|---|---|---|---|---|
| `get_all_configured_applications_segments` | Get All Configured Applications Segments | investigation | ✓ | `customerId`(Customer ID, REQ), `search`(Filter String), `page`(Offset), `pagesize`(Limit), `microtenantId`(Micro Tenant ID) |
| `get_specific_application_segment_details` | Get Specific Application Segment Details | investigation | ✓ | `customerId`(Customer ID, REQ), `applicationId`(Application ID, REQ), `micro_tenant_id`(Micro Tenant ID) |
| `get_customer_certificates` | Get Customer Certificates | investigation | ✓ | `customerId`(Customer ID, REQ) |
| `get_all_issued_certificates` | Get All Issued Certificates | investigation | ✓ | `customerId`(Customer ID, REQ), `search`(Filter String), `page`(Offset), `pagesize`(Limit) |
| `get_certificate_details` | Get Certificate Details | investigation | ✓ | `customerId`(Customer ID, REQ), `certificateId`(Certificate ID, REQ) |
| `execute_api_request` | Execute an API Request | utilities | ✓ | `endpoint`(Endpoint, REQ), `method`(Method, REQ), `query_params`(Query Parameters), `payload`(Request Body/Payload) |

## Connectors NOT on GitHub (built-in)

These connector slugs appear in official FortiSOAR playbooks but have no `connector-<slug>` repo in the fortinet-fortisoar GitHub org. They ship with the FortiSOAR platform itself. Consult the in-instance connector documentation (Settings > Connector Configurations, or the connector's info dialog in the playbook designer) for their operation lists and parameter schemas.

| slug | notes |
|---|---|
| `cyops_utilities` | Built-in utility connector: No-Op (end step), comment, etc. |
| `code-snippet` | Built-in Python snippet runner. (Note: the GitHub repo `jscode-snippet` exposes the JS equivalent `run_js_code`.) |
| `smtp` | Email send/receive. |
| `exchange` |  |
| `slack` |  |
| `ssh` | Remote command execution over SSH. |
| `mysql` |  |
| `http` | Generic HTTP/REST call. |
| `awss3` |  |
| `netshot-utilities` |  |
| `AtlassianConfluenceCloud` |  |
| `elasticsecurity` |  |
| `kibana` |  |
| `logrhythm` |  |
| `sentinelone` |  |
| `whois-rdap` |  |
