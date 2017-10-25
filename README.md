# BitShifter Identity Server

Author: Pedro Guzmán (pedro@subvertic.com)

Version: 0.1 

BitShifter is an Identity Management Server that provides a simple, yet powerful
authentication and authorization infrastructure for multi-tenant cloud-based 
applications. 

The server exposes a very simple claim-based schema that allow users to have specific
roles in a given organization. The design of assumnes users are independent of 
any organization but can performa actions within one or more organizations by 
acquiring entitlements that establish a set of roles and actions a given user 
can perform in a given organization.  

The data model is implemented through graphs which allow fast retrieval of claims
and localized queries. For example:

```javascript

(user:1) -[:isSysAdmin]-> (org:3)

```

