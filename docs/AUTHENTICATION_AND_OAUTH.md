# Authentication and provider authorization

Application sign-in and provider authorization are different systems.

## Application sign-in

Use a standard identity system for users, organizations, sessions, MFA where appropriate, password reset, and role-based access. Signing in with Google does not automatically authorize Search Console, Analytics, Ads, or Business Profile data.

## Provider authorization

Use the provider-supported delegation mechanism. Prefer OAuth authorization code flows for server applications, read-only permissions first, incremental authorization, refresh-token revocation handling, and explicit asset selection.

Never request a provider's primary account password. WordPress integrations should use a dedicated low-privilege user and an individually revocable Application Password over HTTPS, or a narrowly scoped connector plugin.

## Token vault contract

A production implementation should store encrypted token material outside this repository. The application database may keep non-secret metadata such as:

- connection ID, provider, organization, creator, and status;
- granted capabilities and scopes;
- provider account identifier;
- expiry, last refresh, last successful sync, and revocation time;
- encryption key version and secret reference, not plaintext token values.

Logs, prompts, examples, issue reports, and analytics must not contain access tokens, refresh tokens, client secrets, private keys, cookies, or WordPress Application Passwords.

## Current official references

- Google OAuth 2.0 web-server flow and token refresh: https://developers.google.com/identity/protocols/oauth2/web-server
- Google OAuth scope guidance: https://developers.google.com/identity/protocols/oauth2/scopes
- Search Console API authorization: https://developers.google.com/webmaster-tools/v1/how-tos/authorizing
- WordPress Application Passwords: https://developer.wordpress.org/advanced-administration/security/application-passwords/
- WordPress REST API authentication: https://developer.wordpress.org/rest-api/using-the-rest-api/authentication/
- Meta permissions reference: https://developers.facebook.com/docs/permissions/

Provider requirements change. Verify current official documentation before implementing or publishing a scope registry.
