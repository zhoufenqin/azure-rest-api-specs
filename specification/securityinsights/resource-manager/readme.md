# Security Insight

> see https://aka.ms/autorest

This is the AutoRest configuration file for SecurityInsights.

---

## Getting Started

To build the SDK for SecurityInsights, simply [Install AutoRest](https://aka.ms/autorest/install) and in this folder, run:

> `autorest`

To see additional help and options, run:

> `autorest --help`

---

## Configuration

### Basic Information

These are the global settings for the SecurityInsights API.

```yaml
openapi-type: arm
tag: package-composite-v1
```

### Tag: package-composite-v1

These settings apply only when `--tag=package-composite-v1` is specified on the command line.

```yaml $(tag) == 'package-composite-v1'
input-file:
- Microsoft.SecurityInsights/stable/2020-01-01/SecurityInsights.json
directive:
  - suppress: R2059
    from: Microsoft.SecurityInsights/stable/2020-01-01/SecurityInsights.json
    reason: it's not actually a resource path; the validator is confused because the LogAnalytics namespace is in the URI path.
    approved-by: "@lirenhe"
```

---

### Tag: package-2021-03-preview-only

These settings apply only when `--tag=package-2021-03-preview-only` is specified on the command line.

```yaml $(tag) == 'package-2021-03-preview-only'
input-file:
- Microsoft.SecurityInsights/preview/2021-03-01-preview/Settings.json
- Microsoft.SecurityInsights/preview/2021-03-01-preview/operations.json
directive:
  - suppress: R4017
    from: Microsoft.SecurityInsights/preview/2021-03-01-preview/Settings.json
    where: $.definitions.Settings
    reason: The Setting does not support list by subscription. It's not a top-level resource. To get the Watchlist, we should have a subscription as well as a resource group and Log Analytics workspace. 
```

---

### Tag: package-2019-01-preview-only

These settings apply only when `--tag=package-2019-01-preview-only` is specified on the command line.

```yaml $(tag) == 'package-2019-01-preview-only'
input-file:
- Microsoft.SecurityInsights/preview/2019-01-01-preview/SecurityInsights.json
directive:
  - suppress: R4017
    from: Microsoft.SecurityInsights/preview/2019-01-01-preview/SecurityInsights.json
    where: $.definitions.ThreatIntelligenceResource
    reason: Our API is designed based on per region per workspace concept. There is no use case of our customers to get all indicators in multiple workspaces.
    approved-by: "@cheggert"
  - suppress: R4017
    from: Microsoft.SecurityInsights/preview/2019-01-01-preview/SecurityInsights.json
    where: $.definitions.Watchlist
    reason: The Watchlist does not support list by subscription. It's not a top-level resource. To get the Watchlist, we should have a subscription as well as a resource group and Log Analytics workspace. 
  - suppress: R4017
    from: Microsoft.SecurityInsights/preview/2019-01-01-preview/SecurityInsights.json
    where: $.definitions.AutomationRule
    reason: The AutomationRule does not support list by subscription. It's not a top-level resource. To get the AutomationRule, we should have a subscription as well as a resource group and Log Analytics workspace. 
```

---

# Code Generation

## Swagger to SDK

This section describes what SDK should be generated by the automatic system.
This is not used by Autorest itself.

```yaml $(swagger-to-sdk)
swagger-to-sdk:
  - repo: azure-sdk-for-net
  - repo: azure-sdk-for-go
  - repo: azure-sdk-for-python-track2
  - repo: azure-sdk-for-js
  - repo: azure-sdk-for-node
  - repo: azure-cli-extensions
  - repo: azure-resource-manager-schemas
    after_scripts:
      - node sdkauto_afterscript.js securityinsights/resource-manager
```

## C#

These settings apply only when `--csharp` is specified on the command line.
Please also specify `--csharp-sdks-folder=<path to "SDKs" directory of your azure-sdk-for-net clone>`.

```yaml $(csharp)
csharp:
  azure-arm: true
  license-header: MICROSOFT_MIT_NO_VERSION
  namespace: Microsoft.Azure.Management.SecurityInsights
  payload-flattening-threshold: 2
  output-folder: $(csharp-sdks-folder)/securityinsights/Microsoft.Azure.Management.SecurityInsights/src/Generated
  clear-output-folder: true
```

## Go

See configuration in [readme.go.md](./readme.go.md)

## Python

See configuration in [readme.python.md](./readme.python.md)

## Node.js

See configuration in [readme.nodejs.md](./readme.nodejs.md)

## TypeScript

See configuration in [readme.typescript.md](./readme.typescript.md)

## AzureResourceSchema

See configuration in [readme.azureresourceschema.md](./readme.azureresourceschema.md)
