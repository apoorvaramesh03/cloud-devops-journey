# ☁️ Microsoft Azure Fundamentals (AZ-900) Notes

> Comprehensive notes created while preparing for the **Microsoft
> Certified: Azure Fundamentals (AZ-900)** certification.

------------------------------------------------------------------------

# Table of Contents

-   Cloud Computing
-   Cloud Benefits
-   Cloud Service Models
-   Cloud Deployment Models
-   Shared Responsibility Model
-   Azure Global Infrastructure
-   Azure Compute
-   Azure Networking
-   Azure Storage
-   Azure Databases
-   Identity & Access Management
-   Security
-   Governance
-   Monitoring
-   Cost Management
-   SLAs
-   Azure Management Tools
-   DevOps
-   AI Services
-   IoT
-   Data & Analytics
-   Frequently Confused Concepts
-   AZ-900 Exam Cheat Sheet

------------------------------------------------------------------------

# 1. Cloud Computing

Cloud computing is the delivery of computing resources over the Internet
instead of maintaining physical infrastructure.

Examples: - Virtual Machines - Storage - Databases - Networking - AI
Services - Analytics

## Benefits

### High Availability

Keeps services running even if hardware fails.

### Scalability

Increase or decrease resources manually according to demand.

### Elasticity

Automatically scales resources depending on workload.

**Memory Tip:** Scalability = Manual \| Elasticity = Automatic

### Reliability

Applications continue operating despite failures.

### Predictability

Consistent performance and predictable costs.

### Security

Microsoft secures the cloud infrastructure while customers secure their
workloads.

### Governance

Maintain compliance using policies and standards.

### Manageability

Resources can be managed using: - Azure Portal - Azure CLI - Azure
PowerShell - ARM Templates - Bicep

------------------------------------------------------------------------

# 2. Cloud Service Models

## IaaS

Microsoft manages: - Physical servers - Storage - Networking

Customer manages: - Operating System - Middleware - Runtime -
Applications - Data

Example: - Azure Virtual Machines

------------------------------------------------------------------------

## PaaS

Microsoft manages: - Infrastructure - Operating System - Runtime

Customer manages: - Applications - Data

Examples: - Azure App Service - Azure SQL Database

------------------------------------------------------------------------

## SaaS

Microsoft manages almost everything.

Examples: - Microsoft 365

------------------------------------------------------------------------

# 3. Shared Responsibility Model

  Model         Customer Manages   Microsoft Manages
  ------------- ------------------ --------------------------
  On-Premises   Everything         Nothing
  IaaS          OS, Apps, Data     Hardware
  PaaS          Apps & Data        Infrastructure + Runtime
  SaaS          Users & Data       Almost Everything

------------------------------------------------------------------------

# 4. Cloud Deployment Models

## Public Cloud

Shared infrastructure operated by Microsoft.

## Private Cloud

Dedicated infrastructure for a single organization.

## Hybrid Cloud

Combination of public cloud and on-premises.

## Multi-cloud

Using Azure together with AWS, GCP, etc.

------------------------------------------------------------------------

# 5. Azure Global Infrastructure

## Regions

Geographical locations containing one or more datacenters.

## Region Pairs

Support disaster recovery.

## Availability Zones

Independent datacenters with separate power, cooling and networking.

## Resource

Any Azure service.

## Resource Group

Logical container for resources.

## Subscription

Billing boundary.

## Management Group

Groups multiple subscriptions.

Hierarchy

Management Group → Subscription → Resource Group → Resources

------------------------------------------------------------------------

# 6. Azure Compute

## Azure Virtual Machines

Virtual servers (IaaS).

## VM Scale Sets

Automatically scale multiple VMs.

## Availability Sets

Protect VMs from hardware failures.

## Azure App Service

Host web applications without managing servers.

## Azure Functions

Serverless event-driven compute.

## Azure Container Instances

Run containers quickly.

## Azure Kubernetes Service

Managed Kubernetes platform.

## Azure Virtual Desktop

Cloud-hosted Windows desktop.

------------------------------------------------------------------------

# 7. Azure Networking

## Virtual Network (VNet)

Private Azure network.

## VPN Gateway

Encrypted internet connection.

## ExpressRoute

Private dedicated connection.

## Azure Load Balancer

Layer 4 (TCP/UDP).

## Application Gateway

Layer 7 (HTTP/HTTPS) + Web Application Firewall.

## Traffic Manager

DNS-based global routing.

## CDN

Caches content closer to users.

------------------------------------------------------------------------

# 8. Azure Storage

## Blob Storage

Images, videos, backups, documents.

## Azure Files

SMB file shares.

## Disk Storage

Persistent VM disks.

## Queue Storage

Messaging between applications.

## Table Storage

NoSQL key-value store.

## Storage Tiers

-   Hot
-   Cool
-   Archive

## Replication

-   LRS
-   ZRS
-   GRS
-   RA-GRS

------------------------------------------------------------------------

# 9. Azure Databases

## Azure SQL Database

Managed relational database.

## Azure Cosmos DB

Globally distributed NoSQL database.

Managed open-source databases: - MySQL - PostgreSQL - MariaDB

------------------------------------------------------------------------

# 10. Identity & Access

## Microsoft Entra ID

Features: - Authentication - Authorization - Single Sign-On -
Multi-Factor Authentication - Conditional Access

## RBAC

Owner - Full access

Contributor - Manage resources

Reader - View only

------------------------------------------------------------------------

# 11. Security

## Microsoft Defender for Cloud

Threat protection and security recommendations.

## Microsoft Sentinel

Cloud-native SIEM & SOAR.

## Azure Key Vault

Securely stores: - Secrets - Keys - Certificates

## Zero Trust

Never trust. Always verify.

------------------------------------------------------------------------

# 12. Governance

## Azure Policy

Enforce organizational rules.

## Resource Locks

-   Delete Lock
-   Read-only Lock

## Tags

Organize resources.

Examples: Department, Owner, Environment

------------------------------------------------------------------------

# 13. Monitoring

## Azure Monitor

Metrics, Logs and Alerts.

## Azure Advisor

Recommendations for: - Cost - Security - Reliability - Performance

## Service Health

Azure platform status.

## Resource Health

Health of your own resources.

------------------------------------------------------------------------

# 14. Cost Management

## Pricing Calculator

Estimate Azure costs.

## TCO Calculator

Compare Azure with on-premises.

## Azure Cost Management

Budgets and reports.

## Reserved Instances

Lower cost for long-term workloads.

## Spot VMs

Low-cost VMs that can be interrupted.

------------------------------------------------------------------------

# 15. SLAs

Higher SLA = Less downtime.

Remember: 99.9% \> 99%

------------------------------------------------------------------------

# 16. Azure Management Tools

-   Azure Portal
-   Azure CLI
-   Azure PowerShell
-   Azure Cloud Shell
-   Azure Resource Manager
-   ARM Templates
-   Bicep

------------------------------------------------------------------------

# 17. Azure DevOps

Components: - Boards - Repos - Pipelines - Test Plans - Artifacts

GitHub Actions provides CI/CD automation from GitHub repositories.

------------------------------------------------------------------------

# 18. Azure AI

## Azure AI Services

Prebuilt AI APIs: - Vision - Speech - Language - Translator - Document
Intelligence - Azure OpenAI

## Azure Machine Learning

Build and deploy custom ML models.

------------------------------------------------------------------------

# 19. IoT

## Azure IoT Hub

Secure device communication.

## Azure IoT Central

Managed IoT platform.

------------------------------------------------------------------------

# 20. Data & Analytics

## Azure Synapse Analytics

Enterprise analytics and data warehouse.

## Azure Data Factory

ETL and data integration.

## Azure Event Hubs

Real-time event ingestion.

------------------------------------------------------------------------

# Frequently Confused Concepts

  -----------------------------------------------------------------------
  Topic                   Difference
  ----------------------- -----------------------------------------------
  Authentication vs       Verify identity vs Grant permissions
  Authorization           

  Azure Monitor vs        Monitor resources vs Give recommendations
  Advisor                 

  Service Health vs       Azure platform vs Your resources
  Resource Health         

  VPN Gateway vs          Internet vs Private connection
  ExpressRoute            

  Blob Storage vs Azure   Object storage vs File shares
  Files                   

  App Service vs Virtual  Managed hosting vs Full server
  Machine                 

  Azure AI Services vs    Prebuilt AI vs Custom ML
  Azure Machine Learning  

  Pricing Calculator vs   Estimate Azure costs vs Compare with
  TCO Calculator          on-premises

  Scalability vs          Manual vs Automatic scaling
  Elasticity              
  -----------------------------------------------------------------------

------------------------------------------------------------------------

# AZ-900 Quick Cheat Sheet

  Requirement          Azure Service
  -------------------- -------------------------
  Host website         Azure App Service
  Run VM               Azure Virtual Machines
  Serverless code      Azure Functions
  Containers           AKS
  Authentication       Microsoft Entra ID
  Secrets              Azure Key Vault
  Monitor resources    Azure Monitor
  Recommendations      Azure Advisor
  Platform outage      Service Health
  Resource outage      Resource Health
  Cost estimate        Pricing Calculator
  Cost comparison      TCO Calculator
  Permissions          RBAC
  Governance           Azure Policy
  Prevent deletion     Resource Locks
  Organize resources   Tags
  NoSQL                Azure Cosmos DB
  SQL                  Azure SQL Database
  Data Warehouse       Azure Synapse Analytics
  ETL                  Azure Data Factory

------------------------------------------------------------------------

## Certification

**Certification:** Microsoft Certified: Azure Fundamentals (AZ-900)

These notes summarize the concepts covered in the AZ-900 learning path
and serve as a quick reference for revision and future projects.
