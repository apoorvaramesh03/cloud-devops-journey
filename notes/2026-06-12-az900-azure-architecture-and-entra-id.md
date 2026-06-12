# AZ-900: Azure Architecture & Microsoft Entra ID

## What I Learned

---

# Azure Core Architecture

Azure resources follow a hierarchy:

```
Azure Account

      |

Azure Subscription

      |

Resource Group

      |

Azure Resources
(VM, Storage Account, Database, Web App)
```

---

# Azure Subscription

## What is an Azure Subscription?

An Azure Subscription is a **billing and management boundary** that contains Azure resources.

It manages:

- Billing
- Resource limits
- Access control
- Resource organization


Example:

```
Azure Account

      |

Azure Subscription

      |

Resource Group

      |

Storage Account
```

---

# Resource Groups

## What is a Resource Group?

A Resource Group is a logical container used to organize related Azure resources.

Benefits:

- Organize resources
- Apply permissions
- Manage resources together
- Delete related resources easily


Example:

```
Static Website Project

Resource Group

      |

Storage Account

      |

Static Website Files
```

---

# Azure Storage Account

A Storage Account provides cloud storage services.

Used for:

- Files
- Images
- Videos
- Documents
- Static websites


Architecture:

```
Storage Account

      |

Blob Container

      |

Files
```

---

# Static Website Hosting

Azure Storage can host static websites.

Steps:

1. Create Resource Group
2. Create Storage Account
3. Enable Static Website Hosting
4. Upload index.html
5. Access website URL


Architecture:

```
User

 |

Website URL

 |

Azure Storage Account

 |

$web Container

 |

index.html
```

---

# Microsoft Entra ID

## What is Microsoft Entra ID?

Microsoft Entra ID is Microsoft's **cloud identity and access management service**.

Previously known as:

```
Azure Active Directory (Azure AD)
```

It manages:

- Users
- Groups
- Applications
- Devices
- Authentication
- Authorization


---

# Authentication vs Authorization

## Authentication

Answers:

"Who are you?"

Example:

```
Username
Password
MFA
```

---

## Authorization

Answers:

"What can you access?"

Example:

```
User

 |

Can access Storage Account

Cannot delete resources
```

---

# Active Directory Domain Services (AD DS)

Traditional on-premises identity service.

Runs on:

```
Windows Server
```

Uses:

- Domain Controllers
- Kerberos Authentication
- LDAP
- Group Policy


Architecture:

```
User

 |

Domain Controller

 |

Company Resources
```

---

# Microsoft Entra ID vs AD DS

| AD DS | Microsoft Entra ID |
|---|---|
| On-premises | Cloud |
| Runs on Windows Server | Microsoft managed |
| Uses Domain Controllers | No domain controllers |
| Uses Kerberos | Uses OAuth/OpenID Connect |
| Uses LDAP | Uses Microsoft Graph |
| Supports Group Policy | Uses modern management |
| Internal apps | Cloud applications |

---

# Microsoft Entra ID Features

## Multi-Factor Authentication (MFA)

Adds an extra verification step.

Example:

```
Password

+

Authenticator Approval
```

---

## Single Sign-On (SSO)

One login provides access to multiple applications.

Example:

```
Microsoft Login

 |

Teams

 |

Outlook

 |

Azure Portal
```

---

## Self-Service Password Reset

Users can reset passwords without contacting administrators.

---

## Conditional Access

Controls access based on:

- User
- Group
- Device
- Location


Example:

```
Allow Access IF:

User = Employee

AND

Device = Trusted

AND

Location = Allowed
```

---

# Microsoft Entra Tenant

## What is a Tenant?

A tenant represents an organization's Microsoft Entra directory.

It contains:

- Users
- Groups
- Applications
- Devices


Example:

```
Company Tenant

 |

 ----------------
 |      |       |
Users Groups Apps
```

---

# Tenant and Subscription Relationship

A subscription is connected to one tenant.

A tenant can support multiple subscriptions.


Example:

```
Company Tenant

      |

 -------------------------
 |          |             |
Dev      Testing      Production

Subscription Subscription Subscription
```

---

# Microsoft Entra Objects

## Users

Represents people.

Example:

```
employee@company.com
```

---

## Groups

Collection of users.

Example:

```
Developers Group

 |

Azure Permissions
```

---

## Applications

Applications registered with Entra ID.

Examples:

- Microsoft 365
- SaaS Applications
- Custom Applications

---

## Devices

Registered devices:

- Laptops
- Phones
- Tablets

---

# Application Object and Service Principal

## Application Object

Contains the application definition.

Example:

```
Application Name
Permissions
Settings
```

---

## Service Principal

Represents the application inside a tenant.

Relationship:

```
Application

 |

Service Principal

 |

Tenant Access
```

---

# Microsoft Identity Manager (MIM)

Used to connect on-premises identity systems with Microsoft Entra ID.


Architecture:

```
AD DS

 |

Microsoft Identity Manager

 |

Microsoft Entra ID
```

---

# Microsoft Entra Connect Health

Provides:

- Monitoring
- Health reports
- Identity infrastructure insights


Architecture:

```
AD DS

 |

Entra Connect

 |

Microsoft Entra ID

 |

Connect Health
```

---

# Microsoft Entra Domain Services

Used for applications requiring:

- LDAP
- Kerberos
- Domain Join


Benefit:

No need to deploy domain controllers.


Traditional:

```
AD DS

 |

Domain Controller

 |

Management
```


Entra Domain Services:

```
Microsoft Managed

 |

LDAP + Kerberos Support
```

--
# Key Points

- Subscription = Billing and management boundary
- Resource Group = Container for Azure resources
- Storage Account = Cloud storage service
- Microsoft Entra ID = Cloud identity service
- AD DS = On-premises identity service
- Kerberos = AD DS authentication
- OAuth = Entra ID authentication
- Tenant = Organization's identity boundary
- MFA = Extra security verification
- SSO = One login for multiple apps
- Conditional Access = Access control rules
- MIM = Identity synchronization
- Entra Connect Health = Monitoring

---

# Questions I Still Have

- When should I choose Azure Virtual Machines over containers?
- Difference between Azure Storage and Virtual Machines?
- How does Azure RBAC work with Entra ID?
- Difference between Entra ID Free, P1, and P2?
- How does authentication flow happen when logging into Azure?
