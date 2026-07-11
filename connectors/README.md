# Connector contract

Connectors collect or prepare provider data. They do not contain growth strategy and should not make production decisions.

A connector implementation should support the relevant subset of:

- authorize or connect;
- revoke;
- health check;
- list assets;
- read incremental data;
- report pagination, rate limit, lag, and last complete period;
- prepare a draft or diff;
- execute a narrowly approved action;
- verify and report the result.

All secret values are passed at runtime through a vault or environment secret reference. Provider registry files in `providers/` contain capability metadata only.

Run the mock connector:

```bash
python scripts/mock_connector.py list-assets examples/multi-channel/mock-connection.json
python scripts/mock_connector.py fetch examples/multi-channel/mock-connection.json
```
